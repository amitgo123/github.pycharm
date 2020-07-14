max = 0
sum = 0
count = 0
grade = int(input("please enter your grade:"))

while 0<=grade<=100 :


    count+=1
    if grade>max and 0<=grade<=100:
        max=grade
        sum += grade
    grade = int(input("please enter your grade:"))



print("the highest test score is:",max,"\nthe grade average is: ",sum/count,"\nthe hefresh is:",max-(sum/count) )


