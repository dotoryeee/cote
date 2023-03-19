target = int(input())
facto = 1
if target == 0:
    print(1)
else:
    for i in range(1, target+1):
        facto *= i
    print(facto)