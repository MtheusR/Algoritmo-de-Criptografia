import csv
import os

def limpar_console():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def load_alphabet_table(filename):
    alphabet_table = {}

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Pula o cabeçalho da tabela

        for row in reader:
            char = row[0]
            bin_code = row[1]
            alphabet_table[char] = bin_code

    return alphabet_table

def convert_text_to_binary(text, alphabet_table):
    binary_text = ""

    for char in text:
        if char in alphabet_table:
            binary_text += alphabet_table[char] + " "
        else:
            binary_text += char + " "

    return binary_text.strip()

limpar_console()

# if __name__ == '__main__':
#     csv_file = 'alphabet_table.csv'
#     alphabet_table = load_alphabet_table(csv_file)

#     input_text = input("Digite uma frase: ")
#     binary_text = convert_text_to_binary(input_text, alphabet_table)

#     binary_text = binary_text.replace(" ", "")

#     print(f"Código binário correspondente: {binary_text}")
    
def load_binary_table(filename):
    binary_table = {}

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Pula o cabeçalho da tabela

        for row in reader:
            char = row[0]
            bin_code = row[1]
            binary_table[bin_code] = char

    return binary_table

def convert_binary_to_text(binary_text, binary_table):
    text = ""

    binary_codes = binary_text.split()
    for binary_code in binary_codes:
        if binary_code in binary_table:
            text += binary_table[binary_code]
        else:
            text += binary_code

    return text

if __name__ == '__main__':
    csv_file = 'alphabet_table.csv'
    alphabet_table = load_alphabet_table(csv_file)

    input_text = input("Digite uma frase: ")
    
    binary_text = convert_text_to_binary(input_text, alphabet_table)

    binary_table = load_binary_table(csv_file)
    
    decoded_text = convert_binary_to_text(binary_text, binary_table)
    
    print(f"Código binário correspondente: {binary_text}")
    print(f"Texto decodificado: {decoded_text}")