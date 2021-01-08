def word_to_pig_latin(word):
    if word[0] in "aeiou":
        return word + "way"
    else:
        return word[1:] + word[0] + "ay"

def sentence_to_pig_latin(sentence):
    return " ".join(map(word_to_pig_latin,sentence.split()))
