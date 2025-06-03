# LLM reasoning functions using GPT-4 or LangChain

from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool
import image_processing, voice_processing

text = image_processing.text
voice_command = voice_processing.voice_command
user_input = 'Is this gluten-free?'

hidden_key = input("Input the openai key:")

llm = ChatOpenAI(model="gpt-4", api_key=hidden_key)

prompt = f"""
Here is the text of a product label:
{text}

The user asked: "{user_input}"

Based on their question, determine if the product is suitable.
If not, suggest alternatives based on healthy snacks.
"""

response = llm.invoke(prompt)

if __name__ == '__main__':
    print(response)
