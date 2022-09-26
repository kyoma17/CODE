import warnings;   warnings.filterwarnings("ignore")
import pandas as pd
import os
import glob
import csv
import array
import LabObject
import os, array, csv

import LabObject as lab

#Written by Kenny Ma. Keep it simple stupid. 
main = True

#Create two libraries, RNA preprocessed Plates, and EXT processed Plates
RNALIB = lab.PlateLibrary()
EXTLIB = lab.PlateLibrary()


def interpreter(command):
    if command == "help":
        print("List of Commands:" +
            "\n loadtac:   Loads Taconic Paperwork" + 
            "\n loadmarge: Loads Marge Paperwork" + 
            "\n loadjax:   Loads Jax paperwork" + 
            "\n loadother: Loads other PI's Paperwork, Must be in Laragen Format" +
            '\n list:      list all paperwork loaded into memory'+
            "\n run:       Compiles all the PlateMap and Consolidates into ExtPlate")
        
    elif command == "loadtac" or command =="lt":
        loadTac()
    elif command == "loadmarge" or command =="lm":
        #printDBBarcodes()
        return
    elif command == "loadjax" or command =="lj":
        #printAllDB()
        return
    elif command == "loadother" or command =="lo":
        #search()
        return
    elif command == "list" or command == "ls":
        For each in RNALIB.listPlates():
           
        
    elif command == "run" or command =="r":
        return
    elif command == "reset":
        print("Clearing Memory")
        RNALIB.reset()
        EXTLIB.reset()
 
    else: 
        return
    


def loadTac():
    # sourcepath = loadFolder("Select Taconic Folder")
    sourcepath = "C:/Users/SERVER/Desktop/Taconic_INPUT/"
    
    sourcefolder = os.listdir(sourcepath)
    for file in sourcefolder:
        print("Loading " + file)
        
    csv_files = glob.glob(os.path.join(sourcepath, "*.csv"))
    
    for file in csv_files:

        df = pd.read_csv(file) 
        projectID = df["Project"][0]
        plateNumber = df["Well Plate"][0]
        
        sampleList = []
        
        for ss in df["Sample Name"]:
                sampleList.append(ss)
                
        AscPlate = LabObject.Plate96(plateNumber, sampleList, "Taconic", "Taconic", file, projectID)
        for unit in  AscPlate.listSamples():
            print(unit)

        RNALIB.addItem(AscPlate)

from tkinter import filedialog as fd
#Opens a Window to Select multiple files
def loadFiles(comment):
    filetypes = (
        ('excel', '*.xlsx'),
        ('All files', '*.*')
    )
    filenames = fd.askdirectory()
    # filenames = fd.askopenfilenames(
    #     title=comment,
    #     initialdir='/',
    #     filetypes=filetypes)
    
    return filenames

#Main Loop intro
#labDB = loadDatabase()
#print("Loaded Fridge Database with " + str(len(labDB)) + " Items")

while main:
    command = input("Enter Command:").lower()
    interpreter(command)
    
    
#Graphical User Interface