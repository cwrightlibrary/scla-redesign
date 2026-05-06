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

st.title("Round Tables")

with st.expander("Round Table for African American Concerns"):
    st.header("Round Table for African American Concerns")
    st.write(
        "The purpose of the Round Table for African American Concerns (RAAC) is to promote the recruitment and retention of minority librarians in South Carolina, support and facilitate library services which will meet the information needs of minorities, encourage dissemination of information resources about minority people to the larger community, provide a mechanism that would encourage minority librarians to participate in local, state, and national associations, and promote libraries as viable institutions in minority communities."
    )

    st.subheader("Annual Reports and Statements")
    st.link_button(
        "Statement of Solidarity",
        "https://www.scla.org/assets/docs/Meeting_Minutes/RAAC_Meeting_Notes/Statement%20for%20Solidarity%20from%20RAAC_6.08.20.pdf",
        help="June 8, 2020",
    )
    st.link_button(
        "2020 RAAC Annual Report",
        "https://www.scla.org/assets/docs/Meeting_Minutes/RAAC_Meeting_Notes/RAAC%202020%20Annual%20Report.docx",
    )
    st.link_button(
        "2019 RAAC Annual Report",
        "https://www.scla.org/assets/docs/Meeting_Minutes/RAAC_Meeting_Notes/RAAC%202019%20Annual%20Report.docx",
    )
    st.link_button(
        "2018 RAAC Annual Report",
        "https://www.scla.org/assets/docs/Meeting_Minutes/RAAC_Meeting_Notes/RAAC%20Annual%20Report%202018_December2018.docx",
    )
    st.link_button(
        "2018 RAAC June Report",
        "https://www.scla.org/assets/docs/Meeting_Minutes/RAAC_Meeting_Notes/RAAC%20Report_June%202018.doc",
    )
    st.link_button(
        "2014 RAAC Annual Report",
        "https://www.scla.org/assets/docs/Meeting_Minutes/RAAC_Meeting_Notes/RAAC%20Annual%20Report_%202014.doc",
    )
    st.link_button(
        "2013 RAAC Annual Report",
        "https://www.scla.org/assets/docs/Meeting_Minutes/RAAC_Meeting_Notes/RAAC%20Annual%20Report_%202013.doc",
    )
    st.link_button(
        "2012 RAAC Annual Report",
        "https://www.scla.org/assets/docs/RAAC%20Annual%20Report_2012.doc",
    )

    st.subheader("2025 Chair")

    st.table(
        {"Dr. Shamella Cromartie": "[scla1stvp@gmail.com](mailto:scla1stvp@gmail.com)"}
    )

with st.expander("Archives and Special Collections Round Table"):
    st.header("Archives and Special Collections Round Table")
    st.write(
        "The purpose of the Archives and Special Collections Round Table of the SCLA is to promote the work and development of Archives and Special Collections in South Carolina; to foster high standards in the preservation of archives, manuscripts, and special collections materials; to develop professional cooperation among those involved with archives and special collections in South Carolina; to encourage the use of archives and special collections in South Carolina; and to work for the objectives of the South Carolina Library Association."
    )

    st.subheader("2025 Chair")

    st.table(
        {"Warren Cobb": "[warren.a.cobb@gmail.com](mailto:warren.a.cobb@gmail.com)"},
        border="horizontal",
    )

with st.expander("Digitization of Cultural Heritage Materials Round Table"):
    st.header("Digitization of Cultural Heritage Materials Round Table")
    st.write(
        "Mission The purpose of the Digitization of Cultural Heritage Materials Round Table of the SCLA is to promote the work, education, training, and development of the digitization of cultural heritage materials in South Carolina; to foster common high standards in the digitization of cultural heritage materials such as archives, manuscripts, and special collections; to encourage and develop professional cooperation among those involved with digitization in South Carolina; to promote collaboration on grant projects for digitization; and to work for the objectives of the South Carolina Library Association."
    )

