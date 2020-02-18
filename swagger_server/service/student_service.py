import json
import logging
import os
import tempfile

from tinydb import TinyDB, Query
from tinydb.middlewares import CachingMiddleware
from functools import reduce
import uuid

from swagger_server.models import Student

db_dir_path = tempfile.gettempdir()
db_file_path = os.path.join(db_dir_path, "students.json")
student_db = TinyDB(db_file_path)

def add_student(student):
  Student = Query()
  res = student_db.search((Student.first_name == student.first_name) and (Student.last_name == student.last_name))
  print("======= POST DATA: ")
  print(student)
  # final_query = reduce(lambda a, b: a & b, queries)
  # res = student_db.search(final_query)
  if res:
    return 'already exists', 405
  else: 
    if (student.first_name == None or student.last_name == None):
      return 'give first and last name', 405
  doc_id = student_db.insert(student.to_dict())
  student.student_id = doc_id
  print("Created student")
  return student.student_id, 200


def get_student_by_id(student_id, subject):
    student = student_db.get(doc_id=int(student_id))
    if not student:
        print('student not found')
        return "student not found", 404
    student = Student.from_dict(student)
    if subject == None:
        print("no subject given")
        return student
    else:
        if not (student.grades[subject]):
          print("grade not found")
          return "grade not found", 404
        else:
          print("grade found")
          return student


def delete_student(student_id):
    student = student_db.get(doc_id=int(student_id))
    if not student:
        return "student not found", 404
    student_db.remove(doc_ids=[int(student_id)])
    return student_id
