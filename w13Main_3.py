﻿def file13_3():
    try:
        fin1=open('python.txt','a')
        fin2=open('outputNum.txt','r')
        for line in fin2:
            fin1.write(line)
        fin1.close()
        fin2.close()
    except Exception as e:
        print e
        
def lab13():
    file13_3()
    
def main():
    lab13()
    
if __name__=="__main__":   
    main()