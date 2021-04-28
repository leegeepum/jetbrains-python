groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

n = int(input())

group_dict = {groups[i]: input() if i <
              n else None for i in range(len(groups))}
print(group_dict)
