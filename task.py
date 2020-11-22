from dataclasses import dataclass, field
from typing import List
from statistics import mean
import random
import json

@dataclass
class Student:
    name : str
    marks : List[int] = field(default_factory=list)
    attendance : List[bool] = field(default_factory=list)

    def get_name(self):
        return self.name
    def add_mark(self, mark):
        self.marks.append(mark)
    def average_mark(self):
        return mean(self.marks)
    def check_attendance(self, attendance):
        self.attendance.append(attendance)
    def frequency(self):
        return mean(self.attendance)*100

@dataclass
class Form:
    form_name : str
    students : List[Student] = field(default_factory=list)

    def add_student(self, student):
        self.students.append(student)
    def form_average_mark(self):
        temp=[]
        map_it=[]
        for s in self.students:
            map_it += list(map(lambda x : temp.append(x), s.marks))
        return mean(temp)
        
    def form_frequency(self):
        temp=[]
        map_it=[]
        for s in self.students:
            map_it += list(map(lambda x : temp.append(x), s.attendance))
        return mean(temp)*100

@dataclass
class School:
    school_name : str
    forms : List[Form] = field(default_factory=list)

    def add_form (self,form):
        self.forms.append(form)

    def get_students_list(self):
        stud = []
        for f in self.forms:
            for s in f.students:
                stud.append(s.name)
        return stud
       
    def get_marks_list(self):
        marks = []
        map_it=[]
        for f in self.forms:
            for s in f.students:
                map_it += list(map(lambda x : marks.append(x), s.marks))
        return marks

def get_student_average_score(name, form):
    for s in form.students:
        if s.name == name:
            return s.average_mark()

def get_form_and_school_name(name, schools):
    for s in schools:
        for f in s.forms:
            for st in f.students:
                if st.name == name:
                    return [f.form_name, s.school_name]

if __name__ == "__main__":

    schools = [School('High School'), School('Primary School')]
    forms = [Form('1A'), Form('1B'), Form('1C')]
    students = [ Student('Jan Kowalski'), Student('Adam Nowak'), Student('Maria Mazur'), 
            Student('Anna Wisniewska'), Student('Kamil Wojcik'), Student('Karol Kowalczyk'),
            Student('Maria Wojciechowska'), Student('Anna Mlynarska'), Student('Maja Wozniak'),
            Student('Zofia Zawadzka'), Student('Filip Kwiatkowski'), Student('Michal Dudek')]

    forms[0].add_student(students[0])
    forms[0].add_student(students[1])
    forms[0].add_student(students[2])
    forms[0].add_student(students[3])
    forms[1].add_student(students[4])
    forms[1].add_student(students[5])
    forms[1].add_student(students[6])
    forms[1].add_student(students[7])
    forms[2].add_student(students[8])
    forms[2].add_student(students[9])
    forms[2].add_student(students[10])
    forms[2].add_student(students[11])

    schools[0].add_form(forms[0])
    schools[0].add_form(forms[1])
    schools[1].add_form(forms[2])

    for i in range(0,3):
        for s in students:
            s.add_mark(random.randrange(20,55,5)/10.0)
            s.check_attendance(random.randrange(0,2,1))
    
    print("{} - students list:\n{}\n".format(schools[0].school_name, schools[0].get_students_list()))
    print("{} - marks list:\n{}\n".format(schools[0].school_name, schools[0].get_marks_list()))

    print("{}: srednia ocena -> {:.2f}, frekwencja -> {:.2f}% ".format(students[0].name, students[0].average_mark(), students[0].frequency() ))
    print("{}: srednia ocena -> {:.2f}, frekwencja -> {:.2f}% ".format(students[1].name, students[1].average_mark(), students[1].frequency() ))
    print("{}: srednia ocena -> {:.2f}, frekwencja -> {:.2f}% \n".format(students[2].name, students[2].average_mark(), students[2].frequency() ))

    print("{}: srednia ocena -> {:.2f}, frekwencja -> {:.2f}%".format(forms[0].form_name, forms[0].form_average_mark(), forms[0].form_frequency()))
    print("{}: srednia ocena -> {:.2f}, frekwencja -> {:.2f}% \n".format(forms[1].form_name, forms[1].form_average_mark(), forms[1].form_frequency()))

    print("{} -> average score: {:.2f}\n".format('Maria Mazur', get_student_average_score('Maria Mazur', forms[0])))
    
    print("{} goes to form {} and {}".format("Maria Mazur", get_form_and_school_name('Maria Mazur', schools)[0], get_form_and_school_name('Maria Mazur', schools)[1]))
    print("{} goes to form {} and {}".format("Filip Kwiatkowski", get_form_and_school_name('Filip Kwiatkowski', schools)[0], get_form_and_school_name('Filip Kwiatkowski', schools)[1]))

    all_students = {}
    for s in students:
       all_students[s.get_name()] = get_form_and_school_name(s.get_name(), schools)

    with open('students.json', 'w') as s:
        json.dump(all_students, s, indent=2, separators=(" ", " goes to: "))