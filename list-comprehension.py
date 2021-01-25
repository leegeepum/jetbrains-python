"""
Given a numeric sequence, create a list in which each number will be a digit from this input string. Then use this list to calculate the running total, or cumulative sum. Essentially, it's a new list of partial sums that gets updated every time a new element appears.

For example, we can transform the list [1, 2, 3] to [1, 1 + 2, 1 + 2 + 3], which equals to [1, 3, 6].

 Report a typo
Sample Input 1:

15325
Sample Output 1:

[1, 6, 9, 11, 16]
"""

list1 = [int(x) for x in input()]
list2 = [sum(list1[:num + 1]) for num in range(len(list1))]

print(list2)
