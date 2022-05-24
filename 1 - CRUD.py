def apresenteSe():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| Nome: Henry Demetrio                                        |')
    print('| Nome: Izabele Vitoria dos Santos                            |')
    print('| Nome: Maria Helena Siqueira dos Santos                      |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+')


def umTexto(solicitacao, mensagem, valido):
    digitouDireito = False
    while not digitouDireito:
        txt = input(solicitacao)

        if txt not in valido:
            print(mensagem, '- Favor redigitar...')
        else:
            digitouDireito = True

    return txt


def opcaoEscolhida(mnu):
    print()

    nroDaOpc = 1
    for opc in mnu:
        print(nroDaOpc, ') ', opc, sep='')
        nroDaOpc += 1

    print()
    return umTexto('Qual é a sua opção? ', 'Opção inválida', [str(opc) for opc in range(1, len(mnu) + 1)])


'''
procura nom em agd e, se achou, retorna:
uma lista contendo True e a posicao onde achou;
MAS, se não achou, retorna:
uma lista contendo False e a posição onde inserir,
aquilo que foi buscado, mas nao foi encontrado,
mantendo a ordenação da lista.
'''


def ondeEsta(nom, agd):
    inicio = 0
    final = len(agd) - 1

    while inicio <= final:
        meio = (inicio + final) // 2

        if nom == agd[meio][0]:
            return [True, meio]
        elif nom < agd[meio][0]:
            final = meio - 1
        else:  # nom>agd[meio][0]
            inicio = meio + 1

    return [False, inicio]


def incluir(agd):
    digitouDireito = False
    while not digitouDireito:
        nome = input('\nNome.......: ')

        resposta = ondeEsta(nome, agd)
        achou = resposta[0]
        posicao = resposta[1]

        if achou:
            print('Pessoa já existente - Favor redigitar...')
        else:
            digitouDireito = True

    aniversario = input('Aniversário: ')
    endereco = input('Endereço...: ')
    telefone = input('Telefone...: ')
    celular = input('Celular....: ')
    email = input('e-mail.....: ')

    contato = [nome, aniversario, endereco, telefone, celular, email]

    agd.insert(posicao, contato)
    print('Cadastro realizado com sucesso!')


def procurar(agd):
    print()
    digitouDireito = False
    while not digitouDireito:
        nome = input('Digite o nome da pessoa que você deseja procurar, ou escreva "menu para voltar":  ')
        if nome == 'menu':
            return
        resposta = ondeEsta(nome, agd)
        achou = resposta[0]
        posicao = resposta[1]
        if not achou:
            print('Pessoa inexistente - Favor redigitar...')

        else:
            digitouDireito = True

    print('Aniversario:', agd[posicao][1])
    print('Endereco...:', agd[posicao][2])
    print('Telefone...:', agd[posicao][3])
    print('Celular....:', agd[posicao][4])
    print('e-mail.....:', agd[posicao][5])


def atualizar(agd):
    digitouDireito = False
    while not digitouDireito:
        pessoa = input('Qual cadastro deseja atualizar? ')

        resposta = ondeEsta(pessoa, agd)
        achou = resposta[0]
        posicao = resposta[1]

        if achou == False or agd == []:
            print('Pessoa inexistente - Favor redigitar...')
        else:
            digitouDireito = True

    print('\n==============Atualizar Agenda====================\n')
    print('\nOpção 1 - Aniversário\nOpção 2 - Endereço\nOpção 3 - Telefone\nOpção 4 - Celular\nOpção 5 - Email')

    while True:

        op = int(input('\nDigite a opção que deseja atualizar: '))

        if op >= 1 or op <= 5:
            break
        else:
            print('Opção inválida, digite novamente!')

    agd[posicao].pop(op)

    dado_atualizado = input('Digite o novo dado da opção selecionada: ')
    agd[posicao].insert(op, dado_atualizado)

    print('Cadastro atualizado com sucesso!\n')
    print('------------------------------------')
    print('Aniversario:', agd[posicao][1])
    print('Endereco...:', agd[posicao][2])
    print('Telefone...:', agd[posicao][3])
    print('Celular....:', agd[posicao][4])
    print('e-mail.....:', agd[posicao][5])


def listar(agd):
    if agd == []:
        print('A agenda não possui pessoas cadastradas!')
    else:
        for contato in agd:
            print('\nNome.......:', contato[0])
            print('Aniversário:', contato[1])
            print('Endereço...:', contato[2])
            print('Telefone...:', contato[3])
            print('Celular....:', contato[4])
            print('e-mail.....:', contato[5])
        '''
        posicao=0
        while posicao<len(agd):
            print('\nNome.......:',agd[posicao][0])
            print('Aniversário:',agd[posicao][1])
            print('Endereço...:',agd[posicao][2])
            print('Telefone...:',agd[posicao][3])
            print('Celular....:',agd[posicao][4])
            print('e-mail.....:',agd[posicao][5])
            posicao+=1
        '''


def excluir(agd):
    print()

    digitouDireito = False
    while not digitouDireito:
        nome = input('Nome.......: ')

        resposta = ondeEsta(nome, agd)
        achou = resposta[0]
        posicao = resposta[1]

        if not achou:
            print('Pessoa inexistente - Favor redigitar...')
        else:
            digitouDireito = True

    print('Aniversario:', agd[posicao][1])
    print('Endereco...:', agd[posicao][2])
    print('Telefone...:', agd[posicao][3])
    print('Celular....:', agd[posicao][4])
    print('e-mail.....:', agd[posicao][5])

    resposta = umTexto('Deseja realmente excluir? ', 'Você deve digitar S ou N', ['s', 'S', 'n', 'N'])

    if resposta in ['s', 'S']:
        del agd[posicao]
        print('Remoção realizada com sucesso!')
    else:
        print('Remoção não realizada!')


# daqui para cima, definimos subprogramas
# daqui para baixo, implementamos o programa (nosso CRUD, C=create(inserir), R=read(recuperar), U=update(atualizar), D=delete(remover,apagar)

apresenteSe()

agenda = []

menu = ['Incluir Contato', \
        'Procurar Contato', \
        'Atualizar Contato', \
        'Listar Contatos', \
        'Excluir Contato', \
        'Sair do Programa'];

opcao = None
while opcao != 6:
    opcao = int(opcaoEscolhida(menu))

    if opcao == 1:
        incluir(agenda)
    elif opcao == 2:
        procurar(agenda)
    elif opcao == 3:
        atualizar(agenda)
    elif opcao == 4:
        listar(agenda)
    elif opcao == 5:
        excluir(agenda)

print('OBRIGADO POR USAR ESTE PROGRAMA!')