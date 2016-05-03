import matplotlib
import matplotlib.pyplot as plt
def graphCount():
    d=dict()
    sentence=raw_input("input word :")
    for c in sentence:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1

    plt.bar(range(len(d)),d.values(), align='center')
    plt.xticks(range(len(d)), list(d.keys()))
    plt.show()

def numberletter(word):
    d=dict()
    d={"number":0, "word":0}
    for i in word:
        if i.isdigit()==True:
            d["number"]=d["number"]+1
        elif i.isdigit()==False:
            d["word"]=d["word"]+1
    import matplotlib
    import matplotlib.pyplot as plt

    plt.bar(range(len(d)),d.values(), align='center')
    plt.xticks(range(len(d)), list(d.keys()))
    plt.show()

myhome=set()
yourhome=set()
myhome={'TV', 'phone', 'camera', 'fridger', 'mixer', 'audio', 'cd player', 'light', 'computer', 'desk', 'recorder'}
yourhome={'coffee machine', 'radio', 'camera', 'running machine', 'ramp', 'computer', 'chair ', 'recorder'}
def Mhome():
    print myhome.difference(yourhome)
def Yhome():
    print yourhome.difference(myhome)
def Same():
    print myhome.intersection(yourhome)
def MYhome():
    print myhome.union(yourhome)
def Count():
    d=dict()
    for i in myhome:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for i in yourhome:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    print d        
def lab9():
    graphCount()
    word=raw_input("input word")
    numberletter(word)
    Mhome()
    Yhome()
    Same()
    MYhome()
    Count()
def main():
    lab9()

main()

wn.exitoncilck()