import streamlit as st
import time
import flag_cms.utils as ut

# https://docs.streamlit.io/develop/concepts/multipage-apps/page-and-navigation

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.image("content/images/934.jpg")
    
    with st.form("loginform"):
        st.text_input("꾸리꾸러 기러꾸", key="magic_spell")
        submit_button = st.form_submit_button("Log in")
        
        if submit_button:
            if ut.is_similar(st.session_state["magic_spell"],"날쭈아리 아리꾸"):
                st.toast("로그인 성공", icon="🎉")
                st.balloons()
                time.sleep(2)
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.image("content/images/Rnfjrl.png", caption="꾸러기, 어린이 드라마, MBC 1986")
                st.snow()
                st.error("🗝️ 꾸리꾸러 기러꾸 ㄴㅉㅇㄹ ㅇㄹㄲ")

def logout():
    # st.sidebar.balloons()
    st.image("content/images/byby.gif")
    time.sleep(10)
    st.session_state.logged_in = False
    st.rerun()

# https://fonts.google.com/icons
login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

dashboard = st.Page(
    "content/reports/dashboard.py", title="Dashboard", icon=":material/dashboard:", default=True
)
bugs = st.Page("content/reports/bugs.py", title="Bug reports", icon=":material/bug_report:")
alerts = st.Page(
    "content/reports/alerts.py", title="System alerts", icon=":material/notification_important:"
)

search = st.Page("content/tools/search.py", title="Search", icon=":material/search:")
history = st.Page("content/tools/history.py", title="History", icon=":material/history:")

if st.session_state.logged_in:
    # st.sidebar.button("Log out", on_click=logout)
    pg = st.navigation(
        {
            "Account": [logout_page],
            "Reports": [dashboard, bugs, alerts],
            "Tools": [search, history],
        }
    )
else:
    pg = st.navigation([login_page])
    


pg.run()