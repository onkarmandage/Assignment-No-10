def sum():
    A=int(input("enter the number: "))
    sum=0
    for i in range(A+1):
        sum=sum+i
    print("sum of first N natural No is ",sum)


if __name__=="__main__":
    sum()