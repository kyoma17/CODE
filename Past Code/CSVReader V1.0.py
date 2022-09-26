import os 
import shutil
import csv
import pandas as pd
import array

platelist =[] 

sourcepath = "C:\\Users\\MaK23074\\Desktop\\LIBSource\\"
libpath = "C:\\Users\\MaK23074\\Desktop\\LIB\\"

testname  = "B0021735RNAEXT"

sourcefolder = os.listdir(sourcepath)
libraryfolder = os.listdir(libpath)



for file in sourcefolder:
	name = sourcepath + file
	df = pd.read_csv(name)
	print(file)
	platelist.append([file.removesuffix(".csv"), " "])


	for (Plate, colval) in df.iterrows():

		for export in libraryfolder:
			name2 = libpath + export
			df2 = pd.read_csv(name2)
			if colval[0] == [0]:
				pass
			elif colval[0] in df2.values:
				platelist.append([colval.values[0], export.removesuffix(".csv")])


print("done")
for couple in platelist:
	print(couple[0] + " " + couple[1])











# filelist = os.listdir(libpath)

# for file in filelist:
# 	name = libpath + file
# 	df = pd.read_csv(name)

# 	if testname in df.values:
# 		print("hi")

