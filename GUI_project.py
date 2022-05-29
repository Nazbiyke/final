from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import colorchooser

root = Tk()
root.title('AIU')
root.geometry("800x800")


def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="/PycharmProjects/Final/images", title="Select a file", filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()

my_btn = Button(root, text="Open File", command=open).pack()


my_img_logo = ImageTk.PhotoImage(Image.open("logo.jpg"))
my_label = Label(image=my_img_logo)
my_label.pack()


frame = LabelFrame(root, padx=5, pady=5)
frame.pack(side="top", padx=10, pady=10)

def open():
    top = Toplevel()
    lbl = Label(top, text="Ala- Too international university is one of the most famous universities,").pack()
    lbl = Label(top, text="and it was established in 1996.").pack()
    lbl = Label(top, text="From that day, till yet, this university is coming up with a"
                          "lot of modifications around.").pack()
    lbl = Label(top, text="The major motive with which this university is moving ahead "
                          "is as the Gateway to the world.").pack()
    lbl = Label(top, text="This means that they are moving ahead for a bright future and want that every student "
                          "must have all the facilities for completing their education. ").pack()
    lbl = Label(top, text="All the students wish to complete MBBS in Kyrgyzstan "
                          "can apply for admission and start their career.").pack()
    lbl = Label(top, text="Also, multiple faculties are here helping the student to achieve their goals.").pack()
    lbl = Label(top, text="This is a private institution, but yet the fee is really very affordable and helps students "
                          "to avail the same through scholarships as well.").pack()

b = Button(frame, text="Ala-Too International University", command=open).pack()

def color():
    my_color = colorchooser.askcolor()[1]
    my_label = Label(root, text=my_color).pack(pady=10)
    my_label2 = Label(root, text="Yoy picked a color!", font=("Helvetica", 32), bg=my_color).pack()

my_button = Button(root, text="Pick a color", command=color).pack()

def myClick():
    my_label = Label(root, text="Thanks for your interest!")
    my_label.pack()

b = Button(frame, text="To get a consultation click here, we will contact you!", command=myClick).pack()

button_quit = Button(frame, text='Exit Program', command=root.quit)
button_quit.pack()


root.mainloop()
