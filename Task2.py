from statistics import mean
print("Swallow Speed Analysis: Version 1.0\n")#message
c=0#counter variable
datas=[]#list 
while True:#while loop
    reading=input("Enter the next reading: ")#input reading
    if c==0 and reading=="":#condition check
        print("No reading entered nothing to do. ")#message
        break
    elif reading=="" and c>=1:#conditionn check
        max_speed=max(datas)#maximum value 
        min_speed=min(datas)#minimum value
        avg_speed=mean(datas)#mean value
        print("Results summary. ")#message
        print(c,"Reading Analysed")#message
        print(f"Max speed: {max_speed:.2f} MPH, {max_speed*1.61:.2f} KPH.")#f string message 
        print(f"Min speed: {min_speed:.2f} MPH, {min_speed*1.61:.2f} KPH.")#f string message 
        print(f"Avg speed: {avg_speed:.2f} MPH, {avg_speed*1.61:.2f} KPH.")#f string message 
        break
    else:
        readings=reading[1:]#removing last value
        c=c+1#counter increase
        if reading[0]=="e" or reading[0]=="E":#condition check
            value=float(readings)/1.61#value change
            datas.append(value)#appending in list
            print("Reading Saved. ")##message
        elif reading[0]=="u" or reading[0]=="U":#condition
            value=float(readings)#value hange in float
            datas.append(value)#appending in list
            print("Reading Saved. ")##message
        else:
            c-=1#counter decrease
            print("Wrong Reading!!")#message