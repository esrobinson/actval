class Assumptions:
	"""Holds our assumptions. Interest, mortality, disability, turnover
	and retirement for now"""

	def __init__(self, interest, maleMortality, femaleMorality, maleDisability,
				 femaleDisability, turnover, retirement):
		self.interest = float(interest)
		self.maleMortality = self.loadTable('./rates/'+maleMortality)
		self.femaleMortality = self.loadTable('./rates/'+femaleMorality)
		self.maleDisability = self.loadTable('./rates/'+maleDisability)
		self.femaleDisability = self.loadTable('./rates/'+femaleDisability)
		self.turnover = self.loadTable('./rates/'+turnover)
		self.retirement = self.loadTable('./rates/'+retirement)

	def loadTable(self, tableName):
		rates = open(tableName)
		table = [float(rate.strip()) for rate in rates]
		return table