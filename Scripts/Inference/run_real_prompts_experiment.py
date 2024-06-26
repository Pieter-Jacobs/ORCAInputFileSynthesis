
from openai import OpenAI
import os
import sys
import argparse
sys.path.append(os.getcwd())
from Classes.Model.Embedder import Embedder


def parse_arguments():
    """Parsess the arguments that are used to determine which model is to be ran on the RealPrompts dataset"""
    parser = argparse.ArgumentParser(
        description='Run the RealPrompts experiment with the provided model configuration.')
    parser.add_argument('--prompt_engineering_technique', type=str, required=False,
                        default="basic", choices=['none', 'basic', 'cot', 'cove', 'tot', 'got'],
                        help='Prompt engineering technique to be used (none, basic, cot, cove, tot, or got).')
    parser.add_argument('--model', type=str, required=False,
                        default='gpt-3.5-turbo', help="OpenAI model to use, if a finetuned model is used one should copy full model name from the OpenAI finetuning dashboard.")
    parser.add_argument('--rag', type=int, required=False,
                        default=0, choices=[0, 1], help="Determines whether the model should use RAG during inference (0 or 1)")
    parser.add_argument('--k', type=int, required=False,
                        default=1, help="Amount of documents to retrieve when using RAG.")
    args = parser.parse_args()
    return args


def predict_input_file_with_gpt(client, user_prompt, system_prompt, model):
    """Makes use of the OpenAI client to run a given model with the provided system and user prompt."""
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return completion.choices[0].message.content


def run_model_on_expert_prompts(model='gpt-3.5-turbo', prompt_engineering_technique='none', rag=False, k=1):
    """Runs a specified model on a set of expert prompts using a specified prompt engineering technique.
    Parameters:
    - model (str): The name or identifier of the model to be used.
    - prompt_engineering_technique (str): The technique to be used for prompt engineering.
    - rag (bool): Flag indicating whether to use Retrieval-Augmented Generation (RAG).
    - k (int): The number of relevant contexts to retrieve if RAG is enabled."""
    client = OpenAI()

    # Initialize input and output paths
    data_folder = os.path.join("Data", "Prompts", "RealPrompts")
    output_folder = "Results/RealPrompts"
    os.makedirs(output_folder, exist_ok=True)

    system_prompt = open(os.path.join("Data", "Prompts", "PromptEngineeringTechniques", f"{
                         prompt_engineering_technique.lower()}.txt"), 'r', encoding='utf-8').read()

    # If rag is employed, we extend the system prompt with relevant instructions on how to handle context.
    if rag:
        rag_instructions = open(os.path.join("Data", "Prompts", "PromptEngineeringTechniques", "rag.txt"),
                                'r', encoding='utf-8').read()
        system_prompt = f'{system_prompt}{rag_instructions}'

    prompts = [open(os.path.join(data_folder, file), 'r').read()
               for file in os.listdir(data_folder)
               if os.path.isfile(os.path.join(data_folder, file))]

    # Perform inference on each prompt
    for i, prompt in enumerate(prompts):
        if rag:
            prompt = Embedder.add_relevant_context_to_prompt(model=model,
                                                             system_prompt=system_prompt,
                                                             prompt=prompt,
                                                             embedding_folder=os.path.join(
                                                                 "Data", "Documents", "Embedded", "index_merged"),
                                                             k=k,
                                                             # GPT-3.5 Turbo's token limit.
                                                             token_limit=15000
                                                             )
        output = predict_input_file_with_gpt(
            client, prompt, system_prompt, model)

        # Write the results to file
        with open(os.path.join(output_folder, f"{"".join(x for x in model if x.isalnum())}_output_{i+1}.txt"), 'w', encoding='utf-8') as f:
            f.write("\n-------------PROMPT-----------\n")
            f.write(prompt)
            f.write("\n-------------OUTPUT-----------\n")
            f.write(output)


if __name__ == "__main__":
    args = parse_arguments()
    run_model_on_expert_prompts(
        args.model, args.prompt_engineering_technique, args.rag, args.k)
