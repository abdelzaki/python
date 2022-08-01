from typing import Counter


def mostelemnt():
    words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under']
    count = Counter(words)
    print(count)
    # u can print the most repeated elements 
    print(count.most_common(2))
    # u can get the number of the element using the key
    print(count["eyes"])
mostelemnt()