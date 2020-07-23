from typing import TextIO

print(8%7)  # % is 余数
#for works for list or range function

#writing file: append or overwriting or create a new file
#create again with every execute     define a file first
file = open("file.txt", "a")
file.write("\n it is right\nyes")
file.close()
file = open("file.txt", "w")
file.write("\n it is right\nyeah")
file.close()
file = open("file.html", "w")
file.write("<p>This is html</p>")
file.close()

'''open and then we can write'''
'''and then we should close'''
# reading files
# execute only 1 time?
# the function of for also works
# file = open("file.txt", "w")  "w" = write
# file = open("file.txt", "a")   "a" = append
# file = open("file.txt", "r"+) "r" = read   "r+"= everything
#remember to close file after using it
# file.close/open/write


file = open("file.txt", "r")   ##file.readlines() becomes a array'''
for word in file.readlines():
    print(word)
file.close()
file = open("file.txt", "r")
try:
    print(file.readline())
    print(file.readline()) #print oen line a time starts from the first line by readline'''
    print(file.readable())
    print(file.read)  #print everything'''
    print(file.readlines)  #print every line'''
    print(file.readlines()[1])##boolean
except:
    print("invalid input")
file.close()





languages = ["English", "French", "Spanish", "Chinese", "Japanese", "Hakka", "Korean"]
for item in languages:
    print(item)
for languege in languages:
    print(languege)
for number in range(10):  # 0, ..., 9
    print(number)
for index in range(1, 8): #1...7
    print(index)
for item in range(len(languages)): # 0, ..., 6
    print(item)
    print(languages[item])  #loop from first to end again and again
for index in languages:
    if index == "Hakka" or index == "Chinese":
        print("mother language")
    else:
        print("not mother language")

