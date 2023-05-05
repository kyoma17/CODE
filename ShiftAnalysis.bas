'Purpose To Generate a Summary of Extraction Batches Completed by Extraction Janus during each shift.
'Usable output will be be Shift Extraction Counts, and Counts by Hour and Day.
'Written by Kenny Ma. Contact: kenny.ma@perkinelmer.com Cell number:(626)-246-2233
'Version 1.0 August,30 2021

'Main Execution for one button macro.
Sub ExtractionSummary()

    SortDates
    insertDataHeaders
    extractExtractionTimeData
    AssignShift
    processBatchData
    ShiftCount
    ShortenTechList
    GenerateTechRuns
    Cells.Select
    Cells.EntireColumn.AutoFit
    
End Sub

'Sort Dataset by Extraction Janus Times
Sub SortDates()
    'Deletes Lims Export Timestamps
    If InStr(1, ActiveWorkbook.Worksheets(1).Range("A1").Value, "Report Batch ") Then
        Rows("1:2").Select
        Selection.Delete Shift:=xlUp
    End If
    
    ActiveSheet.Range("$A$1:$L$20000").RemoveDuplicates Columns:=4, Header:= _
        xlYes
    ActiveWorkbook.Worksheets(1).Sort.SortFields.Add2 Key:=Range("E:E") _
        , SortOn:=xlSortOnValues, Order:=xlAscending, DataOption:=xlSortNormal
    With ActiveWorkbook.Worksheets(1).Sort
        .SetRange Range("A1:L20000")
        .Header = xlYes
        .MatchCase = False
        .Orientation = xlTopToBottom
        .SortMethod = xlPinYin
        .Apply
    End With
End Sub

'Insert Headers for Dataoutput and
Sub insertDataHeaders()
    ActiveWorkbook.Worksheets(1).Range("O1") = "Ext_Month"
    ActiveWorkbook.Worksheets(1).Range("P1") = "Ext_Day"
    ActiveWorkbook.Worksheets(1).Range("Q1") = "Ext_Hour"
    ActiveWorkbook.Worksheets(1).Range("R1") = "Shift Data"
    ActiveWorkbook.Worksheets(1).Range("S1") = "Time Label"
    ActiveWorkbook.Worksheets(1).Range("T1") = "Group Month"
    ActiveWorkbook.Worksheets(1).Range("U1") = "Group Day"
    ActiveWorkbook.Worksheets(1).Range("V1") = "Group Hour"
    ActiveWorkbook.Worksheets(1).Range("W1") = "Ext Per Hour"
    ActiveWorkbook.Worksheets(1).Range("X1") = ""
    
    ActiveWorkbook.Worksheets(1).Range("Y1") = "Shift"
    ActiveWorkbook.Worksheets(1).Range("Z1") = "Batches Completed"
            
End Sub

'Converts Janus Extraction Times to usable data
Sub extractExtractionTimeData()
    Dim totalExtractionBatches As Integer
    totalExtractionBatches = Application.WorksheetFunction.CountA(Columns("E"))
    
    For Batch = 2 To totalExtractionBatches
        ActiveWorkbook.Worksheets(1).Cells(Batch, 15) = "=Month(E" & Batch & ")"
        ActiveWorkbook.Worksheets(1).Cells(Batch, 16) = "=Day(E" & Batch & ")"
        ActiveWorkbook.Worksheets(1).Cells(Batch, 17) = "=Hour(E" & Batch & ")"
    Next Batch
        
    ActiveWorkbook.Worksheets(1).Cells(totalExtractionBatches + 1, 16) = "=Day(E" & totalExtractionBatches & " + 1)"
End Sub

