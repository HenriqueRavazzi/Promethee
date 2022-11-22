from typing import List
from promethee import Promethee, Criteria, UsualCurve

class MCDM(Promethee):
    def __init__(self, alternatives: List[str]):
        criterias = self.__set_criterias()
        super().__init__(alternatives, criterias)

    def __set_criterias()-> List[Criteria]:
        criteria = list()

        first_criteria = Criteria(
            name='OEE',
            weight=0.25,
            goal='max',
            curve=UsualCurve()
        )
        criterias.append(first_criteria) 

        second_criteria = Criteria(
            name='Production',
            weight=0.25,
            goal='min',
            curve=UsualCurve()
        )
        criterias.append(second_criteria)

        third_criteria = Criteria(
            name='MTTR',
            weight=0.25,
            goal='min',
            curve=UsualCurve()
        )
        criterias.append(third_criteria)

        fourth_criteria = Criteria(
            name='MTBF',
            weight=0.25,
            goal='min',
            curve=UsualCurve()
        )
        criterias.append(fourth_criteria)

        # You could have as many criterias you want

        return criteria