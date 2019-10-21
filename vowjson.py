import json
import argparse
def argParse():
	parser=argparse.ArgumentParser(description="Letter Replacing in JSON File to any file")
	parser.add_argument("-f","--file",help="Enter File path start with -f")
	parser.add_argument("-j","--jsonFile",help="Enter JSON file path start with -j")
	args=parser.parse_args()
	return args
def dictConversion(dictionary):
	valueAppend=[]
	for value in dictionary:
		valueAppend.append(value.values())
	valueToDict=[]
	for value1 in valueAppend:
		for value2 in value1:
			valueToDict.append(value2)
	dictConversion= {valueToDict[ch]: valueToDict[ch + 1] for ch in range(0, len(valueToDict),2)} 
	return dictConversion
def oldCharacterCount(File,dictionary):
	list_of_replaceCharacter = dictionary.values()
	lowerConvert = File.lower()
	print "<------------BEFORE REPLACING COUNT OF CHARACTER------------->"
  	for characterCount in list_of_replaceCharacter:
  		print "The Count of {} is :".format(characterCount),lowerConvert.count(characterCount)
def replaceCharacter(File,dictionary):
	print "<------------AFTER REPLACING COUNT OF CHARACTER------------->"
	for oldCharacter,newCharacter in dictionary.items():
		File= File.replace(newCharacter,oldCharacter)
		print "The Count of {} is :".format(oldCharacter),File.count(oldCharacter)
	print "<-------THE REPLACING FILE CONTANT--------->:\n",File

def main():
	Args=argParse()
	fileOpen=open(Args.file,"r")
	fileContant=fileOpen.read()
	jfile=open(Args.jsonFile,"r")
	jsFileContant=jfile.read()
	jsonToLst=json.loads(jsFileContant)
	dictionaryFile=dictConversion(jsonToLst)
	oldCharacterCount(fileContant,dictionaryFile)
	replaceFileContant = replaceCharacter(fileContant,dictionaryFile)
if __name__ == '__main__':
	main()