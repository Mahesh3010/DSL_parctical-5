"""Expt:5
        Write a python program to compute following operations on string
        1) To display word with the longest length
        2) To determines the frequency of occurrence of particular character        in the string
        3) To check whether given string is palindrome or not
        4) To display index of first appearance of the substring
        5) To count the occurrences of each word in a given string
        6) Exit."""

def one():
    
    str1=input("Enter the string:")
    list1=str1.split()
    m=0
    word=0
    print(list1)
    for i in range(len(list1)):
        len(list1[i])
        if m<len(list1[i]):
            m=len(list[i])
            word=i
    print("a) The word with longest length:",list1[word])

def two():
    str1=input("Enter the string:")
    char = input("Enter character")
    print(str1)
    counter=0
    for i in range(len(str1)):
        if char==str1[i]:
            counter+=1
    print("Character %s is present %i times in the string %s"% (char,counter,str1))

def three():
    str2 = input("Enter string")
    lenstr2=len(str2)
    j=lenstr2-1

    flag=0
    for i in range(int(lenstr2/2+1)):
        if(str2[i]==str2[j]):
            flag=1
        else:
            break
        j=-1

    if(flag==1):
        print("It is Palindrome")
    else:
        print("It is not Palindrome")

def four():
    str1 = input("Enter the string:")
    sub1 = input("Enter substring:")
    sublen=len(sub1)
    index1=1
    j=0
    for i in range(len(str1)):
        if(sub1[j]==str[i]):

            j=j+1
            if(j==sublen):
                index1=i-(sublen-1)
                break
        else:
            j=0
    print("substring index:",index1)

def five():
    str1 = input("Enter the string:")
    list1 = str1.split()
    list2=set(list1)
    list3=list(list2)
    print(list1)
    print(list3)
    list4=[]
    list5=[]
    counter=0
    for i in range(len(list3)):
        counter=0
        for j in range(len(list1)):
            if(list3[i]==list1[j]):
                counter+=1
        list4=list3[i],counter
        list5.append(list4)
    print(list5)

while True:
    ch=int(input("Enter your choice:"))
    if(ch==1):
        one()
    elif (ch==2):
        two()
    elif (ch==3):
        three()
    elif (ch==4):
        four()
    elif (ch==5):
        five()
    elif (ch==6):
        break

