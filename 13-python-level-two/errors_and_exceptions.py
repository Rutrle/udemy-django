

try:
    f = open('simple.txt', 'r')
    f.write("writing to simple text")
except IOError:
    print("ERROR: COULD NOT FIND FILE OR READ DATA!")

else:
    print("Success!")
    f.close()


print('some code after try except')
