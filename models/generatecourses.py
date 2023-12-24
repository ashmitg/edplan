from pdfminer.high_level import extract_text
from io import BytesIO
from flask import jsonify
from models.deanzadb import subject_to_courses,igetc_prefs,prefix_options, Course, igetc_rankings, lab_set

from models.generateschedule import create_balanced_schedule

import re
import pdfminer.high_level
requirements_data = {
    "English Composition": {"courses" : 1, "discipline":1},
    "Critical Thinking-English Composition":{"courses" : 1, "discipline":1},
    "Mathematics": {"courses" : 1, "discipline" : 1},
    "Arts": {"courses" : 2, "discipline" : 1},
    "Humanities": {"courses" : 1, "discipline" : 1},
    "Social Science": {"courses": 3, "discipline" : 2},
    "Physical Science": {"courses" : 1, "discipline" : 1},
    "Biological Science": {"courses" : 1, "discipline" : 1 },
    "Lab Science" : {"courses" : 1, "discipline" : 1}
}
def remove_whitespace_from_end(string):
    while string.endswith(' '):
        string = string[:-1]

    return string

#extract courses from assist.org agreement
def extract_courses_from_pdf(pdf_file):
    pdf_stream = BytesIO(pdf_file)
    text = pdfminer.high_level.extract_text(pdf_stream)

    # Split text into lines
    lines = text.split('\n')

    # Extract courses after ← symbol
    courses = []
    for line in lines:
      if '←' in line:
        course = line.split('←')[-1].strip()
        if course != "This Course is Never Articulated" and course != "No Course Articulated":
            parts = course.split("-")
            parts = parts[0]
            parts = remove_whitespace_from_end(parts)
            if(parts[-1].upper()=="H"):
              courses.append(parts[:-1])
            else:
              courses.append(parts)
      
    return courses

#process the courses as well as update igetc requirements
def process(pdf_data,  qmax, smax, passed_interest):
  requirements_data = {
    "English Composition": {"courses" : 1, "discipline":1},
    "Critical Thinking-English Composition":{"courses" : 1, "discipline":1},
    "Mathematics": {"courses" : 1, "discipline" : 1},
    "Arts": {"courses" : 2, "discipline" : 1},
    "Humanities": {"courses" : 1, "discipline" : 1},
    "Social Science": {"courses": 3, "discipline" : 2},
    "Physical Science": {"courses" : 1, "discipline" : 1},
    "Biological Science": {"courses" : 1, "discipline" : 1 },
    "Lab Science" : {"courses" : 1, "discipline" : 1}
}

  courses = extract_courses_from_pdf(pdf_data)
  courses = [re.sub('\u200b', '', course) for course in courses]
  courses = set(courses)
  courses = sorted(courses)

  valuess = []
  for course in courses:
    parts = course.split(" ")
    parts = parts[0]
    parts = remove_whitespace_from_end(parts)
    if parts=="ESL":
       continue
    see = False
    if parts in igetc_prefs:
      
      for course_sections in subject_to_courses[igetc_prefs[parts]]:
        
        if course in course_sections.name:
          valuess.append(course_sections)
          see = True
          if requirements_data[igetc_prefs[parts]]["courses"]>0:
              requirements_data[igetc_prefs[parts]]["courses"]-=1 
              if course_sections in lab_set and requirements_data["Lab Science"]["courses"]>0:
                requirements_data["Lab Science"]["courses"]-=1

    if see==False:
      section = ""
      if parts.upper() in igetc_prefs:
          section = igetc_prefs[parts.upper()]
      else:
          section = prefix_options[parts]["name"]
      temp = Course(course, section, prefix_options[parts]["difficulty"],prefix_options[parts]["credits"])
      valuess.append(temp)

      #loop must also adjust the deanza_db igetc reqs accordingly

  for interest in passed_interest:
    interest = interest.upper()
    if interest in igetc_prefs:
        for course in subject_to_courses[igetc_prefs[interest]]:
          igetc_rankings[igetc_prefs[interest]][interest] = igetc_rankings[igetc_prefs[interest]][interest]*3

          
  sorted_rankings = dict(sorted(igetc_rankings.items(), key=lambda x: max(x[1].values()), reverse=True))
  values_set = set(valuess)
  #check for duplicates in the alr added courses
  for subject_area, scores in sorted_rankings.items():
      top_courses = sorted(scores, key=scores.get, reverse=True)[:requirements_data[subject_area]["discipline"]]
      for categories in top_courses:
          total = min(2,requirements_data[subject_area]["courses"])
          for course in subject_to_courses[igetc_prefs[categories]]:
              if total==0:
                break
              if categories in course.name and course not in values_set:
                  total-=1
                  valuess.append(course)
                  values_set.add(course)
                  requirements_data[subject_area]["courses"]-=1

  course_schedule = create_balanced_schedule(valuess,qmax,smax)
  deserialized_data = []

  for quarter_courses in course_schedule:
      deserialized_quarter = [course.to_dict() for course in quarter_courses]
      deserialized_data.append(deserialized_quarter)
  # Return the deserialized data
  return deserialized_data
  
  


