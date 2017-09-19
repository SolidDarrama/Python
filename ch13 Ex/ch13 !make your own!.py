#Jose Guadarrama
#11/17/2014

import tkinter
import tkinter.messagebox

class Bio_info_GUI:
    def __init__(self):

        #Create main window
        self.main_window = tkinter.Tk()

        #create frames to group widgets
        self.title_frame = tkinter.Frame(self.main_window)
        self.first_frame = tkinter.Frame(self.main_window)
        self.second_frame = tkinter.Frame(self.main_window)
        self.third_frame = tkinter.Frame(self.main_window)
        self.fourth_frame = tkinter.Frame(self.main_window)
        self.fifth_frame = tkinter.Frame(self.main_window)
        self.sixth_frame = tkinter.Frame(self.main_window)
        self.buttons = tkinter.Frame(self.main_window)

        #create the widgets to the title frame==================================================
        self.title = tkinter.Label(self.title_frame, \
                                          text = "Bio Document")

        #pack the title frame's widget
        self.title.pack()

        #create the widgets to the first frame=====================================================
        self.F_Name = tkinter.Label(self.first_frame, \
                                          text = "Enter First Name:")
        self.F_Name_input = tkinter.Entry(self.first_frame, \
                                       width = 15)

        #pack the first frame's widget
        self.F_Name.pack(side='left')
        self.F_Name_input.pack(side='left')

        #create the widgets to the second frame=====================================================
        self.L_Name = tkinter.Label(self.second_frame, \
                                          text = "Enter Last Name:")
        self.L_Name_input = tkinter.Entry(self.second_frame, \
                                       width = 15)

        #pack the second frame's widget
        self.L_Name.pack(side='left')
        self.L_Name_input.pack(side='left')

        #create the widgets to the third frame=====================================================
        self.Age = tkinter.Label(self.third_frame, \
                                          text = "Enter Age:")
        self.Age_input = tkinter.Entry(self.third_frame, \
                                       width = 10)

        #pack the third frame's widget
        self.Age.pack(side='left')
        self.Age_input.pack(side='left')

        #create the widgets to the fourth frame=====================================================
        self.Height = tkinter.Label(self.fourth_frame, \
                                          text = "Enter Height:")
        self.Height_input = tkinter.Entry(self.fourth_frame, \
                                       width = 5)
        self.Height_input_cm = tkinter.Entry(self.fourth_frame, \
                                       width = 5)

        #pack the fourth frame's widget
        self.Height.pack(side='left')
        self.Height_input.pack(side='left')
        self.Height_input_cm.pack(side='right')

        #create the widgets to the fifth frame=====================================================
        self.Weight = tkinter.Label(self.fifth_frame, \
                                          text = "Enter Weight:")
        self.Weight_input = tkinter.Entry(self.fifth_frame, \
                                       width = 10)

        #pack the fifth frame's widget
        self.Weight.pack(side='left')
        self.Weight_input.pack(side='left')

        #create radio buttons======================================================================
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        self.rb1 = tkinter.Radiobutton(self.sixth_frame, \
                                       text='Caucasian', variable=self.radio_var, \
                                       value=1)
        self.rb2 = tkinter.Radiobutton(self.sixth_frame, \
                                       text='African-American', variable=self.radio_var, \
                                       value=2)
        self.rb3 = tkinter.Radiobutton(self.sixth_frame, \
                                       text='Hispanic / Latino', variable=self.radio_var, \
                                       value=3)
        self.rb4 = tkinter.Radiobutton(self.sixth_frame, \
                                       text='Asian / Eastern', variable=self.radio_var, \
                                       value=4)
        self.rb5 = tkinter.Radiobutton(self.sixth_frame, \
                                       text='Other', variable=self.radio_var, \
                                       value=5)


        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.rb4.pack()
        self.rb5.pack()

        #create the widgets for the buttons frame===============================================
        self.calc_buttom = tkinter.Button(self.buttons, \
                                          text = 'Complete', \
                                          command = self.show)
        self.quit_buttom = tkinter.Button(self.buttons, \
                                          text = 'Exit', \
                                          command = self.main_window.destroy)

        #pack the bottom
        self.calc_buttom.pack(side='left')
        self.quit_buttom.pack(side='left')

        #pack the frames---------------------------------------------------------------------------
        self.title_frame.pack()
        self.first_frame.pack()
        self.second_frame.pack()
        self.third_frame.pack()
        self.fourth_frame.pack()
        self.fifth_frame.pack()
        self.sixth_frame.pack()
        self.buttons.pack()

        #enter the tkinter main loop
        tkinter.mainloop()

    #the convert method is a callback function for the calculate buttom
    def show(self):
        fname = self.F_Name_input.get()
        lname = self.L_Name_input.get()
        age = int(self.Age_input.get())
        height = int(self.Height_input.get())
        height_2 = int(self.Height_input_cm.get())
        weight = int(self.Weight_input.get())
        radio = (self.radio_var.get())

        #creating the 'race' variable
        race=0
        #if-elif \assigning the 'race' variable based on the selected radio button
        if radio == 1:
            race='Caucasian'
        elif radio  == 2:
            race="African-American"
        elif radio == 3:
            race='Hispanic / Latino'
        elif radio == 4:
            race='Asian / Eastern'
        elif radio == 5:
            race='Other / Mix-Race'



        tkinter.messagebox.showinfo(fname+' '+lname+' Information', \
                                    'First Name:   '+ fname +\
                                    '\nLast Name:    '+ lname +\
                                    '\nAge:  '+ str(age) +\
                                    '\nHeight:   '+ str(height) + "'" + str(height_2) +\
                                    '\nWeight:   '+ str(weight) +\
                                    '\nRace:  '+ race)

#create an instance of the Cel_to_Fahr class
BIO = Bio_info_GUI()