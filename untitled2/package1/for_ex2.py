count=0
sum=0
for i in range(6):
    num=int(input("please enter number"))

    if num%2==0:
        sum = sum + num
        count+=1


else:
    print(sum/count)
    print(sum)
