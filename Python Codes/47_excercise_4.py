# Python program to translate a message into secret code language

st = input("enter message: ")
words = st.split(" ")

# this is for coding
# coding = True

# this for decoding
# coding = False

coding = input("1 for Coding 0 for Decoding")
coding = True if (coding=="1") else False

if(coding):
    nwords = []
    for word in words:
        if(len(word)>=3):
            r1 = "dsf"
            r2 = "jkr"
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords = []
    for word in words:
        if(len(word)>=3):
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))