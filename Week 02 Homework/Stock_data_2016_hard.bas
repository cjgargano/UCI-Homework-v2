Attribute VB_Name = "Module1"
Sub Stock_Hard()

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
    
    
    'Hard Solution being included with second For Loop
    Dim maxInc, maxDec, maxVol As Double
    Dim maxIncTicker, maxDecTicker, maxVolTicker As String
        

    For i = 2 To lastRow
    
        'Color shading based on positive / negative changes
        If Range("J" & i) < 0 Then
            Range("J" & i).Interior.ColorIndex = 3
        
        ElseIf Range("J" & i) > 0 Then
            Range("J" & i).Interior.ColorIndex = 4
        
        End If
        
        
        'Reset maxInc if new row's data is greater than existing value
        If Range("K" & i) > maxInc Then
            maxInc = Range("K" & i)
            maxIncTicker = Range("I" & i)
        End If
        
        'Reset maxDec if new row's data is less than existing value
        If Range("K" & i) < maxDec Then
            maxDec = Range("K" & i)
            maxDecTicker = Range("I" & i)
        End If

        'Reset maxVol if new row's data is greater than existing value
        If Range("L" & i) > maxVol Then
            maxVol = Range("L" & i)
            maxVolTicker = Range("I" & i)
        End If
        
    Next i
    
    'Output new summary table
    Range("O2") = "Greatest % Increase"
    Range("O3") = "Greatest & Decrease"
    Range("O4") = "Greatest Total Volume"
    Range("P1") = "Ticker"
    Range("Q1") = "Value"
    
    Range("P2") = maxIncTicker
    Range("P3") = maxDecTicker
    Range("P4") = maxVolTicker
    
    Range("Q2") = maxInc
    Range("Q3") = maxDec
    Range("Q4") = maxVol
    
    Range("Q2:Q3").NumberFormat = "0.00%;(0.00%)"
    Range("Q4").NumberFormat = "$#,##0"
    
End Sub