Sub AssignShift()
    Dim totalExtractionBatches As Integer
    totalExtractionBatches = Application.WorksheetFunction.CountA(Columns("Q"))
    
    For Batch = 2 To totalExtractionBatches
        hour_ = ActiveWorkbook.Worksheets(1).Cells(Batch, 17)
        If hour_ = 7 Or hour_ = 8 Or hour_ = 9 Or hour_ = 10 Or hour_ = 11 Or hour_ = 12 Or hour_ = 13 Or hour_ = 14 Or hour_ = 15 Or hour_ = 16 Or hour_ = 17 Or hour_ = 18 Then

            ActiveWorkbook.Worksheets(1).Cells(Batch, 18) = MonthName(ActiveWorkbook.Worksheets(1).Cells(Batch, 15)) & " " & ActiveWorkbook.Worksheets(1).Cells(Batch, 16) & " " & "DayShift"
        End If
            
        If hour_ = 19 Or hour_ = 20 Or hour_ = 21 Or hour_ = 22 Or hour_ = 23 Or hour_ = 0 Or hour_ = 1 Or hour_ = 2 Or hour_ = 3 Or hour_ = 4 Or hour_ = 5 Or hour_ = 6 Then
            ActiveWorkbook.Worksheets(1).Cells(Batch, 18) = MonthName(ActiveWorkbook.Worksheets(1).Cells(Batch, 15)) & " " & ActiveWorkbook.Worksheets(1).Cells(Batch, 16) & " " & "NightShift"
            
        End If
                
        cellCounter = cellCounter + 1

    Next Batch
    
    
    


End Sub

'Counts All Janus Extraction Runs by Hour
Sub processBatchData()

    Dim scanMonth As Range
    Dim scanDay As Range
    Dim scanHour As Range
    Dim timeSlot As Integer
    
    Dim timeLabel
    
    Set scanMonth = ActiveWorkbook.Worksheets(1).Range("O2")
    Set scanDay = ActiveWorkbook.Worksheets(1).Range("P2")
    Set scanHour = ActiveWorkbook.Worksheets(1).Range("Q2")
    timeSlot = 2
    
    For Each month_ In ActiveWorkbook.Worksheets(1).Range("O:O")
        If Not month_ = "Ext_Month" And Not month_ = scanMonth And month_ = "" Then
        
            For Each day_ In ActiveWorkbook.Worksheets(1).Range("P:P")
                If Not day_ = "Ext_Day" And Not day_ = scanDay And Not day_ = "" Then
                
                    For hour_ = 0 To 23
                        ActiveWorkbook.Worksheets(1).Cells(timeSlot, 19) = MonthName(scanMonth) & "/" & scanDay & "/" & hour_ & ":00"
                        ActiveWorkbook.Worksheets(1).Cells(timeSlot, 20) = scanMonth
                        ActiveWorkbook.Worksheets(1).Cells(timeSlot, 21) = scanDay
                        ActiveWorkbook.Worksheets(1).Cells(timeSlot, 22) = hour_
                        
                        ActiveWorkbook.Worksheets(1).Cells(timeSlot, 23) = "=COUNTIFS(O:O,T" & timeSlot & ",P:P,U" & timeSlot & ",Q:Q,V" & timeSlot & ")"
                                        
                        timeSlot = timeSlot + 1
                    
                    Next hour_
                    Set scanDay = day_
                End If
                Next day_
                
            Set scanMonth = month_
        End If
        Next month_
        
End Sub

