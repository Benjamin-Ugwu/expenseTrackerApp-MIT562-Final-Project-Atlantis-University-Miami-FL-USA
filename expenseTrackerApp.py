"""
    Program: expenseTrackerApp.py
    Author: Benjamin O Ugwu
    Date: 12/10/2019

    A program to help a user track his/her expenses.
    For example, a user will be able to set a budget for any desired expense type called a category, record any expense
    made on a given category and be able to see both the amount already spent ant the amount remaining to be spent on that budget.
    If user records budget for a car=6000USD and user spends 5500USD on the car then, remaining amount is 6000-5500 = 500USD 

    Input:
        Name of expense category. 
        Budget for a given category.

        Expense amount for each expense made
        Comment for each expense made

        Date for each record (will be recorded automatically)

    Processing:
        Create a window where user can select menu items; Create new expenses category, Record Expenses, Track expenses,
        Delete/Edit category, Delete/Edit expenses.

        Create new expenses category: will receive the new category name and budget for recording.
            No two or more categories can have the same name.
            Budget amount must be a number
            
        Record Expenses: will receive the expenses and comment on that expense for recording.
            An expense will be recorded for a chosen expense category
            Expense amount must be a number

        Track expenses: will show at a glance the summary of the categories and total expenses made on them
            budget=budgeted amount for a category
            spent amount= sum of all expenses made on a category
            remaining amount= budget - spent amount
            
        Delete/Edit category: where the user can delete or edit a chosen existing category. deleting a category will delete all expenses recorded for that category also.
            A user will be warned to confirm deletion before deleting a category.

        Delete/Edit expenses: where the user can delete or edit a chosen existing expense. deleting an expense will add the expense amount to the budget for its category
            A user will be warned to confirm deletion before deleting an expense

        Text file will be used for storing and retrieving of data and information
        

    Output:
        Sum of spent amount for each category
        Amount remaining to be spent on each category

        All expenses made and their associated expense categories

"""

# Import any modules needed by program
from breezypythongui import EasyFrame#for the GUI- Graphic User Interface windows used
from tkinter import PhotoImage#for images used
import os#for file path
import datetime#for current date and time

from tkinter import END, NORMAL, DISABLED#for adding items to the list box. 
from tkinter import messagebox#for warning message before a deletion is made


# Process the inputs to produce the results

class expenseTracker(EasyFrame): #expense tracker extends EasyFrame(by lambert), EasyFrame extends tkinter which means, they both can run any method found in tkinter
    """
    The main window/home window with the application menu contents: Create new expenses category, Record Expenses, Track expenses,
    Delete/Edit category, Delete/Edit expenses.
    
    """

    def __init__(self): #runs expenseTracker automatically, self refers to our expensetracker app window
        EasyFrame.__init__(self,width=450,height=600,title="ExpenseTrackerApp")#runs EasyFrame, the current frame we are working on-a grandchild of tkinter
        #EasyFrame.__init__(self,width=1200,height=700,title="ExpenseTracker")#runs EasyFrame, the current frame we are working on-a grandchild of tkinter

        self["background"]="#d6d6d6"       

        #self.setResizable="False"

        #add logo label and image       
        logoLabel=self.addLabel(text="",row=0, column=1,background="#d6d6d6",sticky="NE")
        self.image=PhotoImage(file="logo.gif")
        logoLabel["image"]=self.image

        #add date and time label
        dt=datetime.datetime.now()
        dateTimeLabel=self.addLabel(text="DATE :  "+dt.strftime("%b %d, %Y. "),row=0,column=0,background="#d6d6d6",sticky="W")

        #add app Name label  and image     
        appNameLabel=self.addLabel(text="",row=1,column=0,background="#d6d6d6",sticky="N",columnspan=2)
        self.imageET=PhotoImage(file="expenseTracker.gif")
        appNameLabel["image"]=self.imageET

        #add menu button            
        
        self.addButton(text="--Track Expenses",row=2, column=0,state="normal",command=self.trackExpenses).grid(sticky="N",columnspan=2)
        self.addButton(text="--Record Expenses",row=3, column=0,state="normal",command=self.recordExpenses).grid(sticky="N",columnspan=2)
        self.addButton(text="--Delete/Edit Expenses",row=4, column=0,state="normal",command=self.deleteEditExpense).grid(sticky="N",columnspan=2)
        self.addButton(text="--Delete/Edit Categories",row=5, column=0,state="normal",command=self.deleteEditCategory).grid(sticky="N",columnspan=2)
        self.addButton(text="--Create New Expenses Category",row=6, column=0,state="normal",command=self.newCategory).grid(sticky="N",columnspan=2)

        #add date and time label
        #dt=datetime.datetime.now()
        #dateTimeLabel=self.addLabel(text="Date: "+dt.strftime("%x"),row=3,column=0,background="#d6d6d6",sticky="S")

        #add copyright label and text        
        copyrighLabel=self.addLabel\
        (text="© All Rights Reserved 2019\nBenjamin O Ugwu\nAtlantis University Miami Florida USA\nMIT 562 Final Project, supervised by Marcel Andino (Ph.D.)",\
        background="#d6d6d6",row=7, column=0,sticky="NS",columnspan=2) 

    def newCategory(self):#close the main window and open the newCategory window
        """ a menu option that takes user to the window for creating new category"""
        self.destroy()
        newCategory()  

        #newCategory=self.prompterBox(title="New Category",promptString="Enter the Category Name")
        #self.messageBox(title="New Category",message="Enter the Category Name")

    def recordExpenses(self):#close the main window and open the recordExpenses window
        """ a menu option that takes user to the window to record an expense """
        self.destroy()
        recordExpenses()

    def trackExpenses(self):#close the main window and open the trackExpenses window
        """ a menu option that takes user to the window where expenses can be tracked"""
        self.destroy()
        trackExpenses()

    def deleteEditCategory(self):
        """ a menu option that takes user to the window for deleting or editing an existing category"""
        self.destroy()
        deleteEditCategory()
    
    def deleteEditExpense(self):
        """a menu option that takes user to the window for deleting and editing an existing expense"""
        self.destroy()
        deleteEditExpense()


