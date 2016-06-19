from person import Person
from utils import get_name

import random

from time import gmtime, strftime

class Population():

	def __init__(self, population_size=0):
		self.pop = []
		for i in range(population_size):
			p=Person(age=int(random.random()*50), gender=random.choice(['m','f']))
			p.set_name(get_name(p.get_gender()))
			self.add_person(p)

	def size(self):
		return len(self.pop)

	def get_population(self):
		return self.pop

	def get_person(self, index):
		return self.pop[index]

	def get_person_by_name(self, name):
		for person in self.pop:
			if(person.get_name()==name):
				return person
			
		return -1

	def add_person(self, person):
		self.pop.append(person)

	def insert_person(self, person, index):
		self.pop.insert(index, person)

	def age(self):
		for person in self.pop:
			person.set_age(person.get_age()+20)

	def kill(self):
		for person in self.pop:
			if(person.get_age() > 100):
				self.pop.remove(person)

	def reproduce(self):
		reproduce_rate=int(self.size()*8/10)
		reproduce_rateo=0.4

		males = [p for p in self.pop if p.get_gender()=='m' and p.get_age() > 20 and p.get_age()<60]
		females = [p for p in self.pop if p.get_gender()=='f' and p.get_age() > 20 and p.get_age()<60]
		if(len(males) > 1 and len(females) > 1):
			for i in range(reproduce_rate):
				if(random.random()>reproduce_rateo):
					male=random.choice(males)
					female=random.choice(females)
					baby=Person(get_name().split()[0]+" "+male.get_name().split()[-1], 0, gender=random.choice(['m','f']))
					self.add_person(baby)
					#log.write("{0} is born from {1} and {2}\n".format(baby.get_name(), male.get_name(), female.get_name()))
		else:
			pass
