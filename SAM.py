#!/usr/bin/python3
AllManuscripts = ""
AllOutput = ""

Adj = []
Noun = []
Pron = []
Prt = []
Conj = []
Verb = []
Adp = []
Det = []
Adv = []

#print("Imporing...")
try:
    #from nltk.corpus import wordnet as wn
    #Imports, are you reading this, you sure must be a cool guy :D
    import sys, os, io, nltk, random
except:
    print("Okay, something fucked up and you know it, you havent installed the required package. DUDE!")

'''
print("Checking if library is installed.\nIf it isnt I'll install it, takes about 10 minutes, be patient.\n")

save_stdout = sys.stdout
sys.stdout = io.BytesIO()
nltk.download('all')
sys.stdout = save_stdout
'''

print("Loading Manuscripts...")

#Code to combine all text files in ("Stimorol Commercials") folder into one text document and load all the text.
Directory = "Stimorol Commercials"
for filename in os.listdir(Directory):
    AllManuscripts += open(os.path.join(Directory, filename), 'r').read() + ".\n"

#print("Working text\n===============\n"+AllManuscripts+"\n===============\n")

print("Starting to divide words into word classes...")

text = nltk.word_tokenize(AllManuscripts)
result = nltk.pos_tag(text, tagset='universal')

#print(str(result) + "\n") # [('table', 'JJ'), ('table', 'VB'), ('table', 'NN')]

i = 0
while(i < len(result)):
    word = result[i][0]
    wordtype = result[i][1]
    if(wordtype == "NOUN"):
        Noun.append(word)
    elif(wordtype == "ADJ"):
        Adj.append(word)
    elif(wordtype == "PRON"):
        Pron.append(word)
    elif(wordtype == "PRT"):
        Prt.append(word)
    elif(wordtype == "CONJ"):
        Conj.append(word)
    elif(wordtype == "VERB"):
        Verb.append(word)
    elif(wordtype == "ADP"):
        Adp.append(word)
    elif(wordtype == "DET"):
        Det.append(word)
    elif(wordtype == "ADV"):
        Adv.append(word)
    else:
        pass
    i += 1

print("Listing word type statistics:\n")
print("Noun: "+str(len(Noun)))
print("Adj: "+str(len(Adj)))
print("Pron: "+str(len(Pron)))
print("Prt: "+str(len(Prt)))
print("Conj: "+str(len(Conj)))
print("Verb: "+str(len(Verb)))
print("Adp: "+str(len(Adp)))
print("Det: "+str(len(Det)))
print("Adv: "+str(len(Adv)))
print("\n")


print("Learning sentence structure from given material")

structurefile = open("structure", "w")
Sentences = AllManuscripts.split(".")
i = 0
while(i < len(Sentences)):
    tokanized = nltk.word_tokenize(Sentences[i])
    sentence = nltk.pos_tag(tokanized, tagset='universal')
    f = 0
    while(f < len(sentence)):
        try:
            #sentence[f+1]
            if(f == len(sentence)-1):
                structurefile.write(sentence[f][1] + "\n")
            else:
                structurefile.write(sentence[f][1] + "+")
        except:
            structurefile.write(sentence[f][1] + "\n")
        f += 1
    i += 1
structurefile.truncate()
structurefile.close()

print("Sentences built based on learning material:\n")

structureData = open("structure", "r").readlines()
i = 0
while(i < len(structureData)):
    sentenceWithWords = ""
    words = structureData[i].split("+")
    f = 0
    while(f < len(words)):
        if(words[f] == "NOUN"):
            sentenceWithWords += random.choice(Noun)
        elif(words[f] == "ADJ"):
            sentenceWithWords += random.choice(Adj)
        elif(words[f] == "PRON"):
            sentenceWithWords += random.choice(Pron)
        elif(words[f] == "PRT"):
            sentenceWithWords += random.choice(Prt)
        elif(words[f] == "CONJ"):
            sentenceWithWords += random.choice(Conj)
        elif(words[f] == "VERB"):
            sentenceWithWords += random.choice(Verb)
        elif(words[f] == "ADP"):
            sentenceWithWords += random.choice(Adp)
        elif(words[f] == "DET"):
            sentenceWithWords += random.choice(Det)
        elif(words[f] == "ADV"):
            sentenceWithWords += random.choice(Adv)
        try:
            if not(f == len(words)):
                sentenceWithWords += " "
        except:
            pass
        f += 1
    print(sentenceWithWords + ".\n")
    AllOutput += sentenceWithWords + ".\n"
    i += 1


print("\nSentences buildt with custom Structure file:\n")

customStructureData = open("structureCustom.txt", "r").readlines()
i = 0
while(i < len(customStructureData)):
    sentenceWithWords = ""
    try:
        words = customStructureData[i].lower().split("+")
    except:
        break
    f = 0
    while(f < len(words)):
        if(words[f] == "noun"):
            sentenceWithWords += random.choice(Noun)
        elif(words[f] == "adj"):
            sentenceWithWords += random.choice(Adj)
        elif(words[f] == "pron"):
            sentenceWithWords += random.choice(Pron)
        elif(words[f] == "prt"):
            sentenceWithWords += random.choice(Prt)
        elif(words[f] == "conj"):
            sentenceWithWords += random.choice(Conj)
        elif(words[f] == "verb"):
            sentenceWithWords += random.choice(Verb)
        elif(words[f] == "adp"):
            sentenceWithWords += random.choice(Adp)
        elif(words[f] == "det"):
            sentenceWithWords += random.choice(Det)
        elif(words[f] == "adv"):
            sentenceWithWords += random.choice(Adv)
        try:
            words[f+1]
            sentenceWithWords += " "
        except:
            pass
        f += 1
    print(sentenceWithWords + ".\n")
    i += 1

'''
print("Structure: Pron + Noun + Verb + Conj + Noun + Verb + Adv + Adj")
print("Output 1: {0} {1} {2} {3} {4} {5} {6} {7}.".format(random.choice(Pron), random.choice(Noun), random.choice(Verb), random.choice(Conj), random.choice(Noun), random.choice(Verb), random.choice(Adv), random.choice(Adj)))
print("Output 2: {0} {1} {2} {3} {4} {5} {6} {7}.".format(random.choice(Pron), random.choice(Noun), random.choice(Verb), random.choice(Conj), random.choice(Noun), random.choice(Verb), random.choice(Adv), random.choice(Adj)))
print("Output 3: {0} {1} {2} {3} {4} {5} {6} {7}.".format(random.choice(Pron), random.choice(Noun), random.choice(Verb), random.choice(Conj), random.choice(Noun), random.choice(Verb), random.choice(Adv), random.choice(Adj)))
print("Output 4: {0} {1} {2} {3} {4} {5} {6} {7}.".format(random.choice(Pron), random.choice(Noun), random.choice(Verb), random.choice(Conj), random.choice(Noun), random.choice(Verb), random.choice(Adv), random.choice(Adj)))
print("Output 5: {0} {1} {2} {3} {4} {5} {6} {7}.".format(random.choice(Pron), random.choice(Noun), random.choice(Verb), random.choice(Conj), random.choice(Noun), random.choice(Verb), random.choice(Adv), random.choice(Adj)))
'''

try:
    i = 0
    while(i < len(sys.argv)):
        if(sys.argv[i] == "-s" or sys.argv[i] == "/s"):
            open(sys.argv[i+1], "w").write(AllOutput)
        i+=1
except:
    pass
