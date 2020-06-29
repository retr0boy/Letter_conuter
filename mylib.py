from chardet.universaldetector import UniversalDetector
def count_ru_letters(text):
    first = 0
    last = 0
    for i in range(0,10000):
        if chr(i) == 'А':
            first = i
        elif chr(i) == 'я':
            last = i
            break
    alphabet=[]
    for i in range(first,last+1):
        alphabet.append(chr(i))
    for i in range(0,10000):
        if chr(i) == 'Ё':
            alphabet.append(chr(i))
        elif chr(i) == 'ё':
            alphabet.append(chr(i))
            break
    alphabet.insert(alphabet.index('е')+1,alphabet.pop(- 1))
    alphabet.insert(alphabet.index('Е')+1,alphabet.pop(-1))
    counter={}
    for letter in alphabet:
        n=text.count(letter)
        if n!=0:
            counter[letter]=n
    return counter
def detect_encoding(filename):
    detector = UniversalDetector()
    with open(filename, 'rb') as fh:
        for line in fh:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
    return detector.result
