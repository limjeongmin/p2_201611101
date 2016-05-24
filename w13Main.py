import os
def readword():
    mydir=os.getcwd()
    filename='python.txt'
    myfilename=os.path.join(mydir,filename)
    file=raw_input("Write file name : ")
    try:
        myfile=open(myfilename)
        line=myfile.readline()
        myfile.close()
        print line
        
        myfile=open(myfilename)
        i=0
        for line in range(0,7):
            line=myfile.readline()
            i+=1
            print line
        myfile.close()
        
        word=raw_input("Write word : ")
        myfile=open(myfilename,'r')
        for line in myfile:
            if line.find('python'):
                print line
        myfile.close()
    except IOError as e:
        print e
        

def wordupper(): 
    myfile=open('output.txt','w')
    line1=raw_input("Write line1: ")
    line2=raw_input("Write line2: ")
    myfile2.write(line1+('\n'))
    myfile2.write(('\t')+line2)
    myfile2=open('output.txt','r')
    contents2=myfile2.readlines()
    for s in range(0,len(contents2)):
        print contents2[s].upper
    myfile2.close()
    
def lab13():
    readword()
    wordupper()

def main():
    lab13()
    
main()
raw_input("")