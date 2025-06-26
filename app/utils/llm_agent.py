# LLM reasoning functions using GPT-4 or LangChain

from langchain_openai import ChatOpenAI
import image_processing, voice_processing


def query_llm(hk, txtfile, voicefile):
    text = image_processing.read_image(txtfile)
    voice_command = voice_processing.process_file(voicefile)

    llm = ChatOpenAI(model="gpt-4", api_key=hk)

    prompt = f"""
Here is the text of a product label:
{text}

The user asked: "{voice_command}"

Based on their question, determine if the product is suitable.
If not, suggest alternatives based on healthy snacks.
"""

    return llm.invoke(prompt).content

if __name__ == '__main__':
    hidden_key = input("Input the openai key:")
    print(query_llm(hidden_key, "doritos_label.png", "voice_memo.m4a"))
