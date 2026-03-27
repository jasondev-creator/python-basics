import pickle
while True:
    print(''' 1. Create Binary File.
2. Display the File.
3. Exit''')
    a = int(input('choose a command (1-2,3-exit):'))
    if a == 1:
        f = open('student.dat','wb')
        x = int(input('How many students:'))
        for i in range(x):
            name = input('Name:')
            english = int(input('English Mark:'))
            lan = int(input("Language Marks:"))
            phy = int(input('Physics Mark:'))
            chem = int(input('Chemistry Mark:'))
            maths = int(input('Maths Mark:'))
            cs = int(input('CS Mark:'))
            t = [name,english,lan,phy,chem,maths,cs]
            pickle.dump(t,f)
        f.close()
    elif a==2:
        f = open('student.dat','rb')
        try:
            while True:
                p = pickle.load(f)
                print(p)
        except:
            f.close()
    if a>2:
        break
