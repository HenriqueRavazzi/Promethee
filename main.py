from .Criterias import MCDM
import numpy as np

alternatives = [
    'First Alternative',
    'Second Alternative',
    'Third Alternative',
    'Fourth Alternative'
]

my_decision = MCDM(alternatives)

first_criteria_values = [10, 22]
second_criteria_values = [9, 98]
third_criteria_values = [10, 30]
fourth_criteria_value = [5, 83]

values = np.array([
    first_criteria_values,
    second_criteria_values,
    third_criteria_values,
    fourth_criteria_value
])

output = my_decision.prioritize(values)