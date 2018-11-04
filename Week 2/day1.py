
# Functions, parameters
def moo(n):
	# print('moo' * n)
	return 'moo' * n

# moo(0)
# moo(1)
# moo(2)

# for i in range(3) :
# 	moo(i)

#Testing

#Reading and writing files
filename = "alice_in_wonderland.txt"
file = open(filename, "r")
# for line in file:
# 	print(line)

raw = file.read()
print(raw[:65])

print(raw[0:65])
print(raw[65:500])

print('the length of aiw in this text is' + str(len(raw)))

print(raw[163000:])

def ask_recursively(question):
	print(question)
	reply = input('> ').lower()
	if reply == 'yes':
		return True
	if reply == 'no':
		return False
	else:
		print('Please answer "yes" or "no".')
		ask_recursively(question)

ask_recursively('Do you wet the bed?')
