#Written by Kenny Ma. Email kenny.ma@perkinelmer for help
import os 
import shutil
import pandas as pd
import winsound
# import warnings filter
from warnings import simplefilter
# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)

print("Please scan the shelf barcode first")

# sourcepath = "Z:\\For Kenny\\\LIBApril\\"
sourcepath = "Z:\\For Kenny\\KLIB\\"
#sourcepath = "Z:\\NGS\\Cherry Picking Files\\"
#sourcepath = "Z:\\For Kenny\\LIBSourceJas\\"
#sourcepath = "C:\\Users\\MaK23074\\Desktop\\LIBSource\\"

sourcefolder = os.listdir(sourcepath)

listofSeqPlates = []
shelfList = []

for file in sourcefolder:
	if file == 'desktop.ini':
		pass
	else: 
		name = sourcepath + file
		df = pd.read_csv(name)
		listofSeqPlates.append([file.removesuffix(".csv"), df])
		print("Loaded " + file.removesuffix(".csv"))

def searchBarcode(barcode):
	if barcode == "":
		return "Please scan Barcode"

	multi = 0 
	multiplate = []
	outputState = ""
	seqplate = ""
	found = False
	for couple in listofSeqPlates:
		df = couple[1]
		if barcode in df.values:
			seqplate = couple[0]
			found = True
			multiplate.append(couple[0])

	if len(multiplate) >= 2:
		playsound()
		return barcode + " is in multiple SeqPlate " + str(multiplate)
	elif found:
		playsound()
		return barcode + " is in SeqPlate" + seqplate
	else: 
		return "Barcode " + barcode + " not in any SeqPlates, Put back in freezer"

def playsound():
	winsound.Beep(400, 100)
	winsound.Beep(600, 100)


def hello ():
	print("help me T_T")


# print(searchBarcode("B0019387RNAEXT"))

while True:
	barcodex = input('Scan a Barcode : ')
	if barcodex == "done":
		print("Hi, here are the plates on this shelf.")
		for each in shelfList:
			print(each)
		shelfList = [] 
		print("Cleared Shelf in Memory, Copy this to Excel")

	else:
		print(searchBarcode(barcodex))
		shelfList.append(barcodex)

input()