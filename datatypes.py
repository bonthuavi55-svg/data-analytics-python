#data tpes - integers,float,boolen,string
# intro to variables
## declaring and accessing variables 
#naming conversations
##type checking and dynamic conversations
##practical examples of common errors 
age=32
height=5.9
name="avinash"
is_employeee=True
## printing variables 
print("age:",age)
print(type(age))
print("height:",height)
print(type(height))
print("name:",name)
print(type(name))
##type checking convesatin 
age_str=str(age)
print(age_str)
 ###except strings not coverted into int or float but u can convert int float into strings 
int(height)
float(int(height))
 ##dynamic typing. python allows the type of a variable to change as the program executes
var=10
print(var,type(var))
var="hello"
print(var,type(var))
var =3.14
print(var,type(var))
###simple caluculator
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
sum = num1+num2
difference = num1-num2
product= num1 * num2
quotient= num1/num2
print("sum:",sum)
print("difference:",difference)
print("product:",product)
print("quotient:",float(quotient))