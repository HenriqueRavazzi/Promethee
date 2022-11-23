from Criterias import MCDM
import numpy

alternatives = [
    'First Alternative',
    'Second Alternative',
    'Third Alternative',
    'Fourth Alternative'
]

my_decision = MCDM(alternatives)

first_criteria_values = [10, 22, 14, 15]
second_criteria_values = [9, 98, 14, 15]
third_criteria_values = [10, 30, 14, 15]
fourth_criteria_value = [5, 83, 14, 15]

values = np.array([
    first_criteria_values,
    second_criteria_values,
    third_criteria_values,
    fourth_criteria_value
])

output = my_decision.prioritize(values)


for i, unicriteria_phi in enumerate(output.unicriteria_phi):
    print(f'{i}- {unicriteria_phi}\n')