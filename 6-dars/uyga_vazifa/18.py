taqiqlangan = ["salom", "eshmat", "toshmat", "dunyo", "noutbuk"]

def replace_words(text):
    words = text.split()
    for i, word in enumerate(words):
        if word in taqiqlangan:
            words[i] = '*' * len(word)
    return ' '.join(words)

text = "Salom do’stim eshmat bugun men yangi noutbuk sotib oldim"
print(replace_words(text))
