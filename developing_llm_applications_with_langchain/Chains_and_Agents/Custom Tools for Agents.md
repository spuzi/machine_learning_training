#LLM #agents #tools

Now that we've created our first agent, let's take a closer look at tools so we can design our own.

```python
from langchain.agents import load_tools

tools = load_tools(["llm-math"], llm=llm)

```