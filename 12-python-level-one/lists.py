mylist = [1, 'dog', 2]
print(mylist)
mylist[1] = 'new thing'
print(mylist)
mylist.append('appended')
print(mylist)
secondlist = [6, 4, 7]
mylist.extend(secondlist)
print(mylist)
i = mylist.pop()
print(mylist)
i = mylist.pop(2)
print(mylist)


secondlist.sort()
print(secondlist)

mylist = [1, 2, [3, 4]]
print(mylist[2][0])

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

first_col = [row[0] for row in matrix]
print(first_col)
