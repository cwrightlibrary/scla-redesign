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

st.title("Sections")

with st.expander("College and University Section", expanded=True):
    st.header("College and University Section")
    college_uni_info = """It is the purpose of the College and University Section to serve persons interested in all aspects of academic libraries. Its objective is to stimulate and support high standards of library service in colleges and universities. It encourages professional growth through attendance at professional meetings, promotion of communication and exchange of ideas among its members, continuing education opportunities, and dissemination of publications of professional interest to its membership. It represents academic library concerns to other Sections within the SCLA as well as to groups and persons outside the Association."""

    st.write(college_uni_info)

    st.divider()

    college_uni_table = [
        ("Chris Vidas", "Chair", "cvidas@clemson.edu"),
        ("April Hobbs", "Secretary", "hobbsap@musc.edu"),
    ]
    college_uni_df = pd.DataFrame(college_uni_table, columns=["Name", "Title", "Email"])

    st.table(college_uni_df, border="horizontal")
    st.write(
        "The College & University Section is working to recruit officers for 2025. Below is some information about what each officer does:"
    )

    with st.container(border=True):
        st.subheader("Chair")
        chair_str = """Being chair of a section means that you are on the SCLA Board and have voting privileges! This is a wonderful way to get involved in SCLA! The board meets quarterly, sometimes in person and sometimes virtually. Also, as chair, it is your responsibility to schedule and run meetings for the section. Last year, we met approximately every two months, but it is up to the section leadership to decide how often you would like to meet and what you would like to do as a section. The chair does have to submit a couple of reports during the year. First, as the College and University section of SCLA, we are a chapter of ACRL. It is necessary to submit a report to SCLA during the summer to receive funding from ACRL. The chair must also submit an annual report to SCLA. This is done in the fall."""
        st.write(chair_str)

        st.subheader("Vice-chair")
        vice_chair_str = """As vice chair, you are responsible for taking over the role of chair if that person cannot fulfill their duties."""
        st.write(vice_chair_str)

        st.subheader("Program coordinator")
        program_coordinator_str = """This person is responsible for programming during the year. It is up to section leadership to determine what programs the section will offer during the year. The program coordinator may contact potential speakers, set up webinars, and/or create advertisements."""
        st.write(program_coordinator_str)

        st.subheader("Secretary")
        secretary_str = """The secretary takes minutes at all meetings (officer meetings and general meetings) and participates in leadership decisions."""
        st.write(secretary_str)

with st.expander("Library Management Section"):
    st.header("Library Management Section")
    library_mgmt_info = """The Library Management Section serves all persons interested in all areas of library administration. It strives to provide opportunities for dialogue, continuing education, and activities which increase its members' knowledge in this area. The Section recognizes the following fields as especially pertinent to its scope: management, personnel, budgeting, facilities design, planning, grantsmanship, public relations, interlibrary cooperation, application of technological devices, and censorship."""
    st.write(library_mgmt_info)

    st.subheader("Past Trainings")
    st.table(
        {
            "Topic": "Leading from the Top, a dicsussion with SC library leaders",
            "Date": "September 19, 2023",
            "Zoom webinar": "[Watch the webinar here](https://drive.google.com/file/d/1cBtxFxpvJ3LNj8Y6OpCyqRlqdMZNB8P7/view?usp=sharing)",
            "Additional materials": "[View additional materials here](https://www.canva.com/design/DAFtH_W0mVM/m2EA_NZZ91Cdc04TssFYTQ/view?utm_content=DAFtH_W0mVM&utm_campaign=share_your_design&utm_medium=link&utm_source=shareyourdesignpanel#1)",
        },
        border="horizontal",
    )

    st.divider()

    library_mgmt_table = [
        ("Tracey L. Elvis-Weitzel", "Chair", "elvist@horrycounty.sc.gov"),
        ("Theresa Wagner", "Vice-Chair", "wagnert@ccpl.org"),
        ("Jessica Duzan", "Secretary", "j.duzan@saludacounty.sc.gov"),
    ]
    library_mgmt_df = pd.DataFrame(
        library_mgmt_table, columns=["Name", "Title", "Email"]
    )

    st.subheader("2026 Officers")
    st.table(library_mgmt_df, border="horizontal")

