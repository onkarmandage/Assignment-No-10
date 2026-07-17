def Factorial():
    Num=int(input("Enter the number: "))
    Fact=1
    for i in range(1,Num+1):
        Fact=Fact*i
    print("Factorial is ",Fact)


if __name__=="__main__":
    Factorial()