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
