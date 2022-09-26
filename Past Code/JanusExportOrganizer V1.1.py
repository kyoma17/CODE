import os 
import shutil

# Comment in which path to exectute script in
#exportpath = "C:\\Users\\MaK23074\\Desktop\\Test\\"
#exportpath = "Z:\\For Kenny\\Test\\"
exportpath = "Z:\\PCRJanusExport\\"

filelist = os.listdir(exportpath)

csvlist = []

for file in filelist:
	if file == "PCR0006191.csv":
		print("still here")
	else:
		if file.endswith(".csv"):
			csvlist.append(file)
			destinationpath = exportpath + file.removesuffix(".csv")

			try: 
				os.makedirs(destinationpath)
			except FileExistsError: 
				print("folder for " + file + "exists already")

			sourcepath = exportpath + file
			trffilepath = destinationpath +  "_L.trf"

			try:
				# os.rename(sourcepath, destinationpath)
				shutil.move(sourcepath, destinationpath)
			except PermissionError:
				print(file + " is in use and cannot be moved")
			except shutil.Error:
				print(file + " is already in folder")

			try:
				shutil.move(trffilepath, destinationpath)
			except shutil.Error:
				print("hihi")
			except FileNotFoundError:
				print("TRF for " + file + " not found")

print("Done!")
print(csvlist)

input()