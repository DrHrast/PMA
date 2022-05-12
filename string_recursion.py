def rec_string(text, word, index = 0, counter = 0):
    if len(text) - index <= 1:
        print(f"U tekstu se nalazi {counter} puta riječ '{word}'.")
        return
    elif text[index:index + len(word)] == word:
        counter += 1
        rec_string(text, word, index + len(word), counter)
    else:
        rec_string(text, word, index + 1, counter)

string1 = 'abcdaefdaghidajkl'
string2 = 'da mi je biti morski pas, plivao bih dalje dalje...'

rec_string(string1, 'da')
rec_string(string2, 'da')
