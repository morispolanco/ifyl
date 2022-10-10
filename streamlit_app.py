from email.policy import default
from multiprocessing.connection import answer_challenge
import os
import openai
import streamlit as st
from streamlit_chat import message
from Bot import mises, session_prompt
from Sentiment import sentiment

openai.api_key = os.getenv('OPENAI_API_KEY')


start_sequence = "\nMises:"
restart_sequence = "\n\nPerson:"

st.set_page_config(
    page_icon='🏢',
    page_title='AI Mises ChatBot',
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "This is a chatbot created using OPENAI's Advance GPT-3 model",
        'Get Help': 'https://github.com',
        'Report a bug': "https://github.com",
    }
)
st.title("AI Mises ChatBot")

st.sidebar.title("🏢 AI Mises Chatbot")
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


question = st.text_input("Say Something to the Mises:",
                         value='Hello Mises')
message(question, is_user=True)

answer = mises(question, chat_log)

# printing the Answer
chat_log = append_interaction_to_chat_log(question, answer, chat_log)
message(answer)

with st.expander("Not sure what to ask?"):
    st.markdown("""
Try some of these:
```
1. What are the causes of poverty?
2. What are the causes of inflation?
3. Does Capitalism creates inequality?
4. How to limit the power of the State?
5. Do you have any difference of opinion with Friedrich Hayek?.
```
    """)
