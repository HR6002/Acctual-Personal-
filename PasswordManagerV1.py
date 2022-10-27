import random, time, string
from string import ascii_lowercase, ascii_uppercase
from typing import final 

def coolLoadingScreen():
    print("---------------------------------------------------------------------------------------------------------------------------")
    print("                                                 initializing passwrod manager app")
    for x in range (0,100):  
        b = 1+x
        print ("                                                                "+str(b)+"%", end="\r")
        time.sleep(0.1)
    print("                                             pasawwrod manager succefully initialized:")
    print("----------------------------------------------------------------------------------------------------------------------------")



def usernameRetrival(website):
    
    if website in global_websiteusername:
        userNamesFound=global_websiteusername.get(website)
        print("""
        
        
        """)
        print("-----------------------------------------USER NAMES FOUND:-----------------------------------------")
        for i in userNamesFound:

            print(i)
        print("---------------------------------------------------------------------------------------------------")
        print("""
        
        
        """)
    else:
        print("-----------------------------------------!!!!! NO USER NAMES FOUND!!!!!:-----------------------------------------")

    
def passwrodRetrival(username):

    if username in global_allpasswords:
        global passwrodFound
        passwrodFound=global_allpasswords.get(username)
        prettyListFormatter()
    else:
        
        print("----------------------------------------!!NO PASSWORDS FOUND!!----------------------------------------")
    

def prettyListFormatter():

    uglyList=passwrodFound
    col=2
    print(""" 


    """)
    print ("----------------------------------------PASSWORDS FOUND:----------------------------------------")
    for x, y in zip(uglyList[::col], uglyList[1::col]):
        print(f'        password: {x: <20}Website:{y} ')
    print ("------------------------------------------------------------------------------------------------")
    print(""" 


    """)
        



def generatePassword():
    password=("")
    specialChar=("!£%^&*@~#/.,")
    for i in range (0,10):
        number=random.randint(0,9)
        upperCase=random.choice(string.ascii_uppercase)
        lowercase=random.choice(string.ascii_lowercase)
        special=random.choice(specialChar)
        randomstorage=[str(number),upperCase, lowercase, special,]
        letterToAdd=random.choice(randomstorage)
        password=password+letterToAdd
    return password








    
        

    


  
    
    
    
    

def greetings():
    print("                                             passwrod manager is up and running")
    while True:
        userChoice=input("""
                                                    To add new password press N 
                                                    to retrieve an old password Press P
                                                    TO retrieve an old username Press U

                                                    Your Choice:          """).upper()
        if userChoice=="N":
            newPassword()
        elif userChoice=="P":
            oldPassword()
        elif userChoice=="U":
            oldusername()
        else:
            True 

        






global_allpasswords={
        "example":["examplePassword","example.com"]
    }




global_websiteusername={
        "ExampleWebsite.com":["Example username", "another example"]

    }





def newPassword():
    while True:
        print("""
        ------------------------------------------NEW PASSWORD ENTRY--------------------------------------------------------""")
        username1=input("enter the username for this password   ")
        website1=input("enter the website for this passwrod    ")
        password1=generatePassword()
        print (f"""
        ------------------------------------------------------------------------------------------------------------------
        PASSWORD: {password1}
        USERNAME  {username1}
        WEBSITE   {website1}
        ------------------------------------------------------------------------------------------------------------------""")

        proceed=input("would you like to proceed? Y/N")
        if proceed.upper()=="Y" :
            print("""
            
            
             """)
            print("--------------------------------")
            print("---------PASSWORD SAVED!--------")
            print("--------------------------------")
            print("""
            
            
             """)
            if username1  not in global_allpasswords:
                global_allpasswords[username1]=[password1,website1]
            else:
                global_allpasswords[username1].append(password1)
                global_allpasswords[username1].append(website1)


            if website1 not in global_websiteusername:
                global_websiteusername[website1]=[username1]
            else:
                global_websiteusername[website1].append(username1)
            




        else:
            print("------------------------------------")
            print("---------PASSWORD NOT SAVED!--------")
            print("------------------------------------")
            print("""
            
            
             """)

        
        x=input(" press X exit or press enter to store another one")
        if x.upper() =="X":
            break
        else:
            True 

def oldPassword():
    while True:
        print("---------------------------------PASSWORD SEARCH---------------------------------")
        username1=input("please enter username:         ")  
        passwrodRetrival(username1) 
        found=input("press x to exit or press enter to search again ").upper()
        if found=="X":
            break

def oldusername():
    while True:
        print("---------------------------------USERNAME SEARCH---------------------------------")
        websitex=input("please enter WEBSITE:         ")  
        usernameRetrival(websitex) 
        found=input("press x to exit or press enter to search again ").upper()
        if found=="X":
            break


if __name__ == "__main__":
    #coolLoadingScreen()
    #storingWebsiteUsername()
    #(usernameRetrival("ExampleWebsite.com"))
    #print(passwrodRetrival("example"))
    #(prettyListFormatter("example"))
    #newPassword()
    coolLoadingScreen()
    greetings()
