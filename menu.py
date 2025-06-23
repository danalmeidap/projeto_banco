from utils import is_valid_option
from banco import depositar, sacar, exibir_extrato


def menu_banco():
    while True:
        print('''\n
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
        ''')
        
        option = input('Escolha uma opção: ').lower()
        
        if is_valid_option(option):
            if option == 'd':
                depositar()
            elif option == 's':
                sacar()
            elif option == 'e':
                exibir_extrato()
            elif option == 'q':
                print('Saindo do sistema...')
                break