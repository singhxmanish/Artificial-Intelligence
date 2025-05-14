import random

# Probability: simulating a coin flip/throw of a dice
outcome = ['Head', 'Tail']
outcome1 = [1,2,3,4,5,6]

def ran(input,nam):
    result = random.choice(nam)
    print(result)

ran(outcome,outcome)
ran(outcome1,outcome1)
