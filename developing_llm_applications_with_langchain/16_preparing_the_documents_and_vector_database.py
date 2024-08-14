"""
Preparing the documents and vector database
-------------------------------------------
Over the next few exercises, you'll build a full RAG workflow to have a 
conversation with a PDF document containing the paper: 

    RAG VS Fine-Tuning: Pipelines, Tradeoffs, and a Case Study on Agriculture by 
    Balaguer et al. (2024). 

This works by splitting the documents into chunks, storing them in a vector 
database, defining a prompt to connect the retrieved documents and user input, 
and building a retrieval chain for the LLM to access this external data.

In this exercise, you'll prepare the document for storage and ingest them into 
a Chroma vector database. You'll use a RecursiveCharacterTextSplitter to chunk 
the PDF, and ingest them into a Chroma vector database using an OpenAI 
embeddings function.

Instructions:
1. Assign your OpenAI API key to openai_api_key.
2. Split the documents in data using a recursive character splitter with a 
  chunk_size of 300 and chunk_overlap of 50; leave the separators argument out, 
  as it defaults to ["\n\n", "\n", " ", ""].
3. Define an OpenAI embeddings model and use it to embed and ingest the 
  documents into a Chroma database.
4. Configure vectorstore into a retriever object that returns the top 3 documents 
  for use in the final RAG chain.
"""
