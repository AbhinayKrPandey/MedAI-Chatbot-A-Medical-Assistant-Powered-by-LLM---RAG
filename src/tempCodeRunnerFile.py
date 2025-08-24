import os
from langchain_community.vectorstores import FAISS
import nltk

from src.helper import load_data, text_split, load_hf_embeddings
from config import *


DATA_PATH = os.path.join(ROOT_DIR, 'data', 'MedQuAD-master')


def fix_nltk():
	# If you get error from nltk package, add the required downloads here
	#nltk.download('all')
	nltk.download('punkt_tab')
	nltk.download('averaged_perceptron_tagger_eng')

def create_index(data_path, save_path, chunk_size, chunk_overlap):
	print("Creating index...")
	fix_nltk()
	print("Loading data...")
