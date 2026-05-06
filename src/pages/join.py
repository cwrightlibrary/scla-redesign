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

st.title("Join SCLA")

join_info = """SCLA is the state’s premier library association. We are a group of librarians, library staff members, and library supporters working together to advocate for and improve library services in South Carolina. If you’re visiting this site, you must care about libraries, and that means **SCLA is for you!**"""
st.markdown(join_info)

with st.expander("Individual Memberships"):
    st.header("Individual Memberships")
    membership_info = """**As a member, you will benefit from:**\n\n- advocacy efforts on behalf of South Carolina libraries and library staff\n- leadership and professional development opportunities\n- partnerships and collaboration with library leaders from across our state\n- reduced registration fees for attendance at our outstanding annual conference"""
    st.markdown(membership_info)

    join_renew_info = """**To join or renew**, [use our easy online membership](https://www.scla.org/membership-application) form or this [printable version](https://www.scla.org/assets/membership/SCLA_Individual%20Membership%20Application_Updated10062025.pdf) you can mail. If you have any questions or concerns, please reach out to our 2nd VP/Membership Chair and/or our Executive Director [Courtney Waldrup](mailto:cwaldrup@pmpamc.com), and they'll be happy to assist."""
    st.markdown(join_renew_info)

    st.markdown(
        "**Library school students**, please see below information about our joint membership opportunities."
    )

    st.subheader("Individual Pricing")
    individual_membership_table = [
        ("First-time Member (1 year only)", "$25.00"),
        ("Full-time Student", "$30.00"),
        ("Retiree/Friend/Student", "$35.00"),
        ("Individual Exhibitor", "$35.00"),
        ("Library Staff Member", "See salary scale below"),
    ]
    individual_membership_df = pd.DataFrame(
        individual_membership_table, columns=["Membership Type", "Price"]
    )
    st.table(individual_membership_df, border="horizontal")

    st.subheader("Salary Scale")
    individual_salary_table = [
        ("\\$0-$19,999", "$35.00"),
        ("$20,000+", "$50.00"),
        ("$40,000+", "$65.00"),
        ("$60,000+", "$80.00"),
        ("$80,000", "$125.00"),
        ("Sustaining Membership", "$125.00"),
    ]
    individual_salary_df = pd.DataFrame(
        individual_salary_table, columns=["Salary", "Price"]
    )
    st.table(individual_salary_df, border="horizontal")

with st.expander("Institutional Memberships"):
    st.header("Institutional Memberships")

    st.write(
        "Institutional membership rates are calculated on the library's total annual budget."
    )

    inst_table = [
        ("\\$1-$50K", "$150.00"),
        ("\\$51K-$100K", "$225.00"),
        ("\\$101K-$500K", "$300.00"),
        ("\\$501K-$1M", "$575.00"),
        ("\\$1.1M-$3M", "$1,500.00"),
        ("\\$3.1M-$10M", "$3,000.00"),
        ("Sustaining Institution", "$4,000.00"),
    ]
    inst_df = pd.DataFrame(inst_table, columns=["Budget", "Price"])
    st.table(inst_df, border="horizontal")

    st.write("**Benefits to Institutions:**")
    inst_bens = """- Convenient and cost-effective way to pay for staff memberships in a single transaction\n- All staff (including part-time) receive the full benefits of SCLA Membership\n- Pay the member rate at the SCLA Conference for all staff members\n- Professional development and training opportunities throughout the year\n- Attract staff\n- Sustaining Institutions will be recognized on the SCLA website and at the annual conference"""
    st.markdown(inst_bens)

    st.write("**Benefits to Staff:**")
    inst_bens_staff = """- Full benefits of SCLA Membership at no individual cost to them\n- Opportunities to participate in SCLA and contribute to the profession\n- Opportunities for professional development and growth\n- Networking opportunities with colleagues from across the state\n- Access to support and resources of SCLA"""
    st.markdown(inst_bens_staff)

    st.info(
        ":material/info: To request an Institutional Membership for your library, please contact the Membership Chair at [secondvpscla@gmail.com](mailto:secondvpscla@gmail.com)"
    )

with st.expander("Joint Memberships"):
    st.header("Joint Memberships")

    joint_mem_info = """**Students:** If you’re joining SCLA for the first time and have never been a member of [ALA](http://www.ala.org/), consider a joint membership! Library school students can join both organizations for just $46 annually, including membership in SCLA's [New Members Roundtable](https://www.scla.org/new-members-round-table)."""
    st.markdown(joint_mem_info)

    st.info(
        ":material/info: [Joint membership forms can be submitted online through ALA.](https://www.ala.org/cfapps/jntapp/index.cfm?urlcode=ST-SC)\n\nFor more information on submitting membership forms by mail, see the **Join Offline** section of ALA's [Joint Membership Program site](http://www.ala.org/groups/joint-membership-program)."
    )

st.divider()

st.info(
    ":material/info: Questions? Contact [Courtney Waldrup](mailto:cwaldrup@pmpamc.com) (SCLA Executive Director) to learn more."
)
