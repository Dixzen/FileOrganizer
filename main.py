import os
import shutil
import tkinter as tk

frame = tk.Tk()

frame.title("OrganizeMaster")

frame.geometry('600x100')


def fileManage():
    
    path = inputtxt.get(1.0, "end-1c")
    files = os.listdir(path)
    
    for file in files:
        filename, extension = os.path.splitext(file)
        extension = extension[1:]
        
        if os.path.exists(path + '/' + extension):
            shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
        else:
            os.makedirs(path+'/'+extension)
            shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
    
    lbl.config(text = "OK")


# TextBox Creation
inputtxt = tk.Text(frame,
				height = 2,
				width = 40)

inputtxt.pack()

# Button Creation
printButton = tk.Button(frame,
						text = "Organize",
						command = fileManage)
printButton.pack()

# Label Creation
lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()





