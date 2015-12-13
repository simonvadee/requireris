#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from tkinter import *
from tkinter import messagebox

class reqGUI(object):
    """
    """

    def __init__(self, manager):
        self.manager = manager
        self.wrongpassword = 0
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
        
    def closePopup(self):
        self.popup.destroy()

    def refreshOTP(self):
        self.code.set(self.manager.get())
        
    def initLogView(self):
        self.wrongpassword = 0
        for child in self.window.winfo_children():
            child.destroy()
        frameGenOTP = Frame(self.window, borderwidth = 0, relief = GROOVE)
        frameGenOTP.pack(side = RIGHT, padx = 20, pady = 50)
        frameBaseOTP = Frame(self.window, borderwidth = 0, relief = GROOVE)
        frameBaseOTP.pack(side = BOTTOM, padx = 0, pady = 0)
        createNewAccButton = Button(frameGenOTP, text = "Create new account", command = self.initCreateAccView)
        createNewAccButton.pack()

        if self.manager.otp != None:
            refreshButton = Button(frameBaseOTP, text = "Refresh", command = self.refreshOTP)
            self.code = StringVar()
            self.code.set(self.manager.get())
            self.OTPlabel = Label(frameBaseOTP, textvariable = self.code)
            refreshButton.pack()
            self.OTPlabel.pack()
            
        frameAccounts = Frame(self.window, borderwidth = 0, relief = GROOVE)
        frameAccounts.pack(side = LEFT, padx = 20, pady = 20)

        accountsField = Label(frameAccounts, text = "Account list :")
        accountsField.pack()
        
        self.accountList = self.manager.listAccounts()

        for account in self.accountList:
            b = Button(frameAccounts, text = account, command = lambda acc=account: modifyDelete(acc))
            b.pack()
        
        def modifyDelete(accountName):
            def execModifyButton(account):
                for child in self.popup.winfo_children():
                    child.destroy()
                self.currAccount = accountName
                frameField = Frame(self.popup, borderwidth = 0, relief = GROOVE)
                frameField.pack(side = LEFT, padx = 0, pady = 20)
                passLabel = Label(frameField, text = "Password")
                passLabel.pack()
                seedLabel = Label(frameField, text = "Seed (optionnal)")
                seedLabel.pack()
                framePassword = Frame(self.popup, borderwidth = 0, relief = GROOVE)
                framePassword.pack(side = RIGHT, padx = 5, pady = 20)
                self.passEntry = Entry(framePassword, relief = GROOVE, show = "*")
                self.passEntry.pack()
                self.seedEntry = Entry(framePassword, relief = GROOVE)
                self.seedEntry.pack()
                frameSubmit = Frame(self.popup, borderwidth = 0, relief = GROOVE)
                frameSubmit.pack(side = BOTTOM)
                submitButton = Button(frameSubmit, text = "Submit",  borderwidth = 1, relief = GROOVE, command = self.genOTPView)
                submitButton.pack()
                
                
            def execDeleteButton(account):
                if messagebox.askyesno('Delete', 'Are you sure you want to delete this account ?'):
                    self.manager.deleteAccount(account)
                    self.popup.destroy()
                    self.initLogView()
                
            def execConnectButton(account):
                    
                for child in self.popup.winfo_children():
                    child.destroy()
                self.currAccount = accountName

                frameField = Frame(self.popup, borderwidth = 0, relief = GROOVE)
                frameField.pack(side = LEFT, padx = 0, pady = 20)
                passLabel = Label(frameField, text = "Password")
                passLabel.pack()
                
                frameInfo = Frame(self.popup, borderwidth = 0, relief = GROOVE)
                frameInfo.pack(side = LEFT, padx = 0, expand = True)
                
                frameFields = Frame(self.popup, borderwidth = 0, relief = GROOVE)
                frameFields.pack(side = RIGHT, padx = 10, pady = 30)
                
                self.passEntry = Entry(frameFields, relief = GROOVE, show = "*")
                self.passEntry.pack()
                
                frameSubmit = Frame(self.popup, borderwidth = 0, relief = GROOVE)
                frameSubmit.pack(side = BOTTOM)
                submitButton = Button(frameSubmit, text = "Submit", command = self.openSession)
                submitButton.pack()
                
            self.popup = Tk()
            self.popup.geometry("400x300")
            self.popup.wm_title("Requireris")
            B1 = Button(self.popup, text = "Update seed", command = lambda account=accountName: execModifyButton(account))
            B1.pack()
            B2 = Button(self.popup, text = "Delete", command = lambda account=accountName: execDeleteButton(account))
            B2.pack()
            B3 = Button(self.popup, text = "Connect", command = lambda account=accountName: execConnectButton(account))
            B3.pack()
            self.popup.mainloop()

    def genOTPView(self):
        if not self.manager.openExistingSession(self.currAccount,
                                                   self.passEntry.get()):
            if self.wrongpassword == 0:
                errorLabel = Label(self.popup, text = "WRONG PASSWORD", fg = "red")
                errorLabel.pack();
                self.wrongpassword = 1
            pass
        else:
            self.wrongpassword = 0
            self.currPassword = self.passEntry.get()
            self.currSeed = self.seedEntry.get()
            for child in self.popup.winfo_children():
                child.destroy()
            self.otp = self.manager.updateKey(self.currAccount, self.currPassword, self.currSeed)
            frameNewSeed = Frame(self.popup, borderwidth = 0, relief = GROOVE)
            frameNewSeed.pack(padx = 40, pady = 40)
            self.popup.destroy()
            self.initLogView()

    def updateOTP(self):
        self.otp = self.manager.updateKey(self.currAccount, self.currPassword, self.currSeed)
        
    def createNewAcc(self):
        if self.nameAccEntry.get() != "" and self.passEntry.get() != "" and self.confirmPassEntry.get() != "":
            if not self.manager.createNewSession(self.nameAccEntry.get(),
                                                self.passEntry.get(),
                                                self.confirmPassEntry.get(),
                                                self.seedEntry.get()):
                if self.wrongpassword == 0:
                    errorLabel = Label(self.window, text = "WRONG PASSWORD OR ALREADY SIGNED IN", fg = "red")
                    errorLabel.pack();
                    self.wrongpassword = 1
                pass
            else:
                self.initLogView()

    def openSession(self):
        if self.currAccount != "" and self.passEntry.get() != "":
            if not self.manager.openExistingSession(self.currAccount,
                                                   self.passEntry.get()):
                if self.wrongpassword == 0:
                    errorLabel = Label(window, text = "WRONG PASSWORD OR ALREADY SIGNED IN", fg = "red")
                    errorLabel.pack();
                    self.wrongpassword = 1
                pass
            else:
                self.wrongpassword = 0
                self.popup.destroy()
                self.initLogView()
