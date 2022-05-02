import csv

file1 = "Bus_info.csv"
file2 = "Ticket_info.csv"
def Busdetails():
    global file1
    sections = ["Bus Sr.No.","Types of Buses","Features","Seats","Cost"]
    bustravels = [
        ["1","Parveen-Travels","Non-AC-seater","2|2","1000"],
        ["2","VRL-Travels","Non-AC-sleeper","2|1","1200"],
        ["3","Prasanna-Travels","Non-AC-airbus","2|2","2000"],
        ["4","Jabbar-Travels","Semi-Sleeper","2|2","1500"],
        ["5","Hans-Travels","AC-sleeper","2|1","1800"],
        ["6","KPN-Travels","AC-seater","2|2","19500"],
        ["7","Kaleswari-Travels","AC-airbus","2|2","23500"]
        ]

    with open(file1,"w",newline='') as bus:
        writing = csv.writer(bus)
        writing.writerow(sections)
        for i in bustravels:
            writing.writerow(i)
        print("File created!")

    with open(file1) as c:
        reading = csv.reader(c)
        for i in reading:
            print(i)

# Busdetails()

def Bookseats():
    global file1,file2

    name = input("Enter your full name: ")
    age = int(input("Enter your age: "))
    while True:
        mob_no = int(input("Enter your mobile number: "))
        if len(str(mob_no)) == 10:
            break
        else:
            print("Enter valid no. of digits of mobile number.")
    businfo = open(file1)                                       # Opened file1 for bus details
    reading = csv.reader(businfo)
    
    while True:
        bus_no = int(input("Enter your travelling bus Sr no. from bus details info: "))
        if bus_no > 7 or bus_no < 1:
            print("Please see bus details and enter Bus Sr.No.")
            continue
        else:
            for i in reading:
                if reading.line_num <= bus_no:
                    continue
                # print(reading.line_num)
                print("Your bus succesfully selected!")
                bus = i[1]
                bustype = i[2],i[3]
                cost = i[4]
                break
            break
                
    businfo.close()
        
    print("\tDestination:-")
    initial_place = input("Enter from where do you want to start: ")
    final_place = input("Enter where do you want to go: ")
    while True:
        date = input("Enter the date of travelling in [xx-yy-zzzz] format: ")
        if date[2] and date[5] != date.isalnum():
            break                                                         #Need Perfection
    
    #details_header = ['name','age','initial_place','final_place','mob_no','Bus_Info','Bus_Type','cost','date']
    details = [name,age,initial_place,final_place,mob_no,bus,bustype,cost,date]

    with open(file2,'a',newline='') as ticket:
        writing = csv.writer(ticket)    
        # writing.writerow(details_header)
        writing.writerow(details)
        print("\t-------Your ticket is succesfully booked-------")

# Bookseats()

def Ticketinfo():
    global file2
    details = []
    with open(file2) as info:
        reading = csv.reader(info)

        for i in reading:                # No other way to extract data from reading object
            if reading.line_num == 1:
                header_details = i
                continue
            details = i

        lol = details[1]            # Unnecessary useful to raise error if there are no tickets booked

        for i in range(9):              #Because there are 8 details of the passenger in csv file
            print(header_details[i], end=':-\t\t')
            print(details[i])

# Ticketinfo() 


def Ticketcheck():
    global file2
    with open(file2) as search:
        reading = csv.reader(search)
        name = input("Enter your reserved name on the ticket: ")
        age = int(input("Enter your reserved age on the ticket: "))
        BOOL = False

        for i in reading:          
            if i[0] == name and i[1] == str(age):
                if reading.line_num == 1:
                    pass
                # print(i[1], i[2])
                print("\t-------Your bus reservation found-------")           
                BOOL = True
                break

        if BOOL == False:
            print("\t-------Your bus reservation NOT found!-------")

# Ticketcheck()

