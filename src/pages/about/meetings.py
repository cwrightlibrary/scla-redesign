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

st.title("Meetings")

st.subheader("Meeting Dates")
st.table(pd.DataFrame([
    ("Wednesday, January 28, 2026", "10:00 am"),
    ("Wednesday, April 29, 2026", "10:00 am"),
    ("Wednesday, July 29, 2026", "10:00 am"),
    ("Wednesday, September 30, 2026", "10:00 am"),
    ("Wednesday, December 30, 2026", "10:00 am")
], columns=["Date", "Time"]), border="horizontal")

st.info(":material/info: Board of Directors meetings include the Chairs of SCLA Sections, Round Tables, Committees, and Interest Groups.  If the Chair cannot attend, please send another officer or member designee.")

st.link_button("Board of Directors Meeting", r"https://www.scla.org/assets/docs/Meeting_Minutes/Minutes%20for%20SCLA%20September%202025%20Board%20Meeting.pdf", help="September, 2025")

with st.popover("Meeting Minutes Archive"):
    st.subheader("Meeting Minutes Archive")
    st.table(pd.DataFrame([
        ("[Leadership Retreat](https://www.scla.org/assets/docs/scla%202014%20leadership%20retreat%20vaa.docx)", "February, 2014"),
        ("[Executive Board Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesapril2014.docx)", "April, 2014"),
        ("[Executive Board Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesjune2014.docx)", "June, 2014"),
        ("[Executive Board Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesaugust2014.docx)", "August, 2014"),
        ("[Executive Board Meeting and Conference Wrap up](https://www.scla.org/assets/docs/sclaboardmeetingminutesoctober2014.docx)", "October, 2014"),
        ("[Leadership Retreat](https://www.scla.org/assets/docs/sclaleadershipretreatminutesfebruary2015.docx)", "February, 2015"),
        ("[Executive Board Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesapril2015.docx)", "April, 2015"),
        ("[Executive Board Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesjune2015.docx)", "June, 2015"),
        ("[Executive Board Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesoctober2015.docx)", "October, 2015"),
        ("[Leadership Retreat](https://www.scla.org/assets/docs/sclaleadershipretreatminutesfebruary2016.docx)", "February, 2016"),
        ("[Executive Board Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesapril2016.docx)", "April, 2016"),
        ("[Executive Board Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesjune2016.docx)", "June, 2016"),
        ("[Executive Board Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesaugust2016.docx)", "August, 2016"),
        ("[Board of Directors Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesnovember2016.docx)", "November, 2016"),
        ("[First General Session & Business Meeting](https://www.scla.org/assets/docs/sclageneralsessionbusinessmeetingminutesnovember2016.docx)", "November, 2016"),
        ("[Leadership Retreat](https://www.scla.org/assets/docs/sclaleadershipretreatminutesfebruary2017.docx)", "February, 2017"),
        ("[Board of Directors Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesapril2017.docx)", "April, 2017"),
        ("[Board of Directors Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesjune2017.docx)", "June, 2017"),
        ("[Board of Directors Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesaugust2017.docx)", "August, 2017"),
        ("[Board of Directors Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesjanuary2018.docx)", "January, 2018"),
        ("[Board of Directors Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesapril2018.docx)", "April, 2018"),
        ("[Board of Directors Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesjune2018.docx)", "June, 2018"),
        ("[Board of Directors Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesseptember2018.docx)", "September, 2018"),
        ("[Board of Directors Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesjanuary2019.docx)", "January, 2019"),
        ("[Board of Directors Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesapril2019.docx)", "April, 2019"),
        ("[Board of Directors Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesjune2019.docx)", "June, 2019"),
        ("[Board of Directors Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesseptember2019.docx)", "September, 2019"),
        ("[Board of Directors Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesjanuary2020.docx)", "January, 2020"),
        ("[Board of Directors Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesapril2020.docx)", "April, 2020"),
        ("[Board of Directors Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesjune2020.docx)", "June, 2020"),
        ("[Board of Directors Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesseptember2020.docx)", "September, 2020"),
        ("[Board of Directors Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesjanuary2021.docx)", "January, 2021"),
        ("[Board of Directors Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesapril2021.docx)", "April, 2021"),
        ("[Board of Directors Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesjune2021.docx)", "June, 2021"),
        ("[Board of Directors Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesnovember2021.docx)", "November, 2021"),
        ("[Board of Directors Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesjanuary2022.docx)", "January, 2022"),
        ("[Board of Directors Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesmay2022.docx)", "May, 2022"),
        ("[Board of Directors Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesjuly2022.docx)", "July, 2022"),
        ("[Board of Directors Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesseptember2022.docx)", "September, 2022"),
        ("[Board of Directors Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesjanuary2023.docx)", "January, 2023"),
        ("[Board of Directors Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesapril2023.docx)", "April, 2023"),
        ("[Board of Directors Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesjuly2023.docx)", "July, 2023"),
        ("[Board of Directors Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesseptember2023.docx)", "September, 2023"),
        ("[Board of Directors Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesjanuary2024.docx)", "January, 2024"),
        ("[Board of Directors Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesapril2024.docx)", "April, 2024"),
        ("[Board of Directors Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesjuly2024.docx)", "July, 2024"),
        ("[Board of Directors Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesseptember2024.docx)", "September, 2024"),
        ("[Board of Directors Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesjanuary2025.docx)", "January, 2025"),
        ("[Board of Directors Meeting](https://www.scla.org/assets/docs/sclaboardmeetingminutesapril2025.docx)", "April, 2025")
    ], columns=["Meeting", "Date"]), border="horizontal")