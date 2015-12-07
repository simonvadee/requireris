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

        frameBack = Frame(self.window, borderwidth = 1, relief = GROOVE)
        frameBack.pack(side = TOP, padx = 10)
            
        previousButton = Button(frameBack, text = "back")
        previousButton.pack(fill = X)

        frameInfo = Frame(self.window,borderwidth = 1, relief = GROOVE)
        frameInfo.pack(side = LEFT, padx = 0, expand = True)

        accNameLabel = Label(frameInfo, text = "Name Account")
        accNameLabel.pack()
        accPassLabel = Label(frameInfo, text = "Password")
        accPassLabel.pack()
        accConfirmPassLabel = Label(frameInfo, text = "Confirm Password")
        accConfirmPassLabel.pack()

        frameFields = Frame(self.window, borderwidth = 1, relief = GROOVE)
        frameFields.pack(side = RIGHT, padx = 10, pady = 30)

        self.nameAccEntry = Entry(frameFields, relief = GROOVE)
        self.nameAccEntry.pack()
        self.passEntry = Entry(frameFields, relief = GROOVE, show = "*")
        self.passEntry.pack()
        self.confirmPassEntry = Entry(frameFields, relief = GROOVE, show = "*")
        self.confirmPassEntry.pack()

        frameSubmit = Frame(self.window, borderwidth = 0, relief = GROOVE)
        frameSubmit.pack(side = BOTTOM)
        
        submitButton = Button(frameSubmit, text = "Submit", command = self.createNewAcc)
        submitButton.pack()

    def initChooseAccView(self):
        print("Choose Account View")
        
    def initLogView(self):
        for child in self.window.winfo_children():
            child.destroy()
        frameGenOTP = Frame(self.window, borderwidth = 0, relief = GROOVE)
        frameGenOTP.pack(side = LEFT, padx = 20, pady = 50)
        genOTPButton = Button(frameGenOTP, text = "Create new account", command = self.initCreateAccView)
        genOTPButton.pack()

        frameUseExistingAcc = Frame(self.window, borderwidth = 0, relief = GROOVE)
        frameUseExistingAcc.pack(side = RIGHT, padx = 10, pady = 50)
        useExistingAccButton = Button(frameUseExistingAcc, text = "Use existing account", command = self.initChooseAccView)
        useExistingAccButton.pack()

    def createNewAcc(self):
        if self.nameAccEntry.get() != "" and self.passEntry.get() != "" and self.confirmPassEntry.get() != "":
            print("nameAcc = " + self.nameAccEntry.get() + " password : " + self.passEntry.get())
