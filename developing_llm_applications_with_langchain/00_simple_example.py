
import os
from langchain_huggingface import HuggingFaceEndpoint


hugging_face_api_key = os.environ["huggingface_apikey"]

# https://huggingface.co/tiiuae/falcon-7b-instruct
llm = HuggingFaceEndpoint(
    repo_id="tiiuae/falcon-7b-instruct", 
    huggingfacehub_api_token=hugging_face_api_key 
)

question = "Can you still have fun"

output = llm.invoke(question)

print("hello")