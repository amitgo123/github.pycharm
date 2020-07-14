num = int(input("please enter a number:"))

if abs(num)<1000 and abs(num)>=100 :

    print("the number is 3 digit length")
    num1 = abs(num)%10
    num2 = abs(num)//10%10
    num3 = abs(num)//100
    sum = num1+num2+num3
    print("the number digits sum is ",sum)

else:
    print("the number is not 3 digits length")