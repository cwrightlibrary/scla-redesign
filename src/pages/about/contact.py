import streamlit as st

st.title("Contact Us")

st.header("Discussion List")
st.write("Connect with the South Carolina Library Association mailing list through our Discussion List. Our online mailing list provides announcements of news, activities, and opportunities of interest to SCLA members.")

with st.popover("Discussion List Information"):
    st.write("The South Carolina Library Association has a mailing Discussion List through its website.  Connect with the South Carolina Library Association mailing list through our Discussion List. Our online mailing list provides announcements of news, activities, and opportunities of interest to SCLA members.")
    st.info(":material/info: SCLA members are automatically subscribed to the SCLA Discussion List\n\nOnly subscribed SCLA members may send and receive messages via the mailing list")

    st.page_link("src/pages/about/join.py")
    st.markdown("""- Send emails to SCLA_List@scala.memberclicks.net . Emails are moderated and may take up to 24 hours to be sent\n- Send your email from the email address you have listed in your website profile.  If you send from a different email account, MemberClicks will not recognize you and your message will not go through""")

with st.popover("ListServ Archives"):
    st.write("Archives of listserv postings are found on your website profile")
    st.write("First, log in.")
    st.page_link("src/pages/login.py")
    st.markdown("""- Select My Community\n- Hover over the "My Features" tab\n- Click on E-Lists\n- Click on the NAME of the listserv (SCLA_List)""")

with st.popover("To Unsubscribe"):
    st.write("First, log in.")
    st.page_link("src/pages/login.py")
    st.markdown("""Select My Community\n- Hover over the "My Features" tab\n- Click on E-Lists\n- Click on the NAME of the listserv (SCLA_List)\n- Click Unsubscribe\n- Click Unsubscribe again in the next box to confirm you wish to unsubscribe\n- You should receive an unsubscribe message in your email""")