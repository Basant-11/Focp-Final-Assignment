from random import choice
import random
print("\nWelcome to Pop Chat")#welcome messages
print("One of our operators will be pleased to help you today.")#welcome messages
mail_address=input("Please enter your Poppleton email address: ")#welcome messages
def check_mail():#funtion-1
    position=mail_address.index("@")#takes position of @ in mail_address
    if mail_address.count("@")==1:#checks position of @ in mail
        if mail_address[position+1:]=="pop.ac.uk":#checks wether the after part of @ is pop.ac.uk or not 
            name=mail_address[:position]#takes the 1st part of mail_address before @ that is the will be the name of the user
            cname=name.capitalize()#capitilizes the name variable
            print(f"Hi,{cname}! Thank You, and Welcome to PopChat!")#message in f string formate to display cname variable value in between
            rnames=["Eric","Brad","Patrick","Tom","Andrew","William","Tobey"]#list for the random name for the computer
            choosen_name=random.choice(rnames)#chooses the name from the list rnames
            print(f"My name is {choosen_name}, and it will be my pleasure to help you.")#displays message in f string with choosen_name variable
            netwoek_check=[1,0,1,1,1,1,1]#list for checking network(only 10%)
            rand_number=random.choice(netwoek_check)#random choosing
            if rand_number==0:#checking random number
                print("*** NETWORK ERROR ***")#message
                print(f"\nThanks, {cname}, for using PopChat. See you again soon!")#messagein f string formate to display cname variable 
                exit()   
        else:
            print("\t!! Invalid email")#message
            exit()
        while True:#while loop
            give_your_question =input("---> ")#input message"
            if "library" in give_your_question:#word check
                print("The library is closed today.")
            elif "wifi" in give_your_question:#word check
                print("Wifi is excellent across campus.")
            elif "deadline" in give_your_question:#word check
                print("Your deadline has been extended by two working days.")
            elif "parking" in give_your_question:#word check
                print("Parking is free inside the building.")
            elif "classroom" in give_your_question:#word check
                print("Its just on the right side of the library.")
            elif "lab" in give_your_question:#word check
                print("Its on next floor.")
            elif "coffee" in give_your_question:#word check
                print("Teekee is open until 9pm this evening.")
            elif give_your_question == "exit" or give_your_question =="bye" or give_your_question =="quit" or give_your_question =="goodbye" or give_your_question =="end" or give_your_question=="help" or give_your_question=="Thankyou" or give_your_question=="thankyou":#word check
                print(f"\nThanks, {cname}, for using PopChat. See you again soon!")
                exit()
            else:
                question_without_respons=["Hmmm","Oh, yes, I see","Tell me more","Really","Intresting","Sure"]#other responses
                print(choice(question_without_respons))#print function
    else:
        exit()

check_mail()