'Summation of Janus Runs by Shifts using Hours
Sub ShiftCount()
    Dim cellCounter As Double
    cellCounter = 2
    
    Dim logCounter As Integer
    logCounter = 2
    
    Dim batchCounter As Integer
    batchCounter = 0
    
    Dim Shift
    Shift = "NightShift"
    
    
    For Each hour_ In ActiveWorkbook.Worksheets(1).Range("V:V")
        
        If Not "Group Hour" = hour_ Then
            
            If hour_ = 7 Or hour_ = 8 Or hour_ = 9 Or hour_ = 10 Or hour_ = 11 Or hour_ = 12 Or hour_ = 13 Or hour_ = 14 Or hour_ = 15 Or hour_ = 16 Or hour_ = 17 Or hour_ = 18 Then
                If Shift = "NightShift" Then
                    ActiveWorkbook.Worksheets(1).Cells(logCounter, 25) = "Night Shift " & MonthName(ActiveWorkbook.Worksheets(1).Cells(cellCounter - 1, 20)) & " " & ActiveWorkbook.Worksheets(1).Cells(cellCounter - 1, 21) - 1
                    ActiveWorkbook.Worksheets(1).Cells(logCounter, 26) = batchCounter
                    
                    Shift = "DayShift"
                    batchCounter = 0
                    logCounter = logCounter + 1
                   
                End If
                batchCounter = batchCounter + ActiveWorkbook.Worksheets(1).Cells(cellCounter, 23)
                cellCounter = cellCounter + 1
            End If
            
                
             If hour_ = 19 Or hour_ = 20 Or hour_ = 21 Or hour_ = 22 Or hour_ = 23 Or hour_ = 0 Or hour_ = 1 Or hour_ = 2 Or hour_ = 3 Or hour_ = 4 Or hour_ = 5 Or hour_ = 6 Then
                If Shift = "DayShift" Then
                

                    ActiveWorkbook.Worksheets(1).Cells(logCounter, 25) = "Day Shift " & MonthName(ActiveWorkbook.Worksheets(1).Cells(cellCounter - 1, 20)) & " " & ActiveWorkbook.Worksheets(1).Cells(cellCounter - 1, 21)
                    ActiveWorkbook.Worksheets(1).Cells(logCounter, 26) = batchCounter
                    
                    
                    Shift = "NightShift"
                    batchCounter = 0
                    logCounter = logCounter + 1

                End If
                batchCounter = batchCounter + ActiveWorkbook.Worksheets(1).Cells(cellCounter, 23)
                cellCounter = cellCounter + 1
            
            End If
                    
        
        End If
        Next hour_
    
End Sub



Sub ShortenTechList()
    Columns("R:R").Select
    Selection.Copy
    Range("AB1").Select
    ActiveSheet.Paste
    Columns("AB:AB").Select
    Application.CutCopyMode = False
    ActiveSheet.Range("AB1").RemoveDuplicates Columns:=1, Header:= _
        xlNo

End Sub


Sub GenerateTechRuns()
    Dim shifts As Integer
    shifts = Application.WorksheetFunction.CountA(Columns("AB"))
    
    Dim runs As Integer
    runs = Application.WorksheetFunction.CountA(Columns("Q"))
    
    Dim rowcount As Integer
    rowcount = 0
    
    Dim cellcount As Integer
    cellcount = 2
    
    Dim hello As Range
    
    
    For Shift = 2 To shifts
    
        shiftdata = ActiveWorkbook.Worksheets(1).Cells(Shift, 28)
        ActiveWorkbook.Worksheets(1).Cells(1, 30 + rowcount) = shiftdata
        
        
        For i = 2 To runs
            tech = ActiveWorkbook.Worksheets(1).Cells(i, 6)
            
            Duplicate = False
            For x = 2 To Application.WorksheetFunction.CountA(Columns(30 + rowcount))
                If ActiveWorkbook.Worksheets(1).Cells(x, 30 + rowcount) = tech Then
                    Duplicate = True
               End If
            Next x



            If shiftdata = ActiveWorkbook.Worksheets(1).Cells(i, 18) And Not Duplicate Then
        
    
                ActiveWorkbook.Worksheets(1).Cells(cellcount, 30 + rowcount) = ActiveWorkbook.Worksheets(1).Cells(i, 6)

                ActiveWorkbook.Worksheets(1).Cells(cellcount, 31 + rowcount) = "=COUNTIFS(R:R," & Cells(1, 30 + rowcount).Address & ",F:F," & Cells(cellcount, 30 + rowcount).Address & ")"
                
                
                cellcount = cellcount + 1
                
            End If
            
        Next i
        
        cellcount = 2
        
        
        rowcount = rowcount + 2
    Next Shift

    
End Sub







Sub DuplicateTechs(column, tech)
    DuplicateTechs = False
    For i = 2 To Application.WorksheetFunction.CountA(Columns(column))
        If ActiveWorkbook.Worksheets(1).Cells(i, row) = tech Then
            DuplicateTechs = True
        End If
       
    
End Sub
