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


#Change the name “John” to “Jane” .
my_ds[5] = list(my_ds)
my_ds[5][1] = "Jane"
my_ds[5] = tuple(my_ds[5])
print(my_ds)