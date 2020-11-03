import fileinput
import pythagorean

a = input('Enter a:')
b = input('Enter b:')

c = pythagorean.Pythagorean.theorem(a,b)

print("c is:" + str(c))