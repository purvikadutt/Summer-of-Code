 #Dictionary Constructor
anne_niekrenz = dict(name = "Anne anne_niekrenz", discord_id = "anne", 
	fav_food = "ice cream")

print(anne_niekrenz)

# my_dict = {
# 	"a": 350000,
# 	"b" : 8000,
# 	"z" : 450
# }


# print(my_dict)

# #access 
# print(my_dict["a"])

# #add
# my_dict["Rocio"] = "pretty"
# print(my_dict["Rocio"])
# print(my_dict)

# #modify
# my_dict["a"] = 50
# print(my_dict["a"])
# print(my_dict)

# #delete item
# del(my_dict["a"])
# print(my_dict)
# print(len(my_dict))

# #delete dictionary
# del(my_dict)
# print(my_dict)


#Classes

class Student():
	def __init__(self, name, discord_id, fav_food, dream):
		self.name = name
		self.discord_id = discord_id
		self.fav_food = fav_food
		self.dream = dream

	def my_print(self):
		print(self.name + " " + self.discord_id + " " + self.fav_food + " " + self.dream)

#instantiate using our new constructor function
s1 = Student("Virginia Balseiro", "Virginia [Gold]", "pasta", "moving to Europe")
# s2 = Student("Andrea Berlin", "Andrea [Gold]", "")
# s3 = Student("Purvika Dutt", "Purvika [Platinum]")

# print(s1.discord_id)
# print(s2.discord_id)
# print(s3.discord_id)

s1.my_print()

s1.fav_food = "ice cream"
s1.my_print()

#del s1.fav_food
#s1.my_print()

#del s1
#print(s1)
#this stuff will give an error and should be avoided





