import re
from collections import Counter

def top_3_words(text):
    text = re.sub(r'[ /][/#:/\\\.\n,]+(?!\w)',' ',text)
    return list(dict(Counter(text.lower().split()).most_common(3)))


def main():
    x = """In a village of La Mancha, the name of which I have no desire to call to
                mind, there lived not long since one of those gentlemen that keep a lance
                in the lance-rack, an old buckler, a lean hack, and a greyhound for
                coursing. An olla of rather more beef than mutton, a salad on most
                nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
                on Sundays, made away with three-quarters of his income."""
    print(top_3_words(x))

    x = "e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"
    print(top_3_words(x))

    x = "  //wont won't won't "
    print(top_3_words(x))

if __name__ == "__main__": main()