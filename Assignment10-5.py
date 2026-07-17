def odd():
    Num=int(input("Enter the Number "))
    for i in range(1,Num+1):
        if (i%2!=0):
            print(i)


if __name__=="__main__":
    odd()