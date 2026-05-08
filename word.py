def longest_word(text):
    word = text.split()
    if not word:
        return ""
    return max(word, key=len)