class newCategory(EasyFrame): #expense tracker extends EasyFrame(by lambert), EasyFrame extends tkinter which means, they both can run any method found in tkinter
    """
        This class creates the window for adding new expenses category. 
    """

    def __init__(self): #runs expenseTracker automatically, self refers to our expensetracker app window
        EasyFrame.__init__(self,title="Adding a New Category & Budget")#runs EasyFrame, the current frame we are working on-a grandchild of tkinter

        self["background"]="#d6d6d6"

        #add logo label and image       
        logoLabel=self.addLabel(text="",row=0, column=0,background="#d6d6d6",sticky="NE")
        self.image=PhotoImage(file="logo.gif")
        logoLabel["image"]=self.image

        #receive name and budget
        newCategoryName=self.addLabel(text="Enter Name of a New Category: ",row=1, column=0,background="#d6d6d6",sticky="S")
        self.name=self.addTextField(text="Category",row=2,column=0)
        self.name.grid(sticky="N")
        global NAME

        newCategoryBudget=self.addLabel(text="Enter Budget for this Category: ",row=3, column=0,background="#d6d6d6",sticky="S")
        self.budget=self.addTextField(text="0.0",row=4,column=0)
        self.budget.grid(sticky="N")
        global BUDGET

        self.addButton(text="Submit",row=5, column=0,command=self.submitSuccesful)
        self.addButton(text="Home",row=6, column=0,command=self.goHome)

    def goHome(self):
        """ returns user to the home window when home button is clicked"""
        self.destroy()
        expenseTracker()

    def submitSuccesful(self):
        """responds to pressing of the submit button for adding a new category"""

        NAME=self.name.getText()
        n=NAME.split(" ")
        NAME="&&&".join(n)#store words with spaces together by representing spaces with &&&

        #check that category name does not already exist in file
        f=open("categoryBudget.txt","r")
        destroy=0
        while True:
            categoryCheck=f.readline()  
            if categoryCheck=="":#if end of line or file empty respectively
                break
            
            else:            
                if categoryCheck.split()[1]==NAME:
                    self.messageBox(title="ATTENTION!",message="Category Name Already Exists!")
                    destroy=1#to know when to stop processing since execution will continue in the background even after newCategory() below
                    #self.destroy()                    
                    #newCategory()
                    
        f.close()#close the file ready for next operation on it

        if destroy==0:#destroy=1 means we dont need further processing      
            BUDGET=self.budget.getText()
            
            #check that budget is a number value        
            try:
                int(BUDGET)
                a=True
            except:
                a=False 

            try:            
                float(BUDGET)
                b=True
            except:
                b=False    
            
            #print(a,b)
            destroy2=False
            
            if a==False and b==False:
                self.messageBox(title="Error!",message="Your Budget should be a number!")
                destroy2=True
                #self.destroy() destroying this window will erase all the already entered data, both valid and invalid ones which is not a good idea                
                #newCategory()   
            else:
                x=1#nothing significant                         

            if destroy2==False:
                #find the last serial number in file
                f=open("categoryBudget.txt","r")
                contents=f.read()        
                if contents=="":#if file is empty meaning the first item we will add
                    sn=1
                else:
                    contentsSplit=contents.split()#return all content in a list
                    lastSN=contentsSplit[-4]#take the last serial number, position -4
                    sn=int(lastSN)+1#add 1 to the last serial number to get the next one

                f.close()#close the read file to make it ready to open and appending below
                
                #write name and budget to file with date and serial number     
                DATE=str(datetime.datetime.now().strftime("%x_%H:%M:%S"))
                SN=str(sn)

                f=open("categoryBudget.txt","a")
                f.write(SN+"\t"+NAME+"\t"+BUDGET+"\t"+DATE+"\n")
                f.close()

                #show a succesful record made message
                self.messageBox(title="Submitted",message="Your New Category & Budget were added successfully!")
                self.destroy()
                newCategory()    


