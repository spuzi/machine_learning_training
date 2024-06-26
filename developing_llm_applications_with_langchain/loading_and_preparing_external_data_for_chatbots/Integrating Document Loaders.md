
We will talk about loading and preparing external data sources for a chat model, the first step of a process called Retrieval Augmented Generation (RAG).

Pre-trained language models do not have access to private or proprietary data sources. 

We call the process of integrating these data sources Retrieval Augmented Generation (or RAG for short).

1. This starts with a user query. The user query is sent to an application created with a framework such as LangChain and transformed the query to a vector representation.
2. This model searches for the most relevant document in a vector database by comparing them to the user's query.
3. It then ranks the most relevant results to the user's query using a chosen distance metric.
4. Finally, the most relevant documents from the vector database are concatenated to the user query and sent to the model.
5. The model generates a response, which is sent back to the end user through the application.


There are 3 primary strep to RAG development in LangChain.
1. Loading the documents into LangChain with document loaders.
2. Next, splitting the documents into chunks. Chunks are units of information that we can index and process individually.
3. The last step is encoding and storing the chunks for retrieval, which could utilize a vector database if that meets the needs of the use case.

We'll discuss all of these steps throughout the next chapter, but for now we'll start with document loaders.

LangChain has more than 160 document loaders. Some loaders are provided by 3rd parties who manage unique document formats. These includes Amazon S3, Microsoft, Google Cloud, Jupyter notebooks, pandas DataFrames, unstructured HTML, YouTube audio transcripts, and more.

We will practice loading data from three common formats. LangChain has excellent documentation on all of its documents loaders, and 