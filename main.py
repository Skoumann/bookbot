with open("books/frankenstein.txt") as f:
    file_contents = f.read()
words = file_contents.split()

def word_count():
    print(len(words))

def char_count():
    lowered = file_contents.lower()
    dic = {
    'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 
    'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 
    'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 
    'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
}
    for c in lowered:
        if c in dic:
            dic[c] +=1
    return dic

def print_text():
    print(file_contents)

def print_report():
    charcount = char_count()
    for c in charcount:
        print(f"The '{c}' character was found {charcount[c]} times")

def main():
    print_report()


main()