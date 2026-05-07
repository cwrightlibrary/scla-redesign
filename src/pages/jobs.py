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

st.title("Job Listings")
st.write("The SCLA Job Listings is a list of job announcements for any type of library within South Carolina and the Southeast.")
st.link_button("Submit Job", "https://scala.memberclicks.net/index.php?option=com_mcform&view=form&id=20061", help="Read the job posting guidelines and submit a new job announcement", type="primary")

with st.expander("Innovative Technologies Librarian (Spartanburg, SC)"):
    st.header("Innovative Technologies Librarian (Spartanburg, SC)")
    st.caption("05/04/2026")

    st.subheader("Job Description")
    st.write("The University of South Carolina Upstate seeks an Innovative Technologies Librarian to integrate generative AI, makerspace and digital technologies, and other digital tools and resources into the library’s teaching and learning services.The Innovative Technologies Librarian will be a technology-forward librarian who understands and fosters the ethical, sustainable, and relevant use of technology and artificial intelligence in library services, faculty teaching, and student learning. The contributions of the Innovative Technologies Librarian will have a position and profound impact on student learning and achievement.The Innovative Technologies Librarian will join a team that strongly supports student belonging, well-being, curiosity, retention, and success.This is a 12‑month professional‑track librarian position, filled at the Instructor Librarian rank, and reports to the Dean of the USC Upstate Library. The position is part of the Research Services and Instruction team.")

    st.subheader("Qualifications")
    st.markdown("""- A master’s degree in library or information sciences from an American Library Association (ALA) – accredited institution\n- Minimum of 2 years of experience with teaching, training, and/or public service in an educational or library setting\n- Experience with, or strong interest in, makerspace and digital technologies, including 3D printing and scanning, digitization, augmented and virtual reality, data visualization, podcasting, et al., and their application to faculty teaching and student learning\n- Knowledge of, or strong interest in the application of generative artificial intelligence and large language models to teaching and learning\n- Excellent written and verbal communication skills\n- Excellent organizational, planning, and interpersonal skills\n- A successful background check is required.""")

    st.subheader("Type")
    st.write("Full Time")

    st.subheader("How to Apply")
    st.link_button("Apply Now", "https://uscjobs.sc.edu/postings/204332")
    st.write("To be considered for this position, applicants must complete the online application and attach any materials that are marked as required. Unofficial transcripts should be uploaded under “Other Supporting Documents”. Candidates will be asked during the process to have three confidential letters of recommendation that are signed, dated, and on official letterhead, sent directly to the Chair of the Search Committee (contact information is below).")

    st.header("Salary")
    st.write("N/A")

    st.subheader("Contact")
    st.table(pd.DataFrame([
        ("Erika Montgomery", "Search Committee Chair", "800 University Way, Spartanburg, SC 29303", "864-503-5530", "montgoer@uscupstate.edu")
    ], columns=["Name", "Title", "Address", "Phone", "Email"]), border="horizontal")

with st.expander("Librarian II - Youth Services (Cayce - West Columbia, SC)"):
    st.header("Librarian II - Youth Services (Cayce - West Columbia, SC)")
    st.caption("04/29/2026")

    st.subheader("Job Description")
    st.write("""Seeking an enthusiastic, community minded person who can lead the Youth Services Department at our Cayce - West Columbia Branch. Would be responsible for leading a team of 4 in coordinating and implementing literacy programming for ages birth through Teen. Would be responsible for building and maintaining a diverse and well-rounded collection of youth materials that meets the community’s needs. Would work with area schools and community partners in promoting library services. Would provide Reader’s Advisory and technology assistance with a Youth focus. Would collaborate with the Branch Manager and other branchstaff on branch initiatives and large events. Would serve as manager on duty on a rotating basis.

- Supervises staff of Youth Services department. Includes scheduling staff, instructing, planning,assigning work, maintaining standards, coordinating activities, allocating personnel, acting onemployee problems. Reviews the work of subordinates for completeness and accuracy; evaluates performance and makes recommendations for improvement. Offers training, advice, and assistance as needed. Coaches and mentors subordinates and colleagues. Assists in the interview and training processes for other employees.
- Serves on internal committees and assists in establishing and implementing policies, procedures, and goals for assigned branch and for own department.Coordinates 1-2 year program schedule for Youth Services department. Plans, implements, andevaluates library programs for children, teens, and adults. Plans and implements workshops and training sessions, including one-on-one training for teachers, home school parents, civic groups, seniors, and the public at large. Analyzes current levels of programming and patron demand to determine need for new programming types or changes in amounts or frequency of programming.
- Coordinates Collection Management of department. Performs Community Analysis to determine customer’s needs and interests. Develops Collection Management Plan for assigned area, including evaluating and determining internal budgeting allocations. Reviews and selects materials for acquisition. Manages weeding and replacement of materials as needed.
- Provides Professional reference services to patrons including researching and answering references questions in person, over the telephone, online, and in writing. Expertly assists library patrons in using various resources and technology such as tablets, eReaders, computers, copiers, scanners, etc.Provides reader's advisory services for adults. Creates bibliographies and maintains and updates reference files. Creates displays to promote resources.
- Promotes the library and its services and programs to the public. Makes media and publicappearances. Assists in the maintenance of the library's website. Leads group tours of the library and represents the library to meetings of civic groups, schools, and other community organizations and events. Attends county and community meetings as appropriate.
- Participates in System Collection Development and program Committees. Maintains records and statistical data including programming, patron references, and collection data. Prepares and processes reports based on that data and provides analysis and action points. Suggests policy and procedure changes to services.
- Serves as Manager on Duty for the branch as needed. Evaluates department equipment and furnishing needs and makes recommendations to Branch Librarian. Ensures department meets performance standards. Coordinates ordering of necessary supplies and equipment for department. Performs other similar duties as required.""")

    st.subheader("Qualifications")
    st.markdown("""- Minimum Education - ALA Accredited MLIS/MLS
- Requires Public Speaking. Requires a SC Driver's License""")

    st.subheader("Type")
    st.write("Full Time")

    st.subheader("How to Apply")
    st.link_button("Apply Now", "https://www.lex-co.sc.gov/employment")
    st.write("Lexington County Human Resources Department\n(803) 785-8225")

    st.subheader("Salary")
    st.write("$50,555 - $54,094")

    st.subheader("Contact")
    st.table(pd.DataFrame([
        ["Michelle Williams", "Senior Deputy Director", "", "(803) 785-2643", "mwilliams@lexcolibrary.org"]
    ], columns=["Name", "Title", "Address", "Phone", "Email"]), border="horizontal")

# --- Job 3: Librarian I - Reference ---
with st.expander("Librarian I - Reference (Lexington, SC)"):
    st.header("Librarian I - Reference (Lexington, SC)")
    st.caption("04/29/2026")

    st.subheader("Job Description")
    st.write("""Plans, coordinates and implements library programs and Collection Development for the Reference Department. Provides technology and reference assistance to patrons. Advocates all library services, technologies, and programs to the community. Establishes partnerships and builds relationships with educational institutions and businesses within the community. Serves on System Committees.

- Plans, implements, and evaluates literacy and technology programs for adults. Plans andimplements workshops, group training, and one-on-one training for senior centers, civic groups, and the public at large. Analyzes current levels of in-house and outreach programming services and patron demand to determine need for new programming types or changes in amounts or frequency of programming. Stays up to date on trends in programming (various literacies and community needs).
- Evaluates and manages assigned collections. Reviews and selects materials for acquisition.Manages weeding and replacement of materials as needed. Collaborates with other librarians to determine budget appropriations. Evaluates donated materials for inclusion in the collection. Serves the library system by sitting on or chairing collection-focused committees. Evaluates Professional book reviews, statistics, and reports related to collection management in the selection and deselection of materials. Organizes materials in Reference department for optimal use. Selects and evaluates web resources.
- Provides reference and Readers Advisory services to patrons including researching andanswering questions in person, over the phone, online, and in writing. Expertly assists librarypatrons in using various resources and technology such as tablets, eReaders, computers,copiers, scanners, etc. Creates bibliographies and maintains and updates Reference files.Creates displays to promote resources.
- Promotes the library and its services and programs to the public. Makes media and publicappearances. Leads group tours of the library and represents the library to meetings of civicgroups and other community organizations and events. Attends county and communitymeetings as appropriate.
- Participates in System Collection Development and program Committees. Maintains records and statistical data including programming, patron references, and collection data. Prepares and processes reports based on that data and provides analysis and action points. Suggests policy and procedure changes to services
- Serves as Manager on Duty for the branch. Assigns tasks to other staff members as needed.Coaches and mentors subordinates and colleagues. Interviews, trains, and supervises volunteers and interns. Assists in the training processes for other employees. Coordinates ordering of necessary supplies and equipment for department. Serves the library on professional committees. Performs other similar duties as required.""")

    st.subheader("Qualifications")
    st.markdown("""- Minimum Education - ALA accredited MLIS/MLS degree
- Minimum Qualification - 3-5 years of professional library experience""")

    st.subheader("Type")
    st.write("Full Time")

    st.subheader("How to Apply")
    st.link_button("Apply Now", "https://www.lex-co.sc.gov/employment")
    st.write("Lexington County Human Resources Department\n(803) 785-8225")

    st.subheader("Salary")
    st.write("$47,693-$51,032 DOQ")

    st.subheader("Contact")
    st.table(pd.DataFrame([
        ["Michelle Williams", "Senior Deputy Director", "", "(803) 785-2643", "mwilliams@lexcolibrary.org"]
    ], columns=["Name", "Title", "Address", "Phone", "Email"]), border="horizontal")

# --- Job 4: Branch Librarian IV ---
with st.expander("Branch Librarian IV (Lexington, SC)"):
    st.header("Branch Librarian IV (Lexington, SC)")
    st.caption("04/29/2026")

    st.subheader("Job Description")
    st.write("""Manages all aspects of a large branch. Supervises, trains, and guides staff. Assists in Strategic Planning for the branch and system. Responsible for all daily operations as well as the facility. Oversees the Collection Development for the branch. Advocates library services through programs and community partnerships. Evaluates programs, collection and services and develops related goals within budget allocations. Analyzes and compiles statistical reports. Serves as the liaison to the Friends of the Library. Guides and assists customers in the use of technology and reference services. Provides high level customer service duties related circulation and customer accounts. Performs related professional, administrative, and supervisory work as required.

Essential Duties and Responsibilities:
- Manages the daily operations of a large branch library, ensuring compliance with all applicable library and county policies and procedures, laws and regulations, and standards of quality and safety. Ensures that the branch is properly staffed and that resources and facilities are accessible for public use. Maintains high level of customer service throughout the branch. Establishes branch-specific procedures and manages branch-specific budgets. Responsible for acting in an emergency.
- Assists in developing policies and procedures for the library system. Serves on library system committees, often in the leadership role. Develops branch-specific policies and procedures when appropriate. Evaluates community needs and interests. Recommends to library administration additions or changes in library services. Evaluates and assists in the planning and implementation of changes and improvements to the facility.
- Supervises staff in a large branch (25-35 staff), including professional, paraprofessional, and support staff. Schedules and plans with professional staff. Works to resolve employee difficulties. Mentors and coaches professional and paraprofessional staff. Evaluates all branch staff and monitors their professional growth and development. Assists in the interview process and selection of new staff.
- Manages library programs, workshops, and services for and within the community. Develops a long-term curriculum for the branch focusing on literacy, technology, and informational programs and workshops for the public and community groups. Coordinates public relations and marketing materials for branch programs, workshops, and services. Collects and analyzes statistics for library programs, workshops, and services. Allocates and manages funds for programs. Responsible for forecasting and meeting community needs.
- Identifies and addresses individual and community technology, literacy, and informational needs. Advocates for library services and programs within the local community. Establishes and maintains partnerships and promotes the branch with the local schools, businesses, and organizations. Serves as the liaison to and guides the governing Board of the Friends of the Library.
- Manages and evaluates the branch's collection and materials. Coordinates community analysis to establish needs and interests in order to select materials. Evaluates collection usage data in order to develop a Collection Management plan. Formulates an annual and long-term materials budget for branch. Delegates responsibility of selection and deselection of materials. Monitors and evaluates the collection management assignments. Monitors expenditures monthly.
- Performs a variety of functions daily to keep library operational. May open and close facility. Updates signage and flyers. Maintains physical appearance, supplies, and seating/collaborative spaces for public. Proactively addresses basic safety and security issues.""")

    st.subheader("Qualifications")
    st.markdown("""- Minimum Education - MLIS from an ALA accredited college or university
- Minimum Qualification - 4-5 years of professional experience in public libraries, including supervisory.""")

    st.subheader("Type")
    st.write("Full Time")

    st.subheader("How to Apply")
    st.link_button("Apply Now", "https://www.lex-co.sc.gov/employment")
    st.write("Lexington County Human Resources Department\n(803) 785-8225")

    st.subheader("Salary")
    st.write("$56,804.07-$60,780.35 DOQ")

    st.subheader("Contact")
    st.table(pd.DataFrame([
        ["Michelle Williams", "Senior Deputy Director", "", "(803) 785-2643", "mwilliams@lexcolibrary.org"]
    ], columns=["Name", "Title", "Address", "Phone", "Email"]), border="horizontal")

