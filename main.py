from parse import parse_pdf
from parse import plt_img_base64
from parse import _parse_pdf_to_images
import pymupdf4llm
import google.generativeai as genai
import chromadb
#from sentence_transformers import SentenceTransformer
import getpass
import base64
import httpx
from langchain_core.messages import HumanMessage
import os
from GeneralAgent import Agent
from langchain_openai import ChatOpenAI
from process import preprocess


def main():
    pdf_path = "東京都.pdf"
    image_paths,recs = parse_pdf(pdf_path)
    md_text = pymupdf4llm.to_markdown(pdf_path)
    find_table = pymupdf4llm.to_markdown(pdf_path,page_chunks=True)
    preprocess(md_text,find_table,image_paths,recs,None)

if __name__ == '__main__':
    main()