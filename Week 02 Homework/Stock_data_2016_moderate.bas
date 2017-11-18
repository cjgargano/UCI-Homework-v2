Attribute VB_Name = "Module1"
Sub Stock_Moderate()

    Dim stock As String
    Dim lastRow, lastStock, total, openPrice, closePrice, yearlyChg, percChg As Double
    
    'Add Column Headers
    Range("I1") = "<ticker>"
    Range("J1") = "<yearly chg>"
    Range("K1") = "<perc chg>"
    Range("L1") = "<total vol>"

    lastRow = Cells(Rows.Count, 1).End(xlUp).Row

    For i = 2 To lastRow
        
        If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
            
            'Set Stock Ticker in Summary Table
            stock = Cells(i, 1)
            lastStock = lastStock + 1
            Cells(lastStock + 1, 9) = Cells(i, 1)
            
            'Calculate Total
            total = total + Cells(i, 7)

            'Set Total in Summary Total
            Cells(lastStock + 1, 12) = total

            'Reset Total
            total = 0
            
            'Get Closing Price
            closePrice = Cells(i, 6)
        
            'Set Yearly Change, Percent Change in Summary Table
            Cells(lastStock + 1, 10) = closePrice - openPrice
            Cells(lastStock + 1, 11) = (closePrice / openPrice) - 1

        ElseIf Cells(i + 1, 1) = Cells(i, 1) Then
            
            'Add to cumulative total
            total = total + Cells(i, 7)
                
        End If
        
        'Get Opening Price
        If Cells(i - 1, 1) <> Cells(i, 1) Then
            
            openPrice = Cells(i, 3)
        
        End If

    Next i
    
    
    'Reformat Total Volume column
    lastRow = Cells(Rows.Count, 10).End(xlUp).Row
    
    Range("J2:J" & lastRow).NumberFormat = "$#,##0.00"
    Range("L2:L" & lastRow).NumberFormat = "$#,##0"
    Range("K2:K" & lastRow).NumberFormat = "0.00%;(0.00%)"
    
    
    'Color shading based on positive / negative changes
    For i = 2 To lastRow
    
        If Range("J" & i) < 0 Then
            Range("J" & i).Interior.ColorIndex = 3
        
        ElseIf Range("J" & i) > 0 Then
            Range("J" & i).Interior.ColorIndex = 4
        
        End If
    
    Next i
    
End Sub
