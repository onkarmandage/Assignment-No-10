def even():
    Num=int(input("Enter the number "))
    for i in range(1,Num+1):
        if(i%2==0):
            print(i)


if __name__=="__main__":
    even()
