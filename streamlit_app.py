from email.policy import default
from multiprocessing.connection import answer_challenge
import os
import openai
import streamlit as st
from streamlit_chat import message
from Bot import mises, session_prompt
from Sentiment import sentiment

openai.api_key = os.getenv('OPENAI_API_KEY')


start_sequence = "\nIFYL:"
restart_sequence = "\n\nPerson:"

st.set_page_config(
    page_icon='🏢',
    page_title='ChatBot del Instituto Fe y Libertad',
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "This is a chatbot created using OPENAI's Advance GPT-3 model",
        'Get Help': 'https://github.com',
        'Report a bug': "https://github.com",
    }
)
st.title("ChatBot del Instituto Fe y Libertad")

st.sidebar.title("🏢 ChatBot del IFYL")
st.sidebar.markdown("""

**Feedback/Questions**:
[Github](https://github.com)
""")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

if 'chat_log' not in st.session_state:
    st.session_state['chat_log'] = session_prompt

chat_log = st.session_state['chat_log']


def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
        return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'


question = st.text_input("Pregúntenos:",
                         value='¿Cuál es su misión?')
message(question, is_user=True)

answer = mises(question, chat_log)

# printing the Answer
chat_log = append_interaction_to_chat_log(question, answer, chat_log)
message(answer)

with st.expander("?No estaá seguro de qué preguntar?"):
    st.markdown("""
Pruebe con alguna de estas preguntas:
```
1. ¿Cuómo influye la fe fe y en libertad, personal y política?
2. ¿Cómo se relacionan fe y desarrollo económico?
3. ¿En qué principios se funda la civilización occidental?
4. ¿Qué postula el principio de subsidiariedad?
5. ¿Qué ideas deben presidir el florecimiento humano?
6. ¿El florecimiento humano necesita del bienestar económico y material?
```
    """)
