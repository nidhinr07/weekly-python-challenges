while True:
    
    print("\n************   CALCULATOR   **************")
    a=int(input("\nEnter First Number : "))
    b=int(input("Enter Second Number : "))
    choice=input("Enter Your Operation [+, -, *, /, //, %, exit] : ").lower().strip()
    
    if choice=="exit":
        print("\nThanks For Using this Calculator")
        break
        
    elif choice=="+":
        print("\nAddition Result:",a+b)
        
    elif choice=="-":
        print("\nSubtraction Result:",a-b)
        
    elif choice=="*":
        print("\nMultiplication Result:",a*b)
        
    elif choice=="/":
        print("\nDivision Result:",a/b)
        
    elif choice=="//":
        print("\nFloor Division Result:",a//b)
        
    elif choice=="%":
        print("\nModules Result:",a%b)
        
    else:
        print("\nInvalid Choice,Enter Correct Choice")
