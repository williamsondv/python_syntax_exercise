def print_upper_words(words):
    """prints out each word on a seperate line in uppercase"""
    for word in words:
        print(f'{word.upper()}')

def print_upper_words_2(words):
    """prints out each word on a seperate line in uppercase if it begins with e"""
    for word in words:
        if word[0] == 'e' or word[0] == 'E':
           print(f'{word.upper()}')

def print_upper_words_3(words, letters):
    """prints out each word on a seperate line in uppercase if it begins with specified letters"""
    for letter in letters:
        for word in words:
            if word[0] == letter.lower():
                print(f'{word.upper()}')
        

print_upper_words(["escalation", "eschew", "throne", "falcon", "fortress", "nonsense", "calamity", "electable"])
print_upper_words_2(["escalation", "eschew", "throne", "falcon", "fortress", "nonsense", "calamity", "electable"])
print_upper_words_3(["escalation", "eschew", "throne", "falcon", "fortress", "nonsense", "calamity", "electable"], ["f","e"])
print_upper_words_3(["escalation", "eschew", "throne", "falcon", "fortress", "nonsense", "calamity", "electable"], ["t","n"])