import csv
import os
import funcoes
import time

def generate_alphabet_table(filename):
    
    # Criação da pasta 'key-cripto'
    folder_name = 'key-cripto'
    os.makedirs(folder_name, exist_ok=True)
    
    funcoes.limpar_console()
    print();
    funcoes.generate_progress_bar(100, sleep_time=0.01, description="Gerando Tabelas", bar_color='blue')
    print();
    print('+-------------------------------------------+');
    print('|             ARQUIVOS CRIADOS              |');
    print('+-------------------------------------------+');
    time.sleep(0.5) 
    
    # Geração do primeiro arquivo CSV (8)
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

    csv_filename1 = os.path.join(folder_name, filename.replace('.xlsx', '8bits.csv'))
    with open(csv_filename1, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Caractere', 'CodigoBinario'])
        writer.writerows(alphabet_data)
        
        funcoes.print_files(csv_filename1)

    # Geração do segundo arquivo CSV (7)
    reversed_bin_data = []
    for row in alphabet_data:
        char = row[0]
        bin_code = row[1]
        reversed_bin = bin_code[::-1]  # Código binário invertido
        reversed_bin = reversed_bin[:7]  # Mantém apenas os primeiros 7 bits
        reversed_bin_data.append([char, reversed_bin])

    csv_filename2 = os.path.join(folder_name, filename.replace('.xlsx', '7bits.csv'))
    with open(csv_filename2, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Caractere', 'CodigoBinario_Invertido'])
        writer.writerows(reversed_bin_data)
    
        funcoes.print_files(csv_filename2)

    # Geração do terceiro arquivo CSV (9)
    inverted_bin_data = []
    for row in alphabet_data:
        char = row[0]
        bin_code = row[1]
        inverted_bin = bin_code.replace('0', 'x').replace('1', '0').replace('x', '1')  # Inverte 0 e 1
        inverted_bin = inverted_bin[:8]  # Mantém apenas os primeiros 8 bits
        inverted_bin += inverted_bin[0]  # Adiciona o primeiro bit no final
        inverted_bin_data.append([char, inverted_bin])

    csv_filename3 = os.path.join(folder_name, filename.replace('.xlsx', '9bits.csv'))
    with open(csv_filename3, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Caractere', 'CodigoBinario_Invertido_Trocados'])
        writer.writerows(inverted_bin_data)
    
        funcoes.print_files(csv_filename3)

if __name__ == '__main__':
    csv_file = 'key.xlsx'  # Nome do arquivo CSV (agora com extensão .xlsx)
    generate_alphabet_table(csv_file)
