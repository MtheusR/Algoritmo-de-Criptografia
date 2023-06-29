# import csv
# import os

# def generate_binary_combinations():
#     combinations = []
#     for i in range(2 ** 3):
#         binary = bin(i)[2:].zfill(3)
#         if binary.count('0') != 3 and binary.count('1') != 3:
#             combinations.append(binary)
#     return combinations

# def write_combinations_to_csv(combinations):
#     folder_path = 'key-cripto'
#     os.makedirs(folder_path, exist_ok=True)
#     file_path = os.path.join(folder_path, 'tabs.csv')
#     with open(file_path, 'w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(['Number', 'Binary'])
#         for combination in combinations:
#             writer.writerow(['8', combination])
#             writer.writerow(['7', combination])
#             writer.writerow(['6', combination])

# # Gerar as combinações
# combinations = generate_binary_combinations()

# # Escrever as combinações em um arquivo CSV dentro da pasta key-cripto
# write_combinations_to_csv(combinations)

# print("Arquivo separadores.csv gerado com sucesso dentro da pasta key-cripto!")


import csv

def generate_binary_combinations():
    combinations = []
    decimal_values = [8, 7, 9] * 5  # Alterna entre 8, 7 e 6 para formar 15 combinações
    for i, decimal in enumerate(decimal_values, start=1):
        binary = format(i, '04b')  # Converte o número decimal para binário de 4 bits
        combinations.append((decimal, binary))
    return combinations

def write_combinations_to_csv(combinations):
    with open('key-cripto/tabs.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Decimal', 'Binary'])
        for decimal, binary in combinations:
            writer.writerow([decimal, binary])

combinations = generate_binary_combinations()
write_combinations_to_csv(combinations)

