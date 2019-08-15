import os
import sys

try:
	inputFileName = sys.argv[1]
	outputFileName = sys.argv[2]
except:
	inputFileName = input("HTML File Name:")
	outputFileName = input("Output File Name:")

firstLine = True

with open(inputFileName, "r") as inputFile:
	with open(outputFileName, "w") as outputFile:
		inputLines = inputFile.readlines()
		for line in inputLines:
			if(firstLine != True):
				outputFile.write("\n+ ")
			firstLine = False
			line = line[:-1]
			line = line.replace('"','\\"')
			print(line)
			outputFile.write("\"" + line + "\"")
		outputFile.write(";")