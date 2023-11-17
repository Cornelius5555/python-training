#question 1
name = "  JOHn  . "
name = name.strip().lower()
name = name[0:4]
print(name)

#question 2a
#sentence_one = “The Dog Breed is German Shepherd” only display “Breed is German”
a = "The Dog Breed is German Shepherd"
print(a[8:23])

#2b
b = sentence_two = "Defeats for the Clinton forces, this was her moment of triumph” only display “Clinton forces"
print(b[16:30])

#3
c = "The lazy dog; ran so fast; it hit the wall."
print(c.split(" ; "))
print(len(c))

#4
first_name = "  Joh.n" 
last_name = "   Do,e" 
first_name = first_name.strip().replace(".", '')
last_name = last_name.strip().replace(",", '')
full_name = first_name + " " + last_name
print(first_name)
print(last_name)
print(full_name)

#5
r = '["E","W","C"]'
r =  str(r).replace(",", '').replace('""', '')
print(r)