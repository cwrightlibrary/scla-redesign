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

st.title("Committees")

with st.expander("Advocacy Committee", expanded=True):
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
    st.table(pd.DataFrame([
        (1983, "Pat Scales"),
        (1985, "Melinda Hare"),
        (1987, "Eva Roussos"),
        (1989, "Judy Fitzgerald"),
        (1999, "John Monk"),
        (2001, "Ida Thompson and Betty Garrison"),
        (2003, "Pat Scales"),
        (2005, "J. Rhett Jackson"),
        (2007, "Michael Giller"),
        (2011, "Emily Woody"),
        (2012, "Ellen Stringer"),
        (2013, "Anne C. Lemieux")
    ], columns=["Year", "Recipient"]), border="horizontal")

with st.expander("Library and Personnel Standards Committee"):
    st.header("Library and Personnel Standards Committee")

    st.subheader("Membership")
    st.write("Six members of the Association, preferably representing various Sections and Round Tables and all types of libraries.")

    st.subheader("Duties")
    st.markdown("""- Recommends standards and/or guidelines to enhance South Carolina library services and resources and to improve benefits to South Carolina library personnel\n- Examines various standards and guidelines relevant to libraries\n- Determines the existence of, and works in conjunction with, other similar groups from the various Sections of related organizations\n- Studies library statistics and methods used in reporting and evaluating library services and resources\n- Undertakes specific projects at the request of the Executive Board""")

with st.expander("Marketing Committee"):
    st.header("Marketing Committee")

    st.subheader("2026 Officers")
    st.table(pd.DataFrame([("Lindsey Taunton", "Chair", "ltaunton@richlandlibrary.com")], columns=["Name", "Title", "Email"]), border="horizontal")

    st.subheader("Membership")
    st.write("Three or more members of the Association, preferably representing the various Sections and Round Tables. The Editorial Committee and the Publicity Committee have merged to form the Marketing Committee")

    st.subheader("Duties")
    st.markdown("""- Recommends guidelines for the website, the Association’s official publication, to the Executive Board for approval.\n- Contributes, updates, and maintains content for Association website, including blog posts, calendar events, and contact information.\n- Edits and posts website content submitted by Association members.\n- Assists webmaster in managing mail group memberships, posting shared documents for online access, and recommending website improvements to the Executive Board for approval.\n- Assists Publicity Committee in ensuring publicity of news (especially dates of events) and information on related professional associations in Association website, print publications, and social media outlets.\n- Contacts Sections and Round Tables of the Association for suggested individuals to provide content for the website.\n- Assists the Executive Secretary in the collection of materials for the South Carolina Library Association Archives.\n- Ensures that an official copy of all publications is sent to the Executive Secretary for inclusion in the South Carolina Library Association Archives.\n- Works with the Local Arrangements Committee for the conference to provide publicity.\n- Notifies national publications, Southeastern Library Association, American Library Association, North Carolina Library Association, and Georgia Library Association of SCLA conference dates, place, contact person, and theme.\n- Sends copies of program to presidents of NCLA and GLA.\n- Plans publicity before and during the conference by local media and for statewide distribution.\n- Arranges to have photographs made at the conference.\n- Notifies national publications, ALA, SELA, NCLA and GLA about workshops and other activities of national and regional interest if given enough lead time.\n- Encourages members of SCLA, Committees, Round Tables, and Sections to submit materials which would be of local, regional, or national interest.\n- Notifies regional and national publications about South Carolina librarians in the news and about personnel changes.\n- Notifies South Carolina newspapers of committee appointments and officers of SCLA.\n- Notifies Southeastern Librarian of officers of SCLA.\n- Maintains records of committee work. Transfers five years of working files to successor. Transfers major documents, reports, and correspondence having impact on the history or directions of the committee to archives after five years.\n- Works with Swap and Shop Subcommittee in arranging a Swap and Shop at the conference and in encouraging all types of libraries within the state to submit printed materials to be shared by other libraries.""")

