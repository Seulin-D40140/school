#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application de gestion d'une école
"""

from ecole.ecole.daos.course_dao import CourseDao
from ecole.ecole.daos.teacher_dao import TeacherDao
from business.school import School

def main() -> None:
    course_dao = CourseDao()
    teacher_dao = TeacherDao()
    """Programme principal."""
    print("""\
--------------------------
Bienvenue dans notre école
--------------------------""")


    id_to_fetch = 4  # Remplacez par l'ID que vous souhaitez lire
    course = School.get_course_by_id(id_to_fetch)
    teacher = School.get_teacher_by_id(id_to_fetch)
    student = School.get_student_by_id(1)
    print(course)
    print(teacher)
    print(student)


if __name__ == '__main__':
    main()
