import random

male=open("./data/inputs/male-first.txt", "r")
female=open("./data/inputs/female-first.txt", "r")
surname=open("./data/inputs/all-last.txt", "r")

FEM=[]
MALE=[]
SUR=[]

while True:
        in_line = male.readline()
        if in_line == "":
            break
	MALE.append(in_line.split()[0])

while True:
	in_line = female.readline()
        if in_line == "":
            break
	FEM.append(in_line.split()[0])

while True:
	in_line = surname.readline()
        if in_line == "":
            break
	SUR.append(in_line.split()[0])

def get_name(gender=None):
	if(gender=='m'):
		return random.choice(MALE)+" "+random.choice(SUR)
	elif(gender=='f'):
		return random.choice(FEM)+" "+random.choice(SUR)
	else:
		ALL=FEM+MALE
		return random.choice(ALL)+" "+random.choice(SUR)
	

