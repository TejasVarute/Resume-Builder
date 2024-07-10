import streamlit as st
from resume import Resume

class strealit_web_gui:
    def __init__(self):
        pass
    def data(self):
        heading = """<h1 align="center">ATS FRIENDLY RESUME BUILDER</h1><br><br>"""
        st.html(heading)

        st.header("PERSONAL INFORMATION")
        name = st.text_input('Your Name', placeholder='Enter Your Name')
        email = st.text_input('Your Email', placeholder='Enter Your Email')
        mobile = st.text_input('Your Mobile No.', placeholder='Enter Your Mobile Number')
        linkedin = st.text_input('Your Linkedin', placeholder='Enter Your Linkedin URL')
        objective = st.text_input('Your Objective (2-3 lines)', placeholder='Enter Your Objective')

        st.header("EDUCATION INFORMATION")
        st.subheader("SSC")
        ssc_place = st.text_input('Your SSC college', placeholder='Enter Your 10th College Name')
        ssc_adr = st.text_input('Your college City', placeholder='Enter Your 10th College City')
        ssc_year = st.text_input('Your SSC Year of Passing')
        ssc_result = st.text_input('Result', placeholder='Enter Your SSC Percentages')
        ssc_degree = "SSC"
        
        branches = ["Computer Science Engineering", "Artificial Intelligence and Data Structure", "Electronics and Telecommunication Engineering",
                    "Electronics and Computer Engineering", "Electrical Engineering", "Automation and Robotics", "Mechatronics Engineering",
                    "Civil Engineering", "Mechanical Engineering"]

        st.subheader("AFTER SSC")
        field = st.selectbox("Your Field after 10th", ["HSC", "DEPLOMA"])
        if field == 'DEPLOMA':
            branch_d = st.selectbox(f"Select your {field} branch", branches)
        else:
            branch_d = ''
        e2_place = st.text_input(f'Your {field} college', placeholder='Enter Your College Name')
        e2_adr = st.text_input('Your college City', placeholder='Enter Your College City')
        e2_year = st.text_input(f'Your {field} Passing Year')
        e2_result = st.text_input('Result', placeholder=f'Enter Your {field} Percentages')

        st.subheader("Under Graduation Course")
        field1 = st.selectbox("Your Field", ["BTech", "BFarmcy"])
        
        if field1 == 'BTech':
            branch = st.selectbox(f"Select your {field1} branch", branches)
        else:
            branch = ''
        e3_place = st.text_input(f'Your {field1} college', placeholder='Enter Your College Name')
        e3_adr = st.text_input('Your college City', placeholder=f'Enter Your {field1} College City')
        e3_year = st.text_input(f'Your {field1} Passing Year')
        e3_result = st.text_input('Result', placeholder=f'Enter Your {field1} Percentages / CGPA')

        st.header("SKILLS")
        st.subheader("Technical Skills")
        tech_skills = st.text_input('Enter Technical skills (use (comma , ) for saperation)', placeholder='Enter Technical Skills')
        soft_skills = st.text_input('Enter Soft skills (use (comma , ) for saperation)', placeholder='Enter Soft Skills')
        lang = st.text_input('Enter Languages you speak (use (comma , ) for saperation)', placeholder='Enter languages Known')
        tools = st.text_input('Enter Computer Competencies You Know (use (comma , ) for saperation)', placeholder='Enter Computer competencies')
        hobbie = st.text_input('Enter Hobbies (use (comma ,) for saperation) (Max 12)', placeholder='Enter Your Hobbies')

        st.header("PROJECTS")
        st.subheader("Project 1")
        proj1_title = st.text_input('Enter Title of Project 1)', placeholder='Enter Project 1 Title')
        proj1_desc = st.text_input('Enter Description of Project 1 (3-5 lines))', placeholder='Enter Project 1 Description')

        st.subheader("Project 2")
        proj2_title = st.text_input('Enter Title of Project 2)', placeholder='Enter Project 2 Title')
        proj2_desc = st.text_input('Enter Description of Project 2 (3-5 lines))', placeholder='Enter Project 2 Description')

        st.header("CERTIFICATIONS")
        cert_count = st.text_input('How many Certificates you have (Max 8)', placeholder="How many certificates you have")
        if cert_count and int(cert_count) > 8:
            st.warning("Providing out of limit consider only 8")
        certificates = {}
        if cert_count:
            for i in range (int(cert_count)):
                cert = st.text_input(f'Enter certificate {i+1} details (Eg. AWS : AICTE, Python : IBM)', placeholder=f'Enter certificate {i+1} details')
                if cert:
                    k, v = cert.split(':')
                    certificates[k] = v

        submitted = st.button("Submit all Information")
        if submitted:
            try:
                buffer = Resume(name, email, mobile, linkedin, objective, ssc_place, ssc_adr, ssc_year, ssc_result, ssc_degree,
                            e2_place, e2_adr, field, branch_d, e2_year, e2_result, e3_place, e3_adr, field1, branch,
                            e3_year, e3_result, tech_skills, soft_skills, lang, tools, hobbie, proj1_title,
                            proj1_desc, proj2_title, proj2_desc, certificates).get_pdf()
                st.download_button(label="Resume Download", data=buffer, file_name=f"Resume {name}.pdf",mime="application/pdf")
            except:
                st.subheader(":red[Please Insert All information to get Resume]")

strealit_web_gui().data()