with st.expander("Membership Committee"):
    st.header("Membership Committee")

    st.subheader("2025 Officers")
    st.table(pd.DataFrame([("Jana Stevenson", "Chair", "secondvpscla@gmail.com")], columns=["Name", "Title", "Email"]), border="horizontal")

    st.subheader("Membership")
    st.write("Eight members of the Association and the Second Vice- President. The Second Vice-President as chair shall select members to fill any vacancies. Members shall be representative of all types of libraries and geographical areas of the state. Selections must be approved by the President. The Executive Secretary is a non-voting ex-officio member of the Committee.")

    st.markdown("""Identifies prospective members within the library profession and among related professional organizations and verifies that they are given membership information\n- Arranges for the design, printing and distribution of the membership renewal/application\n- Monitors personnel changes through professional publications and personal contacts and sees that those new to the state or new to the profession receive information about SCLA membership\n- Secures a list of lapsed memberships and verifies that membership information is mailed or given to those on the list\n- Enlists SCLA members as assistants to the committee members for accomplishing the above duties\n  - Second Vice-President approves the selection of the assistants\n  - The assistant works with a committee member to achieve the above-stated goals within the regional area in which the assistant resides""")

with st.expander("Nominating Committee"):
    st.header("Nominating Committee")

    st.subheader("2025 Officers")
    st.table(pd.DataFrame([
        ("Angela Craig", "Nominating Committee Chair", "craiga@ccpl.org"),
        ("Amanda Myers", "Library Management Section Chair", "amyers@richlandlibrary.com"),
        ("Chris Vidas", "College and University Section Chair", "cvidas@clemson.edu"),
        ("Kate Dentzman", "Public Library Section Chair", "dentzmank@ccpl.org"),
        ("Leigh Ramey", "Youth Services Section Chair", "lramey@statelibrary.sc.gov")
    ], columns=["Name", "Title", "Email"]), border="horizontal")

    st.subheader("Membership")
    st.write("The chairs of the Sections with the immediate Past-President of the association serving as chair of the committee.")

    st.subheader("Duties")
    st.markdown("""- Nominates a slate of candidates for each elective position, consideration being given to type of library and geographic distribution\n- Notifies the membership of the slate at least thirty days prior to the annual conference\n- Secures information from Association members about their interests and willingness to serve on association committees, and works with the President in filling committee positions, seeing that the committees are broadly representative of the membership in respect to length and variety of experience, ethnic and geographic distribution, etc""")

with st.expander("Planning Committee"):
    st.header("Planning Committee")

    st.subheader("Membership")
    st.write("Nine members of the Association, representing all types of libraries and all geographical areas of the state. A member may serve another term after a year off the committee.")

    st.subheader("Duties")
    st.markdown("""- Makes recommendations on the basis of periodic surveys of the interests of the membership and of continuous study of the goals and objectives of the Association to the Executive Board of activities and projects for the Association, and refers information to appropriate Committees for study and possible action, (sending a copy of such referrals to the Executive Board)\n- Undertakes specific projects at request of the President""")

with st.expander("Scholarship for Diversity Committee"):
    st.header("Scholarship for Diversity Committee")

    st.subheader("Membership")
    st.write("Six members of the association including a past-president, one member each of the Round Table For African American Concerns (RAAC), the Paraprofessional Round Table, the Public Library Section, the College and University Section, and one member at large. Also, the Director of Development, College of Mass Communications and Information Studies at USC who shall serve as a non-voting ex-officio member.")

    st.subheader("Duties")
    st.markdown("""- To ensure that an annual scholarship is awarded in the name of the South Carolina Library Association to a library school student(s) of an under-represented population at the USC College of Mass Communications and Information Studies. The school's scholarship committee actually makes the award within the parameters of the gift agreement. Priority is to be given to an ALA Spectrum Scholar who is attending the University, and then to South Carolina residents\n- To seek donations of funds to augment the scholarship awards\n- To publicize the awarding of scholarships and present awardees at the Annual Conference\n- To solicit recommendations/nominations for the scholarship.""")

    st.subheader("2025 Officers")
    st.table(pd.DataFrame([("Cathi Mack", "Chair", "ccooopermack@scsu.edu")], columns=["Name", "Title", "Email"]), border="horizontal")

with st.expander("Sponsorship Committee"):
    st.header("Sponsorship Committee")

    st.subheader("Membership")
    st.write("Three or four association members from different types of libraries.")

    st.subheader("Duties")
    st.write("To secure funding for conference events and the general association.")