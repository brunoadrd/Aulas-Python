import streamlit as st
import streamlit_authenticator as stauth
from dependencies import user_query, general_query, create_table, register_user

COOKIE_EXPIRY_DAYS = 30

def main():
    try:
        general_query()
    except:
        create_table()
    
    db_query = general_query()
    registers = {'usernames': {}}
    for data in db_query:
        registers['usernames'][data[1]] = {'name': data[0], 'password': data[2]}

    authenticator = stauth.Authenticate(
        registers,
        'random_cookie_name',
        'random_signature_key',

        COOKIE_EXPIRY_DAYS,
    )

    if 'register_btn' not in st.session_state:
        st.session_state['register_btn'] = False
    
    if st.session_state['register_btn'] == False:
        login_form(authenticator=authenticator)
    else: 
        register_form()

def login_form(authenticator):
    name, authentication_status, username = authenticator.login('Login')

    if authentication_status:
        authenticator.logout('Logout', 'main')
        st.title('Area do Dashboard')
        st.write(f'* {name} está logado!')
    else:
        register_btn = st.button('Registrar')
        if register_btn:
            st.session_state['register_btn'] = True
            st.rerun()
        
        if authentication_status == False:
            st.error('Usuário ou Senha incorretos.')
        elif authentication_status == None:
            st.warning('Por favor informe um usuário e senha')
    
def register_form():
    with st.form(key = 'register_form', clear_on_submit = False):
        name = st.text_input('Nome', key='name')
        username = st.text_input('Usuário', key = 'user')
        password = st.text_input('Senha', key = 'password', type = 'password')
        confirm_password = st.text_input('Confirmar senha', key = 'confirm_password', type = 'password')
        submit = st.form_submit_button('Registrar')

    login_btn = st.button('Voltar')

    if login_btn:
        st.session_state['register_btn'] = False
        st.rerun()

    if st.session_state.user:
        hashed_password = stauth.Hasher([st.session_state.password]).generate()

        if st.session_state.password != st.session_state.confirm_password:
            st.warning('As senhas não conferem!')
        elif user_query(st.session_state.user):
            st.warning('Nome de usuário já cadastrado!')
        else:
            register_user(st.session_state.name, st.session_state.user, hashed_password[0])
            st.success('Registro realizado com sucesso!')

if __name__ == '__main__':
    main()