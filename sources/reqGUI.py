#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from tkinter import * 

class reqGUI(object):
    """
    """

    def __init__(self):
        self.window = Tk()
        self.window.title("Requireris")
        self.window.geometry("350x200")
        self.initLogView()
        self.window.mainloop()


    def initCreateAccView(self):
        for child in self.window.winfo_children():
            child.destroy()

        frameInfo = Frame(self.window,borderwidth = 0, relief = GROOVE)
        frameInfo.pack(side = LEFT, padx = 10, pady = 30)

        accNameLabel = Label(frameInfo, text = "Name Account")
        accNameLabel.pack()
        accPassLabel = Label(frameInfo, text = "Password")
        accPassLabel.pack()
        accConfirmPassLabel = Label(frameInfo, text = "Confirm Password")
        accConfirmPassLabel.pack()

        frameFields = Frame(self.window, borderwidth = 0, relief = GROOVE)
        frameFields.pack(side = RIGHT, padx = 10, pady = 30)

        nameAccEntry = Entry(frameFields, relief = GROOVE)
        nameAccEntry.pack()
        passEntry = Entry(frameFields, relief = GROOVE, show = "*")
        passEntry.pack()
        confirmPassEntry = Entry(frameFields, relief = GROOVE, show = "*")
        confirmPassEntry.pack()
        
    def initLogView(self):
        frameGenOTP = Frame(self.window, borderwidth = 0, relief = GROOVE)
        frameGenOTP.pack(side = LEFT, padx = 20, pady = 50)
        genOTPButton = Button(frameGenOTP, text = "Create new account", command = self.initCreateAccView)
        genOTPButton.pack()

        frameUseExistingAcc = Frame(self.window, borderwidth = 0, relief = GROOVE)
        frameUseExistingAcc.pack(side = RIGHT, padx = 10, pady = 50)
        useExistingAccButton = Button(frameUseExistingAcc, text = "Use existing account", fg = "black")
        useExistingAccButton.pack()
