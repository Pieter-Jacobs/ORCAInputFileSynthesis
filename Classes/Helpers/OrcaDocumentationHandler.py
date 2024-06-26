from Data.Manual.ExtractedDocumentation import basis_sets, input_blocks, keywords_density_functionals, keywords_simple_input
import random


class ORCADocumentationHandler:
    """Static class that processes the gathered ORCA documentation."""

    def choose_random_keyword(documentation):
        return random.choice(list(ORCADocumentationHandler.process_documentation(documentation).keys()))

    def get_basis_set_documentation():
        return ORCADocumentationHandler.process_documentation('\n'.join(getattr(basis_sets, var) for var in dir(basis_sets) if isinstance(getattr(basis_sets, var), str)))

    def get_all_keyword_documentation():
        all_documentation = {}
        all_documentation.update(
            ORCADocumentationHandler.get_density_functional_documentation())
        all_documentation.update(
            ORCADocumentationHandler.get_basis_set_documentation())
        all_documentation.update(
            ORCADocumentationHandler.get_keywords_simple_input_documentation())
        return all_documentation

    def get_density_functional_documentation():
        return ORCADocumentationHandler.process_documentation('\n'.join(getattr(keywords_density_functionals, var) for var in dir(keywords_density_functionals) if isinstance(getattr(keywords_density_functionals, var), str)))

    def get_input_block_documentation():
        return ORCADocumentationHandler.process_documentation(input_blocks.input_blocks)

    def get_keywords_simple_input_documentation():
        return ORCADocumentationHandler.process_documentation('\n'.join(getattr(keywords_simple_input, var) for var in dir(keywords_simple_input) if isinstance(getattr(keywords_simple_input, var), str)))

    def process_documentation(documentation):
        doc_dictionary = {}
        lines = documentation.split('\n')
        for line in lines:
            # Skip empty lines
            if not line.strip():
                continue
            # Split line by whitespace
            parts = line.split('@', maxsplit=1)
            if len(parts) >= 2:
                code = parts[0].lower()
                explanation = parts[1].strip()
                doc_dictionary[code] = explanation
        return doc_dictionary
