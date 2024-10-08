import os
from Classes.Helpers.ORCAInputFileManipulator import ORCAInputFileManipulator
from Classes.Helpers.ORCAManualManipulator import ORCAManualManipulator
from Classes.Helpers.ORCADocumentationHandler import ORCADocumentationHandler
from openai import OpenAI
import json
import re


class Prompter:
    """
    Prompter class for generating prompts from ORCA input files and improving them using GPT models.

    Parameters:
        contextual_prompt (str): System prompt for GPT completion.
        input_files (list): List of ORCA input files.
        simple_input_keyword_mappings (dict): Simple input keyword mappings.
        df_keyword_mappings (dict): Density functional keyword mappings.
        basis_set_mappings (dict): Basis set mappings.
        input_block_mappings (dict): Input block mappings.
        prompt_engineered_input_files (list): Engineered prompts from input files if created.
        client (OpenAI): OpenAI API client instance.
    """

    def __init__(self, contextual_prompt, data_folder, input_files=None, create_synthetic_labels=False):
        self.client = OpenAI()
        self.contextual_prompt = contextual_prompt
        self.input_files = self.load_input_files(
            data_folder) if not input_files else input_files
        self.simple_input_keyword_mappings = ORCADocumentationHandler.get_keywords_simple_input_documentation()
        self.df_keyword_mappings = ORCADocumentationHandler.get_density_functional_documentation()
        self.basis_set_mappings = ORCADocumentationHandler.get_basis_set_documentation()
        self.input_block_mappings = ORCADocumentationHandler.get_input_block_documentation()
        self.prompt_engineered_input_files = list(
            map(self.create_cot_label_from_input_file, self.input_files)) if create_synthetic_labels else None
        self.input_files = list(map(self.clean_input_file, self.input_files))

    def prompt(self, input_files=None, data_folder=None):
        """Generates prompts from a list of input files."""
        prompts = []
        input_files = self.input_files if input_files is None else input_files
        for input_file in input_files:
            prompts.append(self.create_prompt_from_input_file(input_file))
        return prompts

    def create_prompt_from_input_file(self, input_file):
        """Creates a prompt from an ORCA input file."""
        molecule_smiles = ORCAInputFileManipulator.extract_molecule_smiles(
            input_file)
        keywords, _ = ORCAInputFileManipulator.extract_keywords(input_file)
        _, input_block_options, input_block_settings = ORCAInputFileManipulator.extract_input_blocks(
            input_file)
        simple_input_descriptions, density_functional_descriptions, basis_set_descriptions = self.map_keywords(
            keywords)
        input_block_descriptions = self.map_input_blocks(input_block_options)

        prompt = self.reformat_prompt_descriptions(
            simple_input_descriptions, density_functional_descriptions,
            basis_set_descriptions, input_block_descriptions,
            input_block_settings, molecule_smiles)
        print(prompt)
        improved_prompt = self.improve_prompt_with_llm(
            prompt)  # Try to make the prompt more human-like
        print(improved_prompt)
        if not improved_prompt:
            return prompt
        return improved_prompt

    def map_keywords(self, keywords):
        """Maps keywords to their respective descriptions."""
        return ([(key, self.simple_input_keyword_mappings[key]) for key in keywords if key in self.simple_input_keyword_mappings],
                [(key, self.df_keyword_mappings[key])
                 for key in keywords if key in self.df_keyword_mappings],
                [(key, self.basis_set_mappings[key]) for key in keywords if key in self.basis_set_mappings])

    def map_input_blocks(self, options):
        """Maps input block options to their descriptions."""
        return [(option, self.input_block_mappings.get(option, "")) for option in options]

    def reformat_prompt_descriptions(self, simple_input_descriptions, density_functional_descriptions,
                                     basis_set_descriptions, input_block_descriptions, input_block_settings, molecule_smiles):
        """
        Formats prompt descriptions into a structured prompt string.

        Parameters:
            simple_input_descriptions (list): Descriptions of simple input keywords.
            density_functional_descriptions (list): Descriptions of density functionals.
            basis_set_descriptions (list): Descriptions of basis sets.
            input_block_descriptions (list): Descriptions of input blocks.
            input_block_settings (list): Settings of input blocks.
            molecule_smiles (str): Molecule SMILES string.

        Returns:
            str: Formatted prompt string.
        """
        prompt = f"#{molecule_smiles}\n"
        prompt += "Basis sets: @" if len(basis_set_descriptions) > 0 else ""
        for description in basis_set_descriptions:
            prompt += f"{description[0]}={description[1]}@"
        prompt += "\nDensity functionals: @" if len(
            density_functional_descriptions) > 0 else ""
        for description in density_functional_descriptions:
            prompt += f"{description[0]}={description[1]}@"
        prompt += "\nOther: @" if len(simple_input_descriptions) > 0 else ""
        for description in simple_input_descriptions:
            prompt += f"{description[0]}={description[1]}@"
        if len(input_block_settings) > 0 and len(input_block_descriptions) == len(input_block_settings):
            prompt += "\n%"
            for i, description in enumerate(input_block_descriptions):
                prompt += f"{description[1]
                             } ({description[0]}): {input_block_settings[i]}%"
        return prompt

    def improve_prompt_with_llm(self, prompt, model="gpt-4o"):
        """Improves prompt using a GPT model, hopefully making them more user-like."""
        completion = self.client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": self.contextual_prompt},
                {"role": "user", "content": prompt}
            ]
        )
        completion = completion.choices[0].message.content
        try:
            prompt = re.search(r"!PROMPT!(.*)!PROMPT!", completion,
                               flags=re.IGNORECASE | re.DOTALL).group(1)
            return prompt
        except:
            return False

    def load_input_files(self, data_folder):
        """Loads ORCA input files from a specified folder."""
        input_files = [ORCAInputFileManipulator.read_file(os.path.join(data_folder, file))
                       for file in sorted(os.listdir(data_folder))]
        return input_files

    def create_cot_label_from_input_file(self, input_file):
        """Create a synthetic CoT reply for a given input file."""
        keywords, _ = ORCAInputFileManipulator.extract_keywords(input_file)
        _, input_block_options, input_block_settings = ORCAInputFileManipulator.extract_input_blocks(
            input_file)
        molecule_smiles = ORCAInputFileManipulator.extract_molecule_smiles(
            input_file)
        molecule_smiles = ORCAInputFileManipulator.get_random_xyz()[1].removesuffix(
            '.txt') if not molecule_smiles else molecule_smiles
        print(molecule_smiles)
        simple_input_descriptions, density_functional_descriptions, basis_set_descriptions = self.map_keywords(
            keywords)

        intro = 'I used the following step-by-step logic to get to my input file prediction:'
        step1 = f"Step 1: The basis sets used are {",".join([x[0] for x in basis_set_descriptions])}.\n{f"The used density functional(s) are: {",".join(
            [x[0] for x in density_functional_descriptions])}" if len(density_functional_descriptions) else "No density functional is used"}. Further keywords used are: {",".join(
                [x[0] for x in simple_input_descriptions])}"
        step2 = f"Step 2: The input block options that should be used are: {
            ",".join(input_block_options)}"
        step3 = f"Step 3: {"\n".join([f"For {input_block_options[i]}, the settings are as follows: {input_block_settings[i]}" for i in range(
            len(input_block_options))]) if len(input_block_options) == len(input_block_settings) or len(input_block_options) == 0 else "N/A"}".removesuffix('\n')
        step4 = f"Step 4: The desired SMILES is {
            molecule_smiles}" if molecule_smiles else "Step 4: There is no SMILES defined."
        step5 = f"Step 5: Given the answers to the above steps, the final ORCA input file is:\n{
            input_file}"
        return "\n".join([intro, step1, step2, step3, step4, step5]).strip()

    def clean_input_file(self, input_file):
        """Removes paralellization and the coordinate block from an input file."""
        input_file = input_file.replace("pal6 ", "")
        input_file = ORCAInputFileManipulator.remove_xyz(input_file)
        return input_file
