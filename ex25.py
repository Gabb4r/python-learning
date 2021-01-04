def break_words(stuff):
    # This function will break up words for us.
    words = stuff.split(" ")
    return words

def sort_words(words):
    # sorts the words.
    return sorted(words)

def print_first_word(words):
    # will print first word after popping it off
    word = words[0]
    return word

def print_last_word(words):
    # will print last word after popping it off 
    word = words.pop[-1]
    print(word)

def sort_sentence(sentence):
    # takes full statement and sort it
    words = break_words(sentence)
    return sort_words(words)