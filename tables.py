def generateAnnuityTable(assumptions, sex):
	""" Generates a table of single life annuity values for each age
	"""
	
	mortality = (assumptions.maleMortality if sex[0].lower == "m" 
				 else assumptions.femaleMortality)
	interest = assumptions.interest
	table = [0.0 for i in range(0, 120)]
	for age in reversed(range(0,119)):
		table[age] = 1 + table[age + 1] * (1 - mortality[age]) / (1 + interest)
	return table

def generateSurvivalTable(assumptions, sex, currentAge):
	""" Given a current age and a mortality table, generate the chance of
	surviving to each age """
	
	mortality = (assumptions.maleMortality if sex[0].lower == "m" 
				 else assumptions.femaleMortality)
	table = [1 for i in range(0, 120)]
	for age in range(currentAge + 1, 120):
		table[age] = table[age - 1] * mortality[age - 1]
	return table

def generateDecramentTable(assumptions, sex, currentAge):
	""" Generate a table with the chance of each decrament occuring at each
	age. Assume decraments occur in the following order: retirement, turnover,
	disability, mortality. """

	retirement = assumptions.retirement
	turnover = assumptions.turnover
	disability = (assumptions.maleDisability if sex[0].lower == "m" 
				 else assumptions.femaleDisability)
	mortality = (assumptions.maleMortality if sex[0].lower == "m" 
				 else assumptions.femaleMortality)
	survival = 1
	decraments = [[0 for i in range(0,120)] for j in range(0,4)]
	for age in range(currentAge, 120):
		decraments[0][age] = survival * retirement[age]
		survival *= 1 - retirement[age]
		decraments[1][age] = survival * turnover[age]
		survival *= 1 - turnover[age]
		decraments[2][age] = survival * disability[age]
		survival *= 1 - disability[age]
		decraments[3][age] = survival * mortality[age]
		survival *= 1 - mortality[age]

	return decraments