import json
import argparse
def argParse():
	parser=argparse.ArgumentParser(description="Letter Replacing in JSON File to any file")
	parser.add_argument("-f","--file",help="Enter File path start with -f")
	parser.add_argument("-j","--jsonFile",help="Enter JSON file path start with -j")
	args=parser.parse_args()
	return args
def dictConversion(configFileContant):
	dictValues=[]
	for value in configFileContant:
		dictValues.append(value.values())
	dictConversion = dict(dictValues)
	return dictConversion
def oldCharacterCount(fileContent,stringCount):
	countOldCharacters = stringCount.values()
	stringLowerConvertion = fileContent.lower()
	print "<------------BEFORE REPLACING COUNT OF CHARACTERS------------->"
  	for characterCount in countOldCharacters:
  		print "The Count of {} is :".format(characterCount),stringLowerConvertion.count(characterCount)
def replaceCharacterAndCount(fileContent,replaceStringDictionary):
	print "<------------AFTER REPLACING COUNT OF CHARACTERS-------------->"
	stringLowerConvertion = fileContent.lower()
	for newCharacter,oldCharacter in replaceStringDictionary.items():
		stringLowerConvertion= stringLowerConvertion.replace(oldCharacter,newCharacter)
		print "The Count of {} is :".format(newCharacter),stringLowerConvertion.count(newCharacter)
	print "<-----------------THE REPLACING FILE CONTENT------------------>\n",stringLowerConvertion
def main():
	args=argParse()
	file=open(args.file,"r")
	fileContent=file.read()
	configFile=open(args.jsonFile,"r")
	configFileContent=configFile.read()
	configFileContentToLst=json.loads(configFileContent)
	dictionaryFile=dictConversion(configFileContentToLst)
	oldCharacterCount(fileContent,dictionaryFile)
	replaceCharacterAndCount(fileContent,dictionaryFile)
if __name__ == '__main__':
	main()