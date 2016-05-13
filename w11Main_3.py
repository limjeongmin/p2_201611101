speech=["Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.",
"Now we are engaged in a great civil war, testing whether that nation, or any nation, so conceived and so dedicated, can long endure.",
"We are met on a great battle-field of that war.We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live.",
"It is altogether fitting and proper that we should do this.But, in a larger sense, we can not dedicate—we can not consecrate—we can not hallow—this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract.",
"The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced.",
"It is rather for us to be here dedicated to the great task remaining before us—that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion—that we here highly resolve that these dead shall not have died in vain—that this nation, under God, shall have a new birth of freedom—and that government of the people, by the people, for the people, shall not perish from the earth."
"]

def countWords(): 
    d = {} 
    for sen in speech: 
        words=sen.split() 
        for word in words: 
            if word in d: 
                d[word]+=1 
            else: 
                d[word]=1 
    return d 
def Frequent(c,d): 
    wordd=list() 
    for i in d: 
        if d[i]>c: 
            wordd.append(i) 
    return wordd 
wordD=countWords() 
Fwords=Frequent(8,wordD) 
print "Licoln speech Frequent words:", Fwords

speech2=["When the bombs fell on our harbor and tyranny threatened the world, she was there to witness a generation rise to greatness and a democracy was saved. Yes, we can.",
"She was there for the buses in Montgomery, the hoses in Birmingham, a bridge in Selma and a preacher from Atlanta who told a people that We Shall Overcome." ,"Yes, we can.",
"A man touched down on the moon, a wall came down in Berlin, a world was connected by our own science and imagination.", "And this year, in this election, she touched her finger to a screen and cast her vote, because after 106 years in America, through the best of times and the darkest of hours, she knows how America can change.", "Yes, we can.",
"America, we have come so far. We have seen so much. But there is so much more to do."," So tonight, let us ask ourselves: If our children should live to see the next century; if my daughters should be so lucky to live as long as Ann Nixon Cooper, what change will they see? What progress will we have made?",
"This is our chance to answer that call. This is our moment.", "This is our time — to put our people back to work and open doors of opportunity for our kids; to restore prosperity and promote the cause of peace; to reclaim the American Dream and reaffirm that fundamental truth that out of many, we are one; that while we breathe, we hope, and where we are met with cynicism, and doubt, and those who tell us that we can't, we will respond with that timeless creed that sums up the spirit of a people: Yes, we can.",
"Thank you, God bless you, and may God bless the United States of America"] 
def OWords(): 
    d = {} 
    for sentence in address: 
        words=sentence.split() 
        for word in words: 
            if word in d: 
                d[word]+=1 
            else: 
                d[word]=1 
    return d 
def UWords(b,d): 
    abc=list() 
    for c in d: 
        if d[c]>b: 
            abc.append(c) 
    return abc 
word=OWords() 
Nword=UWords(23,wordT) 
print "Bush address Frequent words:", Nword 
raw_input()
wn.exitonclick() 
