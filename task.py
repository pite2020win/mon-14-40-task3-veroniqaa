# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
#
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school(s?).
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface (might be text-like).
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.


class Student:
  
  def __init__ (self, name, surname):
    self.name = name
    self.surname = surname
    self.marks = []
    self.attendance = []
  def add_mark(self, mark):
    self.marks.append(mark)
  def average_mark(self):
    return sum(self.marks)/len(self.marks)
  def check_attendance(self, attendance):
    self.attendance.append(attendance)
  def frequency(self):
    retrun (sum(self.attendance)/len(self.attendance))*100

class Form: 

  def __init__ (self, name):
    self.form_name = name
    self.students = []
  def add_student(self, student):
    self.students.append(student)
  def form_average_mark(self):
    temp = 0.0
    for s in students_list:
      temp+=s.average_mark()
    return temp/len(self.students_list)
  def form_frequency(self):
    temp = 0.0
    for s in students_list:
      temp+=s.frequency()
    return temp/len(self.students_list)
 

class School:

  def __init__ (self, name):
    self.school_name = name
    self.forms = []
  def add_form (self, form):
    self.forms.append(form)

if __name__ == "__main__":
  student1 = Student('Jan', 'Kowalski')
  student2 = Student('Adam', 'Nowak')
  student3 = Student('Maria', 'Mazur')
  student4 = Student('Anna', 'Wisniewska')

  form1 = Form('1A')
  form2 = Form('1B')

  form1.add_student(student1)
  form1.add_student(student2)
  form2.add_student(student3)
  form2.add_student(student4)

  school1 = School('High School')
  school1.add_form(form1)
  school1.add_form(form2)

  student1.add_mark(3.5)
  student1.add_mark(2)
  student1.add_mark(5)
  student2.add_mark(4.5)
  student2.add_mark(5)
  student3.add_mark(2)
  student3.add_mark(5)
  student3.add_mark(5)
  student3.add_mark(3.5)
  student4.add_mark(2)
  student4.add_mark(5)

  student1.check_attendance(1) 
  student1.check_attendance(1)
  student1.check_attendance(1)
  student2.check_attendance(1) 
  student2.check_attendance(0)
  student2.check_attendance(1)
  student3.check_attendance(0) 
  student3.check_attendance(0)
  student3.check_attendance(1)
  student4.check_attendance(1) 
  student4.check_attendance(1)
  student4.check_attendance(0)
