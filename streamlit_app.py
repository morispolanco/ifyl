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
        'Get Help': 'mailto:mpolanco@feylibertad.org',
        'Report a bug': "mailto:mpolanco@feylibertadd.org",
    }
)
st.title("ChatBot del Instituto Fe y Libertad")

st.sidebar.title("🏢 ChatBot del IFYL")
st.sidebar.markdown("""

**Feedback/Questions**:
[Instituto Fe y Libertad](https://feylibertad.org)
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

with st.expander("¿No está seguro de qué preguntar?"):
    st.markdown("""
Pruebe con alguna de estas preguntas:
```
1. ¿Cómo influye la fe en la libertad, personal y política?
2. ¿Cómo se relacionan fe y desarrollo económico?
3. ¿En qué principios se funda la civilización occidental?
4. ¿Qué postula el principio de subsidiariedad?
5. ¿Qué ideas deben presidir el florecimiento humano?
6. ¿Qué lugar ocupa el bienestar material en el florecimiento humano?
7. ¿Cómo se relaciona la verdad con la libertad?
8. ¿Cómo damos gloria a Dios?
9. ¿Puede un cristiano ser liberal?
10. ¿Qué ideas o principios deben presidir el ordenamiento social y político?
11. ¿Puede un cristiano ser capitalista?
12. ¿Cómo sostener que la moral es universal y objetiva, después de Darwin?
13. ¿Qué es más importante: la libertad o la verdad?
14. ¿Por qué permitieron los cristianos que se cerraran las iglesias durante la pandemia de Covid?
15. ¿Occidente sigue siendo cristiano o ya es poscristiano?
16. ¿Es la modernidad un proyecto cultural cristiano?
```
    """)
