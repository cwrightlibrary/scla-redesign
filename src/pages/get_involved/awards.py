import pandas as pd
import streamlit as st

st.title("Awards")

st.header("2025 SCLA Award Winners")
st.write("Congratulations to our 2025 award winners who are listed below.")
st.image("src/images/Awards 2025 Header.png")

st.subheader("Friend of Libraries Award")
st.success(":material/celebration: **2025 Award Winner**\n\nFriends of the Union County Carnegie Library, Union County Library System")
st.write("The SCLA Friend of Libraries Award recognizes outstanding service to a library or libraries which furthered the expansion of library services in South Carolina. The contribution made by the person or organization may include, but not be limited to: financial benevolence, advocacy/promotion, or creative/innovative initiatives, programs, or events.")
st.write("This award will be presented at the annual SCLA Conference to a deserving nominee that meets the following criteria:")
st.markdown("""A person or organization deemed to be a "friend" to any type of library (academic, public, school, or special) or to the library profession as a whole. e.g. a Friends of the Library Group, a volunteer, a legislator, a donor\n- Activities within the past five years are eligible for consideration\n- Individuals or teams may nominate themselves or be nominated by others.""")

st.subheader("Hall of Fame Award")
st.success(":material/celebration: **2025 Award Winners**\n\n- Clo Cammarata, Program and Events Manager, Richland Library\n- Tucker Taylor, Editor-in-Chief, Journal of Copyright in Education and Librarianship")
st.write("The SCLA Hall of Fame recognizes current or past SCLA member(s) with a long-standing, distinguished record of professional achievements and accomplishments. This Award is open to both librarians and library workers who have made a substantial, lasting impact through their work within South Carolina libraries. Multiple nominees may be inducted each year if appropriate.")
st.write("This award will be presented at the annual SCLA Conference to deserving nominee(s) that meet the following criteria:")
st.markdown("""A current or retired member of SCLA\n- At least ten years of experience working at any South Carolina library\n- Significant career accomplishments and contributions to the development of library and information services in their local community, the state of South Carolina, and/or the nation\n- Leadership and service contributing to the advancement of the goals and objectives of the South Carolina Library Association\n- Individuals must be nominated by others.""")

st.subheader("Intellectual Freedom Award")
st.success(":material/celebration: **2025 Award Winner**\n\nStephanie Howard, Director, Pickens County Library System")
st.write("The SCLA Intellectual Freedom Award recognizes members of our community who have contributed to an awareness of intellectual freedom and censorship issues in South Carolina libraries. Such contributions may include: demonstration of related advocacy, programs, service, educational workshop, or promotion or legislative support on the local, state, or national level.")
st.write("This award will be presented at the annual SCLA Conference to a deserving nominee that meets the following criteria:")
st.markdown("""- Any member of the community, library worker or not, who has contributed to upholding the principles of intellectual freedom\n- Activities within the past five years are eligible for consideration\n- Individuals must be nominated by others""")

st.subheader("Legacy of Service Award")
st.success(":material/celebration: **2025 Award Winners**\n\n- Mary Daubenspeck, Systems & E-Resources Librarian, Spartanburg Community College (30 years of service)\n- Eva Pough, Information Specialist, University of South Carolina (31 years of service)\n- Mary Jones, Information Specialist, University of South Carolina (31 years of service)\n- Rayburne Turner, Branch Manager of the Otranto Road Library, Charleston County Public Library (32 years of service)\n- Gwen Wright, Outreach Associate, Charleston County Public Library (33 years of service)\n- Steven C. Sims-Brewton, Head of Access Services, Librarian, and Associate Professor, Francis Marion University (34 years of service)\n- Clo Cammarata, Programs and Events Manager, Richland Library (34 years of service)\n- Paula Childers, Youth Services Coordinator, Florence County Public Library (35 years of service)\n- Teri Alexander, Director of Learning Environments, Clemson University (37 years of service)\n- Carrie Smalls, Adult Services Specialist, Charleston County Public Library (39 years of service)\n- Ed Babinski, Circulation Services and Interlibrary Loan Specialist, Furman University (41 years of service)\n- Alfreda Doyle, Children's Services Associate, Charleston County Public Library (46 years of service)\n- Wesley Sparks, Cataloger, South Carolina State Library (49 years of service)\n- Nancy Berry, Deputy Director, Lancaster County Library (51 years of service)\n- Jimmy Smith, Interlibrary Loan and Government Documents Librarian, Greenville County Public Library (56 years of service)")

