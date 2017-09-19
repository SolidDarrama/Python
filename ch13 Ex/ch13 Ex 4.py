#Jose Guadarrama
#11/17/2014

import tkinter
import tkinter.messagebox

class Cel_to_Fahr_GUI:
    def __init__(self):

        #Create main window
        self.main_window = tkinter.Tk()

        #create two frames to group widgets
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #create the widgets to the top frame
        self.prompt_label = tkinter.Label(self.top_frame, \
                                          text = "Enter Celsius to convert:")
        self.cel_entry = tkinter.Entry(self.top_frame, \
                                       width = 10)

        #pack the top frame's widget
        self.prompt_label.pack(side='left')
        self.cel_entry.pack(side='left')

        #create the bottom widgets for the bottom frame
        self.calc_buttom = tkinter.Button(self.bottom_frame, \
                                          text = 'Convert', \
                                          command = self.convert)
        self.quit_buttom = tkinter.Button(self.bottom_frame, \
                                          text = 'Quit', \
                                          command = self.main_window.destroy)

        #pack the bottom
        self.calc_buttom.pack(side='left')
        self.quit_buttom.pack(side='left')

        #pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        #enter the tkinter main loop
        tkinter.mainloop()

    #the convert method is a callback function for the calculate buttom

    def convert(self):
        #get the value entered by the user into the cel_entry widget
        cel = float(self.cel_entry.get())
        fahr = ((9/5) * cel) + 32

        #display the results in a ino dialog box
        tkinter.messagebox.showinfo('Results', \
                                    str(cel) + ' Celsius is equal to ' + \
                                    str(fahr) + ' Fahrenheit')

#create an instance of the Cel_to_Fahr class
cel_conv = Cel_to_Fahr_GUI()