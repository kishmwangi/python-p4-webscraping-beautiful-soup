from turtle import ht
from bs4 import BeautifulSoup
import requests


headers = {'user-agent': 'my-app/0.0.1'}

# We will be uses the our-courses page
html = requests.get("https://flatironschool.com/our-courses/", headers=headers)

doc = BeautifulSoup(html.text, 'html.parser')

course = doc.select('.heading-60-black.color-black.mb-20')

for course in course in courses:
    print(course.contents[0].strip())