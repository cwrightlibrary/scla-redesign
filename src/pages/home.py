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

st.title("South Carolina Library Association")

save_the_date_image = "src/images/FB_Save the Date.png"
st.image(save_the_date_image)

text1 = """The South Carolina Library Association is hard at work planning for the **2026 SCLA Conference**! Our Conference Planning Committee is already hard at work creating an engaging and inspiring experience for library professionals across the state.

From researching dynamic speakers to planning fun networking opportunities and organizing memorable author luncheons, the committee is focused on building a conference that brings South Carolina’s library community together to learn, collaborate, and celebrate the important work happening in our libraries. """
st.markdown(text1)

st.subheader("Save the date")

date_and_location = """Tuesday, October 27 - Thursday, October 29, 2026

**Columbia Metropolitan Convention Center**

1101 Lincoln Street Columbia, SC 29201"""
st.markdown(date_and_location)

st.subheader("Stay tuned for updates")

updates = """Additional conference details will be shared in the coming months, including:

- Poster session proposal submissions
- Session proposal opportunities
- Author luncheons and featured speakers
- Networking events and special programs
- Registration details and conference schedule

The SCLA Conference is one of the best opportunities for library workers across South Carolina to connect, share ideas, and learn from one another. We hope you’ll save the date and join us in Columbia in October 2026.
"""
st.markdown(updates)

st.divider()

st.page_link("src/pages/join.py", icon=":material/person_add:")

join_text = """:material/info: Not yet a member of the South Carolina Library Association? Becoming a member is a great way to stay connected with the library community across the state, access professional development opportunities, and receive updates about the annual conference and other SCLA events."""
st.info(join_text)

with st.expander("Upcoming Events", expanded=True):
    st.header("Upcoming Events")
    events_table = [
        (
            "May 27, 2026",
            "[Public Library Section Meeting](https://www.scla.org/index.php?option=com_jevents&task=icalrepeat.detail&evid=209&Itemid=115&year=2026&month=05&day=27&title=public-library-section-meeting&uid=485083b4ecb959135f77a98f6dd79a6b)",
        ),
        (
            "May 28, 2026",
            "[Library Marketing and Outreach Round Table Meeting](https://www.scla.org/index.php?option=com_jevents&task=icalrepeat.detail&evid=214&Itemid=115&year=2026&month=05&day=28&title=-library-marketing-and-outreach-round-table-meeting&uid=2bb76aa2661d88ac38315ed9a83fdcb9)",
        ),
        (
            "July 23, 2026",
            "[Library Marketing and Outreach Round Table Meeting](https://www.scla.org/index.php?option=com_jevents&task=icalrepeat.detail&evid=215&Itemid=115&year=2026&month=07&day=23&title=-library-marketing-and-outreach-round-table-meeting&uid=612844cac4e4ce4f560082b52d7a0e26)",
        ),
        (
            "August 19, 2026",
            "[Public Library Section Meeting](https://www.scla.org/index.php?option=com_jevents&task=icalrepeat.detail&evid=210&Itemid=115&year=2026&month=08&day=19&title=public-library-section-meeting&uid=1022c2f438a0a719547aaf5ec3e29bb8)",
        ),
        (
            "September 24, 2026",
            "[Library Marketing and Outreach Round Table Meeting](https://www.scla.org/index.php?option=com_jevents&task=icalrepeat.detail&evid=216&Itemid=115&year=2026&month=09&day=24&title=-library-marketing-and-outreach-round-table-meeting&uid=f17bda716cf48af12b028b69e61d45cb)",
        ),
    ]
    events_df = pd.DataFrame(events_table, columns=["Date", "Event"])
    st.table(events_df, border="horizontal")

with st.expander("Announcements"):
    st.header("Announcements")
    reg_text = """Registration is now open for **Library Link**, a one-day professional development event focused on leadership, connection, and conversation for library professionals across South Carolina. Join us on Wednesday, May 13 from 9:00 AM to 4:30 PM at Richland Library Main in Columbia, SC. Registration is \\$25 for SCLA members and $35 for non-members, with light refreshments provided (lunch not included). More details about sessions and speakers will be shared soon."""
    st.write(reg_text)
    st.link_button(
        "Register Now",
        "https://docs.google.com/forms/d/e/1FAIpQLSdUDV3ndewvO0OkgMBXuMC277DILLNvVZNTGg1R6RkN0yRwNA/viewform?usp=header",
    )

with st.expander("Support SCLA at Kroger"):
    st.header("Support SCLA at Kroger")
    st.write(
        "SCLA is now part of the **Kroger Community Rewards Program!** Every time you shop at Kroger, you can support libraries across South Carolina at no extra cost to you."
    )
    st.write("**Here's how to join:**")
    kroger_text = """1. Visit [kroger.com](https://www.kroger.com/)\n2. Log in or create an account\n3. Search for **SOUTH CAROLINA LIBRARY ASSOCIATION** or use code **LC252**\n4. Click **Enroll** and start shopping!\n\nEvery grocery trip helps strengthen our library community."""
    st.write(kroger_text)

with st.expander("South Carolina Digital Library"):
    st.header("South Carolina Digital Library")
    st.write(
        "This [digital collection](https://digital.tcl.sc.edu/digital/collection/scla) curated by the South Carolina Digital Library showcases 100 years of SCLA history, including photographs, conference brochures, and publications."
    )

with st.expander("SCLA Continuing Education Webinars"):
    st.header("SCLA Continuing Education Webinars")

    st.write(
        "View all previous webinars on the [SCLA YouTube channel](https://www.youtube.com/channel/UCES4xRifDCfuNX9W6GbV01w)."
    )
    st.info(
        ":material/info: To submit a webinar proposal, [visit this link](https://forms.gle/CXkeXHwbUcrtCg6A8)."
    )
