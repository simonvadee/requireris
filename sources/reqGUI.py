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

        frameInfo = Frame(self.window,borderwidth = 0, relief = GROOVE)
        frameInfo.pack(side = LEFT, padx = 0, expand = True)

        accNameLabel = Label(frameInfo, text = "Name Account")
        accNameLabel.pack()
        accPassLabel = Label(frameInfo, text = "Password")
        accPassLabel.pack()
        accConfirmPassLabel = Label(frameInfo, text = "Confirm Password")
        accConfirmPassLabel.pack()
        seedLabel = Label(frameInfo, text = "Enter seed (optional)")
        seedLabel.pack()

        frameFields = Frame(self.window, borderwidth = 0, relief = GROOVE)
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

        frameBack = Frame(self.window, borderwidth = 0, relief = GROOVE)
        frameBack.pack(side = TOP, padx = 10)
            
        previousButton = Button(frameBack, text = "back", command = self.initLogView)
        previousButton.pack(fill = X)

        frameInfo = Frame(self.window,borderwidth = 1, relief = GROOVE)
        frameInfo.pack(side = LEFT, padx = 0, expand = True)

        accNameLabel = Label(frameInfo, text = "Name Account")
        accNameLabel.pack()
        accPassLabel = Label(frameInfo, text = "Password")
        accPassLabel.pack()

        frameFields = Frame(self.window, borderwidth = 0, relief = GROOVE)
        frameFields.pack(side = RIGHT, padx = 10, pady = 30)

        self.nameAccEntry = Entry(frameFields, relief = GROOVE)
        self.nameAccEntry.pack()
        self.passEntry = Entry(frameFields, relief = GROOVE, show = "*")
        self.passEntry.pack()

        frameSubmit = Frame(self.window, borderwidth = 0, relief = GROOVE)
        frameSubmit.pack(side = BOTTOM)
        
        submitButton = Button(frameSubmit, text = "Submit", command = self.openSession)
        submitButton.pack()
        
    def closePopup(self):
        self.popup.destroy()
            
    def genNewSeedView(self):
        for child in self.popup.winfo_children():
            child.destroy()
        frameNewSeed = Frame(self.popup, borderwidth = 0, relief = GROOVE)
        frameNewSeed.pack(padx = 40, pady = 40)
        newSeedEntry = Entry(frameNewSeed, text = "gen new seed here", state = 'normal')
        newSeedEntry.insert(0, "gen new seed here")
        newSeedEntry.configure(state = 'disabled')
        newSeedEntry.pack()
#ICI
        doneButton = Button(self.popup, text = "done", borderwidth = 1, relief = GROOVE, command = self.closePopup)
        doneButton.pack()

    def initLogView(self):
        for child in self.window.winfo_children():
            child.destroy()
        frameGenOTP = Frame(self.window, borderwidth = 0, relief = GROOVE)
        frameGenOTP.pack(side = RIGHT, padx = 20, pady = 50)
#        frameGenOTP.pack(side = LEFT, padx = 20, pady = 50)
        genOTPButton = Button(frameGenOTP, text = "Create new account", command = self.initCreateAccView)
        genOTPButton.pack()

#        frameUseExistingAcc = Frame(self.window, borderwidth = 0, relief = GROOVE)
 #       frameUseExistingAcc.pack(side = RIGHT, padx = 10, pady = 50)
        useExistingAccButton = Button(frameGenOTP, text = "Use existing account", command = self.initChooseAccView)

        frameAccounts = Frame(self.window, borderwidth = 0, relief = GROOVE)
        frameAccounts.pack(side = LEFT, padx = 20, pady = 20)

        accountsField = Label(frameAccounts, text = "Account list :")
        accountsField.pack()
        
        useExistingAccButton.pack()
        self.accountList = self.manager.listAccounts()
        print(self.accountList)
        
        def modifyDelete(accountName):
            def execModifyButton(account):
                #self.manager.updateKey(account)
                for child in self.popup.winfo_children():
                    child.destroy()
                frameField = Frame(self.popup, borderwidth = 0, relief = GROOVE)
                frameField.pack(side = LEFT, padx = 20, pady = 20)
                passLabel = Label(frameField, text = "Password")
                passLabel.pack()

                framePassword = Frame(self.popup, borderwidth = 0, relief = GROOVE)
                framePassword.pack(side = RIGHT, padx = 20, pady = 20)
                passEntry = Entry(framePassword, relief = GROOVE)
                passEntry.pack()
                submitButton = Button(framePassword, text = "submit",  borderwidth = 1, relief = GROOVE, command = self.genNewSeedView)
                submitButton.pack()
                #verifier que le mot de passe est bon
                
                
            def excDeleteButton(account):
                self.manager.updateKey(account)
                self.initLogView()

            print("account name = ")
            print(accountName)
            self.popup = Tk()
            self.popup.geometry("200x200")
            self.popup.wm_title("Requireris")
            B1 = Button(self.popup, text = "Modify", command = lambda account=accountName: execModifyButton(account))
            B1.pack()
            B2 = Button(self.popup, text = "Delete", command = lambda account=accountName: execDeleteButton(account))
            B2.pack()
            self.popup.mainloop()
        for account in self.accountList:
            b = Button(frameAccounts, text = account, command = lambda acc=account: modifyDelete(acc))
            print(account)
            b.pack()

    def modify(self):
      #  self.manager.updateKey()
        print("okok")
        
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
