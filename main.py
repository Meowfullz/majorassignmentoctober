from passwords import *
def main():
# create a credential object named p1
# that has a password equal to 1234567
# and a username equal to datastructures
	p1 = credential(1234567, "datastructures")

# display string representation of p1
	print (p1)
# create a credential object named p2
# that has a password equal to abcdefgh
# and a username equal to datastructures
	p2 = credential("abcdefgh", "datastructures")

# display string representation of p2
	print(p2) #print(p2.__strength__)
	
# create a credential object named p3
# that has a password equal to abcd1234
# and a username equal to datastructures
	p3 = credential("abcd1234", "datastructures")
# display string representation of p3
	print(p3)
# create a credential object named p4
# that has a password equal to abcd123!
# and a username equal to datastructures
	p4 = credential("abcd123!", "datastructures")

# display string representation of p4
	print(p4)

# display the result of testing if p1 is equal to p2
	print("p1 = p2?", p1.__eq__(p2))
	
# create a list named l1 that contains the numbers 1234567
	l1 = [1234567]

# display the result of testing if p1 is equal to l1
	print("p1 = l1?", p1.__eq__(p2))

# set l1 to None
	l1 = []
# display the result of testing if p1 is equal to l1
	print("p1 = l1?", p1.__eq__(p2))
# display the result of testing if p3 is equal to p2
	print("p3 = p2?", p3.__eq__(p2))
# use getter and setter methods to make p2 the same credential
# as p3
	p2.setPassword("abcd1234")
# display a string representation of p2
	print(p2)
# display the result of testing if p3 is equal to p2
	print("p3 = p2?", p3.__eq__(p2))
# test constructor to ensure ValueErrors are being raised when appropriate

	p4 = credential(None, None)
if __name__ == "__main__":
	main()