def pow(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    print(result)
pow(2, 3)

print(range(3))  #range(3)=range(0, 3)=[0, 1, 2]

def pow(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
print(pow(3, 4))
# for loop, loop as many times as how many items are there

number_grid = [
    [2, 3],
    [3, 4,7,8],
    [4, 5, 6],
    [0]
]

# 2 dimension array in python:  ...=[[, , ], [,], [], []]
print(number_grid[2])
print(number_grid[2][2])
print(number_grid[1][2])
for row in number_grid:
    print(row)
    for number in row:
        print(number)

for row in number_grid:
    for number in row:
        print(number)
# nested for loop--- for ...in...: ...  for...in...: ...
# only the print operation is seen in for loop, and is essential

def translate(word):
    translation = ""
    for letter in word :
        if letter.isupper() and letter in "AEIOU":
            translation = translation + "G"
        elif letter.islower() and letter in "aeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    print(translation)
translate(input("Enter a word you want to translate: "))

# if is very good to combine with boolean

def translate(word):
    translation = ""
    for letter in word :
        if letter.isupper() and letter in "AEIOU":
            translation = translation + "G"
        elif letter.islower() and letter in "aeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    print(translation)
translate(input("Enter a word you want to translate: "))

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "z"
        else:
            translation = translation + letter
    print(translation)
translate(input("Enter a word: "))

# translate(input(""))

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "z"
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter a phrase: ")))

#for loop in python, for...in... if...in... :   else: ,,,
#define a variable used later, just set the initial value by ...=""

def sayhi(name):
    print("hello " + name)
sayhi("Jack")
sayhi("Rose")

is_thin = True   # True in Python must be "T"
print(is_thin)  #variable should not be added quotation marks

# object are necessary in main files

from chef import chef
from ChineseChef import ChineseChef
my_chef = chef()
my_chef.make_chicken()
my_chinese_chef = ChineseChef()
my_chinese_chef.make_chicken()
# object_name = class() to make a new object and call the method by object_name.method_name

from company import company
company1 = company("IT", "Tokyo", "developer", 230000, True)
company2 = company("IT", "Toronto", "developer", 300000, True)
print(company2.is_good_salary())
print(company1.is_good_salary())
## constructor and calling method


# attributes of objects should be strings
#definitions of functions should be the same in the beginning and in the end, about the content in the ()
#" " of input can be left out
#float or integals should be chnaged to strings when added to strings

from question import question
question_prompt = [
    "Where is the capital of Japan?\n(a) Tokyo\n(b) Osaka\n(c) Sendai\n\n",
    "Which kind of animal is the symbol of America?\n(a) Rabbit\n(b) Bear\n(c) Eagle\n\n",
    "Which country is in Europe?\n(a) Canada\n(b) France\n(c) China\n\n"
]
questions = [
    question(question_prompt[0], "a"),
    question(question_prompt[1], "c"),
    question(question_prompt[2], "b")
]
def quiz_score():
    score = 0
    for question in questions:
        answer = input(question.prompt + " ")
        if answer == question.answer:
            score = score + 1
        else:
            score = score + 0
    print("You got " + str(score/ len(questions)) + " correct")
quiz_score()



from question import question
question_prompt = [
    "Where is the capital of Japan?\n(a) Tokyo\n(b) Osaka\n(c) Sendai\n\n",
    "Which kind of animal is the symbol of America?\n(a) Rabbit\n(b) Bear\n(c) Eagle\n\n",
    "Which country is in Europe?\n(a) Canada\n(b) France\n(c) China\n\n"
]
questions = [
    question(question_prompt[0], "a"),
    question(question_prompt[1], "c"),
    question(question_prompt[2], "b")
]
# array  and define new objects in array by using constructors and index of array
#array is also a kind of variable, and name of array can be used in a method as parameters
def quiz_score(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score = score + 1
        else:
            score = score + 0
    print("You got " + str(score) + "/" +str(len(questions)) + " correct")
quiz_score(questions)

# for loop means play as many times of the number of items and each time play the item in order which is its turn
# the central parameter should include everything we use, especially in a quiz


#when not importing class from other files
class company:
    def __init__(self, type, place, position, salary, is_good):
        self.type = type
        self.place = place
        self.position = position
        self.salary = salary
        self.is_good = is_good
company1 = company("IT", "Tokyo", "developer", "230,000yen/month", True)
company2 = company("IT", "Toronto", "developer", "300,000yen/month", True)
print(company2.is_good)
print(company1.salary)

#class in another file and objects in main file
#from file import class
#use string when write attributes of objects
#attributes are like functions-> use dot
from company import company
class company:
    def __init__(self, type, place, position, salary, is_good):
        self.type = type
        self.place = place
        self.position = position
        self.salary = salary
        self.is_good = is_good
company1 = company("IT", "Tokyo", "developer", "230,000yen/month", True)
company2 = company("IT", "Toronto", "developer", "300,000yen/month", True)
print(company2.is_good)
print(company1.salary)

#import external files    use "pip install files" in cmd; import files; use functions in files
import company   #use the method in other class by import class_name and call the method
company.pow(2,4)






# try:    except:   for smooth process   similiar tp try catch method in java
# except not only input error but also code error(such as ValueError, ZeroDivisionError)
# print string or traditional error by using "as" to create new variables

try:
    10 / 0
    number = float(input("Enter a number: "))
    print(number * 2 )
except ZeroDivisionError:
    print(ZeroDivisionError)
except ValueError:
    print("invalid input")

try:
    10 / 0
    number = float(input("Enter a number: "))
    print(number * 2 )
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("invalid input")

try :
    10 / 0
    number = float(input("Enter a number: "))
    print(number * 2 )
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid input")

try :
    10 / 0
    number = float(input("Enter a number: "))
    print(number * 2 )
except ZeroDivisionError as error:
    print(error)
except ValueError:
    print("invalid input")

try :
    10 / 0
    number = float(input("Enter a number: "))
    print(number * 2 )
except:
    print("invalid input")

try :
    number = float(input("Enter a number: "))
    print(number * 2 )
except:
    print("invalid input")


''''
try:
except ValueError:
except ZeroDivisionError:
 except:
 '''


# comment: for note or check
# 2 ways of comment: # for each line or use ''' ''' for multiple lines
'''
really ?
can this work?
'''




secret_word = "apple"
guess = " "
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter your guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guess, you lose!")
else:
    print("You win!")




secret_word = "apple"
guess = " "
guess_count = 0
guess_limit = 4
out_of_guess = False

while guess != secret_word and guess_count < guess_limit:
    guess = input("Enter your guess ")
    guess_count += 1

if guess == secret_word:
    print("You win!")
else:
    print("Out of guess, you lose!")






a = 2
while a <= 20:
    print(a + 1)
    a += 2
print("Done with loop")

i = 10
while i < 100 :
    print(i * 8)
    i *= 2
print("Done with loop")
# *= += -= /=    means operation continuously

month_conversions = {     ## is it an object or a switch function???
    "1" : "Jan",
    "2" : "Feb",
    "3" : "Mar",
    "4" : "Apr"
}
print(month_conversions["1"])
print(month_conversions.get("3"))
print(month_conversions.get("5", "Not a valid key"))
# default
print("字典里都是字符")
print("get可以设置默认回答；符号要英文半角")
#similiar to switch method in java, but more convenient
# use get mothod by ".", or use case_value and []

num1 = float(input("Enter the first number: "))
op = input("Enter an operator: ")
num2 = float(input("Enter the second number: "))
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("invalid operator")

def max_num(num1, num2, num3, num4):
    if num1 >= num2 and num1 >= num3 and num1 >= num4:
        return num1
    elif num2 >= num1 and num2 >= num3 and num2 >= num4:
        return num2
    elif num3 >= num1 and num3 >= num2 and num3 >= num4:
        return num3
    else:
        return num4
print(max_num(400,2,1,350))

def max_num(num1, num2, num3, num4):
    if num1 >= num2 and num1 >= num3 and num1 >= num4:
        print(num1)
    elif num2 >= num1 and num2 >= num3 and num2 >= num4:
        print(num2)
    elif num3 >= num1 and num3 >= num2 and num3 >= num4:
        print(num3)
    else:
        print(num4)
max_num(2,5,6,7)

print("== >= <= !=  >  <")

print(max(2, 4, 90, 890))

is_a_human = True
is_brave = True
if is_a_human and is_brave:
    print("Congratulations! Keep going despite fear")
elif is_a_human and not is_brave:
    print("It's alright! Keep going despite fear")
elif is_brave and not is_a_human:
    print("You are a great life no less than a brave human")
else:
    print("Keep going despite fear and you will be a great life")
#combine boolean and if loop
as_human = True
is_brave = False
if as_human and is_brave:
    print("Congratulations! Keep going despite fear")
elif as_human and not is_brave:
    print("It's alright! Keep going despite fear")
elif is_brave and not as_human:
    print("You are a great life no less than a brave human")
else:
    print("Keep going despite fear and you will be a great life")

def cube(num):
    print(num*num*num)
cube(3)
# use parenthesis to include parameter or nothing
def cube(num):
    return num*num*num
print(cube(2))

result = cube(4)
print(cube(4))


def sayhi():
    print("hello user")
print("today is Wednesday")
sayhi()
print("byebye")

def sayhi(name):
    print("hello " + name)
sayhi("Jack")
sayhi("Rose")

def sayhi(name, age):
    print("hello " + name + ", you are " + age + " years old")
say_hi("Huiqin", "24")
def say_hi(name, age):
    print("hello " + name + ", you are " + str(age) + " years old.")
say_hi("Huiqin", 24)
say_hi("Koto", 24)

# call method after defining it

coordinate1 = (1, 9)
coordinate2 = ([1, 9], [1, 2])
print(coordinate1[1])



friends = ["Kelly", "Jack", "Oscar", "Rose", "Amy", "Belly"]
lucky_numbers = [2, 3, 4, 6, 8, 12, 22 , 28, 37, 36]
print(friends)
print(lucky_numbers)
friends.sort()
print(friends)
friends.extend(lucky_numbers)
print(friends)
friends.append("Edward")
print(friends)
friends.insert(3, "Rose")
print(friends)
print(friends.index("Jack"))
print(friends.count("Rose"))
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)
friends.remove("Jack")
print(friends)
friends.pop()
print(friends)
friends2 = friends.copy()
print(friends2)
friends[1] = "Lily"
print(friends[1])
print(friends)
friends.clear()
print(friends)

# sort, append, extend, insert, reverse, remove, pop, copy, index, count,  in array


color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")
print("Roses are " + color + ".")
print(plural_noun + " are blue" + ".")
print("I love " + celebrity + ".")

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) * float(num2)
print(result)

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) + int(num2)
print(result)