# --- Job 5: Library Director (Gaston County, NC) ---
with st.expander("Library Director (Gaston County, NC)"):
    st.header("Library Director (Gaston County, NC)")
    st.caption("04/27/2026")

    st.subheader("Job Description")
    st.write("""The Library Director provides executive leadership for a county‑wide public library system, creating a welcoming, inclusive environment that delivers excellent customer service and positive user experiences. This role plans, organizes, and directs all administrative, technical, and public service operations across seven departments and ten branches, ensuring services meet community needs.The Director prepares and oversees the annual departmental budget; manages county, state, federal, grant, and donated funds; and ensures accurate financial and statistical reporting. Responsibilities include personnel management, policy and service planning, collection development oversight, and facilities management. Serving as a key liaison to the Library Board of Trustees, County officials, community partners, and the public, the Director promotes the Library through advocacy, marketing, and civic engagement while mentoring leaders and staff and supporting long‑term strategic planning.""")

    st.subheader("Qualifications")
    st.markdown("""- Requires a Master’s degree in Library and/or Information Science from an ALA‑accredited institution, with coursework meeting all requirements for certification by the North Carolina Public Librarian Certification Commission.
- Minimum of ten (10) years of progressively responsible public library experience, including at least five (5) years in supervisory and administrative roles.
- Thorough knowledge of modern public library operations, county and municipal government functions, and diverse information resources.
- Demonstrated ability to plan, administer, and lead a library system; communicate effectively; build strong working relationships; and engage community groups.
- Commitment to serving diverse populations is required.
- Must meet physical demands, operate office technology, and work evenings and weekends as needed.""")

    st.subheader("Type")
    st.write("Full Time")

    st.subheader("How to Apply")
    st.link_button("Apply Now", "https://www.governmentjobs.com/careers/GastonNC")

    st.subheader("Salary")
    st.write("$109,599.98 - $180,800.05 Annually")

    st.subheader("Contact")
    st.table(pd.DataFrame([
        ["Sharon Costner", "", "", "(704) 866-3416", ""]
    ], columns=["Name", "Title", "Address", "Phone", "Email"]), border="horizontal")

# --- Job 6: Library Director (Pickens County, SC) ---
with st.expander("Library Director (Pickens County, SC)"):
    st.header("Library Director (Pickens County, SC)")
    st.caption("04/23/2026")

    st.subheader("Job Description")
    st.write("""The purpose of the class is to plan, direct, supervise and evaluate all County Library programs and activities, and to perform related professional, supervisory and administrative work as required. This class researches and formulates long-range goals for the organization, develops policy and position papers, and negotiates with chief administrative officers and/or elected officials.

ESSENTIAL TASKS:
- Plans, coordinates and manages the programs, activities, facilities and personnel of the Pickens County Library, ensuring compliance with all applicable laws, regulations and guidelines.
- Supervises department staff; supervisory duties include instructing, planning and assigning work, reviewing work, maintaining standards, coordinating activities, selecting new employees, allocating personnel, acting on employee problems, and approving employee discipline and discharge.
- Provides adequate training and development of department staff.
- Develops and implements Library policies and procedures.
- Develops and administers the department budget; controls budget expenditures; ensures effective and efficient use of budgeted funds, personnel, materials, facilities and time.
- Develops and monitors capital projects.
- Prepares grant applications for federal and other funding; monitors expenditures and evaluates project results at end of grant period.
- Assists the Library Board of Trustees and Library Foundation in developing short- and long-range goals and objectives for the Library system in an effort to effectively meet present and future community needs; develops and interprets Library policies and procedures for Board approval.
- Attends all meetings of the Board of Trustees and Foundation and keeps members informed of all Library activities, operations and problems; implements Board directives; serves as liaison to the Friends of the Library; submits recommendations to the various boards and provides administrative support as needed.
- Plans, develops and implements long and short-range programs for the improvement of County-wide Library services; determines long- and short-term budget, facility, staffing and technology needs.
- Works with the Library Foundation in planning and implementing fund-raising projects and events.
- Directs personnel in planning, executing and evaluating complex library services and activities.
- Provides general oversight of professional library activities, including cataloging and classifying library materials and collection development.
- Oversees the administration of Library automated systems.
- Plans and executes the Library’s public information program; promotes the Library and its services to community organizations and the public at large; prepares all publicity for the Library system, including signs, news releases, fliers, brochures, etc.
- Maintains cooperative working relationships with state, county and local officials, community leaders and civic groups; develops and maintains community support and sponsorships for Library programs.
- Assists patrons and staff with reference inquiries, including the use of print, electronic and Internet resources.
- Ensures the provision of professional customer service.
- Oversees the maintenance and improvement of Library buildings and grounds; ensures the proper maintenance of Library equipment; establishes replacement schedules for equipment and authorizes equipment expenditures.
- Prepares periodic and special studies, reports and other information as required by Library boards, the County and other agencies.
- Receives and responds to public inquiries and complaints regarding Library programs and services.
- Attends professional meetings, conferences and workshops to maintain knowledge of current theories and trends in public library operations and technology; participates on various committees and in professional meetings and activities.
- Performs general administrative / clerical work as required, including but not limited to preparing reports and correspondence, entering and retrieving computer data, copying and filing documents, reviewing mail and literature, etc.

ADDITIONAL JOB FUNCTIONS: Performs other related duties as required.""")

    st.subheader("Qualifications")
    st.markdown("""- VOCATIONAL/EDUCATIONAL PREPARATION: Requires a Master’s degree in library science from an ALA-accredited college or university.
- EXPERIENCE REQUIREMENTS: Five (5) years of related work experience.
- SPECIAL CERTIFICATIONS AND LICENSES: Must possess a valid state driver's license. Must possess Professional Librarian certification from the S.C. State Library.""")

    st.subheader("Type")
    st.write("Full Time")

    st.subheader("How to Apply")
    st.link_button("Apply Now", "https://selfservice.pickenscountysc.us/ess/employmentopportunities/default.aspx")

    st.subheader("Salary")
    st.write("$44.53/hr")

    st.subheader("Contact")
    st.write("N/A")

# --- Job 7: Branch Librarian III ---
with st.expander("Branch Librarian III (Lexington, SC)"):
    st.header("Branch Librarian III (Lexington, SC)")
    st.caption("04/20/2026")

    st.subheader("Job Description")
    st.write("""Schedule includes day, evening, and weekend hours.Manages a small branch. Supervises, trains, and guides staff. Assists in Strategic Planning for the branch, including facilities management. Oversees the Collection Development for the branch. Advocates library services through programs, community partnerships, and as the liaison to the Friends of the Library. Guides and assists customers in the use of technology and reference services. Provides high level customer service duties related to circulation and customer accounts.

- Manages all aspects of the branch. Ensures branch is staffed and operational for the public. Supervises staff including; scheduling, training, and evaluating. Coaches and mentors staff. Makes informed decisions concerning customer service and facilities management. Maintains accurate records of fines and fees and makes bank deposits. Plans and budgets for office and household supplies.
- Plans for the branch based on community needs and on the vision and the mission of the library. Recommends changes or additions to facilities, services, and staffing. Assists in formulation of library policy and procedures and ensures they are implemented.Manages the collection of materials for the branch. Develops internal branch collection budget based on allocations. Analyzes circulation statistics and trends in order to create a Collection Development Plan for the branch. Selects and deselects materials.
- Advocates for the library by promoting services and programs to individuals, civic organizations,community agencies and educational institutions. Cultivates partnerships through communication and interaction. Develops and presents dynamic programs for the public within the branch and through outreach activities. Provides opportunities for all ages to strengthen job skills, literacy, and recreation to build lifelong learning skills. Collaborates with the Friends of the Library.
- Provides reference and technology services for the public. Trains and assists the public in the use of the library equipment, print and online resources, and electronic devices, including instruction for downloading electronic materials. Prepares bibliographic tools to provide readers’ advisory for adults and youth. Provides Notary Service.
- Provides quality customer service following library policies and procedures to successfully fulfill the needs and expectations of the public. Manages the day-to-day duties, such as the circulation of materials, customer account issues, and customer registrations. Generates and processes documents and reports relating to customer requests and internal operations.
- Performs other similar duties as required.Requires Public Speaking""")

    st.subheader("Qualifications")
    st.markdown("""- Minimum Education - MLIS from an ALA accredited college or university; supplemented by 3-5 years of professional experience in public libraries, including supervisory and management experience.
- Minimum Qualification - 3-5 years of professional experience in public libraries, including supervisory and management experience.
- 5-10 years in public library management preferred.""")

    st.subheader("Type")
    st.write("Full Time")

    st.subheader("How to Apply")
    st.link_button("Apply Now", "https://www.lex-co.sc.gov/employment")

    st.subheader("Salary")
    st.write("$53,589.25 - 61,627.64")

    st.subheader("Contact")
    st.table(pd.DataFrame([
        ["Michelle Williams", "", "", "(803) 785-2636", "mwilliams@lexcolibrary.org"]
    ], columns=["Name", "Title", "Address", "Phone", "Email"]), border="horizontal")

