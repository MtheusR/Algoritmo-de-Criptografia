#Comdando GPT:
# Crie uma tabela onde eu possa exportar pro excel: 
# O alfabeto maiusculo e minusculo usando o codigo binario de trás pra frente da tabela asci 

import csv

def generate_alphabet_table(filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)

        # Cabeçalho da tabela
        writer.writerow(["Caractere", "Código Binário"])

        # Geração do alfabeto maiúsculo e minúsculo em código binário reverso
        for i in range(25, -1, -1):
            char_upper = chr(ord('Z') - i)
            char_lower = chr(ord('z') - i)

            bin_code_upper = bin(ord(char_upper))[2:][::-1]  # Código binário reverso
            bin_code_lower = bin(ord(char_lower))[2:][::-1]  # Código binário reverso

            writer.writerow([char_upper, bin_code_upper])
            writer.writerow([char_lower, bin_code_lower])

        # Geração de caracteres especiais
        special_chars = [' ', ',', '.', '?', '!', ':', ';', '"', "'", '(', ')', '[', ']', '{', '}', '<', '>']
        for char in special_chars:
            bin_code = bin(ord(char))[2:][::-1]  # Código binário reverso
            writer.writerow([char, bin_code])

        # Geração de acentos
        accents = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'â': 'a', 'ê': 'e', 'ô': 'o', 'û': 'u'}
        for accent, base_char in accents.items():
            bin_code_accent = bin(ord(accent))[2:][::-1]  # Código binário reverso
            bin_code_base = bin(ord(base_char))[2:][::-1]  # Código binário reverso
            writer.writerow([accent, bin_code_accent])
            writer.writerow([base_char, bin_code_base])

    print(f"Tabela do alfabeto gerada com sucesso em {filename}")

if __name__ == '__main__':
    csv_file = 'alphabet_table.csv'  # Nome do arquivo CSV
    generate_alphabet_table(csv_file)