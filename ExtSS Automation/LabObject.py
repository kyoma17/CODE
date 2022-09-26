#List of all the Plates getting parsed into Database
class PlateLibrary:
    def __init__ (self):
        self.DB = []

    def addItem(self, item):
  
        self.DB.append(item)
    
    def listPlates(self):
        return self.DB
    
    def reset(self):
        self.DB = []

    def searchItem(self, itemName):
        for each in self.DB:
            if each.name == itemName:
                return each.index
        return None

#Plate object which stores a List of samples objects
class Plate96:
    def __init__ (self, plateName, sampleImportList, PrincipleInvestigator, Institute, RequisitionNumber, StrainNumber):
        self.PlateName = plateName
        self.SampleArray = sampleImportList
        
        self.StrainNumber = StrainNumber
        self.reqNum = RequisitionNumber
        self.PI = PrincipleInvestigator
        self.Institute = Institute
  
    def name(self):
        return self.PlateName

    def listSamples(self):
        return self.SampleArray

    def searchSample(self, sample):
        index = 0
        for each in self.storedItems:
            if sample.name == each.name:
                return index
        return None


#Sample Objects. It will include OriginalPlate name, PI, Current location ect.
class sample:
    def __init__ (self, AscesionName, LaragenID, OriginalIndex, OriginalWellPos, ExtIndex, 
               PrincipleInvestigator, Institute, RequisitionNumber, StrainNumber, receieveDate):
        self.status = "na"
        self.AscName = AscesionName
        self.LaragenID = LaragenID
        self.OGindex = OriginalIndex
        self.OGwellpos = OriginalWellPos
        self.ExtIndex = ExtIndex
        self.StrainNumber = StrainNumber
        self.reqNum = RequisitionNumber
        self.PI = PrincipleInvestigator
        self.Institute = Institute
        self.receiveDate= receieveDate
  
    def LID(self):
        return self.LaragenID
  