# --- Job 8: Children's Services Librarian ---
with st.expander("Children's Services Librarian (Charleston, SC)"):
    st.header("Children's Services Librarian (Charleston, SC)")
    st.caption("04/16/2026")

    st.subheader("Job Description")
    st.write("""Branch Location: Baxter Patrick James Island
Reports To: Department Manager

General Summary: The Librarian, under the general direction of the Branch/Department Manager, provides library services for children ages birth through grade 5. Creates attractive displays, develops new and maintains ongoing innovative children’s programs. As a Librarian, you must demonstrate outstanding interpersonal skills, as a great part of this job will involve interacting with the local community.

Essential Roles and Responsibilities:
- Assist patrons with locating resources and computer usage.
- Make recommendations for reading materials or websites to obtain this information.
- Create, plan and coordinate community programs for children that increase library awareness; this will include off-site programs.
- Represent the library at external programming and outreach events.
- Participate in committees and/or organizations that support the library’s mission and goals.
- Must be comfortable proactively seeking out customers to help in all areas of the library (desk, roving, e-mail, phone, or additional methods of communication).
- Create booklists and book displays and provide technology assistance and demonstrations.
- Perform routine desk duties under professional supervision; help patrons locate and check out materials.
- Keep informed of current services and trends as related to public libraries.
- Candidates should be good listeners and communicators, present a positive attitude, enjoy working cooperatively as a team member, and place top priority on customer service.
- Must be flexible to assume additional responsibilities and scheduling requirements as needed to meet the coverage needs of the public service desks in other departments.
- Provide library services for children ages birth through grade 5.
- Develops new and maintains ongoing innovative children’s programs, story times/storytelling, STEAM programs, and puppetry programs to promote literacy.
- Assist children and caregivers in use of library resources.
- Must demonstrate knowledge, appreciation, and understanding of children’s materials, both print and electronic.
- Assist with Community Hub Services such as the rental assistance program, vaccine clinics, voting process, as well as other programs and services that are provided by CCPL.
- Perform other duties as assigned.

Knowledge, Skills, and Abilities:
- Knowledge of library amenities and the ability to provide information about library policies.
- Ability to use tact, courtesy and good judgment when communicating with coworkers and the public.
- Ability to demonstrate knowledge, appreciation, and understanding of library materials, both print and electronic.
- Ability to communicate effectively and present ideas orally and in writing.
- Ability to carry out assignments independently and work collaboratively with a team.""")

    st.subheader("Qualifications")
    st.markdown("""- MLIS degree or enrolled in an MLIS program with a completion date within three (3) years.
- MLIS student in good standing while enrolled in the MLIS program; documentation must be submitted with application.
- Eligible for or hold South Carolina State Library Certification. Candidates that do not have their MLIS degree must be currently enrolled in library school and will be required to obtain their South Carolina State Library certification upon completion of their MLIS degree.
- Must be able to work a flexible schedule including evenings and weekends.
- Must be proficient in Microsoft Office suite, with the ability to learn and use new methods and emerging technical advances.
- Must possess excellent customer service skills, ability to get along well with others and to communicate effectively with the public and with library staff, and a strong work ethic.""")

    st.subheader("Type")
    st.write("Full Time")

    st.subheader("How to Apply")
    st.write("To apply, please visit the Careers page of Charleston County Public Library.")

    st.subheader("Salary")
    st.write("$50,440.00 - $56,804.80 annually commensurate with education and experience.")

    st.subheader("Contact")
    st.write("For more information or application questions, please contact humanresources@ccpl.org")

# --- Job 9: Teen Services Librarian ---
with st.expander("Teen Services Librarian (Charleston, SC)"):
    st.header("Teen Services Librarian (Charleston, SC)")
    st.caption("04/16/2026")

    st.subheader("Job Description")
    st.write("""Branch Location: Hurd/St. Andrews & Wando Mount Pleasant
Reports To: Department Manager

General Summary: The Librarian, under the general direction of the Branch/Department Manager, is responsible for planning, implementing, and promoting in-branch and outreach programming to young adults. Responsible for collection maintenance of young adult materials. Collects and reports young adult programming statistics. Please note that the location of this library is directly across from a middle and high school and sees a large number of teen patrons daily. As a Librarian, you must demonstrate outstanding interpersonal skills, as a great part of this job will involve interacting with the local community.

Essential Roles and Responsibilities:
- Assist patrons with locating resources and computer usage.
- Make recommendations for reading materials or websites to obtain this information.
- Create, plan and coordinate community programs for different age groups that increase library awareness; this will include off-site programs.
- Represent the library at external programming and outreach events.
- Participate in committees and/or organizations that support the library’s mission and goals.
- Must be comfortable proactively seeking out customers to help in all areas of the library (desk, roving, e-mail, phone, or additional methods of communication).
- Create booklists, book displays and provide technology assistance and demonstrations for young adults.
- Collects and reports young adult programming statistics.
- Perform routine desk duties under professional supervision; help patrons locate and check out materials.
- Responsible for assisting the public in the use of technology, including software, online tools, and mobile devices.
- Responsible for planning, implementing, and promoting in-branch, as well as outreach programming for young adults.
- Keep informed of current services and trends as related to public libraries.
- Candidates should be good listeners and communicators, present a positive attitude, enjoy working cooperatively as a team member, and place top priority on customer service.
- Must be flexible to assume additional responsibilities and scheduling requirements as needed to meet the coverage needs of the public service desks in other departments.
- Must demonstrate knowledge, appreciation and understanding of young adult materials, both print and electronic.
- Assist with Community Hub Services such as the rental assistance program, vaccine clinics, voting process, as well as other programs and services that are provided by CCPL.
- Perform other duties as assigned.

Knowledge, Skills, and Abilities:
- Ability to remain positive and proactive in a busy teen space.
- Knowledge of library amenities and the ability to provide information about library policies.
- Ability to use tact, courtesy and good judgment when communicating with coworkers and the public.
- Ability to demonstrate knowledge, appreciation, and understanding of library materials, both print and electronic.
- Ability to communicate effectively and present ideas orally and in writing.
- Ability to carry out assignments independently and work collaboratively with a team.""")

    st.subheader("Qualifications")
    st.markdown("""- MLIS degree or enrolled in an MLIS program with a completion date within three (3) years.
- MLIS student in good standing while enrolled in the MLIS program; documentation must be submitted with application.
- Eligible for or hold South Carolina State Library Certification. Candidates that do not have their MLIS degree must be currently enrolled in library school and will be required to obtain their South Carolina State Library certification upon completion of their MLIS degree.
- Must be able to work a flexible schedule including evenings and weekends.
- Must be proficient in Microsoft Office suite, with the ability to learn and use new methods and emerging technical advances.
- Must possess excellent customer service skills, ability to get along well with others and to communicate effectively with the public and with library staff, and a strong work ethic.""")

    st.subheader("Type")
    st.write("Full Time")

    st.subheader("How to Apply")
    st.write("To apply, please visit the Careers page of Charleston County Public Library.")

    st.subheader("Salary")
    st.write("$50,440.00 - $56,804.80 annually commensurate with education and experience.")

    st.subheader("Contact")
    st.write("For more information or application questions, please contact humanresources@ccpl.org")

# --- Job 10: Children's Services Manager ---
with st.expander("Children's Services Manager (Charleston, SC)"):
    st.header("Children's Services Manager (Charleston, SC)")
    st.caption("04/16/2026")

    st.subheader("Job Description")
    st.write("""Branch Location: Johns Island (JOH)
Reports To: Department Manager

General Summary: The Children’s Manager, under the general direction of the Branch Manager, provides support to the Children’s staff and library services for children ages birth through grade 5. Creates attractive displays, develops new and maintains ongoing innovative children’s programs. As a Librarian, you must demonstrate outstanding interpersonal skills, as a great part of this job will involve interacting with the local community.

Essential Roles and Responsibilities:
- Assist patrons with locating resources and computer usage.
- Provide reader’s advisory and information services to customers of the Children’s Department.
- Create, plan and coordinate community programs for children that increase library awareness, this will include off site programs.
- Represent the library at external programming and outreach events.
- Participate in committees and/or organizations that support the library’s mission and goals.
- Must be comfortable proactively seeking out customers to help in all areas of the library (desk, roving, email, phone, or additional methods of communication).
- Create booklists and book displays and provide technology assistance and demonstrations.
- Perform routine desk duties, help patrons locate and check out materials.
- Keep informed of current services and trends as related to public libraries.
- Candidates should be good listeners and communicators, present positive attitude, enjoy working cooperatively as a team member, and place top priority on customer service.
- Must be flexible to assume additional responsibilities and scheduling requirements as needed to meet the coverage needs of the public service desks in other departments.
- Provide library services for children ages birth through grade 5.
- Develops new and maintains ongoing innovative children’s programs, story times/storytelling, STEAM programs, and puppetry programs to promote literacy.
- Assist children and caregivers in use of library resources.
- Contribute content about the Children’s Department to the Communications and Programming Department for inclusion in the Library’s social media presence.
- Must demonstrate knowledge, appreciation, and understanding of children’s materials, both print and electronic.
- Assist with Community Hub Services such as the rental assistance program, vaccine clinics, voting process, as well as other programs and services that are provided by CCPL.
- Perform other duties as assigned.

Knowledge, Skills, and Abilities:
- Must possess exceptional knowledge and competency of modern principles and practices in Children’s Services.
- Knowledge of and experience with parent education initiatives, Every Child Ready to Read, Early childhood development, and early literacy skills are desirable.
- Knowledge of library amenities and the ability to provide information about library policies.
- Ability to use tact, courtesy and good judgment when communicating with coworkers, and the public.
- Ability to demonstrate knowledge, appreciation, and understanding of library materials, both print and electronic.
- Ability to communicate effectively and present ideas orally and in writing.
- Ability to carry out assignments independently and work collaboratively with a team.""")

    st.subheader("Qualifications")
    st.markdown("""- Must possess exceptional knowledge and competency of modern principles and practices in Children’s Services.
- Master of Library and Information Science degree.
- 2 years library experience and 1-year supervisor preferred.
- Eligible for or hold South Carolina State Library Certification.
- Must be able to work a flexible schedule including evenings and weekends.
- Must be proficient in Microsoft Office suite, with the ability to learn and use new methods and emerging technical advances.
- Must possess excellent customer service skills, ability to get along well with others and to communicate effectively with the public and with library staff, a strong work ethic.""")

    st.subheader("Type")
    st.write("Full Time")

    st.subheader("How to Apply")
    st.write("To apply, please visit the Careers page of Charleston County Public Library.")

    st.subheader("Salary")
    st.write("$56,513.60 - $63,648.00 annually commensurate with education and experience.")

    st.subheader("Contact")
    st.write("For more information or application questions, please contact humanresources@ccpl.org")

# --- Job 11: Creative Studio Librarian ---
with st.expander("Creative Studio Librarian (Charleston, SC)"):
    st.header("Creative Studio Librarian (Charleston, SC)")
    st.caption("04/16/2026")

    st.subheader("Job Description")
    st.write("""Branch Locations: Baxter Patrick James Island (BPJI)
Reports To: Assistant Branch Manager

General Summary: The Librarian, under the general direction of the Branch/Department Manager, provides professional research, reference and technical services for the organization and users, to ensure efficient library operations and maintenance of its materials. Also responsible for coordination of Creative Studio schedule, activities, and equipment. As a Librarian, you must demonstrate outstanding interpersonal skills, as a great part of this job will involve interacting with the local community.

Essential Roles and Responsibilities:
- Assist patrons with locating resources and computer usage.
- Make recommendations for reading materials or websites to obtain this information.
- Create, plan and coordinate community programs for adult age group that increase library awareness, this will include off site programs.
- Responsible for coordination of Creative Studio schedule, activities and equipment which includes 3D printer, Cricut Maker, large format printer and laminator, sewing machine and more.
- Represent the library at external programming and outreach events.
- Participate in committees and/or organizations that support the library’s mission and goals.
- Must be comfortable proactively seeking out customers to help in all areas of the library (desk, roving, email, phone, or additional methods of communication).
- Create booklists and book displays and provide technology assistance and demonstrations.
- Perform routine desk duties under professional supervision, help patrons locate and check out materials.
- Keep informed of current services and trends as related to public libraries.
- Assist with Community Hub Services such as the rental assistance program, vaccine clinics, voting process, as well as other programs and services that are provided by CCPL.
- Responsible assisting the public in the use of technology, including software, online tools, and mobile devices.
- Candidates should be good listeners and communicators, present positive attitude, enjoy working cooperatively as a team member, and place top priority on customer service.
- Must be flexible to assume additional responsibilities and scheduling requirements as needed to meet the coverage needs of the public service desks in other departments.
- Must demonstrate knowledge, appreciation, and understanding of adult materials, both print and electronic.
- Perform other duties as assigned.

Knowledge, Skills, and Abilities:
- Knowledge of library amenities and the ability to provide information about library policies.
- Ability to use tact, courtesy and good judgment when communicating with coworkers, and the public.
- Knowledge or ability to learn Creative Studio equipment which includes 3D printer, Cricut Maker, large format printer and laminator, sewing machines and more.
- Ability to demonstrate knowledge, appreciation, and understanding of library materials, both print and electronic.
- Ability to communicate effectively and present ideas orally and in writing.
- Ability to carry out assignments independently and work collaboratively with a team.""")

    st.subheader("Qualifications")
    st.markdown("""- MLIS degree or enrolled in an MLIS program with a completion date within three (3) years.
- MLIS student in good standing while enrolled in the MLIS program, documentation must be submitted with application.
- Eligible for or hold South Carolina State Library Certification. Candidates that do not have their MLIS degree must be currently enrolled in library school and will be required to obtain their South Carolina State Library certification upon completion of their MLIS degree.
- Must be able to work a flexible schedule, including evenings and weekends.
- Must be proficient in Microsoft Office suite, with the ability to learn and use new methods and emerging technical advances.
- Must possess excellent customer service skills, ability to get along well with others and to communicate effectively with the public and with library staff, a strong work ethic.""")

    st.subheader("Type")
    st.write("Full Time")

    st.subheader("How to Apply")
    st.write("To apply, please visit the Careers page of Charleston County Public Library.")

    st.subheader("Salary")
    st.write("$50,440.00 - $56,804.80 annually commensurate with education and experience.")

    st.subheader("Contact")
    st.write("For more information or application questions, please contact humanresources@ccpl.org")

