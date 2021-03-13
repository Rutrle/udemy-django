

try:
    f = open('simple.txt', 'r')
    f.write("writing to simple text")
except IOError:
    print("ERROR: COULD NOT FIND FILE OR READ DATA!")

finally:
    print("I always work")


print('some code after try except')
