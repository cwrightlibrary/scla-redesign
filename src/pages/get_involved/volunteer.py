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

st.title("Volunteer")

st.write("There are many opportunities for leadership and participation in SCLA! Consider putting your talents and skills to work for the Association in one of these categories:")

st.page_link("src/pages/about/executive_officers.py")
st.write("Voting members include the Executive Officers, immediate Past-President, section chairs, ALA Councilor, and SELA representative. Ex-offico members include the Executive Secretary, APLA representative, round table chairs, SCASL representative, and SCSLA representative.")

st.page_link("src/pages/organization/sections.py")
st.write("Represent distinct kind of libraries or areas of activity. Section members elect their respective officers at the annual conference or by mail ballot. Membership in two sections or round tables is included in your annual dues, but you're encouraged to join additional sections or round tables by paying a small annual fee.")

st.page_link("src/pages/organization/round_tables.py")
st.write("Represent common interests not confined to either a kind of library or an area of activity. Round table members elect their respective officers at the annual conference or by mail ballot. Membership in two sections or round tables is included in your annual dues, but you're encouraged to join additional sections or round tables by paying a small annual fee.")

st.page_link("src/pages/organization/committees.py")
st.write("Carry out the business and planning of the organization. Members of both special and standing committees are appointed by the President.")

st.info(":material/info: To learn more about how to get involved, get in touch with our current officers. Contact information can be found on each Section, Round Table, and Committee page")