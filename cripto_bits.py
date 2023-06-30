import csv
import os
import random
import sys
import funcoes, main

#Verificando se arquivos estão criados
def check_csv_files():   
    csv_files = ['key-cripto/key8bits.csv', 'key-cripto/key7bits.csv', 'key-cripto/key9bits.csv']
    
    csv_gerador = ['key-cripto/tabs.csv']

    for csv_files in csv_files:
        if not os.path.isfile(csv_files):
            os.system('python chave_bits.py')
            break
    
    for csv_gerador in csv_gerador:
        if not os.path.isfile(csv_gerador):
            os.system('python gerador.py')
        break

#Carregar chaves
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


characters_csv = 'key-cripto/key8bits.csv'
reversed_csv = 'key-cripto/key7bits.csv'
inverted_csv = 'key-cripto/key9bits.csv'

#Criptografar mensagens
def translate_text(text, combinations):
    translation = ""
    character_count = {}

    for char in text:
        try:
            if char not in character_count:
                character_count[char] = 1
                bin_code = random.choice(translation_table[8])
                bin_code += find_character(char, characters_csv)
            elif character_count[char] == 1:
                character_count[char] += 1
                bin_code = random.choice(translation_table[7])
                bin_code += find_character(char, reversed_csv)
                character_count[char] += 1
                bin_code = random.choice(translation_table[9])
                bin_code += find_character(char, inverted_csv)
                del character_count[char]

            if bin_code is not None:
                translation += bin_code + " "
        except:
            # Tratamento de exceção em caso de erro durante o processamento de um número
            print(f"\033[91mErro ao processar o caractere '{char}'.\033[0m")
            input()
            funcoes.limpar_console()
            main.execute()

    return translation


#Carregar separadores
def load_tabs_csv(csv_file):
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        return list(reader)

#Indentificar tamanho e enviar código
def find_character(char, csv_file):
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[0] == char:
                return row[1]
    return None

#Indentificar código e enviar tamanho
def find_character2(char, csv_file):
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            if row[1] == char:
                return row[0]
    return None

#Traduzir mensagem
def traverse_translated_text(translated_text, tabs_csv):
    result = ""
    bits_to_skip = 0

    while bits_to_skip < len(translated_text):
        separator = translated_text[bits_to_skip:bits_to_skip + 4]
        bits_to_skip += 4

        separator_value = None
        for row in tabs_csv:
            if row['Binary'] == separator:
                separator_value = int(row['Decimal'])
                break

        if separator_value is not None:
            binary_code = translated_text[bits_to_skip:bits_to_skip + separator_value]
            
            if separator_value == 8:
                file_csv = characters_csv
            elif separator_value == 7:
                file_csv = reversed_csv
            elif separator_value == 9:
                file_csv = inverted_csv
                
            character = find_character2(binary_code, file_csv)
            if character is not None:
                result += character
 
            bits_to_skip += separator_value

    return result.strip()

input_text = input("Iniciar programa (y/n): ")
resposta = input_text.lower()  

if resposta == "y":
    check_csv_files() 
    tabs_csv = load_tabs_csv('key-cripto/tabs.csv')
    translation_table = load_translation_table('key-cripto/tabs.csv')       
else:
    sys.exit() 
tabs_csv = load_tabs_csv('key-cripto/tabs.csv')
translation_table = load_translation_table('key-cripto/tabs.csv')    