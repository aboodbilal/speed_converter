import schedule as sch

wel=" This is speed converter program "

print(f"\n    {wel:*^63}")

cont = True

while cont :
    choice = input('''
    You want to convert from :
    --> 1. Miles per hour to kilometers per hour.
    or 
    --> 2. Kilometers per hour  to miles per hour. 
    ==>''')

    def mph_kmph():
        cont = True
        while cont:
            miles = input("    Enter the speed in miles per hour ")
            try :
                miles = float(miles)
                kilos = float(miles * 1.609344)
                print(f"    {miles} mph = {kilos} kmph")
                cont = False
            except: 
                p = "Please enter a number"
                print (f"\n    {p:!^51}\n")       
                cont = True



        
    def kmph_mph():
        cont = True
        while cont:
            kilos = input("    Enter the speed in kilometers per hour ")
            try :
                kilos = float(kilos)
                miles = kilos * 0.621371192 
                print(f"    {kilos} kmph = {miles} mph")
                cont = False
            except :
                p = "Please enter a number"
                print (f"\n    {p:!^51}\n")       
                cont = True


    if choice == "1":
        mph_kmph()
    elif choice == "2":
        kmph_mph()
    else :
        ic = "INVALID CHOICE, TRY AGAIN"
        print('')
        print(f"    {ic:!^55} \n    (Type '1' for the first choce and '2' for the second choice)")
        continue 

    
    
    cont_choice = input('''
    Do you want to countinue the program ?, (yes/no),(0/1).  ==>''')

    while cont_choice.lower() not in ["yes","no","y","n","1","0"]:
        ic = "INVALID CHOICE, TRY AGAIN"
        print('')
        print(f"    {ic:!^55} \n    (Type 'yes' of for continue or 'no' for exit)")
        cont_choice = input('''
    Do you want to countinue the program ?, (yes/no),(0/1).  ==>''')


    if cont_choice == "yes".lower() or cont_choice.lower() == "y" or cont_choice.lower() == "1":
        cont = True
    elif cont_choice == "no".lower() or cont_choice.lower() == "n" or cont_choice.lower() == "0":
        p = "Program ended"
        print(f'\n   {p:*^43}\n')
        quit()
        