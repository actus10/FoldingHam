import re
from phrase import phrase


def read(txt):
    for k,v in phrase.items():
        txt = (txt).replace(v, k+" ")
    return txt

def write(txt):
    #remove special char for now for POC.
    txt = re.sub("[\']"," ", txt,)
    #print(txt)
    for k, v in phrase.items():
        txt = (txt.lower()).replace(re.sub("[\']"," ", k.lower()), v + " ")

    return txt

if __name__ == "__main__":
    txt = "In this post, we will discuss the importance of Dedup. " \
          "This is a beginner's guide to the subject. " \
          "More things to come"
    w_txt = write(txt)
    r_txt = read(w_txt)
    tl = len(txt)
    w_len = len(w_txt)
    r_len = len(r_txt)
    optimization = w_len/tl
    print(r_txt)
    print(w_txt)
    print(optimization)
    print(r_txt)
