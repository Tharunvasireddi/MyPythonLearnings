def Count(num):
    if num<=9 and num>=0 :
        return 1
    else:
        count=0
        while num>0:
            count+=1
            num//=10
    return count
num=abs(int(input("enter the number :")))
count=Count(num)
print("the number of digits in {0} is :".format(num),count)
