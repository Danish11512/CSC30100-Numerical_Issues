from math import sin, cos, cosh, sinh, exp, factorial
from fractions import Fraction


x1 = 1/4
x2 = 1/2
x3 = 1
x4 = 2

n1 = 4
n2 = 16
n3 = 64

# -------------------------------------------------

# Exact Values - Sin

print("Exact Value for sin(1/4):")
exactsinx1 = sin(x1)
print(exactsinx1, "\n")

print("Exact Value for sin(1/2):")
exactsinx2 = sin(x2)
print(exactsinx2, "\n")

print("Exact Value for sin(1):")
exactsinx3 = sin(x3)
print(exactsinx3, "\n")

print("Exact Value for sin(2):")
exactsinx4 = sin(x4)
print(exactsinx4, "\n")

# Exact Values - Exp

print("Exact Values for exp(1/4):")
exactexp1 = exp(x1)
print(exactexp1, "\n")

print("Exact Values for exp(1/2):")
exactexp2 = exp(x2)
print(exactexp2, "\n")

print("Exact Values for exp(1):")
exactexp3 = exp(x3)
print(exactexp3, "\n")

print("Exact Values for exp(2):")
exactexp4 = exp(x4)
print(exactexp4, "\n")

# Exact Values - Cosh

print("Exact Calues for cosh(1/4):")
exactcoshx1 = cosh(x1)
print(exactcoshx1, "\n")

print("Exact Calues for cosh(1/2):")
exactcoshx2 = cosh(x2)
print(exactcoshx2, "\n")

print("Exact Calues for cosh(1):")
exactcoshx3 = cosh(x3)
print(exactcoshx3, "\n")

print("Exact Calues for cosh(2):")
exactcoshx4 = cosh(x4)
print(exactcoshx4, "\n")

# -------------------------------------------------

# The Kth Derivatives

# Sin


def dersin(k):
    if k % 4 == 0:  # Since it repeats every 4th time it's easier to find out that way
        return sin(0)  # sin (0) == 0, but im not using this, instead I want to show the function
    if k % 4 == 1:
        return cos(0)
    if k % 4 == 2:
        return (-1) * sin(0)  # It's -sin but -sin(0) is just 0, no need for the -
    if k % 4 == 3:
        return (-1) * cos(0)


# Exp


def derexp(k):
    return exp(0)


# Cosh


def dercosh(k):
    if k % 2 == 0:  # cosh's derivatives repeat every two times, so it's more like finding if it's even or odd
        return 1 * cosh(0)
    if k % 2 == 1:
        return 1 * sinh(0)


# -------------------------------------------------

# Taylor functions

# Taylor - Sin


def taylorsin(x, n):
    result = 0
    for k in range(n + 1):
        result = result + (dersin(k) / factorial(k)) * pow(x, k)
    return result


# Taylor - Exp


def taylorexp(x, n):
    result = 0
    for k in range(n + 1):
        result = result + (derexp(k) / factorial(k)) * pow(x, k)
    return result


# Taylor - Cosh


def taylorcosh(x, n):
    result = 0
    for k in range(n + 1):
        result = result + ((dercosh(k) / factorial(k)) * pow(x, k))
    return result


# -------------------------------------------------

