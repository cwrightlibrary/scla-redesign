import pandas as pd
import streamlit as st

st.title("Committees")

with st.expander("Advocacy Committee"):
    st.header("Advocacy Committee")

    st.subheader("Important Advocacy Links")
    st.link_button("ALA Advocacy Website", "http://www.ala.org/advocacy/")
    st.link_button("Libraries to Transform Tool Kit", "http://www.ilovelibraries.org/librariestransform/toolkit")
    st.link_button("Letters to Senators", "http://www.senate.gov/general/contact_information/senators_cfm.cfm")
    st.link_button("ALA Advocacy ToolKit", "http://www.ala.org/advocacy/advleg/advocacyuniversity/frontline_advocacy")
    st.link_button("Advocacy University", "http://www.ala.org/advocacy/advocacy-university")
    st.link_button("iLoveLibraries.org", "http://www.ilovelibraries.org/")

    st.subheader("Censorship and Challenged Resources Links")
    st.table(pd.DataFrame([
        ("Report a Censorship Challenge", "[ALA Report](https://www.ala.org/tools/challengesupport/report)"),
        ("Request Assistance from SCLA", "scla.advocacy@gmail.com")
    ], columns=["Resource", "Link"]), border="horizontal")

    st.divider()

    st.subheader("SCLA Advocacy Committee News and Resources")
    with st.container(border=True):
        st.iframe("https://docs.google.com/document/d/1L9AYnN7HUesvBI88aLbVmFEtBEjJWF1BPR1pg_6kpBU/edit")
    
    with st.container(border=True):
        st.iframe("https://www.billtrack50.com/public/stakeholderpage/RxYFRIyOG0ikUlAP1qq0fA/embed")
    
    st.divider()

    st.subheader("Past Advocacy Campaign Materials")
    st.link_button("SC Library Advocacy Campaigns", "https://uscupstate.libguides.com/SCLibraries")
    st.link_button("SCLA's Advocacy Committee", "https://scholarcommons.sc.edu/uplib_facpub/1/", help="Campaign Efforts and Best Practices")

    st.subheader("Related South Carolina Library Organizations")
    st.link_button("SCLA of School Librarians", "http://www.scasl.net/advocacy-committee")
    st.link_button("Partnership Among South Carolina Academic Libraries", "http://pascalsc.libguides.com/teams")
    st.link_button("South Carolina State Library Funding Resource Page", "http://www.statelibrary.sc.gov/library-funding")
    st.link_button("Friends of South Carolina Libraries", "http://www.foscl.org/home.html")
    st.link_button("South Carolina Center for Community Literacy", "https://sc.edu/study/colleges_schools/cic/library_and_information_science/literacy/south_carolina_center_for_community_literacy/")
    st.link_button("Get Ready Stay Ready", "https://www.getreadystayready.info/")


with st.expander("Archives and History Committee"):
    st.header("Archives and History Committee")

    st.subheader("2025 Officers")
    st.table(pd.DataFrame([
        ("Warren Cobb", "warren.a.cobb@gmail.com")
    ], columns=["Name", "Email"]), border="horizontal")

    st.subheader("Membership")
    st.write("SCLA Executive Director, the chair of the Archives and Special Collections Round Table, and four other members who shall serve staggered terms of office.")

    st.subheader("Duties")
    st.markdown("""- To ensure the integrity of the Association's records by gathering annual reports and records of association officers, Section, Round Tables, and Committees. In order to do this the chair of the committee will edit and publish the report in NEWS AND VIEWS at the end of each year. The records will be systematically transferred at the end of each year to the association's archives\n- To encourage interest in the history of the association, in particular, and the profession in SC in general, the committee will encourage research and writing about the association and the profession in SC. This can include, but is not limited to, the sponsorship of essays, bibliographies, oral histories, and exhibits for the widest possible exposure in the profession""")

