s1="shiva is god we all %$^worship"
s2="SHiva"
thislist=["sachin","viru","yuvi","dhoni","dhoni"]
secondlist=["ronaldo","messi"]
thislist.sort(reverse=True)
print(thislist)
result=sorted(thislist)
print(result)
print(thislist[0].count("d"))
thislist.insert(0,"Raina")
print(thislist)

thislist.extend(secondlist)
print(thislist)
newlist=set(thislist)
print(list(newlist))

l1=["a",1,2,'c',"shiva",1,1,4,1,2]
print("before removing duplicates value",l1)
l2=[]
for i in l1:
    if i  not in l2:
        l2.append(i)
print(list(l2))
my_list = [1,2,2,3,1,4,5,1,2,6]

myFinallist = []
for i in my_list:
     if i not in myFinallist:
        myFinallist.append(i)
print(list(myFinallist))


#This is the program to sum and mul of all elements in list

list1=[1,4,6,8,4,56,34]
sum=0
mult=1
for i in list1:
    sum=sum+i
    mult=mult*i
print("result",sum)
print("result",mult)

#This is the program to find largest number in  all elements in list
#ist method
list1.sort(reverse=True)
print("the largest number is",list1[0])

#second method
max=list1[0]
for a in list1:
    if a>max:
        max=a
print("the largest number is",max)

#smallest number

min=list1[0]
for a in list1:
    if a<min:
        min=a
print("the smallest number is",min)

#Python program to count the number of strings where the string length
# is 2 or more and the first and last character are same from a given list of strings

list4=['aba','bdb','aca','1241']
ctr=0
for word in list4:
    if len(word)>1 and word[0]==word[-1]:
        ctr+=1
print("number is",ctr)

#program to find out weather a list is empty or not

l1=[2]
print(len(l1))
if len(l1)>0:
    print("not empty")
else:
    print("empty")
l2=l1
print(l2)

#Write a Python program to find the list of words that are longer than n from a given list of words.
n=2
myword=[]
str="hello every one how are you"
txt=str.split(" ")
print(txt)
for i in txt:
    if len(i)>2:
        myword.append(i)
print(myword)

#Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
l1=["banana","papaya","apple","mango","straberry","guava"]



