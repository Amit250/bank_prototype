import os
import json
import sys

clear=lambda:os.system("cls")

#                 function to return main page
def redirect():
    n=input("\n\tEnter 'R' to return main page and 'E' to exit  ")
    n.upper()
    if n=='R':
        switch()
    elif n=='E':
        sys.exit()
    
#                 function to check password to gain access
def check_password(i):
    
    
    filename='account'+str(i)+'.json'
    
    with open(filename,'r')as f:
        data=json.load(f)
        acess=data['Password']
        pass_word=input('\nEnter password of account'+str(i)+' to gain access\n\tPassword: ')
        
        while pass_word!=acess:
            print('Invalid password')
            pass_word=input('Please re-enter password to gain acess  ')
        if pass_word==acess:
            return data



#                  funtion to open existing account

def open_account(i):
    data={}
    data=check_password(i)
    clear()
    for i in data.keys():
        if i!='Password':
            print(f'{i}:{data[i]}')
    
    redirect()



# #                function to create new account
def create_new_account(i):
    clear()
    print('Creating new account')
    
    # using string concatenation to create new file name every time program creates new account
    filename='account'+str(i)+'.json'

    # writing information to files
    with open(filename,'w')as f:
        
        first_name=input('Enter your first name:') 
        last_name=input('Enter your Last name:')
        age=int(input('Enter your age:'))
        sex=input('enter your sex:')
        address=input('Enter address:')
        citizenship_no=input('Enter citizenship.no:')
        

           
        list_of_info=[('First name ',first_name),
                  ('last name ',last_name),
                  ('age ',age),
                  ('sex ',sex ),
                  ('address ',address ),
                  ('citizenship.no ',citizenship_no ),
                  ('Total_Amount',0)]
        
        # password to access account  
        password=input('Enter password: ')
        confirm_password=input('Confirm password: ')
    
        # loop for confirming password
        while password!=confirm_password:
            print('Invalid Password\n') 
            confirm_password=input('\t\tPlease re-enter password\n\t\t')
            
        if password==confirm_password:
            data=dict(list_of_info)
            data['Password']=password
            data1=json.dumps(data,indent=2)
            
            f.write(data1)
            
            print('\n\tNew account sucessfully created')

    
    redirect()
    
#                 Function to deposit money

def deposit(i,amount):
    
    
    filename='account'+str(i)+'.json'
    with open(filename,'r')as f:
        data=json.load(f)
        amt=data["Total_Amount"]
        

    with open(filename,'w')as f:
        if amt==0:
            data['Total_Amount']=amount
            


        else:
            data["Total_Amount"]+=amount
        
        data1=json.dumps(data,indent=2)
        f.write(data1)

        print(' Total amount of account',i,'is',data['Total_Amount'])
    
        return amount
        
        
    
#                  Function to withdraw money

def withdraw(i):
    data={}
    data=check_password(i)
    amt=int(input('Enter amount of money you want to withdraw: '))
    total=data["Total_Amount"]

    if amt>total:
        print('\t Insufficent amount! \n\taccount',i,' has Total Balance=',total)

    else:
        
        
        updated=total-amt
        data["Total_Amount"]=updated
        filename='account'+str(i)+'.json'
        with open(filename,'w')as f:
            data1=json.dumps(data,indent=2)
            f.write(data1)

    return amt


    
    



# Function to transfer money
def transfer_amt(i,j):
    amt=withdraw(i)
    deposit(j,amt)
    print(amt,'has been transfered from account',i,' to account',j)

    



#               Main page program here
def switch():
    clear()
    print('BANK TRANSACTION:\n 1)Create new account \n 2)Open existing account \n 3)Deposit \n 4)Withdraw \n 5)Transfer money \n 6)Exit ')
    case=int(input('Enter to choose a  bank transaction: ', ))
    
    
    if (case==1):
        i=int(input('\n\tEnter new account number of account to be made:'))
        create_new_account(i)

    elif(case==2):
        i=int(input('\n\tEnter account number of account you want to open. '))
        open_account(i)

    
    elif(case==3):
        i=int(input('\nEnter acount number of account in which you want to depsoit money. '))
        amount=int(input('Enter amount of money you want to deposit: '))
        amount=deposit(i,amount)
        print(amount,'has been deposited\n')
        redirect()

    
    elif(case==4):
        i=int(input('\nEnter account number of account from which you want to withdraw money.  '))
        amt=withdraw(i)
        print(amt,'units has been sucessfully withdrawn\n')
        redirect()
    
    elif(case==5):
        i=int(input('Enter account number of donor account'))
        j=int(input('Enter account number of reciver account'))
        transfer_amt(i,j)

    elif(case==6):
        clear()
        sys.exit()


    else:
        print('Enter valid option')

switch()