st.subheader("New Librarian Award")
st.success(":material/celebration: **2025 Award Winner**\n\nMadison Gaskins, Teen Services Manager, Charleston County Public Library")
st.write("The SCLA New Librarian Award recognizes the achievements of librarians (with an MLIS or equivalent degree) who are already making significant contributions to the field early in their careers. Such contributions may include: demonstrating leadership in innovative programs or services, contributing to their library’s impact on its community, and/or promoting the profession through teaching or professional writing.")
st.write("This award will be presented at the annual SCLA Conference to a deserving nominee that meets the following criteria:")
st.markdown("""A current employee of and have at least one year of experience working at any South Carolina library\n- At least one year of experience working at any South Carolina library\n- Five or fewer years of post-graduate (MLIS or equivalent degree) library experience\n- Individuals must be nominated by others.""")

st.subheader("Outstanding Librarian Award")
st.success(":material/celebration: **2025 Award Winner**\n\nKathleen Montgomery, Associate Director, Community Engagement, Charleston County Public Library")
st.write("The SCLA Outstanding Librarian Award recognizes and honors a mid-career librarian (with an MLIS or equivalent degree) whose work has enduring value. Such contributions may include excellence in leadership, innovative program or service development, impactful advocacy initiatives, or promotion of the profession through teaching or professional writing.")
st.write("This award will be presented at the annual SCLA Conference to a deserving nominee that meets the following criteria:")
st.markdown("""A current employee of a South Carolina library\n- At least one year of experience working at any South Carolina library\n- Six or more years of post-graduate (MLIS or equivalent degree) library experience\n- Nominees without an MLIS or equivalent degree, but who meet all other requirements, may be considered\n- Activities within the past five years are eligible for consideration\n- Individuals must be nominated by others.""")

st.subheader("Outstanding Library Staff Award")
st.success(":material/celebration: **2025 Award Winner**\n\nRobyn Andrews, Coordinator for Circulation and Research Services, Furman University")
st.write("The SCLA Outstanding Library Support Staff Award recognizes the achievements of a library support staff member. Such contributions may include: excellent performance in their field of expertise, demonstration of leadership, innovations in customer service (internal and external) or technical service, development of new programs or services, or advocacy initiatives.")
st.write("This award will be presented at the annual SCLA Conference to a deserving nominee that meets the following criteria:")
st.markdown("""A current employee of a South Carolina Library\n- At least one year of experience working at any South Carolina library\n- Employed in a library position that does not require an MLIS or equivalent degree\n- Activities within the past five years are eligible for consideration\n- Individuals must be nominated by others.""")

st.subheader("Student Award")
st.success(":material/celebration: **2025 Award Winner**\n\nJennifer Jean, Statewide Services Coordinator, South Carolina State Library")
st.write("The SCLA Student Award recognizes a student who demonstrates dedication to the profession, is actively engaged in professional development, and is making important or innovative contributions to the field of librarianship or information science during their course of study.")
st.write("This award will be presented at the annual SCLA Conference to a deserving nominee that meets the following criteria:")
st.markdown("""- A full-time or part-time graduate student working towards the completion of their MLIS OR an undergraduate student majoring or minoring in library science\n- A current employee, volunteer, or intern at any South Carolina library\n- Individuals must be nominated by others""")

st.subheader("2025 Honorable Mentions")
st.table(pd.DataFrame([
    ("Friends of the Library Award", "Kathy Hunter, Library Friends and Campaign Cabinet Member, Clemson University"),
    ("New Librarian Award", "Bailey Pierce, Adult Services Librarian, Charleston County Public Library"),
    ("Outstanding Library Support Staff", "Bailey Pierce, Adult Services Librarian, Charleston County Public Library")
], columns=["Award", "Honorable Mention"]), border="horizontal")
