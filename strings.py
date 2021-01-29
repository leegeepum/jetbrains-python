"""
problem 1 

Sample Input 1:
3

Sample Output 1:
  #  
 ### 
#####
"""

x = int(input())
for i in range(1, x * 2, 2):
    string = "#" * i
    string = string.center(1 + 2 * (x - 1))
    print(string)

"""
better solution
"""
ui = int(input())

hash_lst = ["#" * i for i in range(1, ui * 2) if i % 2 != 0]

for h in hash_lst:
    print(h.center(len(hash_lst[-1])))
