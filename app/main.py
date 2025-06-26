# Entry point for the app

import streamlit as st
import sys
sys.path.append("utils")
import llm_agent


'''
openai YES
whisper YES
pytesseract YES
Pillow
langchain YES
streamlit YES
transformers
faiss-cpu
'''

if __name__ == '__main__':
    print('Run Streamlit or FastAPI app here')

    hidden_key = input("Input the openai key:\n")
    response = llm_agent.query_llm(hidden_key, 'other_doritos_label.png', 'other_voice_memo.m4a')
    print(response)

    '''
    name = st.text_input("Name")
    if not name:
        st.warning('Please input a question.')
        st.stop()
    st.success("Question received.")
    # st.write(docbot.invoke(name)['result'])
    '''
