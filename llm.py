# pip install langchain huggingfacehub

import os
from langchain import PromptTemplate, HuggingFaceHub, LLMChain
token = os.getenv('HUGGINGFACEHUB_API_TOKEN')

google_key = None

template = """Two words are going to fight. Which of the following words wins?

{player_word} VS {npc_word}

Answer: The word that would win is: """

prompt = PromptTemplate(template=template, input_variables=["player_word", "npc_word"])

llm_chain = LLMChain(prompt=prompt,
                     llm=HuggingFaceHub(repo_id="google/flan-t5-large",
                                        model_kwargs={"temperature":0,
                                                      "max_length":64}))


def get_winner(player_word, npc_word):
    llm_answer = llm_chain.run(player_word=player_word, npc_word=npc_word)
    return llm_answer