with st.expander("Awards Committee"):
    st.header("Awards Committee")

    st.subheader("2026 Officers")
    st.table(pd.DataFrame([
        ("Halley Repasch", "Chair", "repaschh@ccpl.org"),
        ("Esther Burgess", None, None),
        ("Aaliyah Day", None, None),
        ("McKenzie Lemhouse", None, None),
        ("Jessica Kohout-Tailor", None, None),
        ("Ash Vaugh", None, None)
    ], columns=["Name", "Title", "Email"]), border="horizontal")

    st.subheader("Membership")
    st.write("Six members of the Association, preferably representing the various Sections and Round Tables.")

    st.subheader("Committee Charge")
    st.write("The Awards Committee is a standing committee of the South Carolina Library Association. It is authorized by and accountable to the SCLA Executive Board for selecting and recommending recipients for annual awards of recognition.")

    st.subheader("Duties")
    st.markdown("""1. Coordinates all aspects of the SCLA awards program.\n2. Solicits and reviews award applications and recommends award winners.\n3. Helps coordinate an event at the SCLA annual conference to recognize award winners.""")

    st.subheader("SCLA Awards 101 Training")
    st.write("Watch this video from our YouTube channel to learn how to nominate someone for an SCLA Award. We’ll walk you through the award categories, how to submit a nomination, tips for creating a strong submission, and what happens after you apply.")
    st.link_button("SCLA Awards 101 Training", "https://youtu.be/AI6comtSUkM", type="primary")

with st.expander("Conference Planning Committee"):
    st.header("Conference Planning Committee")

    st.subheader("Membership")
    st.write("First Vice-President/President Elect shall serve as the Chair of the Conference Planning Committee. The Executive Director and Treasurer will also serve. The Publicity Committee will provide advertisement and coverage of the conference. The President, with input from the Chair, shall appoint a Local Arrangements Chair, Exhibits Chair, Registration Chair, and Poster Session Chair. The Local Arrangements Chair must be from the conference city.")

    st.subheader("Duties")
    st.write("The duties of the Conference Program Committee are to coordinate all of the events at the annual conference. Sections, Round Tables, and Committee Chairs work with the Conference Planning Chair to provide programming at the conference. The Committee will work with the conference site to provide for meal events and receptions and will coordinate poster sessions, registration, and exhibitors.")

    st.subheader("Officers")
    st.table(pd.DataFrame([
        ("Shamella Cromartie", "First Vice-President/Conference Chair", "scla1stvp@gmail.com"),
        ("Kristin Amsden", "Registration team", None),
        ("Jessica Serrao", "Registration team", None),
        ("Beka Darrah", "Registration team", None),
        ("Renna Redd", "Session Coordinator", None),
        ("Gerald Moore", "Session planning committee", None),
        ("Amber Conger", "Session planning committee", None),
        ("Aleck Williams", "Session planning committee", None),
        ("Lindsay Kesten", "Session planning committee", None),
        ("Mary Horton", "Session planning committee", None),
        ("Leigh Ramey", "Session planning committee", None),
        ("Jonathan Newton", "Session planning committee", None),
        ("Brittany Champion", "Session planning committee", None),
        ("Ray Turner", "Session planning committee", None),
        ("Sonaite Debebe-Kumssa", "Marketing Chair", None),
        ("Lindsey Taunton", "Conference Photographer", None),
        ("Caroline Smith", "Poster Session Co-Chair", None),
        ("Karen Burton", "Poster Session Co-Chair", None),
        ("Christy Allen", "Awards Committee Chair", None),
        ("Cathi Mack", "Scholarship for Diversity Chair", None),
        ("Ariel Turner", "Sponsorship Co-Chair", None),
        ("Chris Vinson", "Sponsorship Co-Chair", None),
        ("Gerald Moore", "All-Conference Reception/Special Events Co-Chair", None),
        ("Ray Turner", "All-Conference Reception/Special Events Co-Chair", None),
        ("Amanda Myers", "Happy Learning Hour Chair", None),
    ], columns=["Name", "Title", "Email"]), border="horizontal")

with st.expander("Constitution, Bylaws, and Handbook Revision Committee"):
    st.header("Constitution, Bylaws, and Handbook Revision Committee")

    st.subheader("2025 Officers")
    st.table(pd.DataFrame([
        ("Tucky Taylor", "Chair", "tucker@jcel.org"),
        ("Sonaite Debebe-Kumssa", "Secretary", "sdebebe-kumssa@richlandlibrary.com")
    ], columns=["Name", "Title", "Email"]), border="horizontal")

    st.subheader("Membership")
    st.write("Six members of the Association and the Executive Secretary (as non-voting ex-officio member).")

    st.subheader("Duties")
    st.markdown("""- Makes a continuing study of the Constitution and Bylaws and recommends to the Executive Board desirable revisions to facilitate the proper functioning of the Association and its parts\n- Forwards proposed changes or revisions to the Constitution, Bylaws or Handbook to the First Vice-President for inclusion in the call to the conference\n- Presents proposed changes and revisions and other items to the membership for action if instructed by the Executive Board\n- Monitors the accuracy and availability of the SCLA Handbook in both print and electronic formats\n- Approved changes to the SCLA Handbook will be incorporated into the published texts in a timely fashion""")

