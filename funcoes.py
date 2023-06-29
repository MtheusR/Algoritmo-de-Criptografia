import os
import time


def limpar_console():
    if os.name == 'nt':
        _ = os.system('cls')


def print_files(csv_filename):
    print(f"| {csv_filename:<23} | \033[94mSuccessful\033[0m      |")
    print("+-------------------------+-----------------+")
    time.sleep(0.3) 

import time
from tqdm import tqdm
from colorama import init, Fore

def generate_progress_bar(total_iterations, sleep_time=0.01, description="Gerando tabelas", bar_color='blue'):
    init()  # Inicializa a biblioteca colorama

    style = "{l_bar}" + getattr(Fore, bar_color.upper()) + "{bar}" + getattr(Fore, 'RESET') + "|{n_fmt}/{total_fmt} [{postfix}]"

    with tqdm(total=total_iterations, ncols=80, desc=description, bar_format=style) as pbar:
        pbar.set_postfix_str("Loading...")
        pbar.set_description("ARQUIVOS CSV")
        for i in range(total_iterations):
            time.sleep(sleep_time)
            pbar.update(1)
        pbar.colour = 'green'
        pbar.set_postfix_str("Completed")
