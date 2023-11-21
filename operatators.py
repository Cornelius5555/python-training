
average_marks = int(input("enter your marks: "))
if( average_marks >= 70):
   print("A")
elif (average_marks >=60):
    print("B")
elif (average_marks >= 50):
    print("C")
elif (average_marks >= 40):
    print("D")
else:
    print("E")

num = int(input("enter your number: "))
if (num % 2 == 0):
    print("Even")
else:
    print("Odd")

#task
#Take three inputs from a user, separately. Print the largest of the numbers.
 #   Hint: Determine what type of data is taken in as input
A = int(input("enter first num: "))
B = int(input("Enter second num: "))
C = int(input("Enter your 3 num: "))
if (A > B and A > C):
    print(A)
elif (B > A and B > C):
    print(B)
else:
    print(C)


#Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”, otherwise display “Normal temperature”
temp = int(input("enter Temprature: "))
if (temp >= 30):
    print("Temp is too high")
else:
    print("Normal temp")