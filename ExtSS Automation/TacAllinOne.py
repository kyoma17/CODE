import warnings;   warnings.filterwarnings("ignore")
import pandas as pd
import os
import glob
import csv
import array



platelist =[] 
# sourcepath = loadFiles("test")


sourcepath = "C:/Users/SERVER/Desktop/Taconic_INPUT/"
sourcefolder = os.listdir(sourcepath)

for file in sourcefolder:
	name = sourcepath + file
	df = pd.read_csv(name)

 
# use glob to get all the csv files in the folder
final_df = pd.DataFrame()
path = os.getcwd()
csv_files = glob.glob(os.path.join(sourcepath, "*.csv"))



#🧐deine project ID to laragen protocal, list as project ID , Laragen qPCR or PCR protocal name, then CAG protcal if there is
assay_dict = {
    "16570" : ["CHDI0001", "CHDI00x", "r62 cag"],
    "16112" : ["CHDI0002", "CHDI00x", "r62 cag"],
    "16113" : ["CHDI0003", "CHDI00x", "r62 cag"],    
    "16114" : ["CHDI0004", "CHDI00x", "r62 cag"],
    "16115" : ["CHDI0005", "CHDI00x", "r62 cag"],    
    "16116" : ["CHDI0006", "CHDI00x", "r62 cag"],
    "16120" : ["CHDI0011", "CHDI00x", "N107 cag"],
    "16332" : ["CHDI0012", "CHDI00x", "N107 cag"],
    "16674" : ["CHDI0014", "CHDI00x", "r62 cag"],
    "16676" : ["CHDI0016", "CHDI00x", "r62 cag"],   
    "17017" : ["CHDI0025", "CHDI00x", "r62 cag"],
    "17997" : ["CHDI0034", "CHDI00x", "r62 cag"],
    "18052" : ["CHDI0035", "CHDI00x", "r62 cag"],
    "17866" : ["CHDI0029", "CHDI00x+Exon49", "r62 cag"],
    "17865" : ["CHDI0029", "CHDI00x+Exon49", "r62 cag"],
    "17864" : ["CHDI0028", "CHDI00x+Exon49", "r62 cag"], 
    "16837" : ["CHDI0013", "CHDI00x", "r62 cag"],  
    "18067" : ["CHDI0026", "CHDI00x", "r62 cag"],
    "18068" : ["Q175cKO", "Q140withneonegative", "r62 cag"], 
    "18051" : ["CHDI0032", "CHDI00x", "N107 cag"],
    "18071" : ["CHDI0031", "CHDI00x", "N107 cag"],
    "18070" : ["CHDI0030", "CHDI00x+Cre", "N107 cag"],
    "18072" : ["CHDI0033", "CHDI00x", "N107 cag"],
    "18446" : ["CHDI0038","CHDI0038_Conditional_PCR", None],
    "18445" : ["CHDI0037", "CHDI0037_PCR+Flp_PCR", None],
    "18535" : ["CHDI0040", "CHDI0040_PCR+Flp_PCR", None],
    "18536" : ["CHDI0041", "CHDI0041_PCR++Flp_PCR", None],
    "19365" : ["CHDI0025+Cre+Constitutive", "CHDI00x+Cre+CHDI00xConstitutivePCR", "r62 cag"],
    "19366" : ["CHDI0026+Cre+Constitutive", "CHDI00x+Cre+CHDI00xConstitutivePCR", "r62 cag"],
    "19370" : ["19370", "SOP_26463+SOP_26465+Cre", None],
    "19026" : ["19026", "Atxn3_Copy", "human_Sca3"],
# need to edit list    
    "19372" : ["19372", "SOP_28555+SOP_28557+Cre", None], 
    "19367" : ["Q175cKO", "Q140withneonegative+Q175LoxP1+Cre", "r62 cag"], 
    "19369" : ["19369", "SOP_26458+SOP_26460+Cre", None],
    "19373" : ["19373", "SOP_28621+SOP_28623+Cre", None],
    "18427" : ["CHDI0036", "CHDI0036_PCR+Flp_PCR", None],
    "18534" : ["CHDI0039", "SOP_28754+Flp_PCR", None],
    "19368" : ["19368", "SOP_????+Cre", None], 
    }
series_dict = pd.Series(assay_dict, index=assay_dict.keys())
series_dict = series_dict.rename('test')


# convert list of samples into plate formate
def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


# used to seperate the nex dataframe before appending
head_name = {0:0,
        1:1,
        2:2,
        3:3,
        4:4,
        5:5,
        6:6,
        7:7,
        8:8,
        9:9,
        10:10,
        11:11,
        'Project':'Project',
        'CHDI_Name':'CHDI_Name',
        'Laragen_Protocal':'Laragen_Protocal',
        'CAG protocal':'CAG protocal',
        'numberOfSample':'numberOfSample',
        "Plate_number":"Plate_number"
       }
df_hname = pd.DataFrame(head_name,index=[8])



for f in csv_files:      
    # read the one csv file at a time and get plate info
    df = pd.read_csv(f) 
    
    sampleArray = []
    
    for ss in df["Sample Name"]:
            sampleArray.append(ss)
            
    for unit in sampleArray:
        print(unit)

exit()

for f in csv_files:      
    # read the one csv file at a time and get plate info
    df = pd.read_csv(f)  
  
    project_ID = df["Project"][0]
    plate_num = df["Well Plate"][0]
    taconic_alter_name = assay_dict[str(project_ID)][0]
    Laragen_genotype_protocal = assay_dict[str(project_ID)][1]
    Laragen_CAG_protocal= assay_dict[str(project_ID)][2]

    #create empty DataFrame with 8 index
    df_temp = pd.DataFrame(index = range(8) )  
 
    #get only sample name and append into a list
    sampleArray = []
    for ss in df["Sample Name"]:
            sampleArray.append(ss)
    plateArray = chunks(sampleArray, 8)
    df_ssname = pd.DataFrame(plateArray)
    df_ssname = df_ssname.T
    
    
    for unit in sampleArray:
        print(unit)

    #write all info into a datafram
    df_temp["Plate_number"] = plate_num
    df_temp['Project'] = project_ID
    df_temp['CHDI_Name'] = taconic_alter_name
    df_temp['Laragen_Protocal'] = Laragen_genotype_protocal
    df_temp['CAG protocal'] = Laragen_CAG_protocal
    df_temp['numberOfSample'] = len(df["Sample Name"])
    df_temp = pd.concat([df_temp, df_ssname], axis=1)
    df_temp= df_temp.append(df_hname, ignore_index = True)
    
    #append all file into one database
    final_df = final_df.append(df_temp)
    
#order column in the order you want
col_name = [0,1,2,3,4, 5,6,7,8,9,10,11, 'Project','CHDI_Name','Laragen_Protocal','CAG protocal','numberOfSample','Plate_number']
final_df= final_df[col_name]


