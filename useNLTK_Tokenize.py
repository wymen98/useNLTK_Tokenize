from nltk.tokenize import sent_tokenize, word_tokenize

mytext = "Hello Mr. Adam, how are you? I hope everything is going well. Today is a good day, see you dude."
#sent_tokenize is use to split out all the sentences
#sent_tokenize(mytext, "english") <<< default if split English word
print(sent_tokenize(mytext))
#word_tokenize is use to split out each of the words in a sentence
print(word_tokenize(mytext))
#now test for French language
mytext2 = "Bonjour M. Adam, comment allez-vous? J'espère que tout va bien. Aujourd'hui est un bon jour."
print(sent_tokenize(mytext2,"french"))

#--------------------------------------------------------------

#Synonyms and Antonyms Part
from nltk.corpus import wordnet

#get the definitions and examples
defi = wordnet.synsets("pain")
print(defi[0].definition())
print(defi[0].examples())

#Here get the synonyms
synonyms = []
for syn in wordnet.synsets('Computer'):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())
print(synonyms)

#Here get the antonyms
antonyms = []
for ant in wordnet.synsets('small'):
    for l in ant.lemmas():
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
print(antonyms)