my_num = 6
print(my_num)
print(str(my_num) + " is said to be a lucky number")
my_num = -6
print(abs(my_num))
print(abs(-7))
print(pow(2, 4))
print(max(3, 4))
print(min(3, 4))
print(round(3.2))

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) + int(num2)
print(result)

print(3)
print(3.567889)
print(-9)
print(-9.72393)
print(0 + 2)
print(9 + 3.45)
print(3 - 1)
print(5 - 2.3)
print(7 * 8)
print(9 / 3)
print(2 * 3 + 7)
print(2*3 + 7)
print(2 * (3+7))
print(57 % 7)


print(80)
print("and\" you")
print("and\ndo your best")
is_good = True
print(is_good)
phrase = "Seeking for jobs"
print(phrase + "is necessary")

print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.islower())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase[0:7])
print(phrase[-2])
print(phrase[3:15])
print(phrase.index("S"))
print(phrase.index(""))
print(phrase.index("e"))
print(phrase.index("ee"))
print(phrase.replace("jobs", "accumulation"))
print(phrase.replace("Seeking", "Looking"))
print(phrase.replace("S", "s"))
##call method by .

print("    /|")
print("   / |")
print("  /  |")
print(" /   |")
print("/____|")
course = 'Python for beginners'
print(len(course))
print(course.lower())

name = "Amy"
age = "80"
print('''There once was a woman named Amy.
She was 80 years old''')
print("There once was a woman named " + name +
". She was " + age + " years old.")

first = "John"
last = "Smith"
message = first + ' [' + last + ']   is a coder'
print(message)
msg = f'{first} [{last}] is a coder'
print(msg)

print('Zhu Huiqin')
print('o----')
print(" ||||")
print("*" * 10)
print("}" * 7)
print("$" * 10)

course = "'Java's Course for Beginners"
print(course)
print(course[0])
print(course[-2])
print(course[10])
print(course[0:9])
print(course[0:])
print(course[3:])
print(course[0:])
print(course[3:])
print(course[:])
##use [:]for charat in python
name = 'Jenifer'
print(name[1:-1])


gender = 'gender is total "nonsense"'
print(gender)

print('''
Hi Koto

Congratuations on your first journey to work and society and more real and meaningful learning!

You can do that.

I love you.

best you

''')

#print('''    ''') for automatic mutiple lines
height = 166
height = 152
rating = 5.0
hobby = "learning"
is_confirmed = True
name = "John Smith"
age = 20
new_patient = True
print(height)
print(new_patient)
name = input("what is your name? ")
color = input("what is your favorite color? ")
print(name + " like " + color)

birth_year = input("Birth year: ")
print(type(birth_year))
age = 2019 - int(birth_year)
print(type(age))
print(age)

# variables and numbers don't need quotation marks



weight = (int(input("how many pounds do you weigh? "))) * 0.454
print(weight)

weight_lbs = input("Weight(lbs): ")
weight_kg = int(weight_lbs) * 0.454
print(weight_kg)





