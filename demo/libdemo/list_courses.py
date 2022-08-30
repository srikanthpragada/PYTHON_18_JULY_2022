import requests
from bs4 import BeautifulSoup

with open("courses.xml", 'rt') as f:
    contents = f.read()

bs = BeautifulSoup(contents, "xml")
courses = bs.find_all("course")
for course in courses:
    print(f"{course.title.text:30} {course.fee.text:5}")
