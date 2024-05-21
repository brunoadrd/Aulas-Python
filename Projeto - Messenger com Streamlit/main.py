import streamlit as st
from functions import *

def _register_message(username, password):
    if register_user(username, password):
        st.success('Usuário cadastrado com sucesso!')
        time.sleep(2)
        st.session_state['user_logged'] = username.title()
        change_page('chat')
        st.rerun()
    else:
        st.error('Erro ao cadastrar usuário!')

def _user_login(username, password):
    if password_validation(username, password):
        st.success('Login efetuado com sucesso!')
        time.sleep(2)
        st.session_state['user_logged'] = username.title()
        change_page('chat')
        st.rerun()
    else:
        st.error('Erro ao realizar Login!')

def login_page():
    st.title('Bem vindo ao Chat')
    tab1, tab2 = st.tabs(['Login', 'Registrar'])

    with tab1.form(key='login'):
        username = st.text_input('Usuário')
        password = st.text_input('Senha', type='password')
        if st.form_submit_button('Logar'):
            _user_login(username, password)

    with tab2.form(key='register'):
        username = st.text_input('Digite o nome de usuário')
        password = st.text_input('Digite sua senha', type='password')
        if st.form_submit_button('Registrar'):
            _register_message(username, password)

def chat_page():
    st.title(f'💬 ASIMOV CHAT - {st.session_state['talking_to']}')
    st.divider()

    if not 'messages' in st.session_state:
        st.session_state['messages'] = []

    user_logged = st.session_state['user_logged']
    talking_to = st.session_state['talking_to']
    
    messages = read_messages(user_logged, talking_to)

    container = st.container()

    for message in messages:
        username = 'user' if message['username'] == user_logged else message['username']
        chat = container.chat_message(username)
        chat.markdown(message['content'])

    new_message = st.chat_input('Digite uma mensagem.')

    if new_message:
        dict_message = {
            'username': user_logged,
            'content': new_message
        }

        chat = container.chat_message('user')
        chat.markdown(dict_message['content'])
        messages.append(dict_message)
        arquive_messages(user_logged, talking_to, messages)

def initialization():
    if not 'atual_page' in st.session_state:
        change_page('login')
    if not 'user_logged' in st.session_state:
        st.session_state['user_logged'] = ''
    if not 'talking_to' in st.session_state:
        st.session_state['talking_to'] = ''
    if not 'last_message' in st.session_state:
        st.session_state['last_message'] = ''

def main():
    initialization()

    if st.session_state['atual_page'] == 'login':
        login_page()
    elif st.session_state['atual_page'] == 'chat':
        if st.session_state['talking_to'] == '':
            container = st.container()
            change_talk(container)
        else:
            chat_page()
            container = st.sidebar.container()
            change_talk(container)
            time.sleep(RERUN_TIME)
            st.rerun()

if __name__ == '__main__':
    main()