class multiple():
    def Subfields():
        print("Sub fields in AI are:")
        Lists=["Machine learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"];
        for temp in Lists:
            print(temp)
   
          
        
    def oddoreven():
        num =int(input("Enter the number:"))
        if(num%2==0):
            print(num,"is even number")
        else:
            print(num,"is odd number")
        
    def Eligible():
        gender=input("Your gender:");
        age=int(input("Your age:"));
        if(gender=="Male"):
            if(age<= 21):
                print("NOT ELIGIBLE");
            else:
                print("ELIGIBLE")
            
    def percentage():
        sub1=(int(input("Subject1=")));
        sub2=(int(input("Subject2=")));
        sub3=(int(input("Subject3=")));
        sub4=(int(input("Subject4=")));
        sub5=(int(input("Subject5=")));
        total = sub1+sub2+sub3+sub4+sub5
        print("Total:",total)
        per=float(total)*(100/500)
        print("Percentage:",per)
        
    def triangle():
        Height=int(input("Height:"));
        Breadth=int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        Area = (Height*Breadth)/2
        print("Area of traingle",Area)
        Height1=int(input("Height1:"));
        Height2=int(input("Height2:"));
        Breadth=int(input("Breadth:"));
        Perimeter=Height1+Height2+Breadth
        print("Perimeter formula:Height1+Height2+Breadth")
        print("Perimeter of triangle",Perimeter)
    
    
 
    




            
    
        
 
 