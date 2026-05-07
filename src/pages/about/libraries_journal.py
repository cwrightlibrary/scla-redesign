import pandas as pd
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

st.title("Libraries Journal")

st.image("src/images/TSscliblogoidea3.png", caption="South Carolina Libraries is the official journal of SCLA")
st.write("*South Carolina Libraries* is an open access journal hosted by the University of South Carolina [Scholar Commons](https://scholarcommons.sc.edu/scl_journal/).")

with st.popover("Available Issues"):
    st.subheader("Available Issues")
    st.table(pd.DataFrame([
        ("[Volume 8, Issue 1](https://scholarcommons.sc.edu/scl_journal/vol8/iss1/)", "Fall 2024"),
        ("[Volume 6, Issue 2](https://scholarcommons.sc.edu/scl_journal/vol6/iss2/)", "Fall 2022"),
        ("[Volume 6, Issue 1](https://scholarcommons.sc.edu/scl_journal/vol6/iss1/)", "Spring 2022"),
        ("[Volume 5, Issue 2](https://scholarcommons.sc.edu/scl_journal/vol5/iss2/)", "Fall 2021"),
        ("[Volume 5, Issue 1](https://scholarcommons.sc.edu/scl_journal/vol5/iss1/)", "Spring 2021"),
        ("[Volume 4, Issue 2](https://scholarcommons.sc.edu/scl_journal/vol4/iss2/)", "Fall 2020"),
        ("[Volume 4, Issue 1](https://scholarcommons.sc.edu/scl_journal/vol4/iss1/)", "Spring 2020"),
        ("[Volume 3, Issue 2](https://scholarcommons.sc.edu/scl_journal/vol3/iss2/)", "Spring 2018"),
        ("[Volume 3, Issue 1](https://scholarcommons.sc.edu/scl_journal/vol3/iss1/)", "Summer/Fall 2017"),
        ("[Volume 2, Issue 2](http://scholarcommons.sc.edu/scl_journal/vol2/iss2/)", "Fall 2016"),
        ("[Volume 2, Issue 1](http://scholarcommons.sc.edu/scl_journal/vol2/iss1/)", "Spring 2016"),
        ("[Volume 1, Issue 2](http://scholarcommons.sc.edu/scl_journal/vol1/iss2/)", "2015"),
        ("[Volume 1, Issue 1](http://scholarcommons.sc.edu/scl_journal/vol1/iss1/)", "Fall 2014")
    ], columns=["Issue", "Date"]), border="horizontal")

st.subheader("About This Journal")
st.write("South Carolina Libraries publishes information relevant to SC libraries and librarians, as well as materials in the field of librarianship in general. Authors are invited to submit articles, news, innovations, columns and book reviews for consideration. The journal will be published twice a year. The spring edition will be dedicated to the previous SCLA conference and will include research, conference proceedings, and posters.")

st.info(":material/info: **Submission of Manusripts**\n\nArticles can be submitted directly through the South Carolina Libraries website. Simply click on the “Submit Article” link to the left of the page and follow the provided directions. During the process you will be able to select the type of article you are submitting. If you have any questions or suggestions about the different article types, please email the Editors. If you are interested in becoming a peer reviewer or have any questions about the peer review process, please email the Peer Review Editor. If you have questions or suggestions about book reviews, please email the Book Review Editor.")

st.subheader("Officers")
st.table(pd.DataFrame([
    ("McKenzie M. Lemhouse", "Editor", "lemhouse@mailbox.sc.edu"),
    ("TBD", "Assistant Editor", None),
    ("Craig Keeney", "Peer Review Editor", "ckeeney@mailbox.sc.edu"),
    ("Valerie Vera", "Book Review Editor", "lookingv@email.sc.edu"),
    ("Ron Stafford", "Communications Editor", "rstafford@netc.edu"),
    ("Amie Freeman", "Technical Advisor", "dillarda@mailbox.sc.edu"),
    ("Adele Chase", "Student Representative", "chaseal@email.sc.edu")
], columns=["Name", "Title", "Email"]), border="horizontal")

st.subheader("Deadlines")
st.link_button("Submission Policies", "https://scholarcommons.sc.edu/scl_journal/policies.html", help="What can be submitted?")
st.link_button("Submission Form", "https://scholarcommons.sc.edu/cgi/submit.cgi?context=scl_journal", help="Submission deadline is **January 31, 2025**", type="primary")

st.info(":material/info: **Who may submit**\n\n Submissions are sought from anyone with a vested interest in libraries in the state of South Carolina from all types of libraries: Academic, K-12, Public, Special, etc. Both peer-review AND non-peer-reviewed articles are welcome!")