import PySimpleGUI as sg

label1 = sg.Text("Select files to compress:")
input1 = sg.InputText()
button1 = sg.FileBrowse("Choose")

label2 = sg.Text("Select Destination folder:")
input2 = sg.InputText()
button2 = sg.FileBrowse("Choose")

compress_button  = sg.Button("Compress")

window = sg.Window(title="File Zipper",layout=[[label1,input1,button1],
                                               [label2,input2,button2],
                                               [compress_button]])
window.read()
window.close()