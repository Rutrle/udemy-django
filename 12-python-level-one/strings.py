
mystring = 'abcdefgh'

print(mystring[-1])

print(mystring[1:-1])

print(mystring[:-1])

print(mystring[::-1])  # in python it's UP TO not INCLUDING!


print(mystring.upper())
mystring2 = 'Hello World'

x = mystring2.split()

print(x)

x = mystring2.split('l')

print(x)

print(f"insert something: {mystring2}")
# or
print("insert {} something: {}".format('dog', mystring2))

print("insert {y} something: {x}".format(x='dog', y=mystring2))
print(x)
