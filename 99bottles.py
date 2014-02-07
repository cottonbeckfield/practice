import sys

verse3 = "No more bottles of beer on the wall, no more bottles of beer! ... Fuck."

def plural(bottles_beer):
	if bottles_beer != 1:
		return "bottles"
	else:
		return "bottle"

def nnbottles(bottles_beer):
	verse1 = "{0} {1} of beer on the wall, {0} {1} of beer!"
	verse2 = "Take one down, pass it around, {} {} of beer on the wall!\n"

	for i in range(bottles_beer, 0, -1):
		print verse1.format(i, plural(i))
		next_bottles = i - 1
		if next_bottles == 0:
			next_bottles = "no more"
		print verse2.format(next_bottles, plural(i))
	return bottles_beer

num = raw_input("How many bottles do you have?: ")
nnbottles(int(num))

print verse3

##########################
#Lessons Learned
##########################
# {0} and {1} are updated with the .format command.
# So for print verse.format(i), it's taking just the i cmd.
# For verse.format(i, variable2(i)) it would update {0} and {1}
