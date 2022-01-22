print("\n\nStop! Who would cross the Bridge of Death\nMust answer me these questions three, 'ere the other side he see.\n")#message
name=input("What is you name: ")#input
cname=name.capitalize()#capatilizing
if cname=="Arthur":#condition
    print("Your name is",cname)#message
    print("My liege! You may pass!")#message
else:
    print("My name is",cname)##message
    what_you_seek=input("What is your quest?")#input
    print("You seek ",what_you_seek)##message
    if "grail" in what_you_seek:#condition check
        colour=input("What is your favourite colour? ")#colour input
        ccolour=colour.capitalize()#capitalizing colour
        if cname[0]==ccolour[0]:#condition check
            print("You choosed the colour: ",ccolour)#message
            print("You may pass!")#message
        else:
            print("Incorrect! You must now face the Gorge of Eternal Peril.")#message
    else:
        print("Only those who seek the Grail may pass.")#message