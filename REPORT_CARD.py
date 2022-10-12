import pickle

file = 'REPORT_CARD.dat'
PT1 = {}
Half_Yearly = {}
PT2 = {}
Finals = {}
strm = ''
grade = ''

# All the basic details of student --> name, admno. dob, gender, stream
def FormerDetails():        
    global strm
    nme = input("Enter student name: ")
    Adm = int(input("Enter adm no.: "))
    dob = input("Enter dob: ")
    gen = input("Enter gender: ")
    strm = input("Enter stream(Hindi(H)/CS(C) ~ Maths(M)/Bio(B): ")
    d = {}
    all = [nme, Adm, dob, gen, strm]
    headers = ['Name', 'AdmNo.', "DOB", "Gender", "Stream"]

    for i in range(len(headers)):
        d[headers[i]] = all[i]

    with open(file, 'ab') as bf:
        pickle.dump(d, bf)

# Taking input from user of marks of a particular exam according to the exam(pt1, pt2, etc) passed to func. 
def MarksInput(examname, exam, S):
    print("******" + examname + " marks******")
    eng = int(input("Enter English marks: "))
    exam['English  '] = eng                 # Ignore spaces in keys
    phy = int(input("Enter Physics marks: "))
    exam['Physics  '] = phy
    chem = int(input("Enter Chemistry marks: "))
    exam['Chemistry'] = chem
    if 'C' in S.upper():
        cs = int(input("Enter Comp.Sc. marks: "))
        exam['Comp.Sc. '] = cs
    if 'M' in S.upper():
        maths = int(input("Enter Maths marks: "))
        exam['Maths    '] = maths
    if 'B' in S.upper():
        bio = int(input("Enter Biology marks: "))
        exam['Biology  '] = bio
    if 'H' in S.upper():
        hin = int(input("Enter Hindi marks: "))
        exam['Hindi    '] = hin

# Func. that counts total marks of a specific subject when passed to func.
def TotalMarks(subject):
    Total = PT1[subject] + Half_Yearly[subject] + PT2[subject] + Finals[subject]
    # print(subject, Total)
    if Total <= 200 and Total > 180:
        grade = 'A'
    elif Total <= 180 and Total > 160:
        grade = 'B'
    elif Total <= 160 and Total > 140:
        grade = 'C'
    elif Total <= 140 and Total > 120:
        grade = 'D'
    elif Total < 120:
        grade = 'E'
    else:
        grade = ''
    return subject, Total, grade

# Func. that adds final info of student(total marks of all sub. and percent)
def AddTotals(stm):
    Teng = TotalMarks("English  ")
    Tchem = TotalMarks("Chemistry")
    Tphy = TotalMarks("Physics  ")
    if 'C' in stm.upper():
        Tcs = TotalMarks("Comp.Sc. ")
        Thin = (None, 0, None)      # --- statement 1
    if 'M' in stm.upper():
        Tmath = TotalMarks("Maths    ")
        Tbio = (None, 0, None)
    if 'B' in stm.upper():
        Tbio = TotalMarks("Biology  ")
        Tmath = (None, 0, None)
    if 'H' in stm.upper():
        Thin = TotalMarks("Hindi    ")
        Tcs = (None, 0, None)
    
    # statement1 like statements throws error in below statement if not defined
    marks = (Teng[1], Tchem[1], Tphy[1], Tmath[1], Tcs[1], Tbio[1], Thin[1])  
    Tmarks = sum(marks)
    per = (Tmarks/1000)*100                 # 200 marks * 5 subjects = 1000
    per = str(per)+"%"                      # Percentage is string
    with open(file, 'ab') as bf:
        for i in (Teng, Tchem, Tphy, Tmath, Tcs, Tbio, Thin):
            pickle.dump(i, bf)
        pickle.dump(per, bf)

def ParticularData(nme, rno):
    BOOL = False
    lst = []
    with open(file, 'rb') as bf:
        while True:
            try:
                data = pickle.load(bf)
                if BOOL == True:
                    lst.append(data)
                    if isinstance(data, str):   # If data is percentage then stop adding
                        BOOL = False
                        break
                elif nme == data.get("Name") and rno == data.get("AdmNo."): # If condition
                    BOOL = True            # matches start adding
                    lst.append(data)
                else:
                    continue
            except EOFError:
                print("No such data found!")
                break
            except AttributeError:    # get func. doesn't exist in tuple and throws error
                continue
    return lst

def DisplayAll():
    bf = open(file, 'rb') 
    try:
        while True:
            print(pickle.load(bf))
    except:
        bf.close()

