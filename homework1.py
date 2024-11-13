print("BASIC CALCULATOR")
print("1.adition")
print("2.multiplication")
print("3.division")
print("4.floor division")
print("5.subtraction")



n1 = int(input("first number :"))
n2 = int(input("second number :"))
operator = int(input("choose a operator (1-5)"))
if operator == 1:
    total = (n1) + (n2)
if operator == 2:
    total = (n1) * (n2)
if operator == 3:
    total = (n1) / (n2)
if operator == 4:
    total = (n1) // (n2)
if operator == 5:
    total = (n1) - (n2)
print(total)