# --- Job 12: Systems Coordinator - Circulation ---
with st.expander("Systems Coordinator - Circulation (Charleston, SC)"):
    st.header("Systems Coordinator - Circulation (Charleston, SC)")
    st.caption("04/16/2026")

    st.subheader("Job Description")
    st.write("""Branch Location: Support Services
Reports To: Systems Manager, LCATS

General Summary: Under the general direction of the Systems Manager, the Systems Coordinator for Circulation serves as the point of contact for Circulation Services for all 20 CCPL locations. In addition to coordinating general circulation services, this position provides support for AMHs, IMMS, inventory management wands, contracts, point of sale and shelf space management. This position is also responsible for developing and communicating policy, procedures, and implementation needs that impact both back of house and front of house staff.

Essential Roles and Responsibilities:
- Coordinate systemwide technical Circulation Services such as Intelligent Material Management System (IMMS), AMH, self-check, RFID, and inventory management wands, point of sale and shelf space management.
- Serve as point of contact for accounts/contracts, scheduled maintenance, and on-demand problem solving.
- Develop and maintain systemwide Circulation Services, procedures and training in coordination with Systems Manager and branch staff.
- Collect and report circulation statistics.
- Dedicated time at welcome desks for circulation work.

Knowledge, Skills, and Abilities:
- Must possess exceptional knowledge and competency of modern principles and practices in Circulation Services.
- Ability to use tact, courtesy and good judgment when communicating with coworkers and the public.
- Ability to demonstrate knowledge, appreciation, and understanding of print and electronic library materials.
- Ability to communicate effectively and present ideas both orally and in writing.
- Ability to carry out assignments both independently and collaboratively.
- Ability to coordinate across departments with staff of varying levels of technical expertise.
- Must possess excellent interpersonal and customer service skills and a strong work ethic.""")

    st.subheader("Qualifications")
    st.markdown("""- Progressive employment in library Circulation Services or related library or information science field.
- 2 years of supervisory or management experience, preferably in library or information science field.
- Degree – MLIS preferred, but not required; combination of education and experience will be considered.
- Must be proficient in Microsoft Office suite and possess the ability to learn and implement emerging technical advances.
- Ability to travel frequently to CCPL branches as required.""")

    st.subheader("Type")
    st.write("Full Time")

    st.subheader("How to Apply")
    st.write("To apply, please visit the Careers page of Charleston County Public Library.")

    st.subheader("Salary")
    st.write("$60,840.00 - $68,515.20 annually commensurate with education and experience.")

    st.subheader("Contact")
    st.write("For more information or application questions, please contact humanresources@ccpl.org")

# --- Job 13: Librarian I (Greenville, SC) ---
with st.expander("Librarian I (Greenville, SC)"):
    st.header("Librarian I (Greenville, SC)")
    st.caption("03/26/2026")

    st.subheader("Job Description")
    st.write("""GREENVILLE COUNTY (SC) LIBRARY SYSTEM JOB ANNOUNCEMENT, NO. 2026-058

- Posting Date: Thursday, March 26, 2026
- Application Deadline: Thursday, April 2, 2026
- Position: Librarian I (Requires MLIS Degree or 12 Credit Hours Completed Towards MLIS Degree for Librarian Trainee), Augusta Road Branch Library
- Pay: $47,916 per year, plus benefits
- Status: Regular Full-time, Exempt
- Available: April 2026
- Location: Ramsey Family Branch Library, 100 Lydia Street, Greenville, South Carolina
- Schedule: Mon., Tues., & Wed. 8:30a-5:00p; Thurs. 1:30p-9:00p; and alternating Fri./Sat. 8:30a-6:00p

FUNCTION Employees in this position:
- Embody the Library’s code of service by creating an atmosphere where customers and coworkers feel invited, informed, impressed and inspired.
- Greet customers and coworkers with a welcoming smile, and enthusiastically provide knowledgeable and meaningful assistance in the discovery and use of Library resources, services and technology.
- Serve as the person in charge in the absence of the manager, maintaining efficient operations by providing support and guidance to paraprofessional staff and volunteers.
- Perform work under general supervision, in accord with the Library’s vision and mission, using good judgment in the application of policies and established procedures.

PHYSICAL REQUIREMENTS Must have the ability to:
- concentrate for long periods of time
- speak clearly and distinctly
- hear and/or comprehend verbal communication
- hear audible alarms and notifications
- see and interpret all job-related materials
- operate Library equipment as assigned
- lift up to 25 pounds and push book carts weighing over 100 pounds
- sit for long periods of time
- stand for long periods of time
- walk, bend and stoop
- reach, grasp and use hands to touch, handle, or feel
- type on an ongoing basis for long periods of time, using both hands
- tolerate low levels of dust and mold associated with working around paper files, books, and other library materials

EXAMPLES OF WORK PERFORMED (Essential job functions designated with E):
- Directs, assigns and coordinates duties of paraprofessional staff and volunteers, and provides coaching and training as needed. (E)
- Opens and closes branch according to established procedures. (E)
- Provides reference service to library patrons, staff and others. (E)
- Assists customers with identifying, locating and using Library materials. (E)
- Assists customers with the use of computer equipment, Windows operating system, MS Office, various Internet browsers, email and the Library’s website; including the online catalog and databases. (E)
- Provides general circulation services, including registering new borrowers, updating customer records, placing holds, checking out materials, etc. (E)
- Uses the Library’s integrated library system (ILS) to process discharges, fill or clear holds, place or receive items in transit and maintain accurate status of items. (E)
- Processes ILS reports to identify and retrieve items to fill hold requests and to return expired holds to the collection. (E)
- Uses Library equipment proficiently and instructs and demonstrates use, including self-checkout stations, to customers as needed. (E)
- Assists customers with current mobile device technology and assists them in downloading and/or accessing the Library’s online digital materials such as eBooks. (E)
- Communicates and enforces the Library’s Code of Conduct and other policies, procedures and rules to customers. (E)
- Reads book reviews and makes acquisition recommendations to supervisor. (E)
- Reviews and studies professional literature to keep abreast of developments in library and information science. (E)
- Assists in preparing work schedules and job assignments of lower level staff members.
- Assists the Branch Manager in planning for changes and improvements in unit operations.
- Attends meetings, training programs, workshops, etc. as requested by supervisor. (E)
- Makes appropriate referrals to other Library units, agencies, etc., for information or materials not available at work location. (E)
- Provides Readers’ Advisory services. (E)
- Assists in various aspects of programming for adults, including planning, organizing, preparing materials, presenting and/or providing instruction. (E)
- Promotes Library programs and assists customers in registering for them. (E)
- Empties materials drops located inside and/or outside the Library. (E)
- Assesses Library materials for needed repair or repackaging and identifies items for discard/replacement review. (E)
- Collects and maintains appropriate records of fines and fees received. (E)
- Accepts meeting space applications in compliance with policy and enters into calendar. If responsible for meeting space reservations, also approves applications and monitors calendar. (E)
- Sorts Library materials and shelves them according to their established arrangement. (E)
- Checks arrangement of shelved materials to assure they are in proper order. (E)
- Assists in conducting inventory of Library collections. (E)
- Moves and arranges Library materials under supervision. (E)
- Assists in keeping the Library clean and neat and the facility and equipment in good repair; submits Helpdesk requests to resolve problems. (E)
- Assists customers in submitting interlibrary loan requests. (E)
- May process 14-day and leased books.
- May conduct presentations, orientation sessions and tours for groups.
- Monitors and stocks brochure display and publicity items.
- Notifies appropriate coworker about low levels of supplies or, if assigned to monitor supplies, coordinates the ordering of supplies as needed. (E)
- Participates in community events on behalf of the Library upon request.
- Follows safe work methods to prevent injury. (E)
- Works a schedule that meets the needs of the unit. (E)
- Maintains regular and reliable attendance and remains compliant with the Library System’s Attendance Guidelines. (E)
- Performs other related duties as required.""")

    st.subheader("Qualifications")
    st.markdown("""Required: Must meet one of the categories of training & experience listed below:

Category 1:
- Master in Library & Information Science (MLIS) degree from an American Library Association (ALA) accredited college or university
- Coursework or experience emphasizing public library reference, readers’ advisory service, and research
- Experience working with the public in a customer service position

Category 2: Applicants who are working towards a Master in Library & Information Science (MLIS) degree may be considered as a Librarian Trainee for Librarian I and II level positions. To be considered, the following requirements must be met:
- Currently enrolled in an ALA accredited university working towards the MLIS degree
- Completed at least 12 credit hours for the MLIS degree
- Able to complete the MLIS degree within two years of the date of hire or promotion to a Trainee position
- Have three years of experience working in a public library or two years of experience working with GCLS

Preferred:
- Supervisory or leadership experience
- Experience working in a library or formal learning environment""")

    st.subheader("Type")
    st.write("Full Time")

    st.subheader("How to Apply")
    st.link_button("Apply Now", "https://www.greenvillelibrary.org")
    st.write("Visit the Job Openings page on our website to submit an online employment application. Inquiries may be directed to René Barajas Jr. at (864) 527-9235 or rbarajas@greenvillelibrary.org. GCLS is an Equal Opportunity Employer. GCLS participates in E-Verify.")

    st.subheader("Salary")
    st.write("$47,916")

    st.subheader("Contact")
    st.table(pd.DataFrame([
        ["René Barajas Jr.", "", "", "(864) 527-9235", "rbarajas@greenvillelibrary.org"]
    ], columns=["Name", "Title", "Address", "Phone", "Email"]), border="horizontal")

# --- Job 14: Library Director (Saluda County, SC) ---
with st.expander("Library Director (Saluda County, SC)"):
    st.header("Library Director (Saluda County, SC)")
    st.caption("03/25/2026")

    st.subheader("Job Description")
    st.write("""Saluda County is accepting applications for Library Director. Duties include but are not limited to:
- Directs the operations of the county library system
- Develops and implements library policies and procedures
- Directs, monitors, evaluates, and administers all the library's programmatic, fiscal, and personnel functions
- Ensures compliance with local, state, and federal regulations
- Coordinates and collaborates with other local agencies and organizations
- Administers grant funds
- Prepares and presents budget requests
- Manages budgeted funds
- Administers personnel policies and supervises library staff
- Completes performance evaluations
- Provides training to library personnel in the use of printed reference materials and electronic resources
- Coordinates long-term library planning for the development of library services
- Directs public relations campaigns to promote the library within the community
- Assists in the planning of new construction or alteration to existing facilities
- Coordinates the development of library collections
- Prepares and submits a variety of regular and special reports
- Participates in professional organizations and meetings
- Knowledge of library science and administration
- Knowledge of library technology""")

    st.subheader("Qualifications")
    st.markdown("""Master's degree in Library Science (MLS/MLIS) from an ALA-accredited program""")

    st.subheader("Type")
    st.write("Full Time")

    st.subheader("How to Apply")
    st.write("Applications along with resume and ten year driving record may be submitted to Regina Turner, Assistant Administrator, at 400 W. Highland Street, Saluda, SC or by email to r.turner@saludacounty.sc.gov")

    st.subheader("Salary")
    st.write("$52,800")

    st.subheader("Contact")
    st.write("A detailed job description is available by emailing r.turner@saludacounty.sc.gov")

