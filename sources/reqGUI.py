#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from tkinter import * 

class reqGUI(object):
    """
    """

    def __init__(self, manager):
        self.manager = manager
        self.window = Tk()
        self.window.title("Requireris")
        self.window.geometry("590x420")
        self.initLogView()
        self.window.mainloop()


    def initCreateAccView(self):
        for child in self.window.winfo_children():
            child.destroy()

        frameBack = Frame(self.window, borderwidth = 1, relief = GROOVE)
        frameBack.pack(side = TOP, padx = 10)
            
        previousButton = Button(frameBack, text = "back", command = self.initLogView)
        previousButton.pack(fill = X)

        frameInfo = Frame(self.window,borderwidth = 1, relief = GROOVE)
        frameInfo.pack(side = LEFT, padx = 0, expand = True)

        accNameLabel = Label(frameInfo, text = "Name Account")
        accNameLabel.pack()
        accPassLabel = Label(frameInfo, text = "Password")
        accPassLabel.pack()
        accConfirmPassLabel = Label(frameInfo, text = "Confirm Password")
        accConfirmPassLabel.pack()
        seedLabel = Label(frameInfo, text = "Enter seed (optional)")
        seedLabel.pack()

        frameFields = Frame(self.window, borderwidth = 1, relief = GROOVE)
        frameFields.pack(side = RIGHT, padx = 10, pady = 30)

        self.nameAccEntry = Entry(frameFields, relief = GROOVE)
        self.nameAccEntry.pack()
        self.passEntry = Entry(frameFields, relief = GROOVE, show = "*")
        self.passEntry.pack()
        self.confirmPassEntry = Entry(frameFields, relief = GROOVE, show = "*")
        self.confirmPassEntry.pack()
        self.seedEntry = Entry(frameFields, relief = GROOVE)
        self.seedEntry.pack()

        frameSubmit = Frame(self.window, borderwidth = 0, relief = GROOVE)
        frameSubmit.pack(side = BOTTOM)
        
        submitButton = Button(frameSubmit, text = "Submit", command = self.createNewAcc)
        submitButton.pack()

    def initChooseAccView(self):
        for child in self.window.winfo_children():
            child.destroy()

        frameBack = Frame(self.window, borderwidth = 1, relief = GROOVE)
        frameBack.pack(side = TOP, padx = 10)
            
        previousButton = Button(frameBack, text = "back", command = self.initLogView)
        previousButton.pack(fill = X)

        frameInfo = Frame(self.window,borderwidth = 1, relief = GROOVE)
        frameInfo.pack(side = LEFT, padx = 0, expand = True)

        accNameLabel = Label(frameInfo, text = "Name Account")
        accNameLabel.pack()
        accPassLabel = Label(frameInfo, text = "Password")
        accPassLabel.pack()

        frameFields = Frame(self.window, borderwidth = 1, relief = GROOVE)
        frameFields.pack(side = RIGHT, padx = 10, pady = 30)

        self.nameAccEntry = Entry(frameFields, relief = GROOVE)
        self.nameAccEntry.pack()
        self.passEntry = Entry(frameFields, relief = GROOVE, show = "*")
        self.passEntry.pack()

        frameSubmit = Frame(self.window, borderwidth = 0, relief = GROOVE)
        frameSubmit.pack(side = BOTTOM)
        
        submitButton = Button(frameSubmit, text = "Submit", command = self.openSession)
        submitButton.pack()
        
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
            if not self.manager.createNewSession(self.nameAccEntry.get(),
                                                self.passEntry.get(),
                                                self.confirmPassEntry.get(),
                                                self.seedEntry.get()):
                # erreur : mettre le emssage d'erreur approprié
                pass
            else:
                # on est connecté, revenir au menu et afficher le code avec un petit compte à rebourd et réactualiser ?
                print("success !")
                self.initLogView()

    def openSession(self):
        if self.nameAccEntry.get() != "" and self.passEntry.get() != "":
            if not self.manager.openExistingSession(self.nameAccEntry.get(),
                                                   self.passEntry.get()):
                # wrong password, afficher erreur !!
                pass
            else:
                # on est connecté, revenir au menu et afficher le code avec un petit compte à rebourd et réactualiser ?
                print("success !")
                self.initLogView()