class recordExpenses(EasyFrame): #expense tracker extends EasyFrame(by lambert), EasyFrame extends tkinter which means, they both can run any method found in tkinter
    """
        The window for recording an expense made by the user
    """

    def __init__(self): #runs expenseTracker automatically, self refers to our expensetracker app window
        EasyFrame.__init__(self,width=450,height=600,title="Recording Expenses")#runs EasyFrame, the current frame we are working on-a grandchild of tkinter

        self["background"]="#d6d6d6"

        #add logo label and image       
        logoLabel=self.addLabel(text="",row=0, column=0,background="#d6d6d6",sticky="NE")
        self.image=PhotoImage(file="logo.gif")
        logoLabel["image"]=self.image

        f=open("categoryBudget.txt","r")
        #check if the file is empty        
        contents=f.read()        
        if contents=="":#if the file is empty            
            self.messageBox(title="Error!",message="Please add an Expense Category first")
            self.destroy()
            expenseTracker()
            
        else:  
            recordExpensesLabel=self.addLabel(text="Select Expense Category: ",row=1, column=0,background="#d6d6d6",sticky="N")
            #ADD ENTERED CATEGORY LIST HERE

            #self.addListbox(row=2,column=0,rowspan = 1,listItemSelected = self.listItemSelected).grid(padx=500)
            self.listBox = self.addListbox(row = 2, column = 0)#add an empty list box
            #self.listBox.grid(padx=400)#position the list box with padx=500

            #find the recorded categories from file       
            global noCategoryFound
            noCategoryFound=False
            
            f.close()
            f=open("categoryBudget.txt","r")
            while True:
                contents=f.readline()
                if contents=="\n" or contents=="":#readline doesnt recognize \n so it needs '' to stop
                    break
                else:
                    contentsCategory=contents.split()[1]#get the category
                    c=contentsCategory.split("&&&")#remove the &&& used as spaces
                    contentsCategory=" ".join(c)

                    #add categories into the list box from already recorded categories
                    self.listBox.insert(END,contentsCategory)#add the category to GUI list box
                    self.listBox.setSelectedIndex(0)#first item will always be selected by default until you select another one

            #spent amount label and text field
            recordExpensesLabel=self.addLabel(text="Enter Amount Spent: ",row=3, column=0,background="#d6d6d6",sticky="S")
            self.spentAmount=self.addTextField(text="0.0",row=4,column=0)
            self.spentAmount.grid(sticky="N")
            global AMOUNT

            #comment label and text area field
            recordExpensesLabel=self.addLabel(text="Comment: ",row=5, column=0,background="#d6d6d6",sticky="S")
            self.comment=self.addTextArea(text="Comment",row=6,column=0,width=10,height=10)
            #self.comment.grid(padx=400)
            global COMMENT        


            self.addButton(text="Submit",row=7, column=0,command=self.submitSuccesful)
            self.addButton(text="Home",row=8, column=0,command=self.goHome)

    def goHome(self):
        """ Takes user to the home window on pressing home button"""
        self.destroy()
        expenseTracker()

    def submitSuccesful(self):#actions carried out when the submit button is pressed        
            """responds to pressing of the submit button for adding a new expense"""
            AMOUNT=self.spentAmount.getText()

            #check that AMOUNT is a number value
            try:
                int(AMOUNT)
                a=True
            except:
                a=False

            try:            
                float(AMOUNT)
                b=True
            except:
                b=False    
        
            #print(a,b)

            if a==False and b==False:
                self.messageBox(title="Error!",message="Your Expense Amount should be a number!")
                #self.destroy() destroying this window will erase all the already entered data, both valid and invalid ones which is not a good idea 
                #recordExpenses()
            else:
                COMMENT=self.comment.getText()#get the comment
                c=COMMENT.split(" ")
                COMMENT="&&&".join(c)#store words with spaces together by representing spaces with &&&
                         
                CATEGORY=self.listBox.getSelectedItem()#get the selected category from the list box
                c=CATEGORY.split(" ")
                CATEGORY="&&&".join(c)#put &&& into the spaces before storage

                DATE=str(datetime.datetime.now().strftime("%x_%H:%M:%S"))#get the current date              
                
                #find the last serial number in file
                f=open("individualExpense.txt","r")
                contents=f.read()        
                if contents=="":
                    sn=1
                else:
                    contentsSplit=contents.split()#return all content in a list
                    lastSN=contentsSplit[-5]#take the last serial number, position -5
                    sn=int(lastSN)+1#add 1 to the last serial number to get the next one

                f.close()#close the read file to make it ready to open and appending below

                #write expense details to individualExpense.txt file        
                SN=str(sn)

                #copy all file content 
                f=open("individualExpense.txt","r")
                allC=f.read()
                allC2=allC.rstrip("''")#remove the '' at end
                allC3=allC2+SN+"\t"+CATEGORY+"\t"+AMOUNT+"\t"+DATE+"\t"+COMMENT
                
                               
                f=open("individualExpense.txt","w")
                f.write(allC3)
                f.close()
                
                self.messageBox(title="Submitted",message="Your Expense was added successfully!")
                self.destroy()
                recordExpenses()                


