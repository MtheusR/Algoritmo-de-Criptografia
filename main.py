import cripto_bits
import sys
if __name__ == '__main__':

    input_text = input("\n" + chr(8594) + " Digite o texto a ser traduzido: ")
    
    translated_text = cripto_bits.translate_text(input_text, cripto_bits.translation_table)
    translated_text = translated_text.replace(" ", "")

    print(f"\n" + chr(128274) + " Texto criptografado: {" + translated_text + "}")
    input()
    
    input("\n" + chr(8594) + " Deseja descriptografar a mensagem? (y/n): ")
       
    separated_codes = cripto_bits.traverse_translated_text(translated_text, cripto_bits.tabs_csv)

    print(f"\n" + chr(128275) + " Texto traduzido: {" + separated_codes +"}\n")