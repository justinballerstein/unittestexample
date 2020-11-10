import fileinput
import pythagorean

a = int(input('Enter a:'))
b = int(input('Enter b:'))
py = pythagorean.Pythagorean()
c = py.theorem(a,b)

print("c is:" + str(c))