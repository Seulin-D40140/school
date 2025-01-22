# -*- coding: utf-8 -*-

"""
Classe Dao[Course]
"""

from ecole.ecole.daos.dao import Dao
from ecole.ecole.models.teacher import Person
from dataclasses import dataclass
from typing import Optional


@dataclass
class TeacherDao(Dao[Person]):
    def create(self, course: Person) -> int:
        """Crée en BD l'entité Course correspondant au cours obj

        :param course: à créer sous forme d'entité Course en BD
        :return: l'id de l'entité insérée en BD (0 si la création a échoué)
        """
        ...
        return 0

    def read(self, id_person: int) -> Optional[Person]:
        """Renvoit le cours correspondant à l'entité dont l'id est id_course
            (ou None s'il n'a pu être trouvé)"""
        teacher: Optional[Person]
        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM person WHERE id_person=%s"
            cursor.execute(sql, (id_person,))
            record = cursor.fetchone()
        if record is not None:
            person = Person(record['hiring_date'])
            teacher.id = record['id_teacher']
        else:
            teacher = None

        return teacher

    def update(self, course: Person) -> bool:
        """Met à jour en BD l'entité Course correspondant à course, pour y correspondre

        :param course: cours déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        ...
        return True

    def delete(self, course: Person) -> bool:
        """Supprime en BD l'entité Course correspondant à course

        :param course: cours dont l'entité Course correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """
        ...
        return True
