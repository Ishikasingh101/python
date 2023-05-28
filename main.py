
#
#price_lookup= {'apple':2.99,'oranges':1.99,'milk':5.80}
#print(price_lookup['apple'])
#
#d= {'k1':123,'k2':[0,1,2],'k3':{'insideKey':100}}
#print(d['k2'][2])
d= {'key1': ['a','b','c']}
#print(d)
my_list= d['key1']
#print(my_list)
letter= my_list[2]
#print(letter)
letter.upper()
#print(letter.upper())
d['key1'][2].upper()
#print(d['key1'][2].upper())
d= {'k1':100,'k2':200}
d['k3']= 300
#print(d)
d.keys()
#print(d.keys())
d.values()
#print(d.values())
d.items()
#print(d.items())

t= (1,2,3)
my_list= [1,2,3]
type(t)
#print(type(t))
#print(len(t))
t= ('a','a','b')
t.count('a')
#print(t.count('a'))
my_list[0]= 'NEW'
#print(my_list)


#set(mylist)
#print(set(mylist))


type(False)
#print(type(False))
1>2
#print(1>2)
1==1
#print(1==1)


# loc = 'Bank'

# if  loc == 'auto shop':
#     print('Cars are cool!')
# elif loc == 'Bank':
#     print('Money is cool!')
#else:
    #print('I do not know much')

mylist = [1,2,3,4,5,6,7,8,9,10]
#for num in mylist:
    # check for even
    #if num % 2 == 0:
       #print(num)
    #else:
        #print(f'odd number: {num}')\
# list_sum = 0
# for num in mylist:
#     list_sum = list_sum + num
# print(list_sum)

# mystring = 'Hello World'
# for letter in mystring:
#     print(letter)

# tup = (1,2,3)
# for item in tup:
#     print(item)



mylist = [(1,2),(3,4),(5,6),(7,8)]
#for item in mylist:
 #   print(item)
# for (a,b) in mylist:
#     print(a)
#     print(b)

# PYTHN STATEMENTS TEST
# #1 Use for, .split(), and if to create a Statement that will print out words that start with 's':
# st = 'Print only the words that start with s in this sentence'
# for word in st.split():
#     if word[0] == 's':
#      print(word)

#2 Use range() to print all the even numbers from 0 to 10.
# mylist = [1,2,3,4,5,6,7,8,9,10]
# for num in range(0,11,2):
#     print(num)

#3 Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
# mylist = [x for x in range(1,51) if x%3 ==0]
# print(mylist)

#4 Go through the string below and if the length of a word is even print "even!"
# st = 'Print every word in this sentence that has an even number of letters'
# for word in st.split():
#     if len(word) %2 == 0:
#         print(word)

#5 Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

#6 Use List Comprehension to create a list of the first letters of every word in the string below:
# st = 'Create a list of the first letters of every word in this string'
# [word[0] for word in st.split()]
# print()

# SECTION 6: METHODS AND FUNCTIONS
#44 Basic Function in Python

# def say_hello():
#     print('Hello')
#     print('how')
#     print('are')
#     print('you')
# say_hello()

#def say_hello(name):
    # print(f'Hello {name}')
# say_hello('Ishika')

# def add_num(num1,num2):
#     return num1+num2
# result= add_num (10,20)
# print(result)

# def print_result(a,b):
#     print(a+b)
# print_result(10,20)


# def return_result(a,b):
#     return a+b
# result = print(return_result(10,20))

# def myfunc(a,b):
#     print(a+b)
#     return a+b
# result= myfunc(10,20)
# result
# def

#45 Logic with Python Functions
# num = 41 % 40
# print(num)

# num= 21%2 == 0
def get_number(num_type):
    input_question_str: str = f'Enter the {num_type} number: '
    num1 = input(input_question_str)
    return num1
# print(num)

num1: int = get_number('1st')
num2: int = get_number('2nd')
sum: float = float(num1)+float(num2)
print(f'The sum of {num1} and {num2} is {sum}')

def get_first_number():
    num1 = input('Enter the first number: ')
    return num1





