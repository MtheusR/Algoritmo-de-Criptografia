# #Gerando 3 Chaves
# import csv
# import pandas as pd

# def generate_alphabet_table(filename):
#     # Geração da primeira planilha
#     alphabet_data = []
#     for i in range(25, -1, -1):
#         char_upper = chr(ord('Z') - i)
#         char_lower = chr(ord('z') - i)

#         bin_code_upper = bin(ord(char_upper))[2:][::-1]  # Código binário reverso
#         bin_code_lower = bin(ord(char_lower))[2:][::-1]  # Código binário reverso

#         alphabet_data.append([char_upper, bin_code_upper])
#         alphabet_data.append([char_lower, bin_code_lower])

#     df_alphabet = pd.DataFrame(alphabet_data, columns=["Caractere", "Código Binário"])

#     # Geração da segunda planilha
#     reversed_ascii_bin_data = []
#     for i in range(25, -1, -1):
#         char_upper = chr(ord('Z') - i)
#         char_lower = chr(ord('z') - i)

#         ascii_code_upper = ord(char_upper)
#         ascii_code_lower = ord(char_lower)

#         bin_code_upper = bin(ascii_code_upper)[2:][::-1]  # Código binário reverso
#         bin_code_lower = bin(ascii_code_lower)[2:][::-1]  # Código binário reverso

#         reversed_ascii_bin = bin(ascii_code_upper + int(bin_code_upper, 2))[2:][::-1]  # Soma do código ASCII invertido com o código binário
#         reversed_ascii_bin_data.append([char_upper, reversed_ascii_bin])

#         reversed_ascii_bin = bin(ascii_code_lower + int(bin_code_lower, 2))[2:][::-1]  # Soma do código ASCII invertido com o código binário
#         reversed_ascii_bin_data.append([char_lower, reversed_ascii_bin])

#     df_reversed_ascii_bin = pd.DataFrame(reversed_ascii_bin_data, columns=["Caractere", "CodigoBinarioASCII"])

#     # Geração da terceira planilha
#     inverted_bin_data = []
#     for i in range(25, -1, -1):
#         char_upper = chr(ord('Z') - i)
#         char_lower = chr(ord('z') - i)

#         bin_code_upper = bin(ord(char_upper))[2:]  # Código binário
#         bin_code_lower = bin(ord(char_lower))[2:]  # Código binário

#         inverted_bin_upper = bin_code_upper.replace('0', 'x').replace('1', '0').replace('x', '1')  # Inverte 0 e 1
#         inverted_bin_lower = bin_code_lower.replace('0', 'x').replace('1', '0').replace('x', '1')  # Inverte 0 e 1

#         inverted_bin_data.append([char_upper, inverted_bin_upper])
#         inverted_bin_data.append([char_lower, inverted_bin_lower])

#     df_inverted_bin = pd.DataFrame(inverted_bin_data, columns=["Caractere", "Código Binário Invertido"])

#     # Escrevendo as três planilhas no arquivo Excel
#     with pd.ExcelWriter(filename) as writer:
#         df_alphabet.to_excel(writer, sheet_name='Alphabet', index=False)
#         df_reversed_ascii_bin.to_excel(writer, sheet_name='Alphabet Reversed', index=False)
#         df_inverted_bin.to_excel(writer, sheet_name='Alphabet Inverted Binary', index=False)

#     # Convertendo as sheets em arquivos CSV
#     csv_filename = filename.replace('.xlsx', '')
#     df_alphabet.to_csv(csv_filename + '_alphabet.csv', index=False)
#     df_reversed_ascii_bin.to_csv(csv_filename + '_reversed.csv', index=False)
#     df_inverted_bin.to_csv(csv_filename + '_inverted.csv', index=False)

#     print(f"Tabelas geradas com sucesso nos arquivos {csv_filename}_alphabet.csv, {csv_filename}_reversed.csv e {csv_filename}_inverted.csv")

# if __name__ == '__main__':
#     csv_file = 'alphabet_table.xlsx'  # Nome do arquivo CSV (agora com extensão .xlsx)
#     generate_alphabet_table(csv_file)

import csv
import pandas as pd

def generate_alphabet_table(filename):
    # Geração do primeiro arquivo CSV
    alphabet_data = []
    for i in range(26):
        if i < 26:
            char_upper = chr(ord('A') + i)
            char_lower = chr(ord('a') + i)
            bin_code_upper = bin(ord(char_upper))[2:].zfill(8)  # Código binário de 8 bits
            bin_code_lower = bin(ord(char_lower))[2:].zfill(8)  # Código binário de 8 bits
            alphabet_data.append([char_upper, bin_code_upper])
            alphabet_data.append([char_lower, bin_code_lower])

    char_space = ' '
    bin_space = bin(ord(char_space))[2:].zfill(8)  # Código binário de 8 bits
    alphabet_data.append([char_space, bin_space])

    punctuations = ['.', ',', ';', ':', '!', '?', '"', "'", '(', ')', '[', ']', '{', '}', '-', '_', '/', '\\']
    for punctuation in punctuations:
        bin_punctuation = bin(ord(punctuation))[2:].zfill(8)  # Código binário de 8 bits
        alphabet_data.append([punctuation, bin_punctuation])

    csv_filename1 = filename.replace('.xlsx', '_characters.csv')
    with open(csv_filename1, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Caractere', 'CodigoBinario'])
        writer.writerows(alphabet_data)

    # Geração do segundo arquivo CSV
    reversed_bin_data = []
    for row in alphabet_data:
        char = row[0]
        bin_code = row[1]
        reversed_bin = bin_code[::-1]  # Código binário invertido
        reversed_bin_data.append([char, reversed_bin])

    csv_filename2 = filename.replace('.xlsx', '_reversed.csv')
    with open(csv_filename2, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Caractere', 'CodigoBinario_Invertido'])
        writer.writerows(reversed_bin_data)

    # Geração do terceiro arquivo CSV
    inverted_bin_data = []
    for row in alphabet_data:
        char = row[0]
        bin_code = row[1]
        inverted_bin = bin_code.replace('0', 'x').replace('1', '0').replace('x', '1')  # Inverte 0 e 1
        inverted_bin_data.append([char, inverted_bin])

    csv_filename3 = filename.replace('.xlsx', '_inverted.csv')
    with open(csv_filename3, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Caractere', 'CodigoBinario_Invertido_Trocados'])
        writer.writerows(inverted_bin_data)

    print(f"Tabelas geradas com sucesso nos arquivos {csv_filename1}, {csv_filename2} e {csv_filename3}")

if __name__ == '__main__':
    csv_file = 'alphabet_table.xlsx'  # Nome do arquivo CSV (agora com extensão .xlsx)
    generate_alphabet_table(csv_file)
