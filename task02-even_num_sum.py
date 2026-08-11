num=int(input("Enter a number :"))
if num<=0:
    print("Enter a number greater than 0")
else:
    sum_num=0
    count=0
    for i in range(1,num+1):
        if i%2==0:
            sum+=i
            count+=1
    print("Sum Of Even Numbers :",sum)
    print("Count Of Even Numbers :",count)
