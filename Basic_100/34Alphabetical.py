def Alpha_sort(sentence):
    s=sentence.split()
    s.sort()
    return ' '.join(s)
sentence="apple zebra tharun buffalo"
sorted_words=Alpha_sort(sentence)
print("sorted words are : ",sorted_words)

