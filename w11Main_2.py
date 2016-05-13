def survey(): 
    DataA=[ 
        [13.1, 37.1], 
        [10.6, 34.6], 
        [27.1, 40.0], 
        [16.2, 37.8], 
        [11.4, 29.8], 
        [12.2, 26.5], 
        [13.5, 29.7], 
        [13.7, 37.6]] 
    DataB=[ 
        [8.7, 1.5], 
        [13.4, 1.9], 
        [2.9, 1.5], 
        [6.8, 0.8], 
        [14.8, 4.9], 
        [14.9, 4.4], 
        [11.1, 2.4], 
        [4.1, 1.2]] 
 
 
    sumA=0 
    sumB=0 


    for i in DataA: 
        sumA=i[0]+i[1] 
 
 
    for s in DataB: 
        sumB=s[0]+s[1] 
 
 
 
 
    print "sum of Satisfaction :",sumA 
    print "sum of Unsatisfaction :",sumB 
    print "average of Satisfaction :",float(sumA/len(DataA)) 
    print "average of Satisfaction :",float(sumB/len(DataB)) 
 
 
def lab11_2(): 
    survey() 
 
 
def main():  
    lab11_2() 
 
 
if __name__=="__main__": 
    main() 
 
 
raw_input()
wn.exitonclick() 