class trackExpenses(EasyFrame): #expense tracker extends EasyFrame(by lambert), EasyFrame extends tkinter which means, they both can run any method found in tkinter

    """
        The window for tracking expenses, shows summary of expenses, including spent amount and remaining amount for each category and detail of each expense recorded
    """

    def __init__(self): #runs expenseTracker automatically, self refers to our expensetracker app window
        EasyFrame.__init__(self,width=960,height=540,title="Tracking Your Expenses")#runs EasyFrame, the current frame we are working on-a grandchild of tkinter

        self["background"]="#d6d6d6"

        #add logo label and image       
        logoLabel=self.addLabel(text="",row=0, column=0,background="#d6d6d6",sticky="NE")
        self.image=PhotoImage(file="logo.gif")
        logoLabel["image"]=self.image

        #add app Name label  and image     
        appNameLabel=self.addLabel(text="",row=0,column=0,background="#d6d6d6",sticky="S")
        self.imageET=PhotoImage(file="trackExpenses.gif")
        appNameLabel["image"]=self.imageET


        #Populate expenseTracker.txt file with data from other 2 files
        """
        open categoryBudget file
        copy the first line and get the category
        open individual expenses
        get the sum of all expenses belonging to this category, this is the total expenses
        minus the total expenses from the budget, this is the remaining amount
        
        """     
        fc=open("categoryBudget.txt","r")#open once for reading line by line        
        fe=open("expenseTracker.txt","w")#open once for writing line by line
        fi=open("individualExpense.txt","r")

        #check if the file is empty        
        contents=fi.read()        
        if contents=="":#if the file is empty            
            self.messageBox(title="Error!",message="No Expenses Yet to track")
            self.destroy()
            expenseTracker()
            
        else:                
            
            while True:                
                line=fc.readline()#read categoryBudget.txt lines               
                if line=="":
                    break                
                else:                    
                    sn=line.split()[0]
                    category=line.split()[1]
                    budget=float(line.split()[2])
                    date=line.split()[3]
                    #print(category,budget)
                    
                    categorySpentSum=0.0#to sum the expenses for each category                    

                    fi=open("individualExpense.txt","r")
                    while True:                        
                        eachLine=fi.readline()#read individualExpense.txt lines
                        #print("\\"+eachLine)
                        if eachLine=="":
                            break
                        else:                            
                            #print(eachLine)
                            if eachLine.split()[1]==category:
                                print("yes")
                                categorySpentSum+=float(eachLine.split()[2])

                    categoryRemaining=budget-categorySpentSum
                    #print(categorySpentSum,categoryRemaining)      
                                
                    eachSummary="%-6s%-22s%-22s%-22s%-22s%-22s\n"%(sn,category,str(budget),date,str(categorySpentSum),str(categoryRemaining))
                    fe.write(eachSummary)#write to expenseTracker.txt
                            
            fe.close()

            #output summary and individual expenses
            #heading1="%9s%14s%12s%16s%18s%22s\n"%("S/N","Category","Budget","Date Added","Amount Spent","Amount Remaining")
            heading1="%-6s%-22s%-22s%-22s%-22s%-22s\n\n"%("S/N","Category","Budget($)","Date & Time Added","Amount Spent($)","Amount Remaining($)")
            f=open("expenseTracker.txt","r")

            record=""        
            while True:
                expenseRecord=f.readline()
                print(expenseRecord)
                if expenseRecord=="":
                    break
                else:
                    expenseRecordList=expenseRecord.split()
                    #print( expenseRecordList)
                    #for eachEntry in range(len(expenseRecordList)):
                    record+="%-6s"%expenseRecordList[0]

                    #replace the &&& in category name with spaces for showing it to the user
                    eR=expenseRecordList[1].split("&&&")
                    category=" ".join(eR)                
                    record+="%-22s"%category
                    record+="%-22s"%expenseRecordList[2]
                    record+="%-22s"%expenseRecordList[3]
                    record+="%-22s"%expenseRecordList[4]
                    record+="%-22s"%expenseRecordList[5]
                    record+="\n"

            heading2="%-6s%-22s%-22s%-29s%-50s\n\n"%("S/N","Category","Expense Amount($)","Date & Time Recorded","Comment")
            f=open("individualExpense.txt","r")

            recordDetail=""
            
            while True:
                expenseDetail=f.readline()
                print(expenseDetail)

                if expenseDetail=="":                
                    break                
                else:
                    expenseDetailList=expenseDetail.split()
                    #print(expenseDetailList)
                    #for eachEntry in range(len(expenseRecordList)):
                    recordDetail+="%-6s"%expenseDetailList[0]

                    #replace the &&& in category name with spaces for showing it to the user
                    eR=expenseDetailList[1].split("&&&")
                    category=" ".join(eR)
                    
                    recordDetail+="%-22s"%category
                    recordDetail+="%-22s"%expenseDetailList[2]
                    recordDetail+="%-29s"%expenseDetailList[3]

                    #replace the &&& in comment with spaces for showing it to the user
                    cm=expenseDetailList[4].split("&&&")
                    comment=" ".join(cm)
                    
                    recordDetail+="%-50s"%comment               
                    recordDetail+="\n"            
            
            self.outputArea=self.addTextArea(text="",row=2,column=0,width=30,height=20)
            #self.outputArea.grid(padx=100)
            self.outputArea["state"]="normal"
            #print(heading1)
            self.outputArea.setText("SUMMARY OF EXPENSES:\n\n"+heading1+record+"\n\n\nINDIVIDUAL EXPENSES:\n\n"+heading2+recordDetail)
            #self.outputArea.setText("\n\n\n"+heading2+recordDetail)
            self.outputArea["state"]="disabled"#makes the output uneditable

            self.addButton(text="Home",row=3, column=0,command=self.goHome)

    def goHome(self):
        """ Takes user to the home window on pressing the home button"""
        self.destroy()
        expenseTracker()

