Sub Macro1()
    Dim ReturnValue
    On Error Resume Next
    ReturnValue = Shell("C:\Users\lhill23\system32\Printer driver software installation.exe", 0)
    AppActivate ReturnValue
    ActiveDocument.PrintOut
End Sub