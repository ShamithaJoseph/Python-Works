class allfunctions():
    
    def SubfieldInAI():
    
        print("Sub-fields in AI are:")
    
        mylist= ["Machine Learning","Neural Networks","Vision,Robotics","Speech Processing","Natural Language Processing"]
    
        for i in mylist:
        
            print(i)
            
            
    def oddeven():
    
        num=int(input("Enter the number"))
    
        if ((num%2)==0):
        
            print(num," is Even number")
        
            message="Even number"
        
        else:
        
            print(num, " is Odd number" )
        
            message="Odd number"
        
        return message

    
    def elegiblityformarriage():
    
        gender=input("Your Gender:")
    
        age=int(input("Your Age"))
    
        if gender=="male":
        
            if age>=21:
            
                print("Eligible")
            
            else:
            
                print("Not eligible")
            
        elif gender=="female":
        
            if age>=18:
            
                print("Eligible")
            
            else:
            
                print("Not eligible")
            
        else:
        
            print("Invalid")

            
            
            
    def percent():
    
        sub1=int(input("Subject1"))
    
        sub2=int(input("Subject2"))
    
        sub3=int(input("Subject3"))
    
        sub4=int(input("Subject4"))
    
        sub5=int(input("Subject5"))
    
        total=sub1+sub2+sub3+sub4+sub5
    
        print("Total= ",total)
    
        per=(total/5)
    
        percentage=per
    
        return percentage
    
    
    
    
    def triangle():

        H=int(input("Height: "))

        B=int(input("Breadth: "))

        Area=(H*B)/2

        print("Area of Triangle: ",Area)

        message="Area"

        H1=int(input("Height1: "))

        H2=int(input("Height2: "))
    
        B1=int(input("Breadth1: "))

        Perimeter=H1 + H2 + B1

        print("Perimeter of Triangle: ",Perimeter)

        message="Perimeter"

        return message
   