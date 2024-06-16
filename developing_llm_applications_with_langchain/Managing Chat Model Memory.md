
#LangChain #LLM #model_memory

We'll discuss how to integrate memory into our chatbots.

Memory is important for conversations with chat models, it opens up the possibility of providing follow-up questions, of building and iterating on model responses, and for chatbots to adapt to the user's preferences and behaviors.

Although LangChain allows us to customize and optimize in-conversation chat memory, it is still limited by the model's context window.

An LLM's context window is the amount of input text the model can consider at once when generating a response, and the length of this window varies from different models. 

LangChain has a standard syntax for optimizing model memory.

We'll cover three LangChain classes for implementing chatbot memory. 
- *ChatMessageHistory*
- *ConversationBufferMemory*
- *ConversationSummaryMemory*