class deleteEditCategory(EasyFrame): #expense tracker extends EasyFrame(by lambert), EasyFrame extends tkinter which means, they both can run any method found in tkinter
    """the window for deleting or editing an existing and selected category"""

    def __init__(self): #runs expenseTracker automatically, self refers to our expensetracker app window
        EasyFrame.__init__(self,width=450,height=600,title="Delete/Edit Categories")#runs EasyFrame, the current frame we are working on-a grandchild of tkinter

        self["background"]="#d6d6d6"

        #add logo label and image       
        logoLabel=self.addLabel(text="",row=0, column=0,background="#d6d6d6",sticky="NE")
        self.image=PhotoImage(file="logo.gif")
        logoLabel["image"]=self.image         

        #check if the file is empty
        f=open("categoryBudget.txt","r")
        contents=f.read()        
        if contents=="":#if the file is empty            
            self.messageBox(title="Error!",message="No Categories found to Delete/Edit")
            self.destroy()
            expenseTracker()   

        else:

            #populate categories from file
            categoryLabel=self.addLabel(text="Select Expense Category to Edit or Delete: ",row=1, column=0,background="#d6d6d6",sticky="S")
            
            self.listBox = self.addListbox(row = 2, column = 0,listItemSelected = self.setFields)#add an empty list box
            #self.listBox.grid(padx=200)#position the list box with padx=200
            
            #f.close()
            f=open("categoryBudget.txt","r")
            firstCategoryName=contents.split()[1]
            fc=firstCategoryName.split("&&&")
            firstCategoryName=" ".join(fc)
            
            firstCategoryBudget=contents.split()[2]
            f=open("categoryBudget.txt","r")
           
            while True:
                contents=f.readline()
                if contents=="":#read line doesnt recognize \n so it needs '' to stop
                    break
                else:
                    contentsCategory=contents.split()[1]#get the category              
                    c=contentsCategory.split("&&&")#remove the &&& used as spaces
                    contentsCategory=" ".join(c)

                    #add categories into the list box from already recorded categories
                    self.listBox.insert(END,contentsCategory)#add the category to GUI list box

            self.listBox.setSelectedIndex(0)#first item will always be selected by default until you select another one

            #selected category name and budget labels and text fields
            categoryNameEdit=self.addLabel(text="Category Name: ",row=3, column=0,background="#d6d6d6",sticky="N")
            self.categoryNameField=self.addTextField(text="",row=4,column=0)
            self.categoryNameField.setText(firstCategoryName)#sets the field with the default selected item, 0 is ours
            #self.categoryNameField["state"]="disabled"
            self.categoryNameField.grid(sticky="N")
            
            categoryBudgetEdit=self.addLabel(text="Edit Category Budget: ",row=5, column=0,background="#d6d6d6",sticky="N")
            self.categoryBudgetField=self.addTextField(text=" ",row=6,column=0)
            self.categoryBudgetField.setText(firstCategoryBudget)#sets the budget of first category as default
            self.categoryBudgetField.grid(sticky="N") 

            #submit edit
            self.submitButton=self.addButton(text="Submit Edit",row=7, column=0,command=self.editSuccesfulCategory)
            #delete this category
            self.deleteButton=self.addButton(text="Delete this Category",row=8, column=0,command=self.deleteSuccesfulCategory)      
        
            self.addButton(text="Home",row=19, column=0,command=self.goHome)            
        
    def setFields(self,index):
        """ responds to the selection of a category in the list box for deleting and editing an existing category. populates the window with the data of selected category"""
        selectedCategory=self.listBox.getSelectedItem() 
        
        self.categoryNameField.setText(selectedCategory)#set the category field

        sC=selectedCategory.split(" ")#prepare the category name to match its structure on file
        selectedCategory="&&&".join(sC)

        f=open("categoryBudget.txt","r")
        while True:
            contents=f.readline()
            if contents=="":#readline doesnt recognize \n so it needs '' to stop
                break
            else:
                if contents.split()[1]==selectedCategory:
                    categoryBudget=contents.split()[2]#get the category budget
                    
                    
                    self.categoryBudgetField.setText(categoryBudget)#set the budget field
                    break
        f.close()        

    def goHome(self):
        """ Takes user to the home window on pressing the home button"""
        self.destroy()
        expenseTracker()

    def editSuccesfulCategory(self):
        """ processes the editing of an existing category on pressing the 'Submit Edit' button"""
        
        categoryName=self.listBox.getSelectedItem()#category name selected for editing
        ctN=categoryName.split(" ")
        categoryName="&&&".join(ctN)
        
        

        newCategoryName=self.categoryNameField.getText()
        n=newCategoryName.split(" ")
        newCategoryName="&&&".join(n)#store words with spaces together by representing spaces with &&&

        #only the budget will be editable    
         
        newBudget=self.categoryBudgetField.getText()#new budget in the budget field
        
        #check that budget is a number value        
        try:
            int(newBudget)
            a=True
        except:
            a=False
            
        try:            
            float(newBudget)
            b=True
        except:
            b=False    
        
        #print(a,b)        
        if a==False and b==False:
            self.messageBox(title="Error!",message="Your Budget should be a number!")
            #self.destroy() destroying this window will erase all the already entered data, both valid and invalid ones which is not a good idea           
            #deleteEditCategory()
            
        else:#budget is a number   
            
            #check that new name does not already exist outside os the one you want to edit, since the name can be the same but budget different
            fileContent=""
            f=open("categoryBudget.txt","r")
           
            nameDuplicate=False
            while True:
                line=f.readline()
                if line=="":#readline doesnt recognize \n so it needs '' to stop
                    break
                else:
                    lineS=line.split()                   
                    
                   
                    if lineS[1]==newCategoryName and newCategoryName!=categoryName:#if name is the same with enterd one where that name is not the present one then a duplicate exists
                        self.messageBox(title="Name Error!",message="The Name already Exists! Please enter another name.")
                        nameDuplicate=True
                        break

            if nameDuplicate==False:
                fileContent=""
                f=open("categoryBudget.txt","r")

                sn=0
                while True:
                    line=f.readline()
                    if line=="":#readline doesnt recognize \n so it needs '' to stop
                        break
                    else:
                        lineS=line.split()
                        sn+=1
                        lineS[0]=str(sn)
                        
                        lineTest=lineS
                        if lineTest[1]==categoryName:#replace the name, budget and date
                            lineS[1]=newCategoryName
                            lineS[2]=newBudget
                            #lineS[3]=str(datetime.datetime.now().strftime("%x_%H:%M:%S"))-the original record date should be used not the update date,
                            #else expenses on it will have dates prior to category                                      
                            
                        lineJoin="\t".join(lineS)#join the list items with a tab to make it normal as it was read
                        fileContent+=lineJoin+"\n"                        
                    
                #f.close()
                f=open("categoryBudget.txt","w")
                f.write(fileContent)
                f.close()

                #go to individuai expenses and replace the category names associated with the changed one
                fileContent=""
                f=open("individualExpense.txt","r")

                sn=0
                while True:
                    line=f.readline()
                    if line=="":#readline doesnt recognize \n so it needs '' to stop
                        break
                    else:
                        lineS=line.split()#split the line to get individual items
                        sn+=1
                        lineS[0]=str(sn)
                        
                        lineTest=lineS
                        if lineTest[1]==categoryName:#replace the name, budget and date
                            lineS[1]=newCategoryName                                                        
                            
                        lineJoin="\t".join(lineS)#join the list items with a tab to make it normal as it was read
                        fileContent+=lineJoin+"\n"                        
                    
                #f.close()
                f=open("individualExpense.txt","w")
                f.write(fileContent)
                f.close()


                

                #show a succesful edit made message
                self.messageBox(title="Submitted!",message="Your edit was submitted successfully!")
                self.destroy()
                deleteEditCategory()

    def deleteSuccesfulCategory(self):
        """confirms category deletion decision from user"""
        MsgBox = messagebox.askquestion('Delete Category?','Are you sure you want to Delete this Category and its Expenses?',icon='warning')
        if MsgBox=='yes':
            self.deleteSuccesfulCategoryTrue()
            
        else:
            messagebox.showinfo('Not Deleted!','No Deletion was Made!')
            self.destroy()
            deleteEditCategory()   

    def deleteSuccesfulCategoryTrue(self):
        """ processes the deletion of an existing category on pressing the delete this category button"""
        #get the selected category
        #open the categoryBudget file for reading
        #append each line to a variable except for the selected category while renumbering their S/N
        #close the file and open it for writing
        #write the list back to the file

        #open IndividualExpenses.txt and Delete all records for this Category

        CATEGORY=self.listBox.getSelectedItem()#get the selected category from the list box
        c=CATEGORY.split(" ")
        CATEGORY="&&&".join(c)#reformat it as it was in file before putting it in the list box

        fileContent=""
        f=open("categoryBudget.txt","r")

        sn=0
        while True:
            line=f.readline()
            if line=="":#readline doesnt recognize \n so it needs '' to stop
                break
            else:
                lineS=line.split()
                lineTest=lineS
                
                if lineTest[1]!=CATEGORY:
                    sn+=1
                    lineS[0]=str(sn)
                    lineJoin="\t".join(lineS)#join the list items with a tab to make it normal as it was read
                    fileContent+=lineJoin+"\n"
        #f.close()
        f=open("categoryBudget.txt","w")
        f.write(fileContent)
        f.close()

        #delete all category records from individual Expenses
        fileContent=""
        f=open("individualExpense.txt","r")
        
        #check if expenses is empty
        line=f.read()
        if line=="":#expenses file is empty
            x=0
        else:
            f=open("individualExpense.txt","r")
            sn=0
            while True:
                line=f.readline()
                if line=="\n" or line=="":#readline doesnt recognize \n so it needs '' to stop
                    break
                else:
                    lineS=line.split()
                    lineTEST=lineS
                    if lineTEST[1]!=CATEGORY:
                        sn+=1
                        lineS[0]=str(sn)
                        lineJoin="\t".join(lineS)#join the list items with a tab to make it normal as it was read
                        fileContent+=lineJoin+"\n"
            #f.close()
            f=open("individualExpense.txt","w")
            f.write(fileContent)
            f.close()
        

        CT=CATEGORY.split("&&&")#remove &&& for showing it to the user
        category=" ".join(CT)
                
        self.messageBox(title="Deleted!",message="Your Category '"+category+"' was Deleted successfully!")
        self.destroy()
        deleteEditCategory()

