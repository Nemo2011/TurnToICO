from tkinter.constants import END
from tkinter import messagebox
from PIL import Image
import os
import time
import tkinter
import sys

FORMAT = ['.bmp', '.jpg', '.png', '.gif', '.jfif', '.jpeg']  

def search_file(start_dir):
    img_list = []
    extend_name = FORMAT
    os.chdir(start_dir)  
 
    for each_file in os.listdir(os.curdir):
        img_prop = os.path.splitext(each_file)
        if img_prop[1] in extend_name:
            img_list.append(os.getcwd() + os.sep + each_file)
 
        if os.path.isdir(each_file): 
            search_file(each_file)  
            os.chdir(os.pardir)

    return img_list

images = search_file(os.curdir)

root = tkinter.Tk()
root.title("Search images")
root.geometry("1000x500")
list = tkinter.Listbox(root, width=100)
list.grid(row=0, column=0)
for image in images:
    list.insert("end", image)

def start():
    list.delete(0, END)
    root.title("Turn to ICO")
    start=time.perf_counter()
    for image in images:
        opend_file = Image.open(image)
        image_name = os.path.splitext(image)[0]
        opend_file.save(image_name + ".png")
        list.insert("end", image)
    root.title("Done. These are ICO files")
    list.delete(0, END)
    for image in images:
        ico_name = os.path.splitext(image)[0] + ".ico"
        list.insert("end", ico_name)
    end = time.perf_counter()
    turn_t = end - start
    messagebox.showinfo("Done", "Turn To ico use:" + str(turn_t) + "second.")
    
    def close():
        sys.exit()
    button = tkinter.Button(root, text="close", width=100, command=close)
    button.grid(row=1, column=0)
    

    
button = tkinter.Button(root, text="turn to ico", width=100, command=start)
button.grid(row=1, column=0)

root.mainloop()
