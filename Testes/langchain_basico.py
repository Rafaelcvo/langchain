# pip install --upgrade --quiet langchain-openai tiktoken langchain-chroma langchain GitPython

from git import Repo
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser
from langchain_text_splitters import Language
import dotenv

print(dotenv.load_dotenv())
