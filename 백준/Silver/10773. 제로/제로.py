import sys
count = int(sys.stdin.readline().rstrip())
nums = []
for i in range(count):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        del nums[len(nums) -1]
    else:
        nums.append(num)
sum = 0
for i in nums:
    sum += i
print(sum)