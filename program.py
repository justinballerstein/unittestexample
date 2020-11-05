import fileinput
import pythagorean

a = int(input('Enter a:'))
b = int(input('Enter b:'))

c = pythagorean.Pythagorean.theorem(a,b)

print("c is:" + str(c))