# --- Job 15: Business Services Manager (Statesboro, GA) ---
with st.expander("Business Services Manager (Statesboro, GA)"):
    st.header("Business Services Manager (Statesboro, GA)")
    st.caption("03/23/2026")

    st.subheader("Job Description")
    st.write("""Position Title: Business Services Manager Classification: FLSA exempt, Full time Reports to: Regional Library Director

Overall Responsibility: The Business Services Manager is responsible for all accounting, payroll, and personnel functions of the Statesboro Regional Public Libraries. This employee works with the Regional Library Director, Library Managers, and Board Members in the preparation of budgets and financial reports. This individual plans, organizes, and supervises all aspects of business services for the library system.

Essential Position Functions:
- Records all accounting adjustments monthly and at year-end.
- Prepares and maintains the library system’s financial reports and budget documents
- Prepares, analyzes and reports to all library boards a full accounting of library funds
- Prepares reports (financial and other) as requested by library management
- Oversees the operation and maintenance of the financial accounting system
- Designs and monitors accounting processes for all libraries in our Regional library system
- Monitors all financial aspects of purchasing, receiving, supply and inventory operations
- Manages all investments while maintaining adequate operating cash reserves
- Prepares financial information for Georgia Public Library Services Annual Report and Renewal for State Aid
- Prepares and maintains all State Grant Budget reports
- Prepares information for the Agreed Upon Procedures per Georgia Public Library Services requirements.
- Maintains employee personnel records and oversees all employee benefit programs
- Prepares all monthly/quarterly/annual state and federal payroll tax reports and other required reports
- Communicates with library funding agencies as required
- Prepares communications to staff concerning employee benefit updates
- Maintains all general fixed assets records per Library policy
- Coordinates the library system’s property, liability and fiduciary insurance
- Supervises, trains, and evaluates Business Services staff
- Assists with the development and review of personnel and other policies
- Assists Regional Library Director in preparing specifications and bidding documents, reviews formal bids, and makes recommendations to the Library Boards for purchases/contracts as necessary
- Performs other duties as assigned

Knowledge, Skills, and Abilities:
- Knowledge of generally accepted accounting principles, governmental accounting practices, financial planning and record keeping, public finance, procurement procedures, budget development and administration
- Proficiency in use of Microsoft Office Programs
- Ability to maintain confidentiality
- Ability to use tact and diplomacy in working with staff, vendors and the public
- Ability to solve problems, exercise discretion, make sound independent judgments, handle job related stress, demonstrate initiative, and employ basic supervisory methods including work delegation and constructive criticism
- Demonstrate attention to detail, accuracy with numbers, and excellent written and verbal communication skills
- Ability to increase knowledge and skills through continuing education and staff development training.

Preferred Qualifications:
- Master’s degree in business or related field
- Knowledge of MIP accounting software
- Knowledge of library operations
- Knowledge of current State of Georgia Employee Benefit Plans
- Knowledge of labor laws

Physical Skills:
- Ability to sit and use computer for extended periods and operate standard office equipment, daily
- Ability to lift and move up to forty (40) pounds and push one hundred (100) pounds, occasionally
- Ability to work weekends and nights as job requires

Training, Supervision, and Evaluation: The Business Services Manager has the latitude and the responsibility to exercise independent professional judgment within the scope of the library policy. The Business Services Manager is responsive to directions given by Library Management. Formal evaluation and review of the Business Services Manager’s performance is provided by the Regional Library Director.

Working Conditions:
- Majority of work performed in general office and library environment
- Requires availability for extended hours as needed
- Requires evenings and/or weekends
- Requires periodic participation and attendance at events and training

Typical Work Schedule: Monday – Friday - 8:00 am – 5:00 pm""")

    st.subheader("Qualifications")
    st.markdown("""Required Qualifications:
- Bachelor’s degree in accounting
- Strong governmental (fund) accounting background with five or more years of progressively responsible accounting and budgeting experience
- Supervisory experience
- Obtain and maintain a valid Georgia Driver’s License and maintain a Motor Vehicle Report that is within the guidelines of the Library’s Insurance carrier""")

    st.subheader("Type")
    st.write("Full Time")

    st.subheader("How to Apply")
    st.link_button("Apply Now", "https://strl.info/statesboro_regional_library_jobs/index.php")
    st.write("Applicants can email application, resume, and cover letter to SearchBS@strl.info or mail to 124 S Main St, Statesboro, GA 30458.")

    st.subheader("Salary")
    st.write("Salary: $65,000+, Commensurate with Experience")

    st.subheader("Contact")
    st.write("912-764-1328\nSearchBS@strl.info")

# --- Job 16: University Archivist (UNC Charlotte, NC) ---
with st.expander("University Archivist (UNC Charlotte, NC)"):
    st.header("University Archivist (UNC Charlotte, NC)")
    st.caption("03/18/2026")

    st.subheader("Job Description")
    st.write("""The J. Murrey Atkins Library at UNC Charlotte is seeking a University Archivist to manage the acquisition, preservation, access, arrangement, and description of the University’s records of enduring value deposited in J. Murrey Atkins Special Collections and University Archives. This position also guides records management practices across campus through training and outreach initiatives and by providing consultation to University offices. The University Archivist promotes the history of the University through events, exhibits, presentations, and other outreach activities and participates in reference and instruction services within the unit. Essential Duties:
- Manages the University’s program for permanently valuable records in analog and digital formats in compliance with State of North Carolina open records laws and the statewide university system’s records retention schedule
- Conducts archival appraisal and selection activities for University records with enduring value
- Processes physical and digital collection materials according to accepted archival standards and procedures
- Guides and promotes records management practices on campus by consulting with and providing training for University offices on the management, retention, and digitization of records
- Supervises the management of the offsite storage and retrieval of University records as needed by University offices
- Collaborates with others in the unit to develop workflows and procedures for accessioning, preservation, arrangement, and description activities for University Archives in all formats
- Manages access and use restrictions to University records as guided by relevant open records laws, privacy laws, and intellectual property laws
- Manages data for University Archives to maintain intellectual control over records holdings
- Contributes to University efforts to acknowledge and promote the history of the University through events, exhibits, presentations, social media, and other outreach activities
- Collaborates to provide instruction services in relation to the University Archives and University history
- Manages the University art collection and collaborates with faculty and staff in the College of Arts + Architecture to promote and support the collection
- Supervises permanent staff. May hire, train, and supervise additional student and temporary employees
- Provides reference services by phone, email, and in-person
- Participates in library and university faculty governance
- Fulfills library faculty obligations relating to job performance, service and research, and participates in appropriate regional and/or national professional associations
- Supports and participates in other work of the unit as assigned""")

    st.subheader("Qualifications")
    st.markdown("""Minimum Education/Experience Requirements: Master’s degree in Library and/or Information Science from a program accredited by the American Library Association. Graduation with a master's degree in a specialized area directly relevant to the position description may be an acceptable substitute in certain situations if approved by the Dean. Preferred Education, Skills and Training Experience:
- Minimum of three years experience directly related to the duties and responsibilities specified
- Experience or demonstrated interest in supervising staff
- Demonstrated experience with archival principles related to the appraisal, arrangement, and description of records
- Knowledge of records management practices and procedures relating to paper and electronic records
- Ability to train others in records management and archival practices
- Experience providing reference services to the public in an archives or related setting
- Understanding of the legal context relating to the management of records in a public institution
- Demonstrated leadership and ability to work well with others on the formation of policies, procedures, and long-range plans
- Strong organizational skills with the ability to manage multiple projects concurrently
- Excellent written, public speaking, and interpersonal communication skills, with a demonstrated ability to work collaboratively with a wide variety of stakeholders
- Experience with outreach activities such as public speaking, exhibits, and social media
- Ability to build and sustain relationships with a variety of individuals and groups, including faculty, students, administrators, donors, researchers, and alumni
- Familiarity with archives management software and digital repository platforms
- Commitment to fostering an environment of mutual respect
- Participation in relevant professional organizations""")

    st.subheader("Type")
    st.write("Full Time")

    st.subheader("How to Apply")
    st.link_button("Apply Now", "https://jobs.uncc.edu/hr/postings/66823")
    st.write("ONLY ELECTRONIC APPLICATIONS WILL BE ACCEPTED. The review of applications will begin April 6, 2026. Anticipated start date is September 2026. Job posting will remain open until filled. The candidate chosen for this position will be subject to a criminal background check and verification of academic credentials.")

    st.subheader("Salary")
    st.write("$80,000-$85,000")

    st.subheader("Contact")
    st.write("Katie Howell, Associate Dean for Special Collections & University Archives")

