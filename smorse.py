#Still part of my learning journey, I stumbled upon a subreddit r/dailyprogrammer
#The code here is a solution to a problem I found on the site.
#Here is the link:
#https://www.reddit.com/r/dailyprogrammer/comments/cmd1hb/20190805_challenge_380_easy_smooshed_morse_code_1/?rdt=63439

#Smooshed morse code
letters = [chr(x) for x in range(97, 123)]
morse_code = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..',
              '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-',
              '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']

alpha_morse = dict(zip(letters, morse_code))


def smorse(n = str):
    """
    The smorse function converts a given string to smorse.
    """
    res_str = ''
    for elem in n:
        if elem in letters:
            res_str += alpha_morse[elem]
        else:
            return
    return res_str

#using listofwords.txt for the bonus challenges
f = open("listofwords.txt")
listofwords = f.readlines()


#According to the sub-problem, smorse(enable1 word list) should yield 1,565,081 '-'
#and 2,499,157 '.'. Here we assert that that is the case.

encodeall = ''
for word in listofwords:
    encodeall += smorse(word.strip())

dash, dot = encodeall.count('-'), encodeall.count('.')

assert dot == 2499157
assert dash == 1565081


#Our program works. We now go ahead and do the sub-problems

#Find the sequence that's the code for only 13 different words
encodedict = {}
for word in listofwords:
    encodedstr = smorse(word.strip())
    
    if encodedstr not in encodedict:
        encodedict.update({encodedstr : 1})
    else:
        encodedict[encodedstr] += 1
    
    if encodedict[encodedstr] == 13:
        print(encodedstr)


#The only word with 15 dashes in a row

fiveteendashes = "---------------"
for word in listofwords:
    encodedstr = smorse(word.strip())

    if encodedstr.find(fiveteendashes) != -1:
        print(word.strip())


#Call a word perfectly balanced if its code has the same number of
#dots as dashes. `counterdemonstrations` is one of two 21-letter words
#that's perfectly balanced. Find the other one.
for word in listofwords:
    if len(word.strip()) == 21:
        encodedstr = smorse(word.strip())

        if encodedstr.count('.') == encodedstr.count('-'):
            print(word.strip())


# protectorate is 12 letters long and encodes to .--..-.----.-.-.----.-..--.,
# which is a palindrome (i.e. the string is the same when reversed).
# Find the only 13-letter word that encodes to a palindrome.
for word in listofwords:
    if len(word.strip()) == 13:
        encodedstr = smorse(word.strip())

        if encodedstr[::-1] == encodedstr:
            print(word.strip())

#--.---.---.-- is one of five 13-character sequences that does not
#appear in the encoding of any word. Find the other four.

print("This last problem may take a while!")
# 1. Build a permutation of - and .
# 2. Search for the permutation in the string
def build_perm(n, sz):
    _thirteenperms = []
    for perm in range(len(n)**sz):
        tempstr = '{:013b}'.format(perm)
        tempstr = tempstr.replace("0", n[0])
        tempstr = tempstr.replace("1", n[1])
        _thirteenperms.append(tempstr)
    return _thirteenperms

thirteenperms = build_perm('.-', 13) #all possible 13-char sequences
all_foundperms = [] #13-char sequences in the listofwords


for word in listofwords:
    encodedstr = smorse(word.strip())

    #check if encodedstr exists in thirteenperms
    if len(encodedstr) >= 13:
        lenx = 0
        while lenx + 13 <= len(encodedstr):
            substr = encodedstr[lenx : lenx + 13]
            
            if substr in thirteenperms:
                all_foundperms.append(substr)
            lenx += 1

#find unique elements in thirteenperms
uniquesequence = []
for pos in range(len(thirteenperms)):
    if thirteenperms[pos] not in all_foundperms:
        uniquesequence.append(thirteenperms[pos])

print(uniquesequence)