def Updateticket():
    global file1, file2
    name = input("Enter your reserved name: ")
    while True:
        mob_no = input("Enter your mobile no. : ")
        if mob_no.isdigit() and len(mob_no) == 10:
            break
        else:
            print("Enter valid phone no.")

    info = []
    def check(name,phone):
        global info
        details = []
        with open(file2) as c:
            reading = csv.reader(c)
            for i in reading:
                details.append(i)
                # if name and phone in i:           # <-- Problem arises because if statement will be satisfied even
                if i[0] == name and i[4] == phone:  # if name and phone is found in different lines
                    info = i
                    break
        
        header = details[0]
        for i in range(9):
            print(header[i],end=':-\t')
            print(info[i])
        return info

    try:                                 # If name or phone not found in file then it will raise error
        # check(name,mob_no)               # that info is referenced before assignment.
        
        info = check(name,mob_no)        # Amazingly it has returned value only       
        # print(info)
   
        change = int(input('''\nEnter what do you want to change? :
        '1' to change name   '2' to change age   '3' to change intial place
        '4' to change final place   '5' to change bus   '6' to change date. \n'''))

        if change == 1:
            new_name = input("Enter new name: ")
            info[0] = new_name

        elif change == 2:
            new_age = int(input("Enter new age: "))
            info[1] = new_age

        elif change == 3:
            new_initial = input("Enter new initial place: ")
            info[2] = new_initial

        elif change == 4:
            new_final = input("Enter your new final place: ")
            info[3] = new_final

        elif change == 5:
            new_bus = input("Enter your new bus Sr.No. from bus details: ")
            with open(file1) as c:              # Extracting data from bus details and updating ticket
                reading = csv.reader(c)
                for i in reading:
                    if i[0] == new_bus:
                        bus = i[1]
                        bustype = i[2],i[3]
                        cost = i[4]
                        break
                info[-4] = bus
                info[-3] = bustype
                info[-2] = cost 
                        
        elif change == 6:
            new_date = input("Enter new date of travelling in (xx-yy-zzzz) form: ")
            info[-1] = new_date

        else:
            print("Invalid number!")

        unchanged_data = []
        with open(file2) as c:
            reading = csv.reader(c)

            for i in reading:
                if i[4] == info[4]:
                    continue                     # Not adding updated data in the middle of file
                else:
                    unchanged_data.append(i)
            # print("Unchanged data: ",unchanged_data)
            
        with open(file2,'w',newline='') as c:       
            writing = csv.writer(c)
            writing.writerows(unchanged_data)
            writing.writerow(info)
            print("Your ticket succesfully updated.")

    except:
        print("Invalid name or phone number. Please try again.")

# Updateticket()


def Cancelticket():
    global file2  
    print("\t-------Enter reserved name and phone no. in ticket to cancel the ticket.-------")
    name = input("Enter your name: ")
    while True:
        mob_no = input("Enter your mobile number: ")
        if mob_no.isdigit() and len(mob_no) == 10:
            break
        else:
            print("Check your mobile number again!")

    renewed_data = []
    with open(file2) as c:
        reading = csv.reader(c)
        BOOL = False

        for i in reading:
            if i[0] == name and i[4] == mob_no:
                BOOL = True
                continue
            else:
                renewed_data.append(i)

        # print("Renewed data: ",renewed_data)

    if BOOL == True:
        confirm = input("Are you sure? (y/n): ")

        if confirm == 'y':
            with open(file2,'w',newline='') as c:
                writing = csv.writer(c)
                for i in renewed_data:
                    writing.writerow(i)
                print("\t-------Ticket succesfully cancelled!-------")
        elif confirm == 'n':
            BOOL = False
        else:
            print("Invalid confirmation!")
            BOOL = False

    elif BOOL == False:
        print("\t-------No such ticket found!-------")

# Cancelticket()

while True:
    opt = int(input('''\nEnter '0' to exit   '1' to see bus details   '2' to book a ticket   '3' to see your ticket info
      '4' to search ticket   '5' to update ticket   '6' to cancel ticket:-\n'''))

    if opt == 0:
        break

    elif opt == 1:
        Busdetails()
    
    elif opt == 2:
        Bookseats()

    elif opt == 3:
        try:                                # To handle the error when no tickets are booked
            Ticketinfo()            
        except:
            print("No tickets booked!")
    elif opt == 4:
        try:
            Ticketcheck()
        except:
            print("No tickets booked!")
    elif opt == 5:
        Updateticket()
    
    elif opt == 6:
        Cancelticket()
    
    else:
        print("Invalid number!")