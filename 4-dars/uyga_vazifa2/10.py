latin_to_cyrillic = {
    'a': 'а', 'b': 'б', 'c': 'ц', 'd': 'д', 'e': 'е', 
    'f': 'ф', 'g': 'г', 'h': 'х', 'i': 'и', 'j': 'й', 
    'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о', 
    'p': 'п', 'q': 'қ', 'r': 'р', 's': 'с', 't': 'т', 
    'u': 'у', 'v': 'в', 'w': 'ў', 'x': 'кс', 'y': 'й', 
    'z': 'з', ' ': ' '
}

def translate_to_cyrillic(text):
    return ''.join([latin_to_cyrillic.get(char, char) for char in text])

input_text = input("So'z kiritng: ")
output_text = translate_to_cyrillic(input_text)
print(output_text)
