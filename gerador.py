import csv, os, funcoes, time

def generate_binary_combinations():       
    combinations = []
    decimal_values = [8, 7, 9] * 5  # Alterna entre 8, 7 e 6 para formar 15 combinações
    for i, decimal in enumerate(decimal_values, start=1):
        binary = format(i, '04b')  # Converte o número decimal para binário de 4 bits
        combinations.append((decimal, binary))

    return combinations



def write_combinations_to_csv(combinations):
    # Criação da pasta 'key-cripto'
    folder_name = 'key-cripto'
    os.makedirs(folder_name, exist_ok=True)
    
    file = 'key-cripto/tabs.csv'
    
    with open(file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Decimal', 'Binary'])
        for decimal, binary in combinations:
            writer.writerow([decimal, binary])
            
    funcoes.print_files(file + '  ')

combinations = generate_binary_combinations()
write_combinations_to_csv(combinations)

