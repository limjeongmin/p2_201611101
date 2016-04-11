def totalList(x):
    x=list()
    for i in range(1,1000):
        if (i%4==0 and i%5>0):
            x.append(i)
            
    
    total=0
    
    for i in range(0,len(x)):
        total+=x[i]
    return total
print total
  




def lab6():
    print """programming is very fun!"""
    labtotal=totalList(x)
    print labtotal
    
def main():
    lab6()
