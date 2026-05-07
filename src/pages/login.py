import streamlit as st
import src.helpers.setup_database as db

st.title("Login")

login_tab, signup_tab = st.tabs(["Login", "Sign Up"])

if not st.session_state.logged_in:
    login_form = login_tab.form(key="login_form")

    email = login_form.text_input(
        "Email", placeholder="your@email.com", icon=":material/account_circle:"
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

    if login_form.form_submit_button("Login", type="primary"):
        is_admin = 1 if admin_login else 0
        login_verified, admin_level = db.verify_user(email, password, is_admin)
        if login_verified:
            st.success("Logged in successfully!") if admin_level == 0 else st.success("Logged in as admin!")
            if admin_level and admin_level > 0:
                st.session_state.admin = True
            
            st.session_state.username = email
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Issue with login")
else:
    if st.button("Sign Out", type="primary"):
        st.session_state.admin = False
        st.session_state.username = ""
        st.session_state.logged_in = False
        st.rerun()

if not st.session_state.logged_in:
    signup_form = signup_tab.form(key="signup_form")

    signup_name_col1, signup_name_col2 = signup_form.columns(2)
    signup_first_name = signup_name_col1.text_input("First name", placeholder="Jane")
    signup_last_name = signup_name_col2.text_input("Last name", placeholder="Doe")

    signup_email = signup_form.text_input(
        "Email", placeholder="your@email.com", icon=":material/account_circle:"
    )
    signup_password = signup_form.text_input(
        "Password",
        type="password",
        placeholder="*" * 20,
        icon=":material/key_vertical:",
        key="signup_password",
    )
    verify_password = signup_form.text_input(
        "Verify",
        type="password",
        placeholder="*" * 20,
        icon=":material/key:",
        key="signup_verify",
    )

    submit_signup_button = signup_form.form_submit_button(
        "Sign Up",
        type="primary"
    )

    if submit_signup_button:
        if not signup_password or not verify_password:
            st.error("Please fill out all password fields.")
        if signup_password != verify_password:
            st.error("Passwords do not match.")
        else:
            admin_level = 1 if signup_email == "cwright@richlandlibrary.com" else 0

            db.add_user(
                {"first_name": signup_first_name, "last_name": signup_last_name},
                signup_email,
                signup_password,
                admin_level=admin_level,
            )
            st.success("Account created successfully!")