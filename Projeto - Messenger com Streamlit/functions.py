import streamlit as st
import pickle
from unidecode import unidecode
from pathlib import Path
import time

PATH_MESSAGES = Path(__file__).parent / 'messages'
PATH_MESSAGES.mkdir(exist_ok=True)

PATH_USERS = Path(__file__).parent / 'users'
PATH_USERS.mkdir(exist_ok=True)

RERUN_TIME = 3

def read_messages(user1, user2):
    talk_arquive = stored_arquive(user1, user2)
    if (PATH_MESSAGES / talk_arquive).exists():
        with open(PATH_MESSAGES / talk_arquive, 'rb') as f:
            return pickle.load(f)
    else:
        return []

def arquive_messages(user1, user2, messages):
    talk_arquive = stored_arquive(user1, user2)
    with open(PATH_MESSAGES / talk_arquive, 'wb') as f:
        pickle.dump(messages, f)

def stored_arquive(user1, user2):
    talk_arquive = [user1, user2]
    talk_arquive.sort()
    talk_arquive = [word.replace(' ', '_') for word in talk_arquive]
    talk_arquive = [unidecode(word) for word in talk_arquive]
    return '&'.join(talk_arquive).lower()

def register_user(username, password):
    arquive_name = unidecode(username.replace(' ', '_').lower())
    if (PATH_USERS / arquive_name).exists():
        return False
    else:
        with open(PATH_USERS / arquive_name, 'wb') as f:
            pickle.dump({'username': username, 'password': password}, f)
        return True

def password_validation(username, password):
    arquive_name = unidecode(username.replace(' ', '_').lower())
    if not (PATH_USERS / arquive_name).exists():
        return False
    else:
        with open(PATH_USERS / arquive_name, 'rb') as f:
            password_arquive = pickle.load(f)
        
        return password_arquive['password'] == password

def change_page(page_name):
    st.session_state['atual_page'] = page_name

def users_list():
    users = list(PATH_USERS.glob('*'))
    users = [arq.stem.replace('_', ' ').title() for arq in users]
    return users

def change_talk(element):
    users = users_list()
    users = [user for user in users if user != st.session_state['user_logged']]
    talking_to = element.selectbox('Escolha um usuário para convesar', users)
    element.button('Iniciar conversa', on_click=_change_talker, args=(talking_to, ))

def _change_talker(user2):
    st.session_state['talking_to'] = user2
    st.success(f'Iniciando conversa com {user2}')
    time.sleep(2)
    change_page('chat')