table = [['Function','X used', 'N used','Value','Relative error','Absolute error','Exact Value'], 
['Sin(x)', '1/4', 'Exact', exactsinx1, (exactsinx1-exactsinx1)/exactsinx1, abs((exactsinx1-exactsinx1)/exactsinx1), exactsinx1],
['Sin(x)', '1/4', '4', taylorsin(x1, n1), (taylorsin(x1, n1)-exactsinx1)/exactsinx1, abs((taylorsin(x1, n1)-exactsinx1)/exactsinx1), exactsinx1],
['Sin(x)', '1/4', '16', taylorsin(x1, n2), (taylorsin(x1, n2)-exactsinx1)/exactsinx1, abs((taylorsin(x1, n2)-exactsinx1)/exactsinx1), exactsinx1],
['Sin(x)', '1/4', '64', taylorsin(x1, n3), (taylorsin(x1, n3)-exactsinx1)/exactsinx1, abs((taylorsin(x1, n3)-exactsinx1)/exactsinx1), exactsinx1],
['-','-','-','-','-','-','-'],
['Sin(x)', '1/2', 'Exact', exactsinx2, (exactsinx2-exactsinx2)/exactsinx2, abs((exactsinx2-exactsinx2)/exactsinx2), exactsinx2],
['Sin(x)', '1/2', '4', taylorsin(x2,n1), (taylorsin(x2,n1)-exactsinx2)/exactsinx2, abs((taylorsin(x2,n1)-exactsinx2)/exactsinx2), exactsinx2],
['Sin(x)', '1/2', '16', taylorsin(x2,n2), (taylorsin(x2,n2)-exactsinx2)/exactsinx2, abs((taylorsin(x2,n2)-exactsinx2)/exactsinx2), exactsinx2],
['Sin(x)', '1/2', '64', taylorsin(x2,n3), (taylorsin(x2,n3)-exactsinx2)/exactsinx2, abs((taylorsin(x2,n3)-exactsinx2)/exactsinx2), exactsinx2],
         ['-','-','-','-','-','-','-'],
['Sin(x)', '1', 'Exact', exactsinx3, (exactsinx3-exactsinx3)/exactsinx3, abs((exactsinx3-exactsinx3)/exactsinx3), exactsinx3],
['Sin(x)', '1', '4', taylorsin(x3,n1), (taylorsin(x3,n1)-exactsinx3)/exactsinx3, abs((taylorsin(x3,n1)-exactsinx3)/exactsinx3), exactsinx3],
['Sin(x)', '1', '16', taylorsin(x3,n2), (taylorsin(x3,n2)-exactsinx3)/exactsinx3, abs((taylorsin(x3,n2)-exactsinx3)/exactsinx3), exactsinx3],
['Sin(x)', '1', '64', taylorsin(x3,n3), (taylorsin(x3,n3)-exactsinx3)/exactsinx3, abs((taylorsin(x3,n3)-exactsinx3)/exactsinx3), exactsinx3],
         ['-','-','-','-','-','-','-'],
['Sin(x)', '2', 'Exact', exactsinx4, (exactsinx4-exactsinx4)/exactsinx4, abs((exactsinx4-exactsinx4)/exactsinx4), exactsinx4],
['Sin(x)', '2', '4', taylorsin(x4,n1), (taylorsin(x4,n1)-exactsinx4)/exactsinx4, abs((taylorsin(x4,n1)-exactsinx4)/exactsinx4), exactsinx4],
['Sin(x)', '2', '16', taylorsin(x4,n2), (taylorsin(x4,n2)-exactsinx4)/exactsinx4, abs((taylorsin(x4,n2)-exactsinx4)/exactsinx4), exactsinx4],
['Sin(x)', '2', '64', taylorsin(x4,n3), (taylorsin(x4,n3)-exactsinx4)/exactsinx4, abs((taylorsin(x4,n3)-exactsinx4)/exactsinx4), exactsinx4],
         ['-','-','-','-','-','-','-'],
['Exp(x)', '1/4', 'Exact', exactexp1, (exactexp1-exactexp1)/exactexp1, abs((exactexp1-exactexp1)/exactexp1), exactexp1],
['Exp(x)', '1/4', '4', taylorexp(x1,n1), (taylorexp(x1,n1)-exactexp1)/exactexp1, abs((taylorexp(x1,n1)-exactexp1)/exactexp1), exactexp1],
['Exp(x)', '1/4', '16', taylorexp(x1,n2), (taylorexp(x1,n2)-exactexp1)/exactexp1, abs((taylorexp(x1,n2)-exactexp1)/exactexp1), exactexp1],
['Exp(x)', '1/4', '64', taylorexp(x1,n3), (taylorexp(x1,n3)-exactexp1)/exactexp1, abs((taylorexp(x1,n3)-exactexp1)/exactexp1), exactexp1],
         ['-','-','-','-','-','-','-'],
['Exp(x)', '1/2', 'Exact', exactexp2, (exactexp2-exactexp2)/exactexp2, abs((exactexp2-exactexp2)/exactexp2), exactexp2],
['Exp(x)', '1/2', '4', taylorexp(x2,n1), (taylorexp(x2,n1)-exactexp2)/exactexp2, abs((taylorexp(x2,n1)-exactexp2)/exactexp2), exactexp2],
['Exp(x)', '1/2', '16', taylorexp(x2,n2), (taylorexp(x2,n2)-exactexp2)/exactexp2, abs((taylorexp(x2,n2)-exactexp2)/exactexp2), exactexp2],
['Exp(x)', '1/2', '64', taylorexp(x2,n3), (taylorexp(x2,n3)-exactexp2)/exactexp2, abs((taylorexp(x2,n3)-exactexp2)/exactexp2), exactexp2],
         ['-','-','-','-','-','-','-'],
['Exp(x)', '1', 'Exact', exactexp3, (exactexp3-exactexp3)/exactexp3, abs((exactexp3-exactexp3)/exactexp3), exactexp3],
['Exp(x)', '1', '4', taylorexp(x3,n1), (taylorexp(x3,n1)-exactexp3)/exactexp3, abs((taylorexp(x3,n1)-exactexp3)/exactexp3), exactexp3],
['Exp(x)', '1', '16', taylorexp(x3,n2), (taylorexp(x3,n2)-exactexp3)/exactexp3, abs((taylorexp(x3,n2)-exactexp3)/exactexp3), exactexp3],
['Exp(x)', '1', '64', taylorexp(x3,n3), (taylorexp(x3,n3)-exactexp3)/exactexp3, abs((taylorexp(x3,n3)-exactexp3)/exactexp3), exactexp3],
         ['-','-','-','-','-','-','-'],
['Exp(x)', '2', 'Exact', exactexp4, (exactexp4-exactexp4)/exactexp4, abs((exactexp4-exactexp4)/exactexp4), exactexp4],
['Exp(x)', '2', '4', taylorexp(x4,n1), (taylorexp(x4,n1)-exactexp4)/exactexp4, abs((taylorexp(x4,n1)-exactexp4)/exactexp4), exactexp4],
['Exp(x)', '2', '16', taylorexp(x4,n2), (taylorexp(x4,n2)-exactexp4)/exactexp4, abs((taylorexp(x4,n2)-exactexp4)/exactexp4), exactexp4],
['Exp(x)', '2', '64', taylorexp(x4,n3), (taylorexp(x4,n3)-exactexp4)/exactexp4, abs((taylorexp(x4,n3)-exactexp4)/exactexp4), exactexp4],
         ['-','-','-','-','-','-','-'],
['Cosh(x)', '1/4', 'Exact', exactcoshx1, (exactcoshx1-exactcoshx1)/exactcoshx1, abs((exactcoshx1-exactcoshx1)/exactcoshx1), exactcoshx1],
['Cosh(x)', '1/4', '4', taylorcosh(x1,n1), (taylorcosh(x1,n1)-exactcoshx1)/exactcoshx1, abs((taylorcosh(x1,n1)-exactcoshx1)/exactcoshx1), exactcoshx1],
['Cosh(x)', '1/4', '16', taylorcosh(x1,n2), (taylorcosh(x1,n2)-exactcoshx1)/exactcoshx1, abs((taylorcosh(x1,n2)-exactcoshx1)/exactcoshx1), exactcoshx1],
['Cosh(x)', '1/4', '64', taylorcosh(x1,n3), (taylorcosh(x1,n3)-exactcoshx1)/exactcoshx1, abs((taylorcosh(x1,n3)-exactcoshx1)/exactcoshx1), exactcoshx1],
         ['-','-','-','-','-','-','-'],
['Cosh(x)', '1/2', 'Exact', exactcoshx2, (exactcoshx2-exactcoshx2)/exactcoshx2, abs((exactcoshx2-exactcoshx2)/exactcoshx2), exactcoshx2],
['Cosh(x)', '1/2', '4', taylorcosh(x2,n1), (taylorcosh(x2,n1)-exactcoshx2)/exactcoshx2, abs((taylorcosh(x2,n1)-exactcoshx2)/exactcoshx2), exactcoshx2],
['Cosh(x)', '1/2', '16', taylorcosh(x2,n2), (taylorcosh(x2,n2)-exactcoshx2)/exactcoshx2, abs((taylorcosh(x2,n2)-exactcoshx2)/exactcoshx2), exactcoshx2],
['Cosh(x)', '1/2', '64', taylorcosh(x2,n3), (taylorcosh(x2,n3)-exactcoshx2)/exactcoshx2, abs((taylorcosh(x2,n3)-exactcoshx2)/exactcoshx2), exactcoshx2],
         ['-','-','-','-','-','-','-'],
['Cosh(x)', '1', 'Exact', exactcoshx3, (exactcoshx3-exactcoshx3)/exactcoshx3, abs((exactcoshx3-exactcoshx3)/exactcoshx3), exactcoshx3],
['Cosh(x)', '1', '4', taylorcosh(x3,n1), (taylorcosh(x3,n1)-exactcoshx3)/exactcoshx3, abs((taylorcosh(x3,n1)-exactcoshx3)/exactcoshx3), exactcoshx3],
['Cosh(x)', '1', '16', taylorcosh(x3,n2), (taylorcosh(x3,n2)-exactcoshx3)/exactcoshx3, abs((taylorcosh(x3,n2)-exactcoshx3)/exactcoshx3), exactcoshx3],
['Cosh(x)', '1', '64', taylorcosh(x3,n3), (taylorcosh(x3,n3)-exactcoshx3)/exactcoshx3, abs((taylorcosh(x3,n3)-exactcoshx3)/exactcoshx3), exactcoshx3],
         ['-','-','-','-','-','-','-'],
['Cosh(x)', '2', 'Exact', exactcoshx4, (exactcoshx4-exactcoshx4)/exactcoshx4, abs((exactcoshx4-exactcoshx4)/exactcoshx4), exactcoshx4],
['Cosh(x)', '2', '4', taylorcosh(x4,n1), (taylorcosh(x4,n1)-exactcoshx4)/exactcoshx4, abs((taylorcosh(x4,n1)-exactcoshx4)/exactcoshx4), exactcoshx4],
['Cosh(x)', '2', '16', taylorcosh(x4,n2), (taylorcosh(x4,n2)-exactcoshx4)/exactcoshx4, abs((taylorcosh(x4,n2)-exactcoshx4)/exactcoshx4), exactcoshx4],
['Cosh(x)', '2', '64', taylorcosh(x4,n3), (taylorcosh(x4,n3)-exactcoshx4)/exactcoshx4, abs((taylorcosh(x4,n3)-exactcoshx4)/exactcoshx4), exactcoshx4]]
