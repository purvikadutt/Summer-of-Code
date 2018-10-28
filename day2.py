#Watching repos are for Notifications
# Star helps us find some repos more easily

# for i in range(65, 65+2*26):
# 	print(i," stands for ", chr(i))

# for i in range(1, 256):
# 	print(i, " stands for ", chr(i))


a = "Elle J"
b = "Sarah Alkhateeb"
c = "Paula Bernal"
d = "Melinda Gates"
students = [a, b, c, d]

print(students)

sisters = ["Christina Tarantino", "Jesse RS", "alteredco", "LamboFantrastico"]
print(sisters)

members = [students, sisters]
print(members)
print(members[1][3])

M = 'land'
o = 'water'
world = [
         [o,o,o,o,o,o,o,o,o,o,o],
         [o,o,o,o,M,M,o,o,o,o,o],
         [o,o,o,o,o,o,o,o,M,M,o],
         [o,o,o,M,o,o,o,o,o,M,o],
         [o,o,o,M,o,M,M,o,o,o,o],
         [o,o,o,o,M,M,M,M,o,o,o],
         [o,o,o,M,M,M,M,M,M,M,o],
         [o,o,o,M,M,o,M,M,M,o,o],
         [o,o,o,o,o,o,M,M,o,o,o],
         [o,M,o,o,o,M,o,o,o,o,o],
         [o,o,o,o,o,o,o,o,o,o,o]
        ]

def continent_counter(world, x, y):
	if world[y][x] != 'land':
		return 0

	size = 1
	world[y][x] = 'counted land'

	#row above
	size = size + continent_counter(world, x-1, y-1)
	size = size + continent_counter(world, x, y-1)
	size = size + continent_counter(world, x+1, y-1)

	#same row
	size = size + continent_counter(world, x-1, y)	
	size = size + continent_counter(world, x+1, y)

	#row below
	size = size + continent_counter(world, x-1, y+1)
	size = size + continent_counter(world, x, y+1)
	size = size + continent_counter(world, x+1, y+1)
	return size


print(continent_counter(world, 5, 5))

#Trace - good tool which tells the number of calls(even for recursive functions) that have been made
#Check it out












