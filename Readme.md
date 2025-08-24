# MedAI Chatbot: A Medical Assistant Powered by LLM & RAG
This is a web application built with Flask, featuring a Medical Assistant Chatbot powered by a Large Language Model (LLM) and Retrieval Augmented Generation (RAG).

The project is designed to run entirely on your local machine, requiring no external API keys. It leverages a suite of powerful, open-source technologies:

LangChain: The core library for building the RAG system, managing agents and tools.

Ollama: Used to serve the llama3.1 LLM locally.

SQLite: A lightweight database for managing structured data like patient, doctor, and appointment information.

FAISS: An efficient library for similarity search, used as a vector store to power the RAG system's knowledge base.

Disclaimer
This is a toy project for educational and demonstration purposes only. The outputs of the Medical Assistant should never be considered medical advice. Always consult a qualified healthcare professional for any medical concerns.

Key Features
The application offers a range of functionalities to simulate a real-world medical assistant:

Interactive Chat: Users can ask health-related questions and receive informative answers. The RAG system expands the chatbot's knowledge by retrieving information from external medical datasets.

Appointment Management: The assistant can suggest suitable doctors, show available time slots, and allow users to reserve, view, or modify their appointments.

Data Persistence: The system maintains a database of patients, doctors, appointments, and chat history. Initially, the database is populated with a limited set of SQL queries, primarily for managing appointment details and related data, to get the application up and running.

Chat History Download: Users can easily download their conversation history for their records.

Emergency Triage: A feature to report health emergencies, which are then tagged with a color code (RED, GREEN, YELLOW) for potential triage and follow-up.

Requirements & Setup
To get this project up and running, follow these steps.

***Requirements***
Python 3.10

***Install requirements***: pip install -r requirements.txt

***Install*** [Ollama](https://ollama.com/download/windows)

At least 8GB of RAM

An Nvidia GPU with a minimum of 2GB dedicated memory is recommended for optimal performance.

**Setup Instructions**
Download Datasets: Download the [MedQuad](https://www.kaggle.com/datasets/pythonafroz/medquad-medical-question-answer-for-ai-research) datasets and place them in the data folder.

Prepare Vector Index: Run (src/create_index.py) to process the datasets and build the vector store.

Prepare SQLite Database: Run (src/create_db.py) to set up the database schema.

Download LLM: From your terminal, run ollama pull llama3.1 to download the language model.

Start Server: Run app.py to start the Flask server.


***Notes***
If you encounter issues with the nltk package during the index creation, refer to the comments within the src/create_index.py file for guidance.

The initial response time for the assistant might be slow on less powerful hardware (up to 10 minutes per query) as the LLM runs locally.
