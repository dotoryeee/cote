import math
num = int(input())
count = 0
for _ in range(num):
    a = int(input())
    if a == 1:
        count += 1
if math.floor(num/2) < count:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')