# --- Job 17: Library Manager II (Sarasota County, FL) ---
with st.expander("Library Manager II (Sarasota County, FL)"):
    st.header("Library Manager II (Sarasota County, FL)")
    st.caption("03/17/2026")

    st.subheader("Job Description")
    st.write("""Start Here. Grow Here. Stay Here. Are you an experienced manager with a passion for libraries and a commitment to exceptional customer service? Join the team as our Library Manager II; in this key role, you will provide day-to-day oversight and operation of our Frances T. Bourne Jacaranda Library, our staff, and system-wide programs.
- This role has varying responsibilities, including hiring, coaching, and evaluating staff as well as collection development/maintenance, and encouraging community relationships.
- There are numerous opportunities for both growth and development, and benefits start within 30 days of hire.
- Take the next step in impacting our community - apply today!

About the Position: In this role you will be responsible for planning, budgeting, directing and supervising the operation of our Frances T. Bourne Jacaranda Library. This includes coaching, mentoring, and supervising staff as well as developing and maintaining community partnerships (i.e.: the Friends of the Library) and participating with the Management Team to meet the objectives of the Library System.

Administration:
- Oversee daily library operations, including participating in budget and business plan development and administration; keeping records/reporting to indicate progress and for future planning.
- Seek alternative revenue sources when necessary.
- Develop, communicate, and implement strategic plans, and establish long and short-range goals for the branch library.
- Develop, implement, and evaluate special projects, services, and programs.
- Interpret policies and procedures for staff and the public.
- Evaluate building, equipment, and repair needs and work with various departments to address issues.

Communication:
- Promote the value, mission, products, and services of the library throughout the community, encouraging the understanding and use of library programs, resources, and services.
- Work with library support groups such as the Friends of the Library, developing and maintaining community partnerships, and networking with other agencies within the County, the community, and the library profession.
- Prepare and present oral, written, and visual presentations to groups.

Customer Service:
- Develop and implement standards of service that ensure the prompt and efficient resolution of each inquiry by both internal and external customers, delivered with the utmost respect and courtesy.
- Keep abreast of developments, new trends, and innovations in libraries.
- Assist the service desks on a regular basis and other sections as needed.
- Represent Sarasota County to library users.
- Participate in and/or facilitate trainings, community meetings, and activities of the Library Advisory Board, Friends, Alliance, Friends of the Library, etc.

Staff Development:
- Evaluate staffing needs for the unit and interview and select candidates for hire.
- Conduct regularly scheduled staff meetings and one-on-one meetings with each employee, monitoring and managing performance, including the administration of corrective action.
- Provide opportunities for continuing professional development of self and others, especially in acquiring relevant understanding and skills.
- Participate in cross-training in other sections and aid in cross-training in their section.

Collection Development/Maintenance:
- Monitor the quality of materials collections for the branch, maintain awareness of library collections, and continually analyze and evaluate the collection based on changing community needs.
- Communicate changing collection needs to the library administration and collection development staff.
- Maintain currency in library literature for awareness of trends in areas of new formats, methods of delivery, circulation models, new technologies, etc.
- Oversee the monitoring and expenditure of the library budget.

About the Schedule:
- Work Hours: Full-Time, 40 hours per week.
- Must be available 8:00 a.m. to 8:00 p.m. as schedules may vary due to split shifts, rotations, on-call, emergencies, etc.

Location Hours: Currently this location is closed on Sundays, however this is subject to change based upon business needs.
- Monday, 10 a.m. - 6 p.m.
- Tuesday, 10 a.m. - 8 p.m.
- Wednesday, 10 a.m. - 8 p.m.
- Thursday, 10 a.m. - 8 p.m.
- Friday, 10 a.m. - 5 p.m.
- Saturday, 10 a.m. - 5 p.m.""")

    st.subheader("Qualifications")
    st.markdown("""Minimum Qualifications:
- Master's degree in Library and Information Science from an American Library Association-accredited institution.
- Three (3) years of supervisory experience in a public library.
- Valid Florida Driver's License by date of hire.

The ideal candidate has the following (bonuses):
- Considerable knowledge of staff management with an ability to establish and maintain effective working relationships with coworkers, officials, contractors, volunteers, community organizations, and the general public.
- Public media interaction, presentation, and negotiation skills.
- Advanced knowledge of computers, software, and the evolving role of technology in library services.

Subject to Passing Substance Screening: This position is subject to passing a pre-employment substance screening. An applicant who fails to pass a required drug screening test shall be disqualified from employment in any class for a period of five (5) years.""")

    st.subheader("Type")
    st.write("Full Time")

    st.subheader("How to Apply")
    st.link_button("Apply Now", "https://scgov.wd5.myworkdayjobs.com/SCGOV?q=library")

    st.subheader("Salary")
    st.write("$77,105.60")

    st.subheader("Contact")
    st.write("Brandi Hastie")

# --- Job 18: Library Branch Manager (Beaufort County, SC) ---
with st.expander("Library Branch Manager (Beaufort County, SC)"):
    st.header("Library Branch Manager (Beaufort County, SC)")
    st.caption("03/16/2026")

    st.subheader("Job Description")
    st.write("""The purpose of this position is to manage all aspects of the library branch operations. The position is responsible for acquiring, maintaining, and organizing library information, coordinating library programs, and assisting library patrons. This class works independently, under limited supervision, reporting major activities through periodic meetings.

Examples of Duties:
- Supervises, directs, and evaluates assigned staff, processing employee concerns and problems, directing work, counseling, disciplining, and completing employee performance appraisals.
- Coordinates, assigns, and reviews work and establishes work schedules; maintains standards; monitors status of work in progress; inspects completed work assignments; answers questions; gives advice and direction as needed.
- Directs all aspects of library operations such as circulation, reference, adult and children’s programs, and outreach programs.
- Monitors expenditures and maintains financial records; may prepare and submit budget information to meet needs of citizens for library services.
- Gathers and maintains information for reports on library income, usage, activities, and events; updates library information as needed.
- Recommends additions to library collections based on needs assessments of public interest and needs.
- Promotes community image of library and public awareness of library services through public information programs, outreach programs, displays, and public presentations.
- Monitors physical branch conditions; makes recommendations on maintaining grounds, buildings, and fixtures.
- Ensures that equipment and facilities used by the public are in working order on a daily basis; advises patrons on the use of computer resources, operations, and the Internet.
- Assists the public at service desk, checks out materials, retrieves reference sources, answers reference questions, makes recommendations, issues library cards, collects fees, and provides information as requested.
- Performs routine office tasks, such as typing, filing, faxing, telephoning, and copying.
- Performs related work as assigned.""")

    st.subheader("Qualifications")
    st.markdown("""- Requires Master’s degree in Library and Information Science (MLIS).
- Over two years and up to and including four years of related experience or an equivalent combination of education, training, and experience.
- South Carolina State Library Certification.
- Must possess and maintain a valid state driver’s license with an acceptable driving history.""")

    st.subheader("Type")
    st.write("Full Time")

    st.subheader("How to Apply")
    st.link_button("Apply Now", "https://www.governmentjobs.com/careers/beaufortcountysc/jobs/5238111/library-branch-manager")

    st.subheader("Salary")
    st.write("$76,086.40 - $91,303.68 Annually")

    st.subheader("Contact")
    st.write("Amanda Brewer Dickman at adickman@bcgov.net")

# --- Job 19: Evening Circulation and Building Supervisor ---
with st.expander("Evening Circulation and Building Supervisor (Presbyterian College, SC)"):
    st.header("Evening Circulation and Building Supervisor (Presbyterian College, SC)")
    st.caption("02/25/2026")

    st.subheader("Job Description")
    st.write("""Reporting to the Library Director, the Evening Circulation and Building Supervisor provides efficient and courteous library circulation and interlibrary loan service, processes incoming print periodicals, encourages and maintains appropriate behavior among students and other library users, supervises student assistants following established guidelines, and works cooperatively with other members of the library staff. This is a 12-month support position with varying schedules during the year. In fall and spring semesters, the regular schedule is 3:15 pm - 12:15 am for a total of 40 hours per week. The schedule for the rest of the year is subject to negotiation with the Library Director.

Core Duties and Responsibilities:
- Implement library policies appropriately; interpret and communicate those policies to patrons clearly and tactfully.
- Maintain a professional atmosphere and discipline in the circulation area, in particular, and the orderly and proper use of the building in general.
- Provide basic circulation service as needed: checking materials in and out, shelving materials, and shelf-reading.
- Provide efficient and courteous delivery of interlibrary loan service, with timely and accurate processing of requests, appropriate communication with patrons and libraries, and reliable record-keeping.
- Train student assistants and supervise their work checking materials in and out, shelving materials, shelf-reading, and performing other tasks as assigned.
- Maintain a clear channel of communication with the Head of Circulation.
- Assist library users with equipment such as public photocopier, computer printer, fax machine, and microfilm reader-printer, restocking with supplies as needed.
- Conduct thorough sweeps of the library multiple times daily: re-shelve materials, straighten furniture.
- Coordinate and contribute to the library's social media presence.
- Pick up and distribute daily mail.
- Resolve non-routine issues, such as responding to patron complaints.
- Refer serious public relations or policy difficulties to the Research Librarian (Evening Manager), Head of Circulation, or Library Director as appropriate.
- Secure and close the building each night.
- Initiate searches for missing materials and report lost items for possible replacement.
- Understand and follow appropriate procedures in emergency situations.
- Assist with library events or programs as needed.
- Perform other related tasks and projects as assigned by the Library Director.

Physical Requirements:
- Ability to lift and carry up to 25 pounds.
- Requires frequent standing, walking, bending, and moving books and carts.""")

    st.subheader("Qualifications")
    st.markdown("""Required Qualifications:
- Minimum of associate's degree.
- Excellent communication and interpersonal skills with a commitment to providing exceptional service.
- Strong organizational and time-management skills with attention to detail and accuracy.
- Demonstrated problem-solving and decision making skills.
- Must be a team player with a willingness to assist and support colleagues.

Preferred Qualifications:
- Related library work experience and familiarity with library systems.
- Proficiency with Google Workspace and Microsoft Office.
- Supervisory experience.""")

    st.subheader("Type")
    st.write("Full Time")

    st.subheader("How to Apply")
    st.write("Application review will begin immediately and continue until the position is filled. Candidates may send application materials via email to the Library Director, Betsy Byrd, eebyrd@presby.edu and should include their resume, a cover letter, and three professional references.")

    st.subheader("Salary")
    st.write("Not specified")

    st.subheader("Contact")
    st.write("Betsy Byrd, eebyrd@presby.edu")

with st.expander("Librarian III - Assistant Branch Librarian (Lexington, SC)"):
    st.header("Librarian III - Assistant Branch Librarian (Lexington, SC)")
    st.caption("03/12/2026")

    st.subheader("Job Description")
    st.write("""Provides professional library service to the public. Assists Senior Branch Librarian in management of daily operations of a large branch library. Manages the Circulation Department and supervises staff within work area. Performs Collection Development duties for the branch. Assists with planning and implementation of library programs. Provides feedback concerning programs and services delivered by staff. Serves on system committees.

- Responsible for branch operations during the absence of Senior Branch Librarian.
- Supervises staff of assigned department. Includes scheduling staff, instructing, planning, assigning work, maintaining standards, coordinating activities, allocating personnel, acting on employee problems.
- Reviews the work of subordinates for completeness and accuracy; evaluates performance and makes recommendations for improvement.
- Offers training, advice and assistance as needed. Coaches and mentors subordinates and colleagues.
- Assists in the interview and training process for branch staff.
- Enforces Code of Conduct regarding patron behavior.
- Serves on internal committees and assists in establishing and implementing policies, procedures, and goals for assigned branch and for own department.
- Coordinates Collection Development of internal department. Performs community analysis to determine customers' needs and interests. Develops Collection Management Plan for assigned areas, including evaluating and determining internal budgeting allocations. Reviews and selects materials for acquisition. Manages weeding and replacement of materials as needed.
- Promotes the library and its services and programs to the public, both internally and through community outreach.
- Provides Readers' Advisory.
- Leads group tours of the library and represents the library to meetings of civic groups, schools, and other community organizations.
- Attends county and community meetings as appropriate.
- Resolves patron account issues, including payment plans and account collections. Reconciles revenue with daily system financial report; prepares and delivers bank deposit. Manages the branch supply budget; evaluates branch needs and orders supplies.
- Participates in System Collection Development and community analysis.
- Evaluates materials budget allocation and develops a Collection Development plan for assigned areas.
- Manages assigned subject areas of library collection including selecting, weeding, and replacing materials according to the System's Collection Development Policy.
- Coordinates use of library meeting spaces for the public. Communicates the Meeting Room Policy and determines eligibility of applicants. Processes applications and collects deposits; compiles and submits usage statistics.
- Helps maintain records and statistical data including programming, patron references, and collection data.
- Ensures department meets performance standards.
- Suggests policy and procedure changes to services.
- Evaluates department equipment and furnishing needs and makes recommendations to Senior Branch Librarian.
- Performs other similar duties as required.

Requires public speaking, working evenings and weekends including Sundays. Responsible for branch operations during absence of Senior Branch Librarian.""")

    st.subheader("Qualifications")
    st.markdown("""- Minimum Education - ALA accredited MLIS/MLS.
- Minimum Qualification - 3-5 years of professional library experience in public libraries including supervisory and management experience.""")

    st.subheader("Type")
    st.write("Full Time")

    st.subheader("How to Apply")
    st.link_button("Apply Now", "https://www.lex-co.sc.gov/employment")
    st.write("Submit Application and Resume to: Lexington County Human Resources Department (803) 785-8225")

    st.subheader("Salary")
    st.write("$53,589.25-$57,340.50 DOQ")

    st.subheader("Contact")
    st.table(pd.DataFrame([
        ["Michelle Williams", "Senior Deputy Director", "", "(803) 785-2643", "mwilliams@lexcolibrary.org"]
    ], columns=["Name", "Title", "Address", "Phone", "Email"]), border="horizontal")

