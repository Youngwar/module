def single_root_words (root_word, *other_words):
    same_words =[]
    for item in other_words:
        if item.casefold() in root_word.casefold() or root_word.casefold() in item.casefold():
            same_words.append(item)
   
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
