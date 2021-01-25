courses = ['computer science', 'msip', 'spare', 'data', 'english']
index = 0

for course in courses:
    print(f"{index}: {course}")
    index += 1

nums = []
num = 2
for i in range(20 / 2 - 1):
    nums.append(num)
    num += 2

for num in nums:
    print(f"{num} is divisible by 10" if num % 10 == 0 else f"{num} is not divisible by 10")