##list comprehension
fruits=["banana","apple","watermelon","kiwi"]
fruits.append("orange")## will add item to end
fruits.insert(1,"cherry")
fruits.remove("watermelon")## removes the first occurance of item 
## remove and return the last -pop
fruits.pop()
print(fruits)
fruits.index("cherry")
fruits.insert(2,"lattice")
print(fruits.count("apple"))
fruits.sort()## sort the list in ascending order 
print(fruits)
fruits.reverse()## sorts in reverse order 
fruits.clear()
print(fruits)
####slicing list
numbers=[2,8,9,11,90,140]
print(numbers[2:5])
print(numbers[3:4])
print(numbers[5:])
print(numbers[:5])
print(numbers[::2])
print(numbers[::-1])
print(numbers[::3])
print(numbers[::])
### iterating over list
for number in numbers:
    print(numbers)
## iterating with the index
for index,number in enumerate(numbers):
    print(index,number)
## list comprehension
lst=[]
for x in range(10):
    lst.append(x**2)
print(lst)
## using technique 
print([x**2 for x in range(10)])
## basic syntax- expression for item iterable
## conditional logic -expression for item in iterable if conditional
squre=[num**2 for num in range(10)]
print(squre)
lst_1=[]
for i in range(10):
    if i%2==0:
        lst_1.append(i)
print(lst_1)
### nested list comprehension -- expresion for item11  iterable in item1 for item2 to in item2
lst_2=[1,2,3,4]
lst_3=['a','b','c','d']
pair=[[i,j] for i in lst_2 for j in lst_3]
print(pair)
# list comprehension with function calls 
words=["hello","world","python","list","comprehension"]
lengths=[len(word) for word in words]
print(lengths)