#Caesar cipher implementation
#https://www.reddit.com/r/dailyprogrammer/comments/t33vi/522012_challenge_47_easy/
import re as regex

def encode_caesar(instr:str, n:int):
    """
    Encode a piece of text using caesar cipher. Returns a ciphertext.
    instr - string to encode
    n - key
    """
    if(n > 26):
        return ''
    cipher = ''
    for elem in instr:
        #Handle CAPs
        if (ord(elem) > 64) and (ord(elem) < 91):
            x = ord(elem) + n
            if x > 90:
                x -= 26
            cipher += chr(x)
        #Handle small
        elif (ord(elem) > 96) and (ord(elem) < 123):
            x = ord(elem) + n
            if x > 122:
                x -= 26
            cipher += chr(x)
        #Handle non-alphanumeric
        else:
            cipher += elem

    return cipher

#decode caesar ciphertext
def decode_caesar(ciphertext:str):
    """
    Decode a piece of caesar cipher ciphertext. It returns a dictionary containing all
    probable plaintexts of the ciphertext and the keys that found them.
    """
    #Use a `listofwords` file to perform a brute-force deciphering by
    #checking every decoded string for a possible match in the listofwords
    #dictionary.
    f = open(r"listofwords.txt")
    lines = f.readlines()

    #probable matches.... {key:key, value:encoded_string}
    probables = {}

    #Assumes the key is among the 26-letters of the alphabet
    for key in range(0, 27):
        outstr = encode_caesar(ciphertext, key)

        parts = outstr.split()

        for x in range(len(parts)):
            if len(parts[x]) > 3:
                pr = regex.sub(r'[\W_]+', '', parts[x]) + '\n'

                if pr.lower() in lines:
                    probables.update({key:outstr})
                break
            else:
                continue

    return probables

#The string given in the problem  linked 
                
s = "Spzalu - zayhunl dvtlu sfpun pu wvukz kpzaypibapun zdvykz pz uv ihzpz mvy h "\
        "zfzalt vm nvclyutlua.  Zbwyltl leljbapcl wvdly klypclz myvt h thukhal myvt aol "\
        "thzzlz, uva myvt zvtl mhyjpjhs hxbhapj jlyltvuf. Fvb jhu'a lewlja av dplsk "\
        "zbwyltl leljbapcl wvdly qbza 'jhbzl zvtl dhalyf ahya aoyld h zdvyk ha fvb! P "\
        "tlhu, pm P dlua hyvbuk zhfpu' P dhz hu ltwlylyvy qbza iljhbzl zvtl tvpzalulk "\
        "ipua ohk sviilk h zjptpahy ha tl aolf'k wba tl hdhf!... Ho, huk uvd dl zll aol "\
        "cpvslujl puolylua pu aol zfzalt! Jvtl zll aol cpvslujl puolylua pu aol zfzalt! "\
        "Olsw! Olsw! P't ilpun ylwylzzlk!"


#Can also be used to decipher the Zen of Python
#from this import s

print(decode_caesar(s))
