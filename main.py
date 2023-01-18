import requests

base_url = ''

resp = requests.get(base_url)

data = resp.json()

import os
import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

doc = SimpleDocTemplate("letter_film.pdf", pagesize=letter,
                        rightMargin=72, leftMargin=72,
                        topMargin=72, bottomMargin=18)

for details in data:
    project_name = details['project_name']
    company_address = details['company_address']
    date = details['date']
    date_to_start = details['date_to_start']
    finish_time = details['start_time']
    street_address = details['street_address']
    fax_number = details['fax_number']
    phone_number = details['phone_number']
    department_Location = details['department_Location']
    company_name = details['company_name']
    start_time = details['start_time']

page = []
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))


def add_space():
    page.append(Spacer(1, 12))


def add_text(text, space=0):
    if type(text) == list:
        for f in text:
            add_text(f)
    else:
        ptext = f'<font size="12">{text}</font>'
        page.append(Paragraph(ptext, styles["Normal"]))
        if space == 1:
            add_space()
        add_space()

    # =============================== The content =======================
    # ============================== of the document ====================


add_text([
    ''' <u> SAMPLE RESIDENT/BUSINESS NOTIFICATION LETTER </u>


    '''.splitlines()])
add_text(company_name)
add_text(date)
add_text(['Dear Neighbors/Businesses, '.splitlines()])

add_text(["""This letter is to inform you that on {},{}  
    will be filming scenes at locations in this area from approximately {}  to  {}.{} is produced by
    {}.""".format(

    date,
    company_name,
    start_time,
    finish_time,
    project_name,
    company_name, )
])

add_text([""" In order to facilitate filming, we will need to hold parking for our
    production vehicles beginning {}  {}.The streets
    affected include:  """.format(

    start_time,
    date_to_start, )

])

add_text(["""
        {}
        """.format(

    street_address, )])

add_text(["""
    We are aware of the inconvenience caused by our activity and
    apologize in advance. Rest assured that we will do everything possible
    to minimize the impact of our activities on your neighborhood. If you
    have particular concerns (scheduled deliveries, construction,
    accessibility needs, etc.) that must be addressed, please call the
    Location Department at {}. We will do everything
    possible to find a mutually agreeable solution. """.format(phone_number, )])

add_text(["""
    Your cooperation will help to make this location shoot a success!
    Thank you in advance for your understanding and cooperation. """])

add_text(["""{}""".format(department_Location, )])
add_text(["""{}""".format(phone_number, )])
add_text(["""{}""".format(company_address, )])
add_text(["""{}""".format(fax_number, )])

# ===========================================================

doc.build(page)

os.startfile("letter_film.pdf")

