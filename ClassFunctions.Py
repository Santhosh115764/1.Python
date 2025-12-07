class SubfieldsInAI():
    def Subfields():
        print("Sub-fields in AI are:")
        lists=["Machine learning", "Neural networks", "Vision", "Robotics", "Speech processing", "Neural Language Processing"]
        for process in lists:
            print(process)

    def oddeven():
        number=int(input("enter the number:"))
        if((number%2)==0):
            print("even number")
        else:
            print("odd number")

    def marriage():
        gender=input("your gender:")
        age=int(input("your age:"))
        if(gender=="male"):
            if(age>=21):
                print("eligible")
            else:
                print("not eligible")
        elif(gender=="female"):
            if(age>=18):
                print("eligible")
            else:
                print("not eligible")
        else:
            print("wrong")

    def percentage():
        sub1=int(input("subject1="))
        sub2=int(input("subject1="))
        sub3=int(input("subject1="))
        sub4=int(input("subject1="))
        sub5=int(input("subject1="))
        total= sub1+sub2+sub3+sub4+sub5
        print("total:", sub1+sub2+sub3+sub4+sub5)
        percent=(total/500)*100
        print("percentage:", percent)

    def triangle():
        height=int(input("height:"))
        breadth=int(input("breadth:"))
        print("area formula: (height*breadth)/2")
        print("area of triangle:",(height*breadth)/2)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        print("perimeter formula: Height1+Heigth2+Breadth")
        print("perimeter of triangle:",Height1+Height2+Breadth)
        

    

    