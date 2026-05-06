import streamlit as st

st.title("Login")

login_form = st.form(key="login_form")

username = login_form.text_input(
    "Username", placeholder="your@email.com", icon=":material/account_circle:"
)
password = login_form.text_input(
    "Password", type="password", placeholder="********************", icon=":material/key_vertical:"
)

col1, col2 = login_form.columns([1, 4])
stay_logged_in = col1.checkbox("Stay logged in")
admin_login = col2.checkbox("Admin")

if login_form.form_submit_button("Login"):
    intro = "Staying logged in as" if stay_logged_in else "Logging in as"
    rest = (
        f" admin {username} (password {'*' * len(password)})"
        if admin_login
        else f" {username} (password {'*' * len(password)})"
    )
    st.write(f"{intro}{rest}")