with st.expander("Public Library Section"):
    st.header("Public Library Section")
    public_lib_info = """It is the purpose of the Public Library Section to promote public libraries, to advocate ways to improve library service in South Carolina, to provide a forum for the exchange of ideas among public librarians, to complement and supplement continuing education activities, and to support the work of the South Carolina Library Association."""
    st.write(public_lib_info)

    st.divider()

    public_lib_table = [
        ("Kate Dentzman", "Co-Chair", "dentzmank@ccpl.org"),
        ("Lindsay Kesten", "Co-Chair", "kestenl@ccpl.org"),
    ]
    public_lib_df = pd.DataFrame(public_lib_table, columns=["Name", "Title", "Email"])

    st.subheader("2026 Officers")
    st.table(public_lib_df, border="horizontal")

    st.markdown(
        r"![Graphic calling all SCLA members to help shape a new mentorship program](https://www.scla.org/assets/images/PLS_Mentorship%20survey_web.png)"
    )
    st.link_button(
        "Take the Public Library Section Mentorship Survey",
        "https://docs.google.com/forms/d/e/1FAIpQLSf7bHlRrsGHWrrZbaqW9T9a0E97zwS9z9J9TJdzNhTe2S6ggQ/viewform",
    )

    st.divider()

    st.subheader("Upcoming Meetings and Trainings")

    st.write(
        "Welcome to a new year with the Public Library Section! Please join us for our next virtual meeting of the year via Teams, on Wednesday, May 27, at 2:00 pm EST.\n\nEmail [Kate](mailto:dentzmank@ccpl.org) or [Lindsay](mailto:kestenl@ccpl.org) with any questions. We look forward to seeing you then!"
    )

    st.table(
        {
            "Date": "Wednesday, May 27, 2026",
            "Time": "2:00 pm - 3:00 pm",
            "Location": "Microsoft Teams. Link TBA.",
        },
        border="horizontal",
    )

    public_lib_meetings = """**Other upcoming meetings:**\n\n- Wednesday, August 19 at 2:00 pm EST\n\n- Wednesday, October 7 at 2:00 pm EST"""
    st.markdown(public_lib_meetings)

with st.expander("Public Services Section"):
    st.header("Public Services Section")
    public_serv_info = """It is the purpose of the Public Services Section to promote and improve library functions that involve direct contact between the library and the library user. The Section seeks to stimulate and support high standards of service and sensitivity to the viewpoint of their users in all types of libraries. In fulfilling its purpose the Section accepts the responsibility of promoting communication and an active exchange of ideas among its membership. Specifically, it regularly provides programs of continuing education and encourages the creation and dissemination of publications relating to the professional interests of its members. The Section also endeavors to define and advance the concepts of interlibrary and interlibrary cooperation."""
    st.write(public_serv_info)

with st.expander("Youth Services Section"):
    st.header("Youth Services Section")
    youth_serv_info = """The purpose of the Youth Services Section is to promote improved library service to the state's children and young people by providing opportunities for its members to increase their understanding of the library needs of children and young people, their knowledge of materials and services, their awareness of current issues that affect and interest their patrons, and their working skills as facilitators of the educational process and as specialists in public libraries and schools. It also fosters cooperation between school and public libraries in the state.\n\n- [December 2017 Multitasker newsletter](https://www.scla.org/assets/docs/SCLA%20YSS%20December%20Newsletter%202017.pdf)\n- [August 2017 Multitasker newsletter](https://www.scla.org/assets/docs/SCLA%20YSS%20Summer%20Newsletter%202017%20pdf.pdf)\n- [December 2016 Multitasker newsletter](https://www.scla.org/assets/docs/SCLA%20YSS%20December%20Newsletter%202016.pdf)"""
    st.markdown(youth_serv_info)

    st.write(
        "The next **Youth Services Section** meeting will be virtual on **May 12, 2026** at **1:00 pm EST**."
    )
    st.link_button(
        "Meeting Link",
        "https://teams.microsoft.com/l/meetup-join/19%3ameeting_YmYzMjU4OGYtZjZiYi00NGM5LTg2YTMtZjY4M2I4ZTc2NWEw%40thread.v2/0?context=%7b%22Tid%22%3a%22c85b3d71-ec48-406a-9e99-909081e47737%22%2c%22Oid%22%3a%22c4923940-753d-43fa-b888-8cb26444b517%22%7d",
    )

    st.divider()

    youth_serv_table = [
        ("Christine LaLonde", "Chair", "lalondec@ccpl.org"),
        ("Ashley Silvera", "Vice-Chair", None),
        ("Susie Baker", "Secretary", None),
        ("Robin Woods", "Membership", None),
        ("Jimmy McClellan", "Program Manager", None),
        ("Anna Brannin", "Advisor", None),
    ]
    youth_serv_df = pd.DataFrame(youth_serv_table, columns=["Name", "Title", "Email"])

    st.subheader("2026 Officers")
    st.table(youth_serv_df, border="horizontal")