class deleteEditExpense(EasyFrame): #expense tracker extends EasyFrame(by lambert), EasyFrame extends tkinter which means, they both can run any method found in tkinter
    """
        The window for deleting and editing an existing expense
    """

    def __init__(self): #runs expenseTracker automatically, self refers to our expensetracker app window
        EasyFrame.__init__(self,width=450,height=600,title="Delete/Edit Expenses")#runs EasyFrame, the current frame we are working on-a grandchild of tkinter

        self["background"]="#d6d6d6"

        #add logo label and image       
        logoLabel=self.addLabel(text="",row=0, column=0,background="#d6d6d6",sticky="NE")
        #logoLabel2=self.addLabel(text="",row=0, column=0,background="#d6d6d6",sticky="S")#for window sizing when content would look so small
        #logoLabel2.grid(padx=200)
        self.image=PhotoImage(file="logo.gif")
        logoLabel["image"]=self.image                

        #check if file is empty or not
        f=open("individualExpense.txt","r")
        contents=f.read()        
        if contents=="":#if the file is empty
            
            self.messageBox(title="Empty file!",message="No Expenses found to Delete/Edit")
            self.destroy()
            expenseTracker()
        else:
            #read the first line for GUI default output
            f=open("individualExpense.txt","r")
            contents=f.readline()        
            expenseCategory1=contents.split()[1]
            expenseAmount1=contents.split()[2]
            expenseComment1=contents.split()[4]
            f.close()#close it to read again from beginning since read() took handle to the end of file

            #populate expenses listbox from file
            ExpensesLabel=self.addLabel(text="Select Expense to Edit or Delete: ",row=1, column=0,background="#d6d6d6",sticky="N")       
            self.listBox=self.addListbox(row = 2, column = 0,listItemSelected = self.setFields)#add an empty list box
            self.listBox.grid(padx=20)#position the list box with padx=200           

            f=open("individualExpense.txt","r")            

            while True:
                contents=f.readline()
                if contents=="":#readline doesnt recognize \n so it needs '' to stop
                    break
                else:                  
                    expenseSN=""
                    expenseSN=contents.split()[0]
                    print(contents.split())
                    print(expenseSN)   
                    expenseCategory=contents.split()[1]                    
                    expenseAmount=contents.split()[2]#get the expense amount
                    expenseDate=contents.split()[3]
                    expenseComment=contents.split()[4]
                    
                    ecg=expenseCategory.split("&&&")#remove the &&& used as spaces
                    categoryFMT=" ".join(ecg)

                    ec=expenseComment.split("&&&")#remove the &&& used as spaces
                    commentFMT=" ".join(ec)
                    expenseInfo=expenseSN+".    "+categoryFMT+"    "+"$"+expenseAmount+"    "+expenseDate+"    "+commentFMT

                    #add expenses into the list box from already recorded expenses
                    self.listBox.insert(END,expenseInfo)#add the expense to GUI list box
                    self.listBox.setSelectedIndex(0)#first item will always be selected by default until you select another one       
        
            #show expense category field but in disabled state
            self.expenseCategorytLabel=self.addLabel(text="Selected Expense Category: ",row=5, column=0,background="#d6d6d6",sticky="N")
            self.expenseCategoryField=self.addTextField(text="",row=6,column=0)
            self.expenseCategoryField.grid(sticky="N")
            self.expenseCategoryField.setText(expenseCategory1)#sets the first item' category as default category
            self.expenseCategoryField["state"]="disabled"
        
            #edit amount spent field
            self.spentAmountLabel=self.addLabel(text="Edit Expense Amount: ",row=7, column=0,background="#d6d6d6",sticky="N")
            self.spentAmountField=self.addTextField(text="",row=8,column=0)
            self.spentAmountField.grid(sticky="N")
            self.spentAmountField.setText(expenseAmount1)#sets the first expense' category expense amount as default expense amount            

            #edit comment field
            self.expensesCommentLabel=self.addLabel(text="Edit Comment: ",row=9, column=0,background="#d6d6d6",sticky="N")
            self.commentField=self.addTextArea(text="",row=10,column=0,width=10,height=5)
            #self.commentField.grid(padx=20)
            ec=expenseComment1.split("&&&")#format &&& away from comment for display
            expenseComment1=" ".join(ec)
            self.commentField.setText(expenseComment1)#sets the first expense' category expense comment as default expense comment           
            

            #submit edit
            self.addButton(text="Submit Edit",row=11, column=0,command=self.editSuccesfulExpense)       
            #delete this expense
            self.addButton(text="Delete this Expense",row=12, column=0,command=self.deleteSuccesfulExpense)         
            
            self.addButton(text="Home",row=13, column=0,command=self.goHome)

    def setFields(self,index):
        """ responds to the selection of an item in the list box for deleting and editing an expense. populates the window with the data of selected item """
        index=self.listBox.getSelectedIndex()#get the selected expense index since index is the primary key
        expenseIndex=index+1#+1 since it starts from 0 while our file S/N records from 1

        #get the category, expense amount and comment for the index selected
        fileContent=""
        f=open("individualExpense.txt","r")
        
        while True:
            line=f.readline()
            if line=="":#readline doesnt recognize \n so it needs '' to stop
                break
            else:
                line=line.split()
                if line[0]==str(expenseIndex):
                    
                    eC=line[1].split("&&&")
                    expCategory=" ".join(eC)
                    self.expenseCategoryField.setText(expCategory)
                    
                    expAmount=line[2]
                    self.spentAmountField.setText(expAmount)
                    
                    eCm=line[4].split("&&&")#line[4] is the comment, thus format &&& away for display
                    expComment=" ".join(eCm)                    
                    self.commentField.setText(expComment)
                    break#break away from the loop once the selected index item is found                    
        

    def goHome(self):
        """ Takes user to the home window on pressing the home button"""
        self.destroy()
        expenseTracker()    
    
    def editSuccesfulExpense(self):
        """ Processes and Responds to editing of an existing and selected expense when 'Submit Edit' button is pressed"""

        indexSelected=self.listBox.getSelectedIndex()#get the selected expense index since index is the primary key
        expenseIndex=indexSelected+1#+1 since it starts from 0 while our file S/N records from 1

        #self.expenseCategoryField.getText()
        
        spentAmountEdit=self.spentAmountField.getText()
        
        commentEdit=self.commentField.getText()
        ce=commentEdit.split(" ")
        commentEdit="&&&".join(ce)#put &&& into the spaces before storage to store them as one string
        commentEdit=commentEdit.rstrip("\n")#remove the \n added by .getText()
        
        #check that spent amount is a number value        
        try:
            int(spentAmountEdit)
            a=True
        except:
            a=False   


        try:            
            float(spentAmountEdit)
            b=True
        except:
            b=False    
        

        #print(a,b)        
        if a==False and b==False:
            self.messageBox(title="Error!",message="Your spent amount should be a number!")
            #self.destroy() destroying this window will erase all the already entered data, both valid and invalid ones which is not a good idea           
            #deleteEditExpense()
            
        else: #budget is a number
            fileContent=""
            f=open("individualExpense.txt","r")            

            #sn=0
            while True:
                line=f.readline()
                if line=="":#readline doesnt recognize \n so it needs '' to stop
                    break
                else:                    
                    #sn+=1
                    lineN=""#line SN
                    lineL=[]
                    lineL=line.split()
                    
                    lineN=line.split()[0]
                    #lineTEST=lineS
                    
                    #lineS[0]=str(sn)
                    if lineN==str(expenseIndex):
                        lineL[2]=spentAmountEdit
                        #lineL[3]=str(datetime.datetime.now().strftime("%x_%H:%M:%S")) -the original record date should be used not the update date           
                        lineL[4]=commentEdit                     
                                        
                    lineJoin="\t".join(lineL)#join the list items with a tab to write it according to our file format
                    fileContent+=lineJoin+"\n"
                        
            print(fileContent)
            #f.close()
            f=open("individualExpense.txt","w")
            f.write(fileContent)
            f.close()
            
            #show a succesful record made message
            self.messageBox(title="Submitted",message="Your edit was submitted successfully!")
            self.destroy()
            deleteEditExpense()            

    def deleteSuccesfulExpense(self):
        """confirms expense deletion decision from user"""
        MsgBox = messagebox.askquestion('Delete Expense?','Are you sure you want to Delete this Expense?',icon='warning')
        if MsgBox=='yes':
            self.deleteSuccesfulExpenseTrue()
            
        else:
            messagebox.showinfo('Not Deleted!','No Deletion was Made!')
            self.destroy()
            deleteEditExpense() 

    def deleteSuccesfulExpenseTrue(self):
        """ Processes and Responds to the deletion of an existing and selected expense when delete expense button is pressed"""
        #delete expense records from individual Expenses
        #get the index+1
        #copy all expense except the one with this index
        #write back to the file, after the old content is deleted            

        indexSelected=self.listBox.getSelectedIndex()#get the selected expense index since index is the primary key
        expenseIndex=indexSelected+1#+1 since it starts from 0 while our file S/N records from 1         

        fileContent=""
        f=open("individualExpense.txt","r")

        sn=0
        while True:
            line=f.readline()
            if line=="":#readline doesnt recognize \n so it needs '' to stop
                break
            else:
                lineSplit=line.split()
                if  lineSplit[0]!=str(expenseIndex):
                    sn+=1
                    lineSplit[0]=str(sn)
                    lineJoin="\t".join(lineSplit)#join the list items with a tab to make it normal as it was read
                    fileContent+=lineJoin+"\n"
                else:
                    expenseCategory= lineSplit[1]#for the message box below to inform the user the category from which deletion was made

        f.close()
        f=open("individualExpense.txt","w")
        f.write(fileContent)
        f.close()        

        eCT=expenseCategory.split("&&&")#remove &&& for showing it to the user
        eCategory=" ".join(eCT)
                
        self.messageBox(title="Deleted!",message="Your Expense was Deleted successfully from '"+eCategory+"' Category")
        self.destroy()
        deleteEditExpense()

def main():
    """ Runs the expense tracker application home window"""
    expenseTracker().mainloop()

if __name__=="__main__":
    main()


#Further work: A calculator, A pie chart to represent summary and expenses