# Func. that deletes particular student data
def DeleteData(nme, rno):
    deldata = ParticularData(nme, rno)
    lst = []
    bf = open(file, 'rb')
    try:
        while True:
            oldata = pickle.load(bf)
            if oldata not in deldata:
                lst.append(oldata)
    except EOFError:
        bf.close()
    with open(file, 'wb') as bf:
        for i in lst:
            pickle.dump(i, bf)

def ReportCardFormat(data):
    if len(data) == 0:
        return None
    k1, v1 = data[0].keys(), data[0].values()
    k2 = data[1].keys()         # Getting all subjects name
    v2 = data[1].values()       # PT1 marks
    v3 = data[2].values()       # Half yearly marks
    v4 = data[3].values()       # PT2 marks
    v5 = data[4].values()       # Finals marks
    totals = []
    for i in data:
        if isinstance(i, tuple) and i[0] is not None:   # statement1 like staements are ignored
            totals.append(i)         # total marks & grades
    k1, k2, v1, v2, v3, v4, v5 = list(k1), list(k2), list(v1), list(v2), list(v3), list(v4), list(v5)

    for i in range(len(k1)):
        print(k1[i], ' : ', v1[i])
    print()
    print("Subjects      |     PT1    | Half Yearly|    PT2     |    Finals  |    Total   |  Grade")
    for i in range(5):
        print(k2[i], end= '     |     ')
        print(v2[i], end= '     |     ')
        print(v3[i], end= '     |     ')
        print(v4[i], end= '     |     ')
        print(v5[i], end= '     |     ')
        print(totals[i][1], end= '     |     ')
        print(totals[i][-1])
    else:
        print("Percentage: ", data[-1])        

# Func. that can modify student name, admno, dob, gender 
def ModifyData(stud, rno, ch, newdata):
    studata = ParticularData(stud, rno)
    for i in studata:
        if ch == 1:
            if isinstance(i, dict) and stud == i.get("Name"):
                i["Name"] = newdata
        elif ch == 2:
            if isinstance(i, dict) and stud == i.get("Name"):
                i["AdmNo."] = newdata
        elif ch == 3:
            if isinstance(i, dict) and stud == i.get("Name"):
                i["DOB"] = newdata
        elif ch == 4:
            if isinstance(i, dict) and stud == i.get("Name"):
                i["Gender"] = newdata
        
    DeleteData(stud, rno)
    with open(file, 'ab') as bf:
        for i in studata:
            pickle.dump(i, bf)

while True:
    print("*******************************************************************************************\n")
    n = int(input("1 to input student details\n 2 to modify student details\n  3 to display student details\n   4 to see student report card\n    5 to delete student details\n     6 to exit\n"))

    if n == 1:
        FormerDetails()
        with open(file, 'ab+') as bf:
            MarksInput("Periodic Test I(40)", PT1, strm)
            pickle.dump(PT1,bf)
            MarksInput("Half Yearly(60)", Half_Yearly, strm)
            pickle.dump(Half_Yearly,bf)
            MarksInput("Periodic Test II(40)", PT2, strm)
            pickle.dump(PT2,bf)
            MarksInput("Finals(60)", Finals, strm)
            pickle.dump(Finals,bf)
        AddTotals(strm)

    elif n == 2:
        stud = input("Enter which student detail you want to change: ")
        rollno = int(input("Enter roll no. of student: "))
        ch = int(input("Enter what do you want to change\n1. name,\n2. admno,\n3. dob\n4. gender: \n"))
        if ch == 1:
            newname = input("Enter new name: ")
            ModifyData(stud, rollno, ch, newname)
        elif ch == 2 :
            newadm = int(input("Enter new admission number: "))
            ModifyData(stud, rollno, ch, newadm)
        elif ch == 3:
            newdob = input("Enter new dob of a student: ")
            ModifyData(stud, rollno, ch, newdob)   
        elif ch == 4:
            newgen = input("male(m) or female(f): ")         
            ModifyData(stud, rollno, ch, newgen)

    elif n == 3:
        DisplayAll()

    elif n == 4:
        name = input("Enter student name: ")
        rollno = int(input("Enter student roll no.: "))
        d = ParticularData(name, rollno)
        ReportCardFormat(d)

    elif n == 5:
        name = input("Enter student name: ")
        rollno = int(input("Enter student roll no.: "))
        DeleteData(name, rollno)

    elif n == 6:
        break
    else:
        print("Invalid input")