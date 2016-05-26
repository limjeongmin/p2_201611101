import time  
def editUpper():  
    File=open('output.txt','w')  
    line1='first line\n'  
    File.write(line1)  
    line2='sceond line\n'  
    File.write(line2)  
    line3='third'  
    File.write(line3)  
    File.close()  
    fin=open('output.txt','r')  
    fout=open('outputUpper.txt','w')  
    for line in fin:  
        words=line.split()  
        for word in words:  
            if word=='line':   
                word=word.upper()  
                word+='[ljm edited {0}]' .format(time.strftime('%Y-%m-%d %H:%M:%S'))  

 
  
            #print word,  
            fout.write(word)  
        print word  
        fout.write('\n')  
    fin.close()  
    fout.close()  

def data():
    data=[1,2,3,4,5,6,7,8,9,10]  
    fout=open('ljm.txt', 'w')  
    for i in data:  
        str="{0}\t".format(i)  
        fout.write(str)  
        if i%2==0:  
            fout.write('\n')  
    fout.close()  

def lab13(): 
    editUpper() 
    data() 

def main(): 
    lab13() 

main()