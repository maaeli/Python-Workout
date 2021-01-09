def word_to_ubbi_dubbi(word):
    for vowel in "uoiea":
        word = word.replace(vowel, f"ub{vowel}" )
    return word
