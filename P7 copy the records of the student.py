import pickle
while True:
    print(''' 1.Create a Binary File.
    2.Display the main File.
    3.Create new file wirh>90
    4.Exit''')
    a=int(input('choose a command(1-2,9-exit):'))
    if a==1:
        f=open('student.dat','wb')
        o=open('stuii.dat','wb')
        x=int(input('How many student:'))
        for i in range(x):
            name=input('Name:')
            english=int(input('English Mark:'))
            lan=int(input('Language Marks:'))
            phy=int (input('Physics Mark:'))
            chem=int(input('Chemistry Mark:'))
            maths=int(input('Maths Mark:'))
            cs=int(input('CS Mark:'))
            total=phy+chem+cs+maths+english+lan
            per=(total/600)*100
            t=[name,english,lan,phy,chem,maths,cs,total,per]
            g=[name,english,lan,phy,chem,maths,cs,total,per]
            pickle.dump(t,f)
            if       per>=90:
             pickle.dump(g,o)
        f.close()
        o.close()
    elif a==2:
        f=open('student.dat','rb')
        try:
            while True:
                p=pickle.load(f)
                print(p)
        except:
            f.close()
    elif a==3:
        print("Studets with>90 Marks")
        f=open('stuii.dat','rb')
        try:
            while True:
                o=pickle.load()
                print(o)
        except:
            f.close()
    else:break
               
      
                
           
          
    


















 
