factor = int(input("please enter the factor percentage:"))
grade = int(input("please enter your grade"))

gf = ((factor*grade)/100)+grade
print(gf)

sum = grade
sumf = gf
count = 1
countf = 1

for i in range(4):
    factor = int(input("please enter the factor percentage:"))
    grade = int(input("please enter your grade"))

    sum+=grade
    count+=1



    gf = ((factor * grade) / 100) + grade

    sumf +=gf
    countf+=1
    print(gf)

print("the new grade scores average is:",sumf/countf)
print("the previous grade scores average is:",sum/count)
print("the hefresh between the two averages is:",(sumf/countf)-(sum/count))




