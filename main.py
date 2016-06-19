from person import Person
from population import Population

from utils import get_name
from time import gmtime, strftime
from sys import argv

log = open("./data/logs/log{0}.txt".format(strftime("%Y%m%d%H%M%S", gmtime())), "a")

def evolve(population):
	pop.age()
	pop.kill()
	pop.reproduce()

POP_SIZE=int(argv[1]) if len(argv) >=2 else 50

pop=Population(POP_SIZE)

generation=0

for person in pop.pop:
	log.write(person.infos())

while(pop.size()>0 and pop.size()<10000):
	generation+=1
	log.write("Generation {0} - Population Size: {1}\n".format(generation, pop.size()))
	evolve(pop)

generation+=1
log.write("Generation {0} - Population Size: {1}\n".format(generation, pop.size()))
