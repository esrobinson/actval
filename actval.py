import sys
import assumptions
import tables

program = open(sys.argv[1])

assumptionInput = program.readline()

assumptionInput = assumptionInput.split(" ")

assumptionSet = assumptions.Assumptions(assumptionInput[0], assumptionInput[1],
										assumptionInput[2], assumptionInput[3],
										assumptionInput[4], assumptionInput[5],
										assumptionInput[6])

