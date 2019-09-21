# image_viewer

from tkinter import *
from PIL import ImageTk, Image
import os

# directory to scan
mydir = input('Type or paste directory path: ')

os.chdir(mydir)

# file extensions to search for
formats = ['jpeg', 'jpg', 'png', 'gif', 'tiff', 'bmp', 'ico']

# list files with above extensions
files = []

for file in os.listdir():
    for form in formats:
        if file.endswith('.' + form):
            files.append(file)

total_img = len(files)

# create GUI window
root = Tk()
root.title('Image Viewer')

# max height of image, fixed width of image field
max_h = 500
width = 1000

# open and resize images, save to dictionary
imgs = {}

for i in range(total_img):
    img = Image.open(files[i])
    s = img.size
    ratio = max_h/s[1]
    newimg = img.resize((int(s[0]*ratio), max_h), Image.ANTIALIAS)
    imgs[i] = ImageTk.PhotoImage(newimg)
    img.close()

# display first image in folder
image = imgs[0]
my_label = Label(root, image=image, width=width)
my_label.grid(row=0, column=0, columnspan=5)
curr_img = 0

# scroll to next image
def fwd():
    global my_label
    global curr_img
    global btn_back
    global btn_fwd
    
    my_label.grid_forget()
    image = imgs[curr_img + 1]
    my_label = Label(root, image=image, width=width)
    my_label.grid(row=0, column=0, columnspan=5)
    curr_img += 1
    if curr_img > 0:
        btn_back.configure(state='normal')
    if curr_img == (total_img-1):
        btn_fwd.configure(state=DISABLED)
        
# scroll to previous image
def back():
    global my_label
    global curr_img
    global btn_back
    global btn_fwd
    
    my_label.grid_forget()
    image = imgs[curr_img - 1]
    my_label = Label(root, image=image, width=width)
    my_label.grid(row=0, column=0, columnspan=5)
    curr_img -= 1
    if curr_img < (total_img-1):
        btn_fwd.configure(state='normal')
    if curr_img == 0:
        btn_back.configure(state=DISABLED)

# skip to first image
def first():
    global my_label
    global curr_img
    global btn_back
    global btn_fwd
    
    my_label.grid_forget()
    image = imgs[0]
    my_label = Label(root, image=image, width=width)
    my_label.grid(row=0, column=0, columnspan=5)
    curr_img = 0
    btn_fwd.configure(state='normal')
    btn_back.configure(state=DISABLED)

# skip to last image
def last():
    global my_label
    global curr_img
    global btn_back
    global btn_fwd
    
    my_label.grid_forget()
    image = imgs[total_img-1]
    my_label = Label(root, image=image, width=width)
    my_label.grid(row=0, column=0, columnspan=5)
    curr_img = total_img-1
    btn_back.configure(state='normal')
    btn_fwd.configure(state=DISABLED)
    
# define buttons for scrolling and closing the programme    
btn_first = Button(root, text='<<', command=first)
btn_back = Button(root, text='<', command=back, state=DISABLED)
btn_exit = Button(root, text='Quit', command=root.destroy)
btn_fwd = Button(root, text='>', command=fwd)
btn_last = Button(root, text='>>', command=last)

btns = [btn_first, btn_back, btn_exit, btn_fwd, btn_last]

# place buttons in window
for i in range(len(btns)):
    btns[i].grid(row=1, column=i)
    
root.mainloop()
