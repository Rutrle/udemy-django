print(1 > 2)
print(1 == '1')


(1 < 2) and (4 > 5)

if 1 < 2:
    print("hello")
elif 4 > 5:
    print('k')

for i in range(5):
    print(i)

d = {"Sam": 1, "Frank": 2, "Dan": 3}

for key in d:
    print(key, d[key])

for key, value in d.items():
    print(key, value)

# tuple unpacking
mypairs = [(1, 2), (3, 4), (5, 6)]

for tup1, tup2 in mypairs:
    print(tup1)
    print(tup2)

i = 1
while i < 5:
    print(f"i is {i}")
    i = i+1

print(list(range(5)))
print(list(range(0, 21, 2)))

x = [1, 2, 3, 4]

out = [num**2 for num in x]

print(out)
