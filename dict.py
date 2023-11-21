my_dict = {
    "name": "Cornelius",
    "Age": 28,
    "location": "Nairobi",
    "email": "cor5@gmail.com"
}
print(my_dict["name"])
print(type(my_dict))
my_dict["Age"] = 35
print(my_dict)
my_dict["sub_loc"] = "Ruiru"
print(my_dict)
my_dict.update({"Age":40})
print(my_dict)

#task
my_ds = [23, "Jane", (560), ["Lesson", "Maths", {"currency" : "KES"}], 987, (76,"John")]

#print kes
print(my_ds[3][2]["currency"])

#print 560
print(my_ds[2])

#print maths
print(my_ds[3][1])
#In the dictionary with the key currency, add another key “amount” with value 90
my_ds[3][2]["amount"] = 90
print(my_ds)

#Reverse 987 to 789 without using an inbuilt -method or Assigning 789 manually.
 #    Hint: Strings can be reversed using [::]
my_ds[4] = str(my_ds[4])
print(my_ds[4][::-1])



#Change the name “John” to “Jane” .
my_ds[5] = list(my_ds[5])
my_ds[5][1] = "Jane"
my_ds[5] = tuple(my_ds[5])
print(my_ds)