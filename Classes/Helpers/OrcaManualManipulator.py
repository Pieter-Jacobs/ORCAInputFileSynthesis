import re
from Classes.Helpers.OrcaDocumentationHandler import OrcaDocumentationHandler

class OrcaManualManipulator:
    """Static class that is able to handle textual data and can manipulate and extract parts of this text that are relevant
    to ORCA input files."""
    
    def extract_input_files(text):
        """Extract input files out of text (start with ! and end with '*' with a star in front of xyz). 
        We limit the characters after ! because otherwise it gathers a lot of exlamation marks that are way before an input file."""
        input_file_regex = r'\s*(!.{0,500}\*\s*xyz[\s\S]*?\*)'
        input_files = list(set(re.findall(input_file_regex, text, re.DOTALL)))
        return input_files
    
    def extract_processed_input_files_wo_xyz(text):
        """Extract input files out of text (start with ! and end with '*' with a star in front of xyz). 
        We limit the characters after ! because otherwise it gathers a lot of exlamation marks that are way before an input file."""
        input_file_regex = r'(!.*?#.*?)\n'
        input_files = re.findall(input_file_regex, text, re.DOTALL)
        if len(input_files) == 0:
            input_file_regex = r'(!.*?#.*?)$'
            input_files = re.findall(input_file_regex, text, re.DOTALL)
        return input_files

    def extract_input_file_coordinates(text):
        """Extract xyz coordinates out of text (start with * followed by one optional whitespace and then xyz and end with *)."""
        coordinate_pattern = r'\*\s?xyz.*?\*'
        coordinates = list(set(re.findall(coordinate_pattern, text, re.DOTALL)))
        return coordinates
    
    def extract_keywords(text):
        """Extract all words out of lines starting with !"""
        keywords = []
        keyword_lines = re.findall(
            r'![^\n\r]*', text)
        # Remove "!"
        keyword_lines = [re.sub("[!\b]", "", line) for line in keyword_lines]
        keywords.extend([keyword.lower()
                        for line in keyword_lines for keyword in line.split()])
        return keywords, keyword_lines

    def extract_known_keywords(text):
        """Extract all words out of lines starting with ! that are in the gathered keywords documentation"""
        keywords = []
        keyword_lines = re.findall(
            r'![^\n\r]*', text)
        # Remove "!"
        keyword_lines = [re.sub("[!\b]", "", line) for line in keyword_lines]
        keywords.extend([keyword.lower() 
                        for line in keyword_lines 
                        for keyword in line.split() 
                        if keyword.lower() in list(OrcaDocumentationHandler.get_all_keyword_documentation().keys())])
        keyword_lines = ([[keyword.lower() for keyword in line.split() if keyword.lower() in list(OrcaDocumentationHandler.get_all_keyword_documentation().keys())] for line in keyword_lines])
        keyword_lines = list(filter(None, keyword_lines))
        return keywords, keyword_lines
        
        
    def extract_input_file_blocks(text):
        options = []
        input_blocks = []
        settings = []

        input_blocks_raw = re.findall(
            r'(%\s*\w+.*?end)', text, flags=re.DOTALL | re.IGNORECASE)
        
        # input_blocks_raw = re.findall(
        #     r'(%\s*\w+\n.{0,200}?\nend)\n', input_file_code_wo_maxcore, flags=re.DOTALL | re.IGNORECASE)
        
        for input_block in input_blocks_raw:
            try: 
                options.append(re.search(r'%\s*(\w+)', input_block).group(1).lower())
                input_blocks.append(input_block)
            except: 
                pass
        
        return input_blocks, options