with st.expander("Technical Services Section"):
    st.header("Technical Services Section")
    tech_serv_info = """The purpose of the SCLA Technical Services Section is to provide a forum for discussion of issues related to collection development; the acquisition of library materials, including serials; preservation; automation and cataloging. It is dedicated to the coordinated development of library resources in South Carolina and to ready access to such resources. The Section is to promote communication, to encourage cooperation, and to provide programs for continuing professional growth for librarians in South Carolina in the areas of collection development and management, acquisitions, cataloging, serials, preservation, and automation. The Section members also seek to represent library technical services issues to other Sections within the Association, as well as to groups and persons outside the Association. To help meet these goals, concentrated effort is made to assure applicable programs for conferences and workshops."""
    st.write(tech_serv_info)

    st.subheader("Documents")
    st.link_button(
        "Technical Services Section Bylaws",
        "https://www.scla.org/assets/docs/20041029_scla_tss_bylaws.pdf",
    )
    st.link_button(
        "2014 Annual Report",
        "https://www.scla.org/assets/docs/scla%20technical%20services%20section%20meeting%20notes.pdf",
    )
    st.link_button(
        "2013 Annual Report",
        "https://www.scla.org/assets/docs/scla%20technical%20services%20section%202013%20annual%20report.pdf",
    )
    st.link_button(
        "2012 Annual Report",
        "https://www.scla.org/assets/docs/2012_scla_tss_annual_report.docx",
    )
    st.link_button(
        "2011 Annual Report",
        "https://www.scla.org/assets/docs/2011_scla_tss_annual_report.docx",
    )
    st.link_button(
        "2011 Annual Meeting Minutes",
        "https://www.scla.org/assets/docs/201110_scla_tss_minutes.docx",
    )

    st.subheader("SCLATECH-L Listserv")

    tech_serv_listerv = """The South Carolina Library Association Technical Services Section has an unmoderated forum for communication among libraries. [SCLATECH-L@listserv.sc.edu](mailto:SCLATECH-L@listserv.sc.edu) is used for announcements regarding the Technical Services Section, discussions pertaining to issues in technical services, or just general questions about acquisitions, cataloging, or the like. The listserv is programmed to archive copies of every message sent through it, so you can search old messages if you do not want to keep all of the messages yourself."""
    st.markdown(tech_serv_listerv)

    st.write("**To subscribe:**")
    tech_serv_sub = """Send the message SUBSCRIBE SCLATECH-L first name last name (substituting your own information for “firstname” “lastname”) to [LISTSERV@LISTSERV.SC.EDU](LISTSERV@LISTSERV.SC.EDU). Leave the Subject field blank. Make sure no other information (e.g. e-mail signature) is included with the message. A confirmation message will be e-mailed to you by the LISTSERV software."""
    st.markdown(tech_serv_sub)

    st.write("**To post a message to the list:**")
    tech_serv_post = """- Send e-mail to [SCLATECH-L@LISTSERV.SC.EDU](mailto:sclatech-l@listserv.sc.edu)\n- By default, replies to messages from the list go to all subscribers to the list, not just the original sender\n- List owner is Scott Phinney, Head of Cataloging, University of South Carolina, [phinney@mailbox.sc.edu](mailto:phinney@mailbox.sc.edu)"""
    st.markdown(tech_serv_post)
