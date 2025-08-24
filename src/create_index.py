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
	data = load_data(data_path)
	print("Data loaded...")
	text_chunks = text_split(data, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
	print("Loading embeddings...")
	embeddings = load_hf_embeddings()
	print("Creating vector store...")
	 # Initialize the vector store with the first document to set up the structure
	vectorstore_from_docs = FAISS.from_documents([text_chunks[0]], embedding=embeddings)

	# Process the rest of the documents in batches
	batch_size = 500  # You can make this smaller (e.g., 200) if you still have memory issues
	for i in range(1, len(text_chunks), batch_size):
		batch = text_chunks[i:i + batch_size]
		vectorstore_from_docs.add_documents(batch)
    	# This print statement will show you the progress
	print(f"Processed documents {i} to {i + batch_size}")
	
	vectorstore_from_docs.save_local(save_path)
	print("Done!")
	return vectorstore_from_docs

if __name__ == '__main__':
	_ = create_index(DATA_PATH, INDEX_PATH, CHUNK_SIZE, CHUNK_OVERLAP)