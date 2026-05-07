import streamlit as st

st.markdown(
    """
    <style>
        /* Only apply these rules to screens wider than 768px (Desktops/Laptops) */
        @media (min-width: 768px) {
            /* Make the main content area wider */
            .block-container {
                max-width: 70%;
                padding-top: 2rem;
            }

            /* Make the Sidebar Logo larger */
            [data-testid="stSidebarHeader"] img {
                max-height: 100px;
                width: auto;
            }
        }
        
        /* Optional: CSS for all screens (Headers) */
        @import url('https://fonts.googleapis.com/css2?family=Darumadrop+One&display=swap');
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Darumadrop One', cursive;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Contact Us")

st.header("Discussion List")
st.write("Connect with the South Carolina Library Association mailing list through our Discussion List. Our online mailing list provides announcements of news, activities, and opportunities of interest to SCLA members.")

st.markdown("""- Send emails to scla_list@scala.memberclicks.net . Emails are moderated and may take up to 24 hours to be sent\n- Send your email from the email address you have listed in your website profile.  If you send from a different email account, MemberClicks will not recognize you and your message will not go through""")

with st.popover("Discussion List Information"):
    st.write("The South Carolina Library Association has a mailing Discussion List through its website.  Connect with the South Carolina Library Association mailing list through our Discussion List. Our online mailing list provides announcements of news, activities, and opportunities of interest to SCLA members.")
    st.page_link("src/pages/about/join.py")
    st.info(":material/info: SCLA members are automatically subscribed to the SCLA Discussion List\n\nOnly subscribed SCLA members may send and receive messages via the mailing list")

with st.popover("ListServ Archives"):
    st.write("Archives of listserv postings are found on your website profile")
    st.write("First, log in.")
    st.page_link("src/pages/login.py")
    st.markdown("""- Select My Community\n- Hover over the "My Features" tab\n- Click on E-Lists\n- Click on the NAME of the listserv (SCLA_List)""")

with st.popover("To Unsubscribe"):
    st.write("First, log in.")
    st.page_link("src/pages/login.py")
    st.markdown("""Select My Community\n- Hover over the "My Features" tab\n- Click on E-Lists\n- Click on the NAME of the listserv (SCLA_List)\n- Click Unsubscribe\n- Click Unsubscribe again in the next box to confirm you wish to unsubscribe\n- You should receive an unsubscribe message in your email""")