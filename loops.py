#Write a program that displays a numbers 1 to 50 inside a list.
numbers = []
for i in range(1, 50):
    if i % 7 == 0 or i % 5 == 0:
      numbers.append(i)
print(numbers)


#Find sum and average of values in the range between 10 to 40.
number = []
for i in range(10, 41):
   number.append(i)
summation = sum(number)
print(f"The sum is: {summation}")
avarage = summation / len(number)
print(f"The avarage is: {avarage}")


#Put in a list the first 10 odd numbers between 10 to 50. 
odd_numbers = []
for i in range(10, 50):
   if i % 2 == 1:
     odd_numbers.append(i)
print(odd_numbers)