# --- Job 21: Librarian III - Branch Librarian (Lexington, SC) ---
with st.expander("Librarian III - Branch Librarian (Lexington, SC)"):
    st.header("Librarian III - Branch Librarian (Lexington, SC)")
    st.caption("02/25/2026")

    st.subheader("Job Description")
    st.write("""Provides professional library service to the public. Assists Senior Branch Librarian in management of daily operations of a large branch library. Manages the Circulation Department and supervises staff within work area. Performs Collection Development duties for the branch. Assists with planning and implementation of library programs. Provides feedback concerning programs and services delivered by staff. Serves on system committees. Responsible for branch operations during the absence of Senior Branch Librarian.

Supervises staff of assigned department. Includes scheduling staff, instructing, planning, assigning work, maintaining standards, coordinating activities, allocating personnel, acting on employee problems. Reviews the work of subordinates for completeness and accuracy; evaluates performance and makes recommendations for improvement. Offers training, advice and assistance as needed. Coaches and mentors subordinates and colleagues. Assists in the interview and training process for branch staff.

Enforces Code of Conduct regarding patron behavior. Serves on internal committees and assists in establishing and implementing policies, procedures, and goals for assigned branch and for own department. Coordinates Collection Development of internal department. Performs community analysis to determine customers' needs and interests. Develops Collection Management Plan for assigned areas, including evaluating and determining internal budgeting allocations. Reviews and selects materials for acquisition. Manages weeding and replacement of materials as needed.

Serves the Library System by sitting on or chairing collection-focused committees. Promotes the library and its services and programs to the public, both internally and through community outreach. Provides Readers' Advisory. Leads group tours of the library and represents the library to meetings of civic groups, schools, and other community organizations. Attends county and community meetings as appropriate. Resolves patron account issues, including payment plans and account collections. Reconciles revenue with daily system financial report; prepares and delivers bank deposit.

Manages the branch supply budget; evaluates branch needs and orders supplies. Participates in System Collection Development and community analysis. Evaluates materials budget allocation and develops a Collection Development plan for assigned areas. Manages assigned subject areas of library collection including selecting, weeding, and replacing materials according to the System's Collection Development Policy. Coordinates use of library meeting spaces for the public. Communicates the Meeting Room Policy and determines eligibility of applicants. Processes applications and collects deposits; compiles and submits usage statistics.

Helps maintain records and statistical data including programming, patron references, and collection data. Ensures department meets performance standards. Suggests policy and procedure changes to services. Evaluates department equipment and furnishing needs and makes recommendations to Senior Branch Librarian. Performs other similar duties as required.

Preferred: 5-10 years of experience in public library management.""")

    st.subheader("Qualifications")
    st.markdown("""- Minimum Education - MLIS from an ALA accredited college or university.
- Minimum Qualification: 3-5 years of professional experience in public libraries, including supervisory and management experience.""")

    st.subheader("Type")
    st.write("Full Time")

    st.subheader("How to Apply")
    st.link_button("Apply Now", "https://www.lex-co.com/Applications/HROnline/PUBLIC/VACANCYLISTING.ASPX")
    st.write("Lexington County Human Resources (803) 785-8225")

    st.subheader("Salary")
    st.write("$53,589.25 - $57,340.50")

    st.subheader("Contact")
    st.table(pd.DataFrame([
        ["Michelle Williams", "Senior Deputy Director", "", "(803) 785-2643", "mwilliams@lexcolibrary.org"]
    ], columns=["Name", "Title", "Address", "Phone", "Email"]), border="horizontal")

# --- Job 22: Head, Collections and Acquisitions (Clemson, SC) ---
with st.expander("Head, Collections and Acquisitions (Clemson, SC)"):
    st.header("Head, Collections and Acquisitions (Clemson, SC)")
    st.caption("02/19/2026")

    st.subheader("Job Description")
    st.write("""Clemson Libraries seeks a collaborative, dynamic, and collegial Head of Acquisitions to provide leadership and expertise for a department that oversees acquisitions, electronic resources, continuing resources, and collection development and analysis. This position provides oversight for a collections budget of $9.5 million and leads efforts related to the procurement, assessment, and management of print and electronic resources, including individual and package subscriptions, e-books, demand-driven acquisitions, open access resources, streaming services, and continuing resources. Clemson Libraries migrated to Alma/Primo VE in June 2020 and is part of a statewide Network Zone that includes 54 other institutions in the Partnership Among South Carolina Academic Libraries (PASCAL) consortium. The Head of Acquisitions will be actively involved in shared collection development decisions and licensing negotiations facilitated by PASCAL, as well as other consortia such as the Carolina Consortium and the Association of Southeastern Research Libraries (ASERL).

Clemson Libraries faculty are members of the academic community, with responsibilities in the areas of librarianship, research, and service. This is a 12-month tenure-track faculty position, minimum salary starts at $95,000, and works under the direction of the Associate Dean for Collections and Discovery. Responsibilities include:
- Leads, plans, and oversees acquisitions operations and processes for materials in all formats acquired for University Libraries.
- Manages and coordinates operations for the Acquisitions Department composed of approximately 11 employees. This position directly supervises 2 faculty and 2 staff members.
- Directs the efficient, appropriate, and timely expenditure of the Libraries' $9.5 million collections budget, which includes both targeted and untargeted gifts and endowments.
- Supervises day-to-day acquisitions processes.
- Develops fund allocations for collection development areas.
- Chairs the Collections Strategy Cross-Functional Team.
- Collaborates with colleagues in Metadata Services, User Services and Teaching and Learning to establish and refine interdepartmental workflows.
- In collaboration with the eCollections Access and Licensing Librarian, leads efforts related to the procurement, assessment, and management of electronic resources, including contract negotiations, renewals, and e-resource workflows.
- Provides oversight and strategic direction for individual subscription renewal assessment.
- Develops policies and procedures related to collection development and acquisitions.

Research, Scholarship, and Creative Activities:
- Develops a focused program of high-quality research and creative accomplishments, consistent with professional responsibilities and the Libraries' mission and goals.

Service:
- Actively participates and demonstrates leadership in professional responsibilities that serve the Libraries, university, profession, and community.""")

    st.subheader("Qualifications")
    st.markdown("""**Required Qualifications:**
- An ALA-accredited graduate degree in librarianship or a relevant accredited graduate degree in another scholarly field as deemed appropriate by the Libraries.
- A minimum of 3 years of professional experience in acquisitions, electronic resources, or collection development in an academic library or a large, multi-branch public library.
- Previous management/supervisory experience.
- Experience with strategic collection development and/or budgeting.
- Demonstrated skills in oral and written communication and creative problem-solving.

**Preferred Qualifications:**
- Demonstrated ability to foster an environment of collegiality, respect, trust, and teamwork.
- Experience with reviewing and negotiating license agreements pertaining to electronic resources.
- Experience with assessment of print and electronic resources (usage reports, overlap reports, cost per use, etc.).
- Experience working with publishers and/or vendors of electronic resources.
- Experience in coordination or management of library services platform functions in a consortial environment, including experience with Ex Libris' Alma and Primo VE.
- Knowledge of current, evolving, and innovative models of collection development, including open access and scholarly communications.""")

    st.subheader("Type")
    st.write("Full Time")

    st.subheader("How to Apply")
    st.link_button("Apply Now", "https://apply.interfolio.com/181824")
    st.write("""Required materials include:
- A cover letter addressing the qualifications for the position.
- A professional curriculum vitae.
- The names and contact information of three (3) professional references.

Search timeline:
- Applications open: Submit your application by March 15, 2026 for guaranteed consideration.
- Review and selection: We'll review applications through mid-March. If shortlisted, expect to hear from us to schedule a virtual interview in early April.
- Campus Interviews: Invitations in early May.
- Ideal start date: July 1st.""")

    st.subheader("Salary")
    st.write("Minimum $95,000")

    st.subheader("Contact")
    st.write("Chris Morris, cmorr25@clemson.edu")

# --- Job 23: Branch Library Services Manager (Greenville, SC) ---
with st.expander("Branch Library Services Manager (Greenville, SC)"):
    st.header("Branch Library Services Manager (Greenville, SC)")
    st.caption("02/17/2026")

    st.subheader("Job Description")
    st.write("""**GREENVILLE COUNTY (SC) LIBRARY SYSTEM JOB ANNOUNCEMENT, NO. 2026-052**

- Posting Date: Monday, February 16, 2026
- Application Deadline: Open until filled
- Position: Branch Library Services Manager, Adult Services, Hughes Main Library
- Pay: $70,580 per year, plus benefits
- Status: Regular Full-time, Exempt
- Available: March 2026
- Location: Hughes Main Library, 25 Heritage Green Place, Greenville, South Carolina
- Schedule: Daytime hours Monday – Friday, with occasional evening, weekend, and holiday hours as needed.

**FUNCTION**
Reporting to the Adult Services Director, this position:
- Supervises activities related to the operation of branch libraries throughout Greenville County as well as the Library System's Bookmobile & Homebound unit.
- Works with branch library managers and other Library System personnel to support development of branch staff, collections, and service offerings.
- Works with branch library managers and other Library System personnel to ensure branch facilities, equipment, and technology are maintained and enhanced as necessary.
- Embodies the Library System's Code of Service by creating an atmosphere where customers and employees feel invited, informed, impressed, and inspired.

**EXAMPLES OF WORK PERFORMED (Essential job functions designated with E):**
- Provides supervision and administrative oversight for Branch Managers and Bookmobile/Homebound Supervisor. (E)
- Provides training, direction, and/or support for subordinates; reviews performance of subordinates and makes recommendations for improvement/growth as appropriate (E).
- Acts as an assistant to the Adult Services Director, working on projects and tasks as assigned. (E)
- Serves as Acting Adult Services Director in that person's absence. (E)
- Serves as a Substitute for Branch Managers and other branch leadership staff, working temporarily in branch libraries as needed. (E)
- Assists in planning for change and improvement in branch operations, including budget recommendations, workflow optimization, and formulation of goals and objectives. (E)
- Participates in the interviewing, selection, and/or approval of new employees. (E)
- Handles sensitive and confidential matters. (E)
- Performs research and analysis of branch staffing levels and provides direction to managers regarding staff schedules and staffing levels. (E)
- Confers with the Adult Services Director and the Human Resources (HR) Manager regarding branch personnel needs, problems, vacancies, recruitment, specific position requirements, and overall employee relations. (E)
- Addresses personnel issues and administers disciplinary actions with guidance and direction from the HR Manager. (E)
- Works with the HR Training Coordinator to develop and implement training for Branch Library Services staff. (E)
- Works with the Technical Services Manager and Branch Managers regarding the development and maintenance of branch collections. (E)
- Serves on internal library working groups and committees as assigned. (E)
- Works with Facilities Maintenance Manager on issues regarding branch facilities. (E)
- Works with Security Manager on issues regarding Code of Conduct violations/enforcement. (E)
- Collaborates with the Adult Events and Outreach Manager, Information Services Manager, Youth Services Manager, and Branch Managers regarding programming and outreach initiatives. (E)
- Works with the Adult Events and Outreach Manager, Branch Managers, Information Services Manager, and/or Youth Services Manager to determine feasibility of allocating staff resources to fulfill proposed programs and outreach initiatives. (E)
- Provides assistance in reference, reader's advisory, and circulation services to customers and employees. (E)""")

    st.subheader("Qualifications")
    st.markdown("""**Required:**
- Master's Degree in Library Science from an A.L.A. accredited college or university.
- Five years of professional public library experience at a supervisory or leadership level.
- Experience working at a branch library and providing circulation services.
- Demonstrably progressive work experience showing an increase in the level of duties and responsibilities.
- Certified or eligible for certification by the South Carolina State Library.

**Preferred:**
- Experience managing a branch library.
- Experience working with collection development and maintenance.
- Experience in planning library outreach and events for adults.""")

    st.subheader("Type")
    st.write("Full Time")

    st.subheader("How to Apply")
    st.link_button("Apply Now", "http://www.greenvillelibrary.org")
    st.write("Visit the Job Openings page on our website to submit an online employment application. Inquiries may be directed to Cindy Quinn at (864) 527-9232 or cquinn@greenvillelibrary.org. GCLS is an Equal Opportunity Employer. GCLS participates in E-Verify.")

    st.subheader("Salary")
    st.write("$70,580")

    st.subheader("Contact")
    st.table(pd.DataFrame([
        ["Cindy Quinn", "", "", "(864) 527-9232", "cquinn@greenvillelibrary.org"]
    ], columns=["Name", "Title", "Address", "Phone", "Email"]), border="horizontal")

