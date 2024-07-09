import io
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph

class Resume:

    def __init__(self, name, email, mobile, linkedin, objective,ssc_place, ssc_adr, ssc_year, ssc_result, ssc_degree, e2_place, e2_adr, field, branch_d, e2_year, e2_result, e3_place, e3_adr, field1, branch, e3_year, e3_result, tech_skills, soft_skills, lang, tools, hobbie, proj1_title, proj1_desc, proj2_title, proj2_desc, certificates):
        #Register fonts
        pdfmetrics.registerFont(TTFont('Arial', './font/Arial.ttf'))
        pdfmetrics.registerFont(TTFont('Roboto-Medium', './font/Roboto-Medium.ttf'))

        self.x = 20
        self.y = 810
        self.filename = 'resume.pdf'

        self.font = 'Arial'
        self.font1 = 'Roboto-Medium'

        #Header Info
        self.name = name
        self.email = email
        self.linkedin = linkedin
        self.mobile = mobile
        self.objective = objective

        #Education Info
        self.e1_place = ssc_place
        self.e1_adrs = ssc_adr
        self.e1_degree = ssc_degree
        self.e1_year = ssc_year
        self.e1_result = ssc_result

        self.e2_place = e2_place
        self.e2_adrs = e2_adr
        self.e2_degree = f'{field} {branch_d}'
        self.e2_year = e2_year
        self.e2_result = e2_result

        self.e3_place = e3_place
        self.e3_adrs = e3_adr
        self.e3_degree = f'{field1} {branch}'
        self.e3_year = e3_year
        self.e3_result = e3_result

        self.skills = tech_skills.split(",")
        self.soft_skills = soft_skills.split(",")
        self.lang = lang.split(",")
        self.tools = tools.split(",")
        self.hobbies = hobbie.split(",")

        self.project1_title = proj1_title
        self.project1_description = proj1_desc

        self.project2_title = proj2_title
        self.project2_description = proj2_desc

        self.certi = certificates

    def draw_paragraph(self, pdf, text, x, y):
        styles = getSampleStyleSheet()
        style = styles["Normal"]
        paragraph = Paragraph(text, style)
        paragraph.wrapOn(pdf, 540, 5)
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
        pdf.drawString((self.x + 10), (self.y - 70), "Objective : ")
        self.draw_paragraph(pdf, self.objective, self.x + 20, self.y - 110)

        self.y = self.y-60
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
        pdf.drawString((self.x + 10), (self.y - 365), self.project1_title)

        pdf.setFont(self.font, 10)
        if len(self.project1_description) > 350:
            self.draw_paragraph(pdf, self.project1_description, self.x + 20, self.y - 430)
        else:
            self.draw_paragraph(pdf, self.project1_description, self.x + 20, self.y - 410)

        # Project 2
        pdf.setFont(self.font1, 11)
        pdf.drawString((self.x + 10), (self.y - 455), self.project2_title)

        pdf.setFont(self.font, 10)
        if len(self.project2_description) > 350:
            self.draw_paragraph(pdf, self.project2_description, self.x + 20, self.y - 520)
        else:
            self.draw_paragraph(pdf, self.project2_description, self.x + 20, self.y - 500)

        # Separator
        pdf.line(10, (self.y - 530), 585, (self.y - 530))

        pdf.setFont(self.font1, 14)
        pdf.drawCentredString(300, (self.y - 550), "CERTIFICATIONS")

        pdf.setFont(self.font, 11)
        x1 = self.x + 80
        x2 = self.x + 330
        y1 = self.y - 565
        y2 = self.y - 565

        for k,v in self.certi.items():
            pdf.drawString(x1, y1, k)
            pdf.drawString(x1 + 170, y1, " : ")
            pdf.drawString(x2, y2, v)
            y1 -= 15
            y2 -= 15

        self.y = y2
        # Separator
        pdf.line(10, (self.y), 585, (self.y))

        pdf.setFont(self.font1, 14)
        pdf.drawCentredString(300, (self.y-20), "HOBBIES")

        #Hobbies
        pdf.setFont(self.font, 11)
        hobbie = ""
        for ele in self.hobbies:
            if ele != self.hobbies[-1]:
                hobbie = hobbie + f'{ele}, '
            else:
                hobbie = hobbie + f'{ele}. '
        pdf.drawString(self.x + 30, self.y - 40, hobbie)
        pdf.save()
        buffer.seek(0)
        return buffer
