import os
from unittest.util import _MAX_LENGTH
import openai
import streamlit as st
openai.api_key = os.getenv('OPENAI_API_KEY')


start_sequence = "\nMises:"
restart_sequence = "\n\nPerson:"


session_prompt = "The following is a conversation between a person and free market advocate Ludwig von Mises."

def mises(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt_text,
        temperature=0,
        # max_length=512,
        max_tokens=512,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.3,
        stop=["\n"],
    )
    story = response['choices'][0]['text']
    return str(story)


def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
        return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
