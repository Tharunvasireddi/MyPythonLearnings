def count_vowel(word):
    count=0
    word=word.lower()
    for i in word:
        k=ord(i)
        if k == 97 or k ==101 or k == 105 or k==111 or k==117 :
            count+=1
    return count
my_string=input("enter the string : ")
count=count_vowel(my_string)
print("count of vowels in {0} is : ".format(my_string),count)