#Chatbot #LangChain #LLM 

Let's use LangChain to start implementing prompting strategies for chatbots. This will apply to both OpenAI chat models and open-source chat models from Hugging Face.

Besides OpenAI's chat models, thousands of chat-optimized language models are available in LangChain via the Hugging Face Hub API.

To find language models specifically optimized for chat, search the chat models sections of Hugging Face and filter on Question Answering

![Hugging Face Question Answering Models](Pasted%20image%2020240615062119.png)

Then, take note of the model name so it can be referenced in the code.

New models are constantly being released on Hugging Face. Many are also fine-tuned on domain-specific datasets, so they are better at capturing the nuance of a particular region, culture, or task, so searching Hugging Face for the most appropriate model for the use case will be worthwhile.

Once we've selected a model, we can begin prompting it by utilizing prompt template.

Prompt template acts as recipes for generating prompts from use inputs in a flexible and modular way. 

A template can include instructions, examples if we were wanting to few-shot prompt, and any additional context that might help the model complete the task. 

Prompt templates are created using LangChain's "*PromptTemplate*" class. 

```python

from langchain.prompts import PromptTemplate

# Create a template string
# The "question" field is defined for dynamic insertion later in the code
template = "You are an artifical intelligence assistant, answer the question. {question}"

prompt = PromptTemplate(
			template=template, 
			input_variables=["question"]
		)
```

Now that we have our prompt template, let's integrate it into a model. 

Different components are combined together in LangChain using **chains**, and we'll use the *LLMChain* to chain the prompt template to an LLM.

We start by choosing an LLM, in this case, a falcom model from Hugging Face. 

```python

from langchain.chains import LLMChain
from langchain_community.llms import HuggingFaceHub

# We start by choosing an LLM, in this case, a falcom model 
# from Hugging Face. 
llm = HuggingFaceHub(
    repo_id="tiiuae/falcon-7b-instruct",
    huggingfacehub_api_token=hugging_face_api_key 
)

# Chain the prompt template to an LLM
llm_chain = LLMChain(
				prompt=prompt, 
				llm=llm
			)

# To begin passing user inputs, we call the run() method 
# on the chain passing the input string
quesiton = "What is LangChain?"

print(llm_chain.run(question))
```

Note 1: the class *HuggingFaceHub* is deprecated and you should use *HuggingFaceEndpoint* instead
Note 2: The LLMChain is deprecated since version 0.1.17, use "prompt | llm" instead.
```python
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI

prompt_template = "Tell me a {adjective} joke"
prompt = PromptTemplate(
    input_variables=["adjective"], 
    template=prompt_template
)
llm = OpenAI()
chain = prompt | llm

chain.invoke("your adjective here")

```

So using the non deprecated methods:
```python
import os
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint

prompt_template = "Tell me a {adjective} joke"
prompt = PromptTemplate(
    input_variables=["adjective"], 
    template=prompt_template
)

hugging_face_api_key = os.environ["huggingface_apikey"]
llm = HuggingFaceEndpoint(
    repo_id="tiiuae/falcon-7b-instruct",
    huggingfacehub_api_token=hugging_face_api_key
)
chain = prompt | llm
output = chain.invoke("black humor")
print(output)
```

In the following sections we'll introduce the *LangChain Expression Language (LCEL)*, which provides a more paired-down syntax for creating chains with even more flexibility, so stay tuned on that.

LangChain also provides classes specifically designed to work with chat models, like *ChatPromtTemplate* and *ChatOpenAI*.

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(temperature=0, openai_api_key=openai_apikey)

prompt_template = ChatPromptTemplate.from_messages(
	[
		("system", "You are soto zen master Roshi."),
		("human", "Respond to the question: {question}")
	]
)

full_prompt = prompt_template.format_message(
					question="What is the sound of one hand clapping?"
				)

# We'll pass the prompt to the model to view 
# the model reponse
llm(full_prompt)
```