with st.expander("Rainbow Round Table"):
    st.header("Rainbow Round Table")
    st.write(
        "The Rainbow Round Table of the South Carolina Library Association seeks to serve both professionals and users of libraries in South Carolina with an interest in LGBTQIA+ information or services. The round table promotes nondiscriminatory access to information for LGBTQIA+ individuals and their allies without censorship and strives to provide information about other relevant organizations providing various services for LGBTQIA+ individuals and allies."
    )
    st.link_button(
        "Join Our Facebook Group", "https://www.facebook.com/groups/SCLAGLBTQRT/"
    )

    st.subheader("Goals")
    st.markdown(
        "- To promote nondiscriminatory access to LGBTQIA+ information\n- To prevent censorship of LGBTQIA+ information\n- To direct individuals to other relevant organizations"
    )

    st.subheader("2025 Round Table Contact Information")

    rainbow_table = [
        ("Hanna Broam", "They/them", "Chair", "broamh@ccpl.org"),
        ("Michelle Rubino", "She/her", "Vice-Chair", "michelle.rubino@gvltec.edu"),
    ]
    rainbow_df = pd.DataFrame(
        rainbow_table, columns=["Name", "Pronouns", "Title", "Email"]
    )
    st.table(rainbow_df, border="horizontal")
    st.write(
        "We are currently looking to fill the **Secretary role**. If you're interested in serving as Secretary for the Rainbow Round Table, please email [Hanna Broam](mailto:broamh@ccpl.org)."
    )

    with st.container(border=True):
        st.subheader("Reading Recommendations from the Rainbow Round Table")
        st.image("src/images/Fall in Love (RRT).png")

        rainbow_books_table = [
            ("Pumpkin Spice & Poltergeist", "Ali K Mulford and K. Elle Morrison"),
            ("A Honeyed Light", "Freddie Milano"),
            ("Everything She Does is Magic", "Bridget Morrissey"),
            ("Not Just Gal Pals", "Elizabeth Luly"),
            ("A Curse for Smhain", "Dahlia Donovan"),
        ]
        rainbow_books_df = pd.DataFrame(
            rainbow_books_table, columns=["Title", "Author(s)"]
        )
        st.table(rainbow_books_df, border="horizontal")
        st.info(
            ":material/info: For additional reading recommendations, please check out our [Instagram page](https://www.instagram.com/sclanews/)"
        )

    with st.container(border=True):
        st.subheader("Resources Available in South Carolina")
        st.caption("All resources were updated in Fall 2025")

        rainbow_resources_table = [
            ("[SC Pride](https://scpride.org/)", "Statewide resource"),
            (
                "[SC Black Pride](https://www.facebook.com/southcarolina.blackpride/)",
                "Statewide resource",
            ),
            (
                "[Harriet Hancock Center Foundation](https://harriethancockcenter.org/)",
                "Statewide resource",
            ),
            (
                "[Safe Zone Project-LGBTQ+ Vocabulary: Glossary of Terms](https://thesafezoneproject.com/resources/vocabulary/%20)",
                "Statewide resource",
            ),
            (
                "[Trans in the South: A Guide to Resources and Services](https://southernequality.org/resources/transinthesouth/%20)",
                "Statewide resource",
            ),
            (
                "[PFLAG: Find a Local Chapter](https://pflag.org/findachapter/)",
                "Statewide resource",
            ),
            (
                "[LGBTQ+ Healthcare Directory](https://lgbtqhealthcaredirectory.org/)",
                "Healthcare",
            ),
            ("[Advocates for Trans Equality](https://transequality.org/)", "Legal"),
            ("[LAMBDA Legal](https://lambdalegal.org/)", "Legal"),
            (
                "[Information on Name Changes](https://genderbenders.org/name-change/)",
                "Legal",
            ),
            (
                "[Grand Strand PRIDE](http://www.grandstrandpride.com/)",
                "Coastal region resource",
            ),
            (
                "[Myrtle Beach Horry County Democratic LGBT Committee](https://www.facebook.com/MBLGBTDems/)",
                "Coastal region resource",
            ),
            (
                "[Alliance for Full Acceptance](https://www.affa-sc.org/)",
                "Advocacy and educational",
            ),
            (
                "[Charleston Pride](https://www.charlestonpride.org/)",
                "Advocacy and educational",
            ),
            (
                "[GLMA: Health Professionals Advancing LGBTQ Equality](http://www.glma.org/)",
                "Health",
            ),
            ("[Palmetto Community Care](https://palmettocare.org/)", "Health"),
            (
                "[The Ryan White Wellness Center, Roper St. Francis Healthcare](https://www.ryanwhiteofcharleston.org/)",
                "Health",
            ),
            (
                "[Planned Parenthood: Gender-Affirming Care in Charleston, South Carolina](https://www.plannedparenthood.org/health-center/south-carolina/charleston/29407/charleston-health-center-4288-90860/gender-affirming-care)",
                "Health",
            ),
            (
                "[Lowcountry in Transition](https://www.charlestontranscommunity.org/)",
                "Support groups and social organizations",
            ),
            (
                "[We Are Family](http://www.waf.org/)",
                "Support groups and social organizations",
            ),
            (
                "[QT Summer Camp](https://www.qtcamp.org/)",
                "Support groups and social organizations",
            ),
            ("[AID Upstate](https://www.aidupstate.org/)", "Upstate resource"),
            (
                "[GenderBenders](http://genderbenders.org/index.html)",
                "Upstate resource",
            ),
            (
                "[Local LGBT Resource List](http://genderbenders.org/uploads/3/5/6/6/35662510/local_groups_resource_list-pdf.pdf)",
                "Upstate resource",
            ),
            (
                "[Upstate Facebook Page](https://www.facebook.com/pg/GenderBendersUpstate/about)",
                "Upstate resource",
            ),
            (
                "[Out and About Upstate](https://www.facebook.com/groups/outandaboutupstate/)",
                "Upstate resource",
            ),
            ("[Piedmont Care](http://www.piedmontcare.org/)", "Upstate resource"),
            ("[Upstate Pride](http://www.upstatepridesc.org/)", "Upstate resource"),
        ]
        rainbow_resources_df = pd.DataFrame(
            rainbow_resources_table, columns=["Resource", "Type"]
        )
        st.table(rainbow_resources_df, border="horizontal")

with st.expander("Government Documents"):
    st.header("Government Documents")

with st.expander("Information Literacy"):
    st.header("Information Literacy")

with st.expander("Library Marketing and Outreach"):
    st.header("Library Marketing and Outreach")

with st.expander("New Members"):
    st.header("New Members")

with st.expander("Paraprofessional"):
    st.header("Paraprofessional")
