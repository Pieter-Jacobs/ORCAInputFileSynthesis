import PyPDF2
from Classes.Model.Embedder import Embedder
import os
from pypdf import PdfMerger


def embed(pdf_paths, saving_folder):
    merger = PdfMerger()

    for path in pdf_paths:
        merger.append(path)
    merger.write(os.path.join("Data", "Documents", "Regular", "merged.pdf"))

    doc = Embedder.split_pdf(os.path.join(
        "Data", "Documents", "Regular", "merged.pdf"))
    Embedder.save_embedding_to_file(
        doc, embedding_folder=os.path.join(saving_folder, "index_merged"))


if __name__ == "__main__":
    embedding_folder = os.path.join("Data", "Documents", "Embedded")
    pdf_folder = os.path.join("Data", "Documents", "Regular")
    pdf_paths = [os.path.join(pdf_folder, "orca_input_file_library.pdf"),
                 os.path.join(pdf_folder, "orca_manual_5_0_4_without_tables2.pdf")]

    embed(pdf_paths=pdf_paths, saving_folder=embedding_folder)
