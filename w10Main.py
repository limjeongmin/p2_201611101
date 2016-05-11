 ﻿def coffee():
 
 
 
     allData=list()
 
 
 
     allData=[["Coffee","Water","Milk","Icecream"],
 
     ["Espresso","No","No","No"],
 
     ["Long Black","Yes","No","No"],
 
     ["Flat White","No","Yes","No"],
 
     ["Cappuccino","No","Yes - Frothy","No"],
 
     ["Affogato","No","No","Yes"]]
 
 
 
     for i in range(1,len(allData)):
 
         print allData[i]
 
     data=allData[1:]
 
 
 
     milk=0
 
     nomilk=0
 
 
 
     for c in data:
 
         if c[2]=="No":
 
             nomilk=nomilk+1
 
         else:
 
             milk=milk+1
 
 
 
     print "milk :",float(milk)/len(data)*100,"%"," nomilk :",float(nomilk)/len(data)*100,"%"
 
 
 
 
 
 def score():
 
     res=list()
 
     res=[['English', 100], ['Math', 200], ['English', 200], ['Math', 200], ['English', 100], ['Math', 300]]
 
     sum_Eng=0
 
     sum_Math=0
 
     len_Eng=0
 
     len_Math=0
 
     for i in result:
 
         if i[0]=='English':
 
             sum_Eng=sum_Eng+i[1]
 
             len_Eng=len_Eng+1
 
         else:
 
             sum_Math=sum_Math+i[1]
 
             len_Math=len_Math+1
 
     average_Eng=sum_Eng/len_Eng
 
     average_Math=sum_Math/len_Math
 
     print ("English Sum: ", sum_Eng)
 
     print ("Math Sum: ", sum_Math)
 
     print ("English Average: ", average_E)
 
     print ("Math Average: ", average_Eng)
 
 
 
 def gasa():
 
     lyrics=list()
 
     lyrics=['When I find myself in times of trouble',
 
     'Mother Mary comes to me',
 
     'Speaking words of wisdom let it be',
 
     'And in my hour of darkness',
 
     'She is standing right in front of me',
 
     'Speaking words of wisdom let it be',
 
     'Let it be let it be',
 
     'Let it be let it be',
 
     'Whisper words of wisdom let it be',
 
     'And when the broken-hearted people',
 
     'Living in the world agree',
 
     'There will be an answer let it be',
 
     'For though they may be parted',
 
     'There is still a chance that they will see',
 
     'There will be an answer let it be',
 
     'Let it be let it be',
 
     'Let it be let it be',
 
     'Yeah there will be an answer let it be',
 
     'Let it be let it be',
 
     'Let it be let it be',
 
     'Whisper words of wisdom let it be',
 
     'Let it be let it be',
 
     'Ah let it be yeah let it be',
 
     'Whisper words of wisdom let it be',
 
     'And when the night is cloudy',
 
     'There is still a light that shines on me',
 
     'Shine on until tomorrow let it be',
 
     'I wake up to the sound of music',
 
     'Mother Mary comes to me',
 
     'Speaking words of wisdom let it be',
 
     'Let it be let it be',
 
     'Let it be yeah let it be',
 
     'Oh there will be an answer let it be',
 
     'Let it be let it be',
 
     'Let it be yeah let it be',
 
     'Whisper words of wisdom let it be']
 
     d=dict()
 
     for line in lyrics:
 
         for i in line.split():
 
             if i not in d:
 
                 d[c]=1
 
             else:
 
                 d[c]=d[c]+1
 
     print d
 
     for c in range(len(d)):
 
         if d.values()[c]>=20:
 
             print d.keys()[c],d.values()[c]
 
 
 
 def lab10():
 
     coffee()
 
     score()
 
     gasa()
 
 
 
 def main():
 
     lab10()
 
 main()
 
 if __name__=="__main__":
 
     main()
 
wn.exitonclick()