from tkinter import *
from tkinter import filedialog

class App(Tk):
	def __init__(self, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs)
		container = Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (home_1, profile_1, home_2, database_1, database_2, database_3):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(home_1)	
	def show_frame(self, context):
		frame = self.frames[context]
		frame.tkraise()

class home_1(Frame):
    def __init__(self, parent, controller):
        

        def open():
            filename = filedialog.askopenfilename(initialdir = "/home", title = "Select a File", filetypes=(("Template files", "*.tplate"),
                                            ("HTML files", "*.html;*.htm"),
                                            ("All files", "*.*") ))
            
            self.e.insert(0, filename)  


        Frame.__init__(self, parent) 

        top_frame = Frame(self)
        top_frame.pack(side = TOP)

        home_button = Button(top_frame, text="Home", fg="white", bd = 3,  bg = "blue", highlightcolor = "darkblue")
        database_button = Button(top_frame, text="Database", fg="white", bd = 3, bg ="cadet blue", command=lambda:controller.show_frame(database_1))
        profile_button = Button(top_frame, text="Profile", fg="white", bd = 3, bg="cadet blue", command=lambda:controller.show_frame(profile_1)) 

        home_button.pack(side = LEFT)
        profile_button.pack(side = LEFT)
        database_button.pack(side = LEFT)


        separator_1 = Frame(self, padx = 50,pady = 70)
        separator_1.pack(padx = 10, pady = 10)

        self.e = Entry(separator_1, width = 50)
        self.e.grid(row=0, column = 0, columnspan = 2)


        select_file = Button(separator_1, text="Select File", fg = "white", bg = "cadet blue", command=open)
        upload = Button(separator_1,text="Run Algorithm", fg="white", bg="green")

        select_file.grid(row=1,column=0)
        upload.grid(row=1, column = 1)

        separator_2 = Frame(self, padx = 50,pady = 70)
        separator_2.pack(padx = 10, pady = 10)

        var1 = IntVar()
        Checkbutton(separator_2, text= "Run Custom Workflow", variable = var1).pack(side = RIGHT)


class profile_1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)


        top_frame = Frame(self)
        top_frame.pack(side = TOP)

        home_button = Button(top_frame, text="Home", fg="white", bg = "cadet blue", bd  =3, command=lambda:controller.show_frame(home_1))
        database_button = Button(top_frame, text="Database", fg="white", bg ="cadet blue", bd = 3, command=lambda:controller.show_frame(database_1))
        profile_button = Button(top_frame, text="Profile", fg="white", bg="blue", bd = 3) 

        home_button.pack(side = LEFT)
        profile_button.pack(side = LEFT)
        database_button.pack(side = LEFT)

        separator_1 = Frame(self)
        separator_1.pack()

        name = Label(separator_1, text = "Name")
        email_id = Label(separator_1, text = "Email Id")
        sub_period = Label(separator_1, text = "Subscription Period")

        name.grid(row = 5, column = 5)
        email_id.grid(row = 6, column = 5)
        sub_period.grid(row = 7, column = 5)

class home_2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        top_frame = Frame(self)
        top_frame.pack(side = TOP)

        home_button = Button(top_frame, text="Home", fg="white", bg = "blue", bd = 3)
        database_button = Button(top_frame, text="Database", fg="white", bg ="cadet blue",bd = 3, command=lambda:controller.show_frame(database_1))
        profile_button = Button(top_frame, text="Profile", fg="white", bg="cadet blue",bd = 3, command=lambda:controller.show_frame(profile_1)) 

        home_button.pack(side = LEFT)
        profile_button.pack(side = LEFT)
        database_button.pack(side = LEFT)

        separator_1 = Frame(self)
        separator_1.pack()

        label_1 = Label(separator_1, text = "Identified Match",fg = "white", bg = "green", height = 3, width =100)
        label_1.pack(fill = "x")

