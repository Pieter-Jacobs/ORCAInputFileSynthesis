from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import tiktoken


class Embedder:
    """Static class used to handle PDFs and to create embeddings from them for RAG."""
    def split_pdf(pdf_path):
        """Split a pdf by page"""
        textSplitter = RecursiveCharacterTextSplitter(
            length_function=len,
            chunk_overlap=0)
        loader = PyPDFLoader(pdf_path)
        text_split_by_page = loader.load_and_split(textSplitter)
        return text_split_by_page

    def save_embedding_to_file(documents, embedding_folder):
        """Use FAISS to embed documents and save them to file"""

        faiss_index = FAISS.from_documents(
            documents, OpenAIEmbeddings(model="text-embedding-3-large"))
        faiss_index.save_local(embedding_folder)

    def add_relevant_context_to_prompt(model, system_prompt, prompt, embedding_folder, k, token_limit):
        """Adds k documents to the user prompt and checks that this does not go over the provided token limit"""
        enc = tiktoken.encoding_for_model(
            model)  # get the correct token encoding
        contextual_information = ""
        count = 0

        index = FAISS.load_local(
            embedding_folder, OpenAIEmbeddings(), allow_dangerous_deserialization=True)
        manual_texts = index.similarity_search(prompt, k)

        for i in range(k):
            if len(enc.encode(f'''{system_prompt}{prompt}\n#context\n{contextual_information}{manual_texts[count].page_content}\n''')) < token_limit:
                contextual_information += manual_texts[i].page_content + "\n" # Add a pdf page
        return f"{prompt}\n#context\n{contextual_information}"
