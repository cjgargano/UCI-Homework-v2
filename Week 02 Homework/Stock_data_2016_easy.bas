Attribute VB_Name = "Module1"
Sub Stock_Easy()

    Dim stock As String
    Dim lastRow, lastStock, total As Double
    
    lastRow = Cells(Rows.Count, 1).End(xlUp).Row

    For i = 2 To lastRow
        
        If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
            
            'Set Stock Ticker in Summary Table
            stock = Cells(i, 1)
            lastStock = lastStock + 1
            Cells(1 + lastStock, 9) = Cells(i, 1)
            
            'Calculate Total
            total = total + Cells(i, 7)
            
            'Set Total in Summary Table
            Cells(1 + lastStock, 10) = total
            
            'Reset Total
            total = 0
        
        Else
            
            total = total + Cells(i, 7)
        
        End If

    Next i
    
    'Add Column Headers
    Range("I1") = "<ticker>"
    Range("J1") = "<total vol>"
    
    'Reformat Total Volume column
    lastRow = Cells(Rows.Count, 10).End(xlUp).Row
    Range("J2:J" & lastRow).NumberFormat = "$#,##0"

    
End Sub
