import nmap

# joga na variável scanner todos os atributos da biblioteca nmap
scanner = nmap.PortScanner()

print('Seja bem vindo ao meu scanner')
print('<------------------------------------------>')

ip = input('Digite o ip ou host a ser varrido: ')
print('O IP digitado foi: ', ip)
type(ip)

menu = input('''\nEscolha o tipo de varredura a ser realizada
            1 -> Varredura do tipo SYN
            2 -> Varredura do tipo  UDP
            3 -> Varredura do tipo Intensa
            Digite a opção escolhida: ''')

print('A opção escolhida foi: ', menu)

if menu == '1':  # varredura tipo SYS
    print('Versão do Nmap: ', scanner.nmap_version())  # mostra a versão do nmap
    # faz um scanner no ip, nas portas de 1 até 1024 com o modo verbose e com o sym do tipo scan
    scanner.scan(ip, '1-1024', '-v -sS')
    print(scanner.scaninfo())  # mostra todas as informações do scan
    print('Status do IP: ', scanner[ip].state())  # printa o status do IP
    print(scanner[ip].all_protocols())  # printa todos os protocolos abertos
    print('')
    print('Portas abertas: ', scanner[ip]['tcp'].keys())  # pega todas as chaves(portas) tcp abertas nesse ip

elif menu == '2':
    print('Versão do Nmap: ', scanner.nmap_version())  # mostra a versão do nmap
    # faz um scanner no ip, nas portas de 1 até 1024 com o modo verbose e com o sym do tipo udp
    scanner.scan(ip, '1-1024', '-v -sU')
    print(scanner.scaninfo())  # mostra todas as informações do scan
    print('Status do IP: ', scanner[ip].state())  # printa o status do IP
    print(scanner[ip].all_protocols())  # printa todos os protocolos abertos
    print('')
    print('Portas abertas: ', scanner[ip]['udp'].keys())  # pega todas as chaves(portas) tcp abertas nesse ip

elif menu == '3':
    print('Versão do Nmap: ', scanner.nmap_version())  # mostra a versão do nmap
    # faz um scanner no ip, nas portas de 1 até 1024 com o modo verbose e com o sym do tipo intenso
    scanner.scan(ip, '1-1024', '-v -sC')
    print(scanner.scaninfo())  # mostra todas as informações do scan
    print('Status do IP: ', scanner[ip].state())  # printa o status do IP
    print(scanner[ip].all_protocols())  # printa todos os protocolos abertos
    print('')
    print('Portas abertas: ', scanner[ip]['tcp'].keys())  # pega todas as chaves(portas) tcp abertas nesse ip

else:
    print('Escolha uma opção correta!!!')
