for i in range(6):
    a=int(input())
    b=int(input())
    f=input("add/sub/mul/div:")
    if(f == "add"):
        print(a+b)
    elif(f == "sub"):
        print(a-b)
    elif(f == "mul"):
        print(a*b)
    elif(f == "div"):
        print(a/b)
    else:
        print("invalid")
