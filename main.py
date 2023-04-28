def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  return x / y

def square(x):
  return x * x

#num1 = input(float("Enter Number 1:"))
#num2 = input(float("Enter Number 2:"))

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.square")

choice = input("Enter choice:")

if choice == '5':
  num = float(input("Enter a number: "))
  print("Square of", num, "is", square(num))
else:
  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))#
if choice == '1':
  print(num1, "+", num2, "=", add(num1, num2))#
elif choice == '2':
  print(num1, "-", num2, "=", subtract(num1, num2))#
elif choice == '3':
  print(num1, "*", num2, "=", multiply(num1, num2))#
elif choice == '4':
  print(num1, "/", num2, "=", divide(num1, num2))#
elif choice == '5':
  print(num, "=", square(num))
else:
  print("Invalid input")

#match choice: 
#  case "1": 
#    print(num1, "+", num2, "=", add(num1, num2))
#  
#  case "2":
#    print(num1, "-", num2, "=", subtract(num1, num2))
#  
#  case "3":
#    print(num1, "*", num2, "=", multiply(num1, num2))
#
#  case "4":
#      print(num1, "/", num2, "=", divide(num1, num2))
# 
#  case "5":
#    print(num, "=", square(num))
#  
#  case _:
#    print("Invalid Input")
