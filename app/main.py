# Entry point for the app

import streamlit as st
from utils import llm_agent, image_processing, voice_processing


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
    '''
    name = st.text_input("Name")
    if not name:
        st.warning('Please input a question.')
        st.stop()
    st.success("Question received.")
    # st.write(docbot.invoke(name)['result'])
    '''