# --- Job 24: Collection Logistics Librarian (University of Georgia, GA) ---
with st.expander("Collection Logistics Librarian (University of Georgia, GA)"):
    st.header("Collection Logistics Librarian (University of Georgia, GA)")
    st.caption("02/06/2026")

    st.subheader("Job Description")
    st.write("For complete job description, please review the long advertisement on the UGA Libraries website.")

    st.subheader("Qualifications")
    st.markdown("""- An ALA-accredited Master's in Library and Information Science or relevant terminal degree""")

    st.subheader("Type")
    st.write("Full Time")

    st.subheader("How to Apply")
    st.link_button("Apply Now", "https://www.ugajobsearch.com/postings/466574")
    st.write("Review the long advertisement on the UGA Libraries website at https://www.libs.uga.edu/jobs")

    st.subheader("Salary")
    st.write("$60,000 - $70,000")

    st.subheader("Contact")
    st.write("libjobs@uga.edu")

# --- Job 25: Affiliate Services Coordinator (Middle Georgia Regional Library, GA) ---
with st.expander("Affiliate Services Coordinator (Middle Georgia Regional Library, GA)"):
    st.header("Affiliate Services Coordinator (Middle Georgia Regional Library, GA)")
    st.caption("02/09/2026")

    st.subheader("Job Description")
    st.write("""**Affiliate Services Coordinator - Starting at $58,725 per year**

Are you ready for your next challenge? Are you a leader with a passion for innovation and talent for teamwork? Would you like to join a library system that is experiencing tremendous growth?

The Affiliate Services Coordinator serves as the certified librarian supporting library services in seven library branches of the affiliate counties served by MGRL. As Affiliate Services Coordinator, you will lead a staff of enthusiastic and committed professionals and paraprofessionals in fulfilling the library's mission "to connect all people to the information necessary to improve their lives through excellent services and materials."

**Our work culture:**
- Middle Georgia Regional Library fosters a collaborative culture where teamwork is necessary to make a difference.
- Diverse backgrounds, identities, and experiences bring unique strengths and perspectives to our team.
- Staff at MGRL enjoy a generous benefits package which includes 20 days of vacation leave, 10 days of sick leave, 11 paid holidays, membership in the Teachers Retirement System of Georgia, and medical insurance.

**Examples of duties:**
- This position drives to each branch a minimum of twice per week to provide certified librarian support.
- Transporting books and materials to the counties.
- Supporting branch managers.
- Reviewing facilities.
- Evaluating collections.
- Managing book budgets.
- Teaching computer classes.
- Attending official meetings as assigned by Director.
- Providing guidance on MGRL policies, procedures, and strategic plan vision.
- Other duties as assigned.

**Physical Requirements:**
- Sufficient clarity of speech and hearing or other communication capabilities.
- Sufficient manual dexterity.
- The job involves a considerable amount of movement and activity.
- Work routinely involves lifting or handling material weighing up to 50 lbs., pushing book carts weighing up to 100 lbs.

**Benefits:**
- Vacation (accrual starting at 20 days per year)
- Sick Leave (10 days per year)
- 11 paid holidays per year
- Macon-Bibb County life insurance
- Teachers Retirement System of Georgia defined benefit retirement plan (401A)
- State Health Benefit Plan (medical insurance)""")

    st.subheader("Qualifications")
    st.markdown("""- Master's degree in Library Science.
- 2–4 years of increasing responsibility and experience in a library environment.
- Valid driver's license and good driving record.
- Supervisory experience (preferred).""")

    st.subheader("Type")
    st.write("Full Time")

    st.subheader("How to Apply")
    st.write("E-mail resume, cover letter, contact information for three references, and MGRL employment application (found at https://shorturl.at/cowzY) to jobs@bibblib.org. First review of applicants is Thursday, February 26th at 12 PM.")

    st.subheader("Salary")
    st.write("$58,725")

    st.subheader("Contact")
    st.write("jobs@bibblib.org")

# --- Job 26: Acquisitions Librarian (University of Georgia, GA) ---
with st.expander("Acquisitions Librarian (University of Georgia, GA)"):
    st.header("Acquisitions Librarian (University of Georgia, GA)")
    st.caption("02/07/2026")

    st.subheader("Job Description")
    st.write("""Reporting to the Director of Collections, the Acquisitions Librarian plays a key leadership role in shaping and overseeing the Libraries' acquisitions strategy for purchased and licensed content. This position is responsible for streamlining resource procurement processes, assisting in managing the collections budget, and supporting collection development to align with the Libraries' goals. The Acquisitions Librarian also fosters strong vendor relationships, addresses order and payment issues, and ensures effective collaboration across departments. Additionally, the role includes staff leadership, including hiring, training, and performance management of approximately 3 staff, while contributing to library-wide planning, governance, and ongoing professional development.""")

    st.subheader("Qualifications")
    st.markdown("""- An ALA-accredited Master's in Library and Information Science or relevant terminal degree.""")

    st.subheader("Type")
    st.write("Full Time")

    st.subheader("How to Apply")
    st.link_button("Apply Now", "https://www.ugajobsearch.com/postings/466551")
    st.write("Review the long advertisement on the UGA Libraries website at https://www.libs.uga.edu/jobs. Candidates are encouraged to submit their materials by March 8, 2026; however, the position will remain open until filled.")

    st.subheader("Salary")
    st.write("$60,000 - $90,000")

    st.subheader("Contact")
    st.write("libjobs@uga.edu")

# --- Job 27: Collections Strategies Coordinator (University of Georgia, GA) ---
with st.expander("Collections Strategies Coordinator (University of Georgia, GA)"):
    st.header("Collections Strategies Coordinator (University of Georgia, GA)")
    st.caption("02/07/2026")

    st.subheader("Job Description")
    st.write("""The University of Georgia Libraries seeks a forward-looking and collaborative individual for the newly developed position of Collection Strategies Coordinator. Reporting to the Director of Collections, the position will manage a recently established Collections Strategy team, which includes approximately three faculty librarians and one or more staff. The coordinator will lead this team in developing strategy and stewarding the UGA Libraries' significant investment in research collections and open scholarship.""")

    st.subheader("Qualifications")
    st.markdown("""- An ALA-accredited Master's in Library and Information Science or relevant terminal degree.""")

    st.subheader("Type")
    st.write("Full Time")

    st.subheader("How to Apply")
    st.link_button("Apply Now", "https://www.ugajobsearch.com/postings/466266")
    st.write("Review the long advertisement on the UGA Libraries website at https://www.libs.uga.edu/jobs. Candidates are encouraged to submit their materials by March 8, 2026; however, the position will remain open until filled.")

    st.subheader("Salary")
    st.write("$60,000 - $80,000")

    st.subheader("Contact")
    st.write("libjobs@uga.edu")

# --- Job 28: Director of Library Services (Anderson, SC) ---
with st.expander("Director of Library Services (Anderson, SC)"):
    st.header("Director of Library Services (Anderson, SC)")
    st.caption("02/05/2026")

    st.subheader("Job Description")
    st.write("""Anderson University seeks an innovative leader who is passionate about students and their success. The director of Thrift Library and its full- and part-time staff play an essential role in Anderson's commitment to academic excellence. The library works closely with the faculty, Office of Information Technology, the Center for Innovation and Digital Learning, the Center for Learning and Teaching Excellence, and other academic personnel to carry out Anderson University's mission.

- Candidates should be prepared to lead all administrative, operational, and technical functions of the Thrift Library, support an ever-growing university, foster a culture of collegiality, hospitality, and innovation in the library, and support the library staff in their daily work and professional development.
- Candidates must be a committed Christian and hold values that are compatible with the institution's Statement of Faith and enthusiastically support Anderson University's mission.

**About the Thrift Library:**
- In 2007, the University completed what was then the largest single-phase building project in its history as the $7.5 million Thrift Library building opened to students.
- Thrift Library's collection contains over 70,000 physical volumes, more than 1.8 million ebooks, and approximately 200 electronic research, reference, and subject-specific databases.
- During fall and spring semesters, the library is open seven days a week.
- Professional librarians provide instruction for groups and individuals covering research process, citation styles, plagiarism, and copyright issues.

**Start Date: June 1, 2026**""")

    st.subheader("Qualifications")
    st.markdown("""- Qualified candidates must hold a master's degree in library science. A second advanced degree is encouraged.
- The ideal candidate will have significant library experience, effective leadership and collaborative skills to build successful partnerships internally and externally, skills and experience in strategic planning, high emotional intelligence, fiscal planning, and budget and resource management.""")

    st.subheader("Type")
    st.write("Full Time")

    st.subheader("How to Apply")
    st.link_button("Apply Now", "https://andersonuniversity.edu/job_opportunity/director-of-library-services/")
    st.write("""To ensure full consideration, please complete the online application for staff employment, along with:
- Letter of application addressing qualifications and previous leadership experience
- Curriculum vitae
- Contact information for three professional references

Please direct application materials and questions to the search chair: Dr. Lisa Zidek, Dean of the College of Engineering, LibraryJobs@andersonuniversity.edu""")

    st.subheader("Salary")
    st.write("Not specified")

    st.subheader("Contact")
    st.write("Dr. Lisa Zidek, LibraryJobs@andersonuniversity.edu")

# --- Job 29: Library Systems Analyst (Davidson, NC) ---
with st.expander("Library Systems Analyst (Davidson, NC)"):
    st.header("Library Systems Analyst (Davidson, NC)")
    st.caption("02/04/2026")

    st.subheader("Job Description")
    st.write("""We're seeking a Library Systems Analyst to help shape the future of library technology at Davidson College. This role provides high-level administration, configuration, leadership, and strategic planning for the library's core technology infrastructure services; the tools that help people discover, share, and create knowledge. You'll collaborate with an amazing team of library colleagues, including our new Systems Specialist, and campus IT partners. There's never been a more exciting time to join our library.

- The George Lawrence Abernethy Library—the largest capital project in Davidson's history—opens in fall 2027.
- It will transform how our community learns, creates, and connects.""")

    st.subheader("Qualifications")
    st.markdown("""**Required:**
- A Bachelor's degree in Information Technology, Computer Science, or Information/Library Science or equivalent experience.
- At least 5 years of experience in administering complex information management systems.
- Strong skills in software and hardware troubleshooting, configuration management, and system integration.
- Proficiency in web content management and web development (i.e. HTML, CSS, JavaScript), coupled with experience working with APIs and data integration processes.
- Commitment to creating an inclusive environment that values diversity.

**Preferred:**
- Experience with Ex Libris Alma/Primo VE or willingness to be certified within 6 months.
- Knowledge of digital preservation and library metadata standards.
- Demonstrated project management skills for large-scale systems implementation or migration projects.""")

    st.subheader("Type")
    st.write("Full Time")

    st.subheader("How to Apply")
    st.link_button("Apply Now", "https://fa-exci-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_2/job/846/")
    st.write("For best consideration, please submit your application materials by Monday, February 23.")

    st.subheader("Salary")
    st.write("Not specified")

    st.subheader("Contact")
    st.write("Ashley Mills, Assistant Director for Learner Engagement & Access Services")