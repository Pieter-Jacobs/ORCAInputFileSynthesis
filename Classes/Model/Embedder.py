from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import tiktoken


class Embedder:
    def split_pdf(pdf_path):
        textSplitter = RecursiveCharacterTextSplitter(
            length_function=len,
            chunk_overlap=0)
        loader = PyPDFLoader(pdf_path)
        text_split_by_page = loader.load_and_split(textSplitter)
        return text_split_by_page

    def save_embedding_to_file(documents, embedding_folder):
        faiss_index = FAISS.from_documents(documents, OpenAIEmbeddings(model="text-embedding-3-large"))
        faiss_index.save_local(embedding_folder)

    def add_relevant_context_to_prompt(model, system_prompt, prompt, embedding_folder, k, token_limit):
        enc = tiktoken.encoding_for_model(model)

        contextual_information = ""
        count = 0

        index = FAISS.load_local(
            embedding_folder, OpenAIEmbeddings(), allow_dangerous_deserialization=True)
        manual_texts = index.similarity_search(prompt, k)

        for i in range(k):
            if len(enc.encode(f'''{system_prompt}{prompt}\n#context\n{contextual_information}{manual_texts[count].page_content}\n''')) < token_limit:
                contextual_information += manual_texts[i].page_content + "\n"
        return f"{prompt}\n#context\n{contextual_information}"

    def merge_embeddings():
        pass
