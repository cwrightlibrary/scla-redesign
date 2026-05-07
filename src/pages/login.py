import streamlit as st

st.title("Login")

login_tab, signup_tab = st.tabs(["Login", "Sign Up"])

login_form = login_tab.form(key="login_form")

username = login_form.text_input(
    "Username", placeholder="your@email.com", icon=":material/account_circle:"
)
password = login_form.text_input(
    "Password",
    type="password",
    placeholder="********************",
    icon=":material/key_vertical:",
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

signup_form = signup_tab.form(key="signup_form")

signup_name_col1, signup_name_col2 = signup_form.columns(2)
signup_first_name = signup_name_col1.text_input("First name", placeholder="Jane")
signup_last_name = signup_name_col2.text_input("Last name", placeholder="Doe")

signup_username = signup_form.text_input(
    "Username", placeholder="your@email.com", icon=":material/account_circle:"
)
signup_password = signup_form.text_input(
    "Password",
    type="password",
    placeholder="********************",
    icon=":material/key_vertical:",
    key="signup_password"
)
verify_password = signup_form.text_input(
    "Verify",
    type="password",
    placeholder="********************",
    icon=":material/key:",
    key="signup_verify"
)

if signup_form.form_submit_button("Sign Up", type="primary"):
    st.write(signup_first_name, signup_last_name, signup_username)