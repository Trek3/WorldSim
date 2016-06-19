from utils import get_name

class Person():

	def __init__(self, name=get_name(), age=0, genes=[], gender=None):
		self.name=name
		self.age=age
		self.genes=genes
		self.gender=gender

	def get_name(self):
		return self.name

	def get_age(self):
		return self.age

	def get_genes(self):
		return self.genes

	def get_gene(self, index):
		return self.genes[index]

	def get_gender(self):
		return self.gender

	def set_name(self, new_name):
		self.name=new_name

	def set_age(self, new_age):
		self.age=new_age

	def set_genes(self, new_genes):
		self.genes=new_genes

	def set_gene(self, new_gene, index):
		self.genes[index]=new_gene

	def set_gender(self, gender):
		self.gender=gender

	def infos(self):
		return ("[Player: {0}, Age: {1}, DNA: {2}, Gender: {3}]\n".format(self.name, self.age, self.genes, self.gender))

