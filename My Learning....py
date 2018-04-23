import datetime

sttime=datetime.datetime.now()

##Calculate prime number
ToInputNum=50000

PriNum=0

PriLst=[]

PriLst.append(2)


a=list(range(ToInputNum))
a.remove(0)
a.remove(1)


##a = [x for x in a if x/a[2] != int(x/a[2]) or x==a[2]]
##a = [x for x in a if x/a[2] != int(x/a[2])]

##b=2
##a = [x for x in a if x/b != int(x/b) or x==b]
##print(a)

while True:

    try:
    
        for i in range(len(a)):

            if i>=len(a): break

            b=a[:i]

            a = [x for x in a[i:] if x/a[i] != int(x/a[i]) or x==a[i]]
            a=b+a

##                a = [x for x in a if x/a[i] != int(x/a[i]) or x==a[i]]


        edtime=datetime.datetime.now()

        print(round((edtime-sttime).total_seconds(),2))

        print("Total Prime Number is "+str(len(a)))

            
        break

    except IndexError:

        print("Oops!  That was no valid number.  Try again...")

        edtime=datetime.datetime.now()

        print(round((edtime-sttime).total_seconds(),2))

        print("Total Prime Number is "+str(len(a)))

        break
            
##    print(a)
    



##
##for a in range(0,ToInputNum,2):
##
##    
##
##    b=a+1
##
##    if b/2!=int(b/2) and b/5!=int(b/5):
##
####        for c in range(int(b/2)):
##        for c in PriLst:
##
##            i=c # previous c+1
##
##            if i>int(b/2): break
##
##            if i!=1 and b/i==int(b/i): break
##
##            if i==PriLst[-1]:
##
##                PriLst.append(c)
##
####            if i==int(b/2):
##
##                PriNum+=1



