Attribute VB_Name = "Module1"
Option Explicit
    Dim CellLineBook As Workbook
    
    Dim SNcolumn, Marker, Allele1, Allele2 As Integer
    Dim sampleList As Variant
    
    

Sub CellLineAuto()
Attribute CellLineAuto.VB_ProcData.VB_Invoke_Func = " \n14"
    Dim fileLocation As String
    
    fileLocation = "C:\Users\SERVER\Desktop\CellLineInput.xlsx"
    'fileLocation = Application.GetOpenFilename(Title:="Open Cell Line ID File", filefilter:=" Excel(*.xlsx*, xlsx")

    
    Workbooks.Open Filename:=fileLocation, Local:=True
    Set CellLineBook = ActiveWorkbook
    
    
    SNcolumn = SearchColumnSource("samplename", CellLineBook)
    Marker = SearchColumnSource("markers", CellLineBook)
    Allele1 = SearchColumnSource("allele1", CellLineBook)
    Allele2 = SearchColumnSource("allele2", CellLineBook)
    

    sampleList = Split(getSamples, ",")
    
    Dim sample As Variant
    For Each sample In sampleList
        Debug.Print (sample)
    
    Next

 


End Sub

Sub sortsample()

End Sub




Function getSamples() As String

    Dim lastRow As Integer
    lastRow = CellLineBook.Sheets(1).Cells(Rows.Count, 1).End(xlUp).Row
    
    Dim columnLetter As String
    columnLetter = Split(Cells(1, SNcolumn).Address, "$")(1)
    Dim name As Variant

    For Each name In CellLineBook.Sheets(1).Range(columnLetter & 2 & ":" & columnLetter & lastRow)
        If InStr(getSamples, name) < 1 Then
            getSamples = getSamples + "," + name
            
        End If
    Next

End Function


'This function will look for the names in the Source File and return the index of that column. Looks for the Last Instance
Public Function SearchColumnSource(search, wb) As Integer
    Dim columnIndex As Integer
    Dim field       As Variant
    
    columnIndex = 1
    For Each field In wb.Sheets(1).Range("A1", "AZ1")
        If cleanInput(field) = cleanInput(search) Then
            SearchColumnSource = columnIndex
        End If
        columnIndex = columnIndex + 1
    Next
End Function


Function cleanInput(inputText) As String
    cleanInput = LCase(inputText)
    cleanInput = Replace(cleanInput, " ", "")        ' Kill Ghost "space"
    cleanInput = Replace(cleanInput, " ", "")        ' Regular Space
    cleanInput = Replace(cleanInput, "_", "")
    cleanInput = Replace(cleanInput, "-", "")
End Function
