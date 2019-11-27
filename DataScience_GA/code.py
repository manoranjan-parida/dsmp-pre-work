# --------------
# Code starts here
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']
new_class = class_1+class_2 
print(new_class)
new_class.remove('Carla Gentry')
print(new_class)
new_class.append('Peter Warden')
print('='*20)
print(new_class)

# Code ends here


# --------------
# Code starts here
courses = {"Math":65,"English":70,"History":80,"French":70,"Science":60}
#courses_values = courses.values()
#print(courses_values)
total=0
for i in courses:
   total+=courses[i]

print("Sum Is:",total)
percentage = (total/500)*100
print(percentage, "%")

# Code ends here


# --------------
# Code starts here




mathematics = {"Geoffrey Hinton":78,"Andrew Ng":95,"Sebastian Raschka":65,"Yoshua Benjio":50,"Hilary Mason":70,"Corinna Cortes":66,"Peter Warden":75}
topper = max(mathematics,key =mathematics.get)
Highest_mark=mathematics.get(topper)
#print(topper, "has scored" ,Highest_mark, "in Mathematics")

#Another way to print the above statement is
print("{} has scored {} in mathematics and is the highest in the class".format(topper,Highest_mark))




# Code ends here  


# --------------
# Given string
topper = 'andrew ng'


# Code starts here
first_name,last_name= topper.split()
full_name = last_name+" "+first_name
print(full_name)
certificate_name = full_name.upper()
print(certificate_name)


# Code ends here


