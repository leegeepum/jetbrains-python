"""
1
Given a numeric sequence, create a list in which each number will be a digit from this input string. 
Then use this list to calculate the running total, or cumulative sum. 
Essentially, it's a new list of partial sums that gets updated every time a new element appears.
For example, we can transform the list [1, 2, 3] to [1, 1 + 2, 1 + 2 + 3], which equals to [1, 3, 6].

Sample Input 1:
15325

Sample Output 1:
[1, 6, 9, 11, 16]
"""

list1 = [int(x) for x in input()]
list2 = [sum(list1[:num + 1]) for num in range(len(list1))]

print(list2)


"""
2
For instance, if your string is 123, an average of 1 and 2 will be 1.5, and an average of 2 and 3 will be 2.5.
Print the result. Notice that this list will have one less item.

Sample Input 1:
12345

Sample Output 1:
[1.5, 2.5, 3.5, 4.5]
"""

num_list = input()

new_num_list = [int(x) for x in num_list]
av_num_list = [sum(new_num_list[y:y + 2]) /
               2 for y in range(len(num_list) - 1)]
print(av_num_list)

# best answer
# print([(int(n[i]) + int(n[i + 1])) / 2 for i in range(len(n) - 1)])

"""
3
Select only students with the best grade ("A") and print their names in a list. 
Do all this in one line. 
We have already created the students variable with other names and grades.
"""

students = [["Jane", "B"], ["Kate", "B"], ["Alex", "C"],
            ["Elsa", "A"], ["Max", "B"], ["Chris", "A"]]
print([student[0] for student in students if student[1] == "A"])

"""
complex one
"""
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']
n = int(input())
group_dict = {groups[i]: input() if i <
              n else None for i in range(len(groups))}
print(group_dict)
