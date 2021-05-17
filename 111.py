import random

a = []
sum = 0
for i in range(50):
    a.append(round(random.uniform(189, 195), 2))
for j in range(50):
    sum += a[j]
    print(a[j])
print(sum / 50)
