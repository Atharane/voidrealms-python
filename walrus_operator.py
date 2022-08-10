"""
The := operator is officially known as the assignment expression operator.
During early discussions, it was dubbed the walrus operator because
the := syntax resembles the eyes and tusks of a sideways walrus.
You may also see the := operator referred to as the colon equals operator.
Yet another term used for assignment expressions is named expressions.
"""

for i in range(x := (int(input("Number: ")))):
    print(f'{i}/{x}')

''' Use cases:
1. Assigning a value to a variable 

2. Debugging
>>> # Distance between Oslo and Vancouver
>>> 2 * rad * asin(
...     sqrt(
...         (ϕ_hav := sin((ϕ2 - ϕ1) / 2) ** 2)
...         + cos(ϕ1) * cos(ϕ2) * sin((λ2 - λ1) / 2) ** 2
...     )
... )
The walrus operator allows you to calculate the value of the full expression and 
keep track of the value of ϕ_hav at the same time. 
Allows you to confirm that you did not introduce any errors while debugging.

3. List comprehension
>>> results = [value for num in numbers if (value := slow(num)) > 0]

'''