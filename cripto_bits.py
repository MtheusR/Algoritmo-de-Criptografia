import csv
import os
import random

def limpar_console():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def check_csv_files():
    csv_files = ['key-cripto/alphabet_table_characters_8bits.csv', 'key-cripto/alphabet_table_reversed_7bits.csv', 'key-cripto/alphabet_table_inverted_9bits.csv']
    for csv_file in csv_files:
        if not os.path.isfile(csv_file):
            print(f"Arquivo CSV '{csv_file}' não encontrado. Executando 'chave_cpx'...")
            os.system('python chave_bits.py')
            break

def load_translation_table(csv_file):
    translation_table = {}
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            number = int(row['Decimal'])
            binary = row['Binary']
            if number not in translation_table:
                translation_table[number] = []
            translation_table[number].append(binary)
    return translation_table


def translate_text(text, combinations):
    characters_csv = 'key-cripto/alphabet_table_characters_8bits.csv'
    reversed_csv = 'key-cripto/alphabet_table_reversed_7bits.csv'
    inverted_csv = 'key-cripto/alphabet_table_inverted_9bits.csv'
    
    translation = ""
    character_count = {}

    for char in text:
        if char not in character_count:
            character_count[char] = 1
            bin_code = random.choice(translation_table[8])  # Selecionar código binário aleatório correspondente ao número 8
            bin_code += find_character(char, characters_csv)  # Concatenar o código binário encontrado
        elif character_count[char] == 1:
            character_count[char] += 1
            bin_code = random.choice(translation_table[7])  # Selecionar código binário aleatório correspondente ao número 7
            bin_code += find_character(char, reversed_csv)  # Concatenar o código binário encontrado
        else:
            character_count[char] += 1
            bin_code = random.choice(translation_table[9])  # Selecionar código binário aleatório correspondente ao número 6
            bin_code += find_character(char, inverted_csv)  # Concatenar o código binário encontrado
            del character_count[char]

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

limpar_console()

if __name__ == '__main__':
    check_csv_files()

    # Ler as combinações do arquivo CSV
    translation_table  = load_translation_table('key-cripto/tabs.csv')

    input_text = input("Digite o texto a ser traduzido: ")
    translated_text = translate_text(input_text, translation_table)
    # translated_text = translated_text.replace(" ", "")

    print(f"Texto traduzido: {translated_text}")