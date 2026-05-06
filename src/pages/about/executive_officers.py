import pandas as pd
import streamlit as st

st.title("Executive officers")

officers_table = [
    ("Jana Stevenson", "President", "sclapresident2025@gmail.com"),
    (
        "Sonaite Debebe-Kumssa",
        "1st Vice President/Conference Chair",
        "sclafirstvp@gmail.com",
    ),
    ("Amanda Myers", "2nd Vice President/Membership Chair", "secondvpscla@gmail.com"),
    ("Valerie Byrd Fort", "Secretary", "valeriebyrdfort@gmail.com"),
    ("Dr. April Williams", "Treasurer", "aprilwilliams@lancastercountysc.gov"),
    ("Kelly Jones", "Immediate Past President", None),
]
reps_table = [
    (
        "Tracey Elvis-Weitzel",
        "South Carolina Association of Public Library Administrators Liason",
        "elvist@horrycountysc.gov",
    ),
    (
        "Virginia Cononie",
        "South Carolina Association of School Librarians Liason",
        None,
    ),
    (
        "Amber Conger",
        "Southeastern Library Association Liason",
        "aconger@lexcolibrary.org",
    ),
]

officers_df = pd.DataFrame(officers_table, columns=["Name", "Title", "Email"])
reps_df = pd.DataFrame(reps_table, columns=["Name", "Title", "Email"])

with st.container(border=True):
    st.header("2026 Executive Officers")
    st.table(officers_df, border="horizontal")

with st.container(border=True):
    st.header("American Library Association Councilor")
    st.write("Sarah Schroeder")

with st.container(border=True):
    st.header("Executive Director")
    st.write(
        "Courtney Waldrup\n\nPremier Management Partners\n\n1 Windsor Cove, Suite 305\n\nColumbia, SC 29223\n\ncwaldrup@pmpamc.com"
    )

with st.container(border=True):
    st.header("2025 Association Representatives")
    st.table(reps_df, border="horizontal")
