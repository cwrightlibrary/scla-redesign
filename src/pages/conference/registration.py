import streamlit as st

st.title("Information")
st.image("src/images/SCLibraryAssociation.jpg")

st.header("Registration")
st.write("Thank you to all of the attendees, vendors, sponsors, and exhibitors who made The Power of Us: Libraries in Action a success! The Conference Planning Committee hopes that you are energized, refreshed, and prepared to bring new ideas to your libraries. We look forward to seeing everyone again in October of 2026.")

st.header("Host Hotel Information")
st.write("Are you ready to register for the 2025 SCLA Conference which will take place from Tuesday, October 28th, 2025 through Thursday, October 30th, 2025 in Columbia, South Carolina? This year's theme \"The Power of Us: Libraries in Action\" is a celebration of libraries as dynamic powerhouses of community engagement, learning innovation, and social change. We can't wait to welcome you to the [Columbia Metropolitan Convention Center](https://www.columbiaconventioncenter.com/). Please see below for additional information on accommodations for the conference:")

st.info(":material/map: **Address**\n\n[Hampton Inn Columbia Downtown Historic District](https://www.hilton.com/en/hotels/caedthx-hampton-columbia-downtown-historic-district/)\n\n822 Gervais Street\n\nColumbia, SC 29201")
st.write("Our special conference rate is $184.00 dollars a night plus tax and the booking deadline is **Saturday, September 28, 2025**.")
st.link_button("Reserve Now", "https://www.hilton.com/en/attend-my-event/caedthx-91y-4d1a8f44-ee29-438e-8c9e-ecc0debf6098/", type="primary")

st.divider()

with st.popover("Past Conferences"):
    st.link_button("SCLA Conference 2024", "#")
    st.link_button("SCLA Conference 2023", "#")
    st.link_button("SCLA Conference 2021", "#")
    st.link_button("SCLA Conference 2020", "#")
    st.link_button("SCLA Conference 2019", "#")
    st.link_button("SCLA/SELA Joint Conference 2018", "#")
    st.link_button("SCLA Conference 2017", "#")
    st.link_button("SCLA Conference 2016", "#")
    st.link_button("SCLA Conference 2015", "#")
    st.link_button("SCLA Conference 2014", "#")
    st.link_button("SCLA/SELA Joint Conference 2013", "#")
    st.link_button("SCLA Conference 2012", "#")

st.divider()

st.page_link("src/pages/get_involved/awards.py")
