num1 = int(input())
num2 = int(input())
num3 = int(input())
mean = (num1 + num2 + num3) / 3
print(mean)

if mean >= 60:
    print("Congratulations, you are accepted!")
else:
    print("We regret to inform you that we will not be able to offer you admission.")
