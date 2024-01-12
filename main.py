import os
import streamlit as st
import openai
import json
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.utilities import WikipediaAPIWrapper

class Chatbot:
  def __init__(self, api_key):
    openai.api_key = api_key
    self.template = PromptTemplate(
      input_variables = ['concept'], 
      template='Give me a popular recipe for {concept}'
    )
    self.chat_history = ConversationBufferMemory(input_key='concept', memory_key='chat_history')
  
  def generate_response(self, input):
    model = OpenAI(temperature=0.6)
    chain = LLMChain(llm=model, prompt=self.template, verbose=False, output_key='concept', memory=self.chat_history)
    res = ''

    if input:
      res = chain.run(input)

    return res

def main():
  # openai_key = ''
  os.environ['OPENAI_API_KEY'] = openai_key

  st.title("Find a Recipe")
  input = st.text_input("Enter Your Text: ") 

  if input:
    bot = Chatbot(openai_key)
    res = bot.generate_response(input)

    st.write(res)

main()

    