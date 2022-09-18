##____Activity 1
n=input("enter a number")
if int(n)%2==0:
    print("the given number is an even number")
else:
        print("the given number is an even number")
        
from pip._vendor.distlib.compat import raw_input
##____Activity 2
sum=0
s=input("Enter an integer value...")
n=int(s)
while n!=0:
    sum=sum+n
    s=input("Enter an integer value...")
    n=int(s)
    print("Sum of given values is ",sum)
##___Activity 3
isPrime=True
i=2
n=int(input("enter a number"))
while i<n:
          remainder=n%i
          if remainder==0:
              isPrime=False
              break
          else:
                i=i+1
            if isPrime:
                    print("Number is Prime")
            else:
                        print("Number is not Prime")
##___Activity 4
summ = 4
i = 0
while i<=4:
    s=input("enter a number")
    n=int(s)
    summ=summ+n
    i=i+1
    print("sum is",summ)
##____Activity5
summation = 0
i=1
while i<=10:
    summation=summation+i
    i=i+1
    print("sum is", summation)
##____Activity 6
name = input('What is your name? ')
print('Hello ' + name)
job = input('What is your job? ')
print('Your job is ' + job)
num = input('Give me a number? ') 
print('You said: ' + str(num))
##____ACtivity 7
import random
MINIMUM = 1
MAXIMUM = 9
NUMBER = random.randint(MINIMUM, MAXIMUM)
GUESS = None
ANOTHER = None
TRY = 0
RUNNING = True
print ("Alright...")
while RUNNING:
 GUESS = raw_input("What is your lucky number? ")
 if int(GUESS) < NUMBER:
     print ("Wrong, too low.")
 elif int(GUESS) > NUMBER:
     print ("Wrong, too high.")
 elif GUESS.lower() == ("exit"):
         print ("Better luck next time.")
 elif int(GUESS) == NUMBER:
             print ("Yes, that's the one, %s.")% str(NUMBER)
             if TRY < 2:
                 print ("Impressive, only %s tries.") % str(TRY)
 elif TRY > 2 and TRY < 10:
             print ("Pretty good, %s tries.") % str(TRY)
 else:
                print ("Bad, %s tries.") % str(TRY)
                RUNNING = False
                TRY += 1
'''

##____Task 1

i= int(input('Enter  Number '))
a=0
print('Entered Number',i)
result = ''
while i!=0:
    a = i%10
    result =result + str(a) 
    i=int(i/10)

print('The Reversed Number',result)


##____Task 2

n=int(input("enter numbers to add : "))
even=0
odd=0

for num in range(1,n+1):
    n=int(input("enter the values : "))
    if(num%2==0):
        even=even+num
    else:
       odd=odd+num

print("total of even numbers=",even)
print("total of odd numbers=",odd)


##_____Task 3

n=int(input("enter the terms : "))
fe=0
se=1
if n<0:
    print("enter positive values")
else:
    print(fe,se,end="")
for x in range(2,n):
    next=fe+se
    print(next,end="")
    fe=se
    se=next

##_____Task 4
    
n = int(input('Enter a marks of student:'))

if n>100 or n<0:
    print('invalid input')
else:
    if n<50:
        print('You Got F Grade, Better luck next time:',n)
    elif n>50 and n<60:
        print(' Your Grade is E, Improvement suggested',n)
    elif n>61 and n<70:
        print('D is your Grade',n)
    elif n>71 and n<80:
        print('C is your Grade',n)
    elif n>81 and n<90:
        print('Your Grade is B,Good',n)
    elif n>91 and n<100:
        print('Your Scored a Great Deal, Excelent',n)


##_____Task 5

n=int(input("Enter a number "))
fac=1
i=1
while i<=n:
    fac=fac*i
    i=i+1
print("Factorial of",n,"is" ,fac)