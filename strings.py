"""
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