class database_1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        top_frame = Frame(self)
        top_frame.pack(side = TOP)

        home_button = Button(top_frame, text="Home", fg="white", bg = "cadet blue",bd = 3, command=lambda:controller.show_frame(home_1))
        database_button = Button(top_frame, text="Database", fg="white", bg ="blue", bd = 3)
        profile_button = Button(top_frame, text="Profile", fg="white", bg="cadet blue", bd = 3, command=lambda:controller.show_frame(profile_1)) 

        home_button.pack(side = LEFT)
        profile_button.pack(side = LEFT)
        database_button.pack(side = LEFT)

        separator_1 = Frame(self, height=20, bd=5, padx= 50, pady = 50)
        separator_1.pack()

        add_dataset = Button(separator_1, text="Add Dataset", command=lambda:controller.show_frame(database_2))

        custom = Button(separator_1, text="Edit Custom Workflow")

        add_dataset.grid(row=0, column = 0)
        custom.grid(row = 0, column = 1, columnspan = 5)

        search_button = Button(separator_1, text="Search")
        search_button.grid(row = 1, column = 6)
        e = Entry(separator_1, width=50)
        e.insert(0, "Enter User Name to Search: ")
        e.grid(row = 0, column = 6)

        frame_1 = Frame(self)
        frame_1.pack()
        Label_1 = Label(frame_1, text = "In Database", fg = "white", bg = "green", width = 150, height=3)
        Label_1.pack(fill = "x")


class database_2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        def open():
            filename = filedialog.askopenfilename(initialdir = "/home", title = "Select a File", filetypes=(("Template files", "*.tplate"),
                                            ("HTML files", "*.html;*.htm"),
                                            ("All files", "*.*") ))
            
            self.e.insert(0, filename)  

        top_frame = Frame(self)
        top_frame.pack(side = TOP)

        home_button = Button(top_frame, text="Home", fg="white", bg = "cadet blue",bd = 3, command=lambda:controller.show_frame(home_1))
        database_button = Button(top_frame, text="Database", fg="white", bg ="blue")
        profile_button = Button(top_frame, text="Profile", fg="white", bg="cadet blue", bd = 3, command=lambda:controller.show_frame(profile_1)) 

        home_button.pack(side = LEFT)
        profile_button.pack(side = LEFT)
        database_button.pack(side = LEFT)


        separator_1 = Frame(self, padx = 50,pady = 70)
        separator_1.pack(padx = 10, pady = 10)

        self.e = Entry(separator_1, width = 50)
        self.e.grid(row=0, column = 0, columnspan = 2)


        select_file = Button(separator_1, text="Select File", fg = "white", bg = "cadet blue", command = open)
        upload = Button(separator_1,text="Upload", fg="white", bg="green", command=lambda:controller.show_frame(database_1))

        select_file.grid(row=1,column=0)
        upload.grid(row=1, column = 1)

class database_3(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        top_frame = Frame(self)
        top_frame.pack(side = TOP)

        home_button = Button(top_frame, text="Home", fg="white", bg = "cadet blue", bd = 3, command=lambda:controller.show_frame(home_1))
        database_button = Button(top_frame, text="Database", fg="white", bg ="blue")
        profile_button = Button(top_frame, text="Profile", fg="white", bg="cadet blue", bd = 3, command=lambda:controller.show_frame(profile_1)) 

        home_button.pack(side = LEFT)
        profile_button.pack(side = LEFT)
        database_button.pack(side = LEFT)

        frame_1 = Frame(self)
        frame_1.pack(side = BOTTOM)

        edit_info = Button(frame_1, text = "Edit Information", bg = "cadet blue")
        delete = Button(frame_1, text = "Delete Details", bg = "red")

        delete.pack(side = RIGHT, padx= 5)
        edit_info.pack(side = RIGHT, padx = 5)

app = App()
app.title("Video Mining Software")
app.mainloop()