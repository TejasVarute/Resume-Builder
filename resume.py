import io
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph

#height : 830 415
#weidth : 550 275
class Resume:

    def __init__(self):  #name, email, mobile, linkedin, ssc_place, ssc_adr, ssc_year, ssc_result, ssc_degree, e2_place, e2_adr, field, e2_year, e2_result, e3_place, e3_adr, field1, branch, e3_year, e3_result, tech_skills, soft_skills, lang, tools, hobbie, proj1_title, proj1_desc, proj2_title, proj2_desc, certificates):
        #Register fonts
        pdfmetrics.registerFont(TTFont('Arial', './font/Arial.ttf'))
        pdfmetrics.registerFont(TTFont('Roboto-Medium', './font/Roboto-Medium.ttf'))

        self.x = 20
        self.y = 810
        self.filename = 'resume.pdf'

        self.font = 'Arial'
        self.font1 = 'Roboto-Medium'

        #Header Info
        self.name = "Tejas Varute"
        self.email = "tvarute@gmail.com"
        self.linkedin = "https://www.linkedin.com/in/tejasvarute"
        self.mobile = "7249025371"

        #Education Info
        self.e1_place = "Janata Secondary School"
        self.e1_adrs = "Hupari"
        self.e1_degree = "SSC"
        self.e1_year = "2019"
        self.e1_result = "79.60"

        self.e2_place = "Parisanna Ingrole Jr. College"
        self.e2_adrs = "Hupari"
        self.e2_degree = "HSC"
        self.e2_year = "2021"
        self.e2_result = "75.17"

        self.e3_place = "Sharad Institute of Technology"
        self.e3_adrs = "Yadrav, Ichalkaranji"
        self.e3_degree = "BTech - Electronics and Computer Engineering"
        self.e3_year = "2025"
        self.e3_result = "8.33"

        self.skills = ['C', 'C++', 'SQL', 'Java', 'Python', 'Oracle']
        self.soft_skills = ['Leadership', 'Quick learner', 'Self Learning']
        self.lang = ['English', 'Hindi', 'Marathi']
        self.tools = ['MS-Word', 'MS-Excel', 'MS-PowerPoint', 'VS-Code']
        self.hobbies = ['Drawing', 'Playing video games', 'Listening music', 'Coding in python']

        self.project1_title = "Elective"
        self.project1_description = "This system automates the subject selection process, ensuring a fair and transparent allocation of elective subjects, while also providing a user-friendly interface for faculties and administrators."

        self.project2_title = "Attendance"
        self.project2_description = "Attendance tracking is a crucial aspect of educational institutions, yet the traditional manual methods are time-consuming and error-prone. This project aims to streamline the attendance tracking process in schools and colleges considering different approach."

        self.certi = {'AWS':"amazon", 'Python':"GUVI", 'DATA ANALYTICS':"CISCO,IBM", 'DATA SCINCE':"Bharat Intern"}

    def draw_paragraph(self, pdf, text, x, y):
        styles = getSampleStyleSheet()
        style = styles["Normal"]
        paragraph = Paragraph(text, style)
        paragraph.wrapOn(pdf, 550, 5)
        paragraph.drawOn(pdf, x, y)

    def get_pdf(self):
        buffer = io.BytesIO()
        pdf = canvas.Canvas(buffer)
        #pdf.drawBoundary(sb=0, x1=10, y1=10, width=575, height=820)

        # Header
        pdf.setFont(self.font1, 18)  #Title Font
        pdf.drawString((self.x + 10), (self.y - 10), self.name)

        pdf.setFont(self.font, 12)
        pdf.drawString((self.x + 10), (self.y - 30), "Email : ")
        pdf.drawString((self.x + 50), (self.y - 30), self.email)
        pdf.drawString((self.x + 10), (self.y - 50), "Linkedin : ")
        pdf.setFillColor(colors.blue)
        pdf.drawString((self.x + 65), (self.y - 50), self.linkedin)
        pdf.setFillColor(colors.black)
        pdf.drawString((self.x + 400), (self.y - 30), "Mobile : ")
        pdf.drawString((self.x + 445), (self.y - 30), self.mobile)

        # Separator
        pdf.line(10, (self.y - 60), 585, (self.y - 60))

        #Education
        pdf.setFont(self.font1, 14)
        pdf.drawCentredString(300, (self.y - 80), "EDUCATION")

        pdf.setFont(self.font1, 11)
        pdf.drawString((self.x + 10), (self.y - 100), self.e1_place)
        pdf.drawString((self.x + 10), (self.y - 135), self.e2_place)
        pdf.drawString((self.x + 10), (self.y - 170), self.e3_place)

        pdf.setFont(self.font, 10)
        pdf.drawString((self.x + 10), (self.y - 115), self.e1_degree+" : Percentage : "+self.e1_result)
        pdf.drawString((self.x + 10), (self.y - 150), self.e2_degree+" : Percentage : "+self.e2_result)
        pdf.drawString((self.x + 10), (self.y - 185), (self.e3_degree+" : CGPA : "+self.e3_result))

        pdf.drawString((self.x + 450), (self.y - 100), self.e1_adrs)
        pdf.drawString((self.x + 450), (self.y - 135), self.e2_adrs)
        pdf.drawString((self.x + 450), (self.y - 170), self.e3_adrs)

        pdf.drawString((self.x + 450), (self.y - 115), self.e1_year)
        pdf.drawString((self.x + 450), (self.y - 150), self.e2_year)
        pdf.drawString((self.x + 450), (self.y - 185), self.e3_year)

        # Separator
        pdf.line(10, (self.y - 200), 585, (self.y - 200))

        # Skills
        pdf.setFont(self.font1, 14)
        pdf.drawCentredString(300, (self.y - 220), "SKILLS")

        #Technical
        pdf.setFont(self.font1, 10)
        pdf.drawString((self.x + 10), (self.y - 250), "TECHNICAL SKILLS")

        pdf.setFont(self.font, 10)
        skills = str()
        for ele in self.skills:
            skills += ele
            if ele != self.skills[-1]:
                skills += ","
            else:
                skills += "."
        pdf.drawString((self.x + 150), (self.y - 250), " : "+skills)

        #Soft
        pdf.setFont(self.font1, 10)
        pdf.drawString((self.x + 10), (self.y - 270), "SOFT SKILLS")

        pdf.setFont(self.font, 10)
        soft = str()
        for ele in self.soft_skills:
            soft += ele
            if ele != self.soft_skills[-1]:
                soft += ","
            else:
                soft += "."
        pdf.drawString((self.x + 150), (self.y - 270), " : "+soft)

        #Language
        pdf.setFont(self.font1, 10)
        pdf.drawString((self.x + 10), (self.y - 290), "LANGUAGES KNOWN")

        pdf.setFont(self.font, 10)
        lang = str()
        for ele in self.lang:
            lang += ele
            if ele != self.lang[-1]:
                lang += ","
            else:
                lang += "."
        pdf.drawString((self.x + 150), (self.y - 290), " : "+lang)

        # Tools
        pdf.setFont(self.font1, 10)
        pdf.drawString((self.x + 10), (self.y - 310), "COMPUTER COMPETENCIES")

        pdf.setFont(self.font, 10)
        tool = str()
        for ele in self.tools:
            tool += ele
            if ele != self.tools[-1]:
                tool += ","
            else:
                tool += "."
        pdf.drawString((self.x + 150), (self.y - 310), " : " + tool)

        # Separator
        pdf.line(10, (self.y - 320), 585, (self.y - 320))

        # Projects
        pdf.setFont(self.font1, 14)
        pdf.drawCentredString(300, (self.y - 340), "PROJECTS")

        #Project 1
        pdf.setFont(self.font1, 11)
        pdf.drawString((self.x + 10), (self.y - 360), self.project1_title)

        pdf.setFont(self.font, 10)
        if len(self.project1_description) > 250:
            self.draw_paragraph(pdf, self.project1_description, self.x + 10, self.y - 420)
        else:
            self.draw_paragraph(pdf, self.project1_description, self.x + 10, self.y - 400)

        # Project 2
        pdf.setFont(self.font1, 11)
        pdf.drawString((self.x + 10), (self.y - 460), self.project2_title)

        pdf.setFont(self.font, 10)
        if len(self.project2_description) > 250:
            self.draw_paragraph(pdf, self.project2_description, self.x + 10, self.y - 510)
        else:
            self.draw_paragraph(pdf, self.project2_description, self.x + 10, self.y - 490)

        # Separator
        pdf.line(10, (self.y - 540), 585, (self.y - 540))

        pdf.setFont(self.font1, 14)
        pdf.drawCentredString(300, (self.y - 560), "CERTIFICATIONS")

        pdf.setFont(self.font, 11)
        x1 = self.x + 80
        x2 = self.x + 330
        y1 = self.y - 590
        y2 = self.y - 590

        for k,v in self.certi.items():
            pdf.drawString(x1, y1, k)
            pdf.drawString(x1 + 120, y1, " : ")
            pdf.drawString(x2, y2, v)
            y1 -= 20
            y2 -= 20

        self.y = y2
        # Separator
        pdf.line(10, (self.y), 585, (self.y))

        pdf.setFont(self.font1, 14)
        pdf.drawCentredString(300, (self.y-20), "HOBBIES")

        #Hobbies
        pdf.setFont(self.font, 11)

        y = self.y - 30
        counter = 0
        for k in range (len(self.hobbies)-1):
            x = self.x + 30
            y -= 20
            for i in range (3):
                if counter == len(self.hobbies):
                    break
                pdf.drawString(x, y, self.hobbies[counter])
                counter+=1
                x += 200
        pdf.save()
        buffer.seek(0)
        return buffer
