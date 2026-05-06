import streamlit as st

st.title("About the organization")

with st.container(border=True):
    st.header("Organization")

    st.subheader("Sections")
    st.page_link(
        "src/pages/organization/sections.py",
        label="Go to Sections",
        icon=":material/groups:",
    )
    st.caption(
        "Represents distinct kind of libraries or areas of activity. Section members elect their respective officers at the annual conference or by electronic ballot."
    )

    st.page_link(
        "src/pages/organization/round_tables.py",
        label="Go to Round Tables",
        icon=":material/table_bar:",
    )
    st.caption(
        "Represents common interests not confined to either a kind of library or an area of activity. Round table members elect their respective officers at the annual conference or by electronic ballot."
    )

    st.page_link(
        "src/pages/organization/committees.py",
        label="Go to Committees",
        icon=":material/diversity_2:",
    )
    st.caption(
        "Carries out the business and planning of the organization. Members of both special and standing committees are appointed by the President."
    )

st.link_button(
    "Instructions on joining sections or round tables",
    r"https://www.scla.org/assets/docs/SCLA%20Section%20and%20Roundtable%20Instructions.pdf",
)

st.link_button(
    "Download SCLA Committee Reports for 2023 PDF",
    r"https://www.scla.org/assets/docs/SCLA%20Section%2C%20Rountable%20Committee%20reports%202023.pdf",
)
st.link_button(
    "Download Officer Guide 2023 PDF",
    r"https://www.scla.org/assets/docs/2023%20SCLA%20Officers%27%20Guide.docx",
)
