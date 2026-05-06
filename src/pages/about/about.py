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

st.title("About SCLA")

# --- ABOUT ---
letter_text = """Welcome to the homepage of the South Carolina Library Association (SCLA). Begun in 1915, The South Carolina Library Association was established on October 27 of that year when fourteen librarians and library supporters met at the University of South Carolina Library and voted unanimously to form the new group.

We are a state chapter of the American Library Association (ALA) and an affiliate of the Southeastern Library Association (SELA). The association is made of librarians from all around our state South Carolina dedicated to providing innovative services and promoting libraries and intellectual freedom to all our citizens including the public, as well as those in higher education and in our schools.

Contact us to learn more and find out how you can get involved.
"""
st.markdown(letter_text)

st.caption("SCLA President Kelly Jones")

# --- GOVERNANCE ---
governance_list = r"""- The SCLA Handbook is currently being updated, please check back soon for the latest edition.
- [SCLA Constitution and Bylaws](https://www.scla.org/assets/docs/revised%20scla%20bylaws%20september%2029%202025-final.pdf), October 2025
- [Emerging Leader Guidelines](https://www.scla.org/assets/docs/emerging%20leader%20guidelines%20approved%204.7.16.docx), June 2016
- [Officer Guidelines](https://www.scla.org/assets/docs/2023%20SCLA%20Officers%27%20Guide%20PDF%20Version.pdf), July 2023"""

st.subheader("Governance")
st.markdown(governance_list)
