import csv
import os

def limpar_console():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def check_csv_files():
    csv_files = ['key-cripto/alphabet_table_characters_8bits.csv', 'key-cripto/alphabet_table_reversed_7bits.csv', 'key-cripto/alphabet_table_inverted_6bits.csv']
    for csv_file in csv_files:
        if not os.path.isfile(csv_file):
            print(f"Arquivo CSV '{csv_file}' não encontrado. Executando 'chave_cpx'...")
            os.system('python chave_bits.py')
            break

def translate_text(text):
    characters_csv = 'key-cripto/alphabet_table_characters_8bits.csv'
    reversed_csv = 'key-cripto/alphabet_table_reversed_7bits.csv'
    inverted_csv = 'key-cripto/alphabet_table_inverted_6bits.csv'
    
    translation = ""
    character_count = {}

    for char in text:
        if char not in character_count:
            character_count[char] = 1
            bin_code = find_character(char, characters_csv)
        elif character_count[char] == 1:
            character_count[char] += 1
            bin_code = find_character(char, reversed_csv)
        else:
            character_count[char] += 1
            bin_code = find_character(char, inverted_csv)

        if bin_code is not None:
            translation += bin_code + " "

    return translation

def find_character(char, csv_file):
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            if row[0] == char:
                return row[1]
    return None

def translate_binary(binary_text):
    characters_csv = 'key-cripto/alphabet_table_characters_8bits.csv'
    reversed_csv = 'key-cripto/alphabet_table_reversed_7bits.csv'
    inverted_csv = 'key-cripto/alphabet_table_inverted_6bits.csv'
    
    translation = ""
    character_count = {}

    binary_list = binary_text.split()
    for bin_code in binary_list:
        char = find_binary(bin_code, characters_csv)
        if char is not None:
            if char not in character_count:
                character_count[char] = 1
                translation += char
            elif character_count[char] == 1:
                character_count[char] += 1
                char = find_binary(bin_code, reversed_csv)
                if char is not None:
                    translation += char
            else:
                character_count[char] += 1
                char = find_binary(bin_code, inverted_csv)
                if char is not None:
                    translation += char

    return translation

def find_binary(bin_code, csv_file):
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            if row[1] == bin_code:
                return row[0].strip()  # Remove leading/trailing whitespaces
    return None

limpar_console()

limpar_console()

if __name__ == '__main__':
    check_csv_files()

    input_text = input("Digite o texto a ser traduzido: ")
    translated_text = translate_text(input_text)
    translated_text = translated_text.replace(" ", "")

    print(f"Texto traduzido: {translated_text}")

    translated_binary = translate_binary(translated_text)  # Traduzindo o código binário gerado a partir do texto

    print(f"Código binário traduzido: {translated_binary}")