with st.expander("Continuing Education Committee"):
    st.header("Continuing Education Committee")

    st.subheader("Membership")
    st.write("Membership shall include four members representing the different types of libraries; one representative each from the S.C. State Library and the USC School of Information Science; with both the First Vice-President and the Executive Director serving ex officio.")

    st.subheader("Duties")
    st.markdown("""- Evaluates the continuing education needs of South Carolina librarians and makes recommendations and suggestions to the various Sections, Round Tables, and Committees of SCLA\n- Endeavors to assure quality in continuing education activities by providing guidelines, training, and information to the Sections, Round Tables, and Committees\n- Evaluates continuing education activities in conjunction with Sections, Round Tables, and Committees and to report findings of the same\n- Coordinates continuing education activities and maintains records on programs, providers, and resources\n- Publicizes and promotes continuing education activities and opportunities""")

    st.subheader("2025 Officers")
    st.table(pd.DataFrame([
        ("Lea Stapleton", "Chair", "lstapleton@richlandlibrary.com"),
        ("Lisa Gieskes", "Chair", "lgieskes@richlandlibrary.com"),
        ("Melanie Griffin", "Chair", "mgriffin@statelibrary.sc.gov"),
        ("Amy Misenheimer", "Chair", "misenheimera@ccpl.org")
    ], columns=["Name", "Title", "Email"]), border="horizontal")

    st.subheader("Upcoming Learning Opportunities")
    st.link_button("South Carolina State Library Continuing Education Training and Events", "https://www.statelibrary.sc.gov/libraries-librarians/professional-development/continuing-education")
    st.link_button("Maine State Library Continuing Education Calendar", "https://maine-msl.libcal.com/calendar?cid=10791&t=m&d=0000-00-00&cal=10791&inc=0")

with st.expander("Financial Planning and Development Committee"):
    st.header("Financial Planning and Development Committee")

    st.subheader("Membership")
    st.write("The Committee consists of the current SCLA President who serves as the chair, the 1st Vice-President, the immediate Past-President, the Treasurer, Chair of the Planning Committee, and four members from the Association.")

    st.subheader("Duties")
    st.markdown("""- Studies the financial posture of the Association and advises the Executive Board on expenditures and other budgetary matters including a yearly operating budget and a conference budget\n- A subcommittee of the Financial Planning and Development Committee shall conduct an annual financial audit or review\n  - The subcommittee shall consist of the Chair of the Financial Planning and Development Committee, the First Vice-President, and two members from the Financial Planning and Development Committee\n  - The Treasurer shall serve ex-officio on the subcommittee\n- Coordinates the on-going planning of functions in Committees and Sections well in advance of the date in order to pursue grants from foundations and other sources for funding such projects or workshops\n- Pursues as an on-going charge the work of obtaining grants for the Association for the endowment and general expenditures of the Association, consistent with our role as a non-profit organization. Special contributions, legacies, and memorials should be sought\n- Provides leadership in financial planning for the Association and recommends changes in revenues, and financial structure to the Association""")

with st.expander("Intellectual Freedom Committee"):
    st.header("Intellectual Freedom Committee")

    st.subheader("Membership")
    st.write("Six members of the Association")

    st.subheader("Duties")
    st.markdown("""- Promotes greater awareness among SCLA members of intellectual freedom and censorship of libraries and librarians\n- Recommends to the Association and to the Executive Board such steps as may be necessary to safeguard the rights of library users, libraries, and librarians\n- Aids libraries and librarians involved in intellectual freedom or censorship problems when assistance is formally requested\n- Fully informs the President and Executive Board of the committee's proceedings""")

    st.divider()

    st.subheader("Intellectual Freedom Award")
    st.write("Consider nominating a colleague or community member for this year's Intellectual Freedom Award! Details and due date coming soon.")

    st.write("**Previous Award Recipients:**")

with st.expander("Library and Personnel Standards Committee"):
    st.header("Library and Personnel Standards Committee")

with st.expander("Marketing Committee"):
    st.header("Marketing Committee")

with st.expander("Nominating Committee"):
    st.header("Nominating Committee")

with st.expander("Scholarship for Diversity Committee"):
    st.header("Scholarship for Diversity Committee")

with st.expander("Sponsorship Committee"):
    st.header("Sponsorship Committee")