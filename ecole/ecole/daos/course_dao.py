# -*- coding: utf-8 -*-

"""
Classe Dao[Course]
"""

from ecole.ecole.models.course import Course
from ecole.ecole.models.teacher import Teacher
from ecole.ecole.daos.dao import Dao
from ecole.ecole.daos.teacher_dao import TeacherDao
from dataclasses import dataclass
from typing import Optional


@dataclass
class CourseDao(Dao[Course]):
    def create(self, course: Course) -> int:
        """Crée en BD l'entité Course correspondant au cours obj

        :param course: à créer sous forme d'entité Course en BD
        :return: l'id de l'entité insérée en BD (0 si la création a échoué)
        """
        ...
        return 0

    def read(self, id_course: int) -> Optional[Course]:
        """Renvoit le cours correspondant à l'entité dont l'id est id_course
            (ou None s'il n'a pu être trouvé)"""
        course: Optional[Course]
        with Dao.connection.cursor() as cursor:
            sql = """
            SELECT 
                c.id_course, c.name, c.start_date, c.end_date, 
                t.id_teacher, t.hiring_date, 
                p.first_name, p.last_name, p.age
            FROM course c
            LEFT JOIN teacher t ON c.id_teacher = t.id_teacher
            LEFT JOIN person p ON t.id_person = p.id_person
            WHERE c.id_course = %s
        """
            cursor.execute(sql, (id_course,))
            record = cursor.fetchone()
        if record is not None:
            course = Course(record['name'], record['start_date'], record['end_date'])
            teacher = Teacher(
                hiring_date=record['hiring_date'],
                first_name=record['first_name'],
                last_name=record['last_name'],
                age=record['age']
            )
            course.teacher = teacher
            course.id = record['id_course']
        else:
            course = None

        return course

    def update(self, course: Course) -> bool:
        """Met à jour en BD l'entité Course correspondant à course, pour y correspondre

        :param course: cours déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        ...
        return True

    def delete(self, course: Course) -> bool:
        """Supprime en BD l'entité Course correspondant à course

        :param course: cours dont l'entité Course correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """
        ...
        return True
