#a=[1,2,3,4,5]
#b=[]
#avg=0
#a.append(30)
#a.insert(1,3)
#a.remove(9)
#print(a)
#if 8 in a:
 #   print("ale")
#else:
 #   print("yelem")
#for i in a:
 #   if i not in b:
 #       b.append(i)
#avg=sum(a)/len(a)
#print("AVG",avg)
head=0
tail=0
#print("MAX",max(a))
from random import randint
from time import sleep

# #print("Min",min(a))

#n = int(input("Enter the no of toss :"))
# for i in range(n):
#  r =randint(1,6)
#  #sleep(1)
#  if r==1:
#      print("1")
#      c1+=1
#  elif r==2:
#     print("2")
#     c2 += 1
#  elif r==3:
#      print("3")
#      c3 += 1
#  elif r==4:
#      print("4")
#      c4 += 1
#  elif r==5:
#      print("5")
#      c5 += 1
#  else:
#      print("6")
#      c6+= 1
# print("one ",c1,"two",c2,"three ", c3,"four ",c4,"five ",c5,"six ",c6)







def myfun ():
    n = int(input("Enter the no of toss :"))
    in1 = int(input("Enter initial :"))
    de = int(input("Enter final : "))
    head = 0
    tail = 0
    for i in range(n):
        r = randint(0, 1)
        if r == 0:
            head += 1
        else:
            tail += 1

        if i>=in1 and i<=de:
         if r==0:
             print(f"{i}= head")
         else:
            print(f"{i}=tail")





    print(" Total Head count is ", head)
    print("Total Tail count is", tail)



def dice():
    n=int(input("Enter the no of roll:"))
    d=[0,0,0,0,0,0]
    for i in range(n):
        r=randint(1,6)
        if r==1:
            d[0]+=1
        elif r==2:
            d[1]+=1
        elif r==3:
            d[2]+=1
        elif r==4:
            d[3]+=1
        elif r==5:
            d[4]+=1
        else:
            d[5]+=1
    print(d)

x=0;
while 1:
    print("Menu")
    print("1.coin")
    print("2.Dice")
    print("3.Exit")
    c = int(input(": "))
    if c == 1:
        myfun()
    elif c==2:
        dice()
    else:
        exit(0)









