#LangChain #Chatbot #LLM

We now live in a world where we're spoiled for choice when it comes to choosing
large language models, or LLMS, for developing AI-powered applications.

However, these LLMs differ based on their model architecture, training data, 
intended use cases, and prompting strategies.

Addionally, these models often have to interact with other systems to retrieve
other data or monitor performance, which adds another layer of complexity. 

LangChain was created by Harrison Chase in 2022 to change all of that.
LangChain is an Open source framework that helps developers connect LLMs, 
data sources, and other functionality under a single, unified syntax. 

With LangChain, developers can create scalable, modular LLM applications for
almost any use.

LangChain encompasses an entire ecosystem of tools, but in this course, we'll 
focus on the core functionality of the LangChain library. 

In this course we'll focus on the core functionality of the LangChain library. We 
will learn about chains and tools, which can be use to improve the quality of
our LLMs output, and also discuss troubleshooting and evaluation techniques.

Note that LangChain is available in Python and JavaScript, but this course will
only cover the Python version.

LangChain has **3 main components**: 
- A **Language Model** chosen by the developer that can be either o**pen source or closed sourced**.
- **Prompts** for **tuning user inputs into model inputs**.
- **Parsers** for organizing **data** for easy **retrieval**.

The system also includes **chains and agents for creating workflows containing different components**. 

Let's first discuss choosing language models.

Hugging Face is a huge repository of open source datasets, tools, and most important for us, models. 

Using language models hosted on Hugging Face is free, but using them in LangChain requires a Hugging Face API token. To create one, log in or create a HuggingFace account, and navigate to the URL show under settings. Here we can create and copy our token. 

Now that we have our key, let's use LangChain to use a model from Hugging Face, and compare to using an OpenAI model.

LangChain has an OpenAI class and HuggingFace class for interacting with the respective APIs.
```python
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
print(output)
```


```python
from lanchain_openai import OpenAI

llm = OpenAI(open_api_key=open_api_key)
question = "Can you still have fun"
output = llm.invoke(question)
print(output)
```

[Simple Example with HuggingFace](./00_simple_example_huggingface.py)


[Simple Example with OpenAi]()


From Hugging Face, we're using the Falcon 7b parameter instruction-optimized model. We'll define an unfinished sentence predict, and use both models to predict the next words.

And finally let's print the result and see the output.

Compare the two different approaches, despite using completely different models from different sources, LangChain unifies them both into a consistent, modular workflow.

LangChain's tools can be used to optimize the outputs of the models for our particular use cases, this we will be focusing on this part.

To summarize, LangChain is a fantastic tool for working with natural language. In the real world of development for production, it unlocks the ability for intelligent conversations with documents, which companies can use to support business decisions, more opportunities for task automation, and different ways to analyze text data.

LangChain makes using AI easier and gives us greater control over the entire workflow.

Note: we will be using the version 0.1.17 of LangChain, if you wish to use a newer version on your own system, be sure to check the LangChain documentation for any changes.

## Exercise: LangChain's core components
When building an application with LangChain, it's important to know about the primary components and what they can do for your application output.

LangChain is an excellent framework for creating applications on large language models (LLMs). Within this framework, there are several core components used to build applications.

- [ ] Parsers
    Parsers are used for organizing and transforming data for easier retrieval.
	
- [ ] Chains
    Chains are used for creating workflows containing multiple components.
	
-  [X] Prompts

- [ ] Agents
Agents are used for creating workflows involving decisions and actions.

