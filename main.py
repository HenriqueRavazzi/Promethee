from Criterias import CriteriasPriorization
import numpy as np

alternatives = [
    'OP 1',
    'OP 2',
    'OP 3'
]

my_decision = CriteriasPriorization(alternatives)

Quality = [10, 22, 34]
Production = [9, 98, 186]
Avaibility = [10, 30, 50]
MTTR = [5, 83, 161]
MTBF = [15, 20, 25]

values = np.array([
    Quality,
    Production,
    Avaibility,
    MTTR,
    MTBF
])

output = my_decision.prioritize(values)


for i, unicriteria_phi in enumerate(output.unicriteria_phi):
    print(f'{i}- {unicriteria_phi}\n')