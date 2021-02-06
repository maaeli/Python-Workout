from typing import Dict, List

def create_occurence_dic(myword: str) -> Dict[str, int]:
    occurence_dic = {}
    for character in myword:
        try:
            occurence_dic[character] += 1
        except KeyError:
            occurence_dic[character] = 1
    return occurence_dic

def get_word_with_the_most_letters(word_list: List[str]) -> str:
    numbers_of_repeated_letters_kv = [(word, max(create_occurence_dic(word))) for word in word_list]
    return max(numbers_of_repeated_letters_kv, key=lambda pair: pair[1])[0]
