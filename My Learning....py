import math
print(dir(math))

# Get the biggest number function, attetion on paramter expression: *args
def biggest_number(*args):
  print (max(args))
  return max(args)

biggest_number(-10, -5, 5, 10)

# This is for List regular usage
a=['2','3',4,5]
a[::-1] # which reverse the list
a.index('2') #return the first mapped value index number
a.insert(a.index('2'),'5') # in the 3rd place insert one value, all the others moving down by 1
a.sort() # return error as string mixed with number
a.pop(1) # return and remove the index as declared
a.remove('2') # remove based on item value
del(a[1]) # similar with pop without return value

"-".join(a) # make list values joined

# Difference among Bracket, Curly Brace
a = [1,2,3]
b = {'key1' : 1, 'key2' : 2, 'key3' : 3} # Dictionary storage, like login headers with username, password...
b['key1']=5 # change one key
b['key4']=6 # assign new value
del b['key3'] # remove existed value
print (b['key1'])

c = {'key1' : 11, 'key2' : 22, 'key3' : 33}
d=[b,c]
for i in d:
  print (i["key1"],i["key2"],i["key3"])


for i,j in enumerate(a): # Iterate with auto-index and value
  print (i,j)

for i,j in zip(a,b): # Iterate for 2 parellel lists
  print (i,j)

for i in range(5):
  if i>5:
    print i
    break
else: # Else in for loop
  print "no 5"



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



