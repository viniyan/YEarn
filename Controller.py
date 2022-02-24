from Models import Categoria, Produtos, Estoque, Venda, Fornecedor, Pessoa, Funcionario
from Dao import DaoCategoria, DaoVenda, DaoEstoque, DaoFornecedor, DaoPessoa, DaoFuncionario
from datetime import datetime



class ControllerCategoria:
    def cadastrarCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True
            if not existe:
                DaoCategoria.salvar(novaCategoria)
                print('Categoria cadastrada com sucesso')
            else:
                print('A categoria que deseja cadastrar já existe')


    def removerCategoria(self, categoriaRemover):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaRemover, x))

        if len(cat) <= 0:
            print('A categoria que voce deseja remover nâo existe')
        else:
            for i in range(len(x)):
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    break                             #tira da memória ram
            print('Categoria removida com sucesso')

            with open('categoria.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')              #tira do arquivo de texto "banco de dados"



        estoque = DaoEstoque.ler()
        estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, 'Sem categoria'), x.quantidade) if (x.produto.categoria == categoriaRemover) else (x), estoque))    #quando removermos uma categoria, os produtos ficam com a classificacao 'Sem categoria'

        with open('estoque.txt', 'w') as arq:
            for i in estoque:
                arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' + i.produto.categoria + '|' +str(i.quantidade))
                arq.writelines('\n')


    def alterarCategoria(self, categoriaAlterar, categoriaAlterada):
        x = DaoCategoria.ler()

        cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))

        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))
            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(categoriaAlterada) if (x.categoria == categoriaAlterar) else [x], x))    #Categoria vira categoriaAlterada se x.categoria == categoriaAlterar
                print('Alteração efetuada com sucesso')

                estoque = DaoEstoque.ler()
                estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, categoriaAlterada), x.quantidade)
                                            if (x.produto.categoria == categoriaAlterar) else (x),estoque))  # quando removermos uma categoria, os produtos ficam com a classificacao 'Sem categoria'
                with open('estoque.txt', 'w') as arq:
                    for i in estoque:
                        arq.writelines(i.produto.nome + '|' + i.produto.preco +'|'+ i.produto.categoria +'|'+ i.quantidade)
            else:
                print('O nome já existe')

        else:
            print('A categoria que deseja alterar nâo existe')

        #Para salvar na memória persistente

        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')



    with open('estoque.txt', 'w') as arq:
        for i in estoque:
            arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' + i.produto.categoria + '|' + str(i.quantidade))
            arq.writelines('\n')


    def mostrarCategoria(self):
        categorias = DaoCategoria.ler()
        if len(categorias) == 0:
            print('Categoria vazia')
        else:
            for i in categorias:
                print('Categoria {}'.format(i.categoria))
#TODO: daora né
class ControllerEstoque:
    def cadastrarProduto(self, nome, preco,categoria, quantidade):      #parametros da models
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: y.categoria == categoria, y))
        est = list(filter(lambda x: x.produto.nome == nome, x))

        if len(h) > 0:
            if len(est) == 0:
                produto = Produtos(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print('Produto cadastrado com sucesso')
            else:
                print('Produto já cadastrado em estoque')


        else:
            print('Categoria inexistente')

    def removerProduto(self, nome):
        x = DaoEstoque.ler()
        #o produto existe?
        est = list(filter(lambda x: x.produto.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x[i]
                    break


        else:
            print('O produto que deseja remover nâo existe')

        with open ('estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' +
                               i.produto.categoria + '|'
                               + str(i.quantidade))

    def alterarProduto(self, nomeAlterar, novoNome, novoPreco, novaCategoria, novaQuantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == novaCategoria, y))
        if len(h) > 0:
            est = filter(lambda x: x.produto.nome == nomeAlterar, x)
            if len(est) > 0:
                est = list(filter(lambda x: x.produto.nome == novoNome, x))
                if len(est) == 0:
#transforme a posicao da lista numa instancia de estoque (com os parametros) se o nome da posicao for igual à posicao que quero alterar
                    x = list(map(lambda x: Estoque(Produtos(novoNome, novoPreco, novaCategoria, novaQuantidade) if (x.produto.nome == nomeAlterar) else(x), x)))
                    print('Nome do produto alterado com sucesso')
                else:
                    print('O nome para o qual deseja alterar já existe')

            else:
                print('O nome do produto que deseja alterar nâo existe')

            with open('estoque.txt') as arq:
                for i in x:
                    arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' +
                               i.produto.categoria + '|'
                               + str(i.quantidade))
        else:
            print('A categoria nâo existe')

    def mostrarEstoque(self):
        estoque = DaoEstoque.ler()
        if len(estoque) == 0:
            print('Estoque vazio')
        else:
            print('=========Produto=========')
            print('{}'.format(i.produto.nome), '\n',
                  '{}'.format(i.produto.preco), '\n' '{}'.format(i.produto.categoria), '\n' 
                  '{}'.format(i.quantidade), '\n')

class ControllerVenda:
        def cadastrarVenda(self,nomeProduto, vendedor, comprador, quantidadeVendida):
            '''
            return 1: produto não existe
            return 2: quantidade não existente em estoque
            return 3: venda efetuada

            :param nomeProduto:
            :param vendedor:
            :param comprador:
            :param quantidadeVendida:
            :return:
            '''
            x = DaoEstoque.ler()
            temp = []
            existe = False
            quantidade = False

            for i in x:
                if existe == False:                            #produto existe?
                    if i.produto.nome == nomeProduto:
                        existe = True
                        if i.quantidade >= quantidadeVendida:  #quantidade existe?
                            quantidade = True
                            i.quantidade = int(i.quantidade) - int(i.quantidadeVendida)    #feita a venda, subtraímos do estoque

                            vendido = Venda(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), vendedor, comprador, quantidadeVendida)
                            valorCompra = int(quantidadeVendida) * int(i.produto.preco)

                            DaoVenda.salvar(vendido)

                temp.append([Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade])    #dentro de cada posicao da lista, existe outra lista, sendo a 1 posicao o produto (que possui categoria, preco etc)  e a 2 a quantidade

            arq = open('estoque.txt', 'w')
            arq.write('')

            for i in temp:
                with open('estoque.txt', 'a') as arq:
                    arq.writelines(i.produto.nome + '|' + i.produto.preco +'|'+ i.produto.categoria + '|' + str(i.quantidade))
                    arq.writelines('\n')

            if existe == False:
                return 1

            elif not quantidade:
                return 2
            else:
                return 3, valorCompra

        def relatorioProdutos(self):
            vendas = DaoVenda.ler()

            produtos = []
            for i in vendas:
                nome = i[0]
                quantidade = i[5]
                tamanho = list(filter(lambda x: x['produto'] == nome, produtos))     #ao adicionar a venda de um produto que ja foi vendido antes, esse filtro permite verificar se existe uma venda desse produto
                if len(tamanho) > 0:    #se existe, altera a posicao, somando a quantidade anterior à quantidade atual
                    produtos = list(map(lambda x:{'produto': nome, 'quantidade': int(quantidade) + int(x['quantidade'])} if (x['produto'] == nome) else (x), produtos))

                else:    #se nao existe, cria a posicao dentro da lista
                    produtos.append({'produto': nome, 'quantidade': int(quantidade)})

            ordenado = sorted(produtos, key=lambda k: k['quantidade'], reverse = True) #ordenar os produtos em ordem decrescente
            print('Esses são os produtos mais vendidos')
            a = 1
            for i in ordenado:
                print('==========Produto {} =========='.format(a))
                print('Produto: {}'.format(i['produto']),'\n'  
                      'Quantidade: {}'.format(i['quantidade']),'\n')

        def mostrarVenda(self, dataInicio, dataTermino):
            vendas = DaoVenda.ler()
            dataInicio1 = datetime.strptime(dataInicio, '%d/%m/%Y')
            dataTermino1 = datetime.strptime(dataTermino, '%d/%m/%Y')
            # vendas num determinado período:
            vendasSelecionadas = list(
                filter(lambda x: datetime.strptime(x.data, '%d/%m/%Y')  # convertemos formato string em formato data
                                 >= dataInicio1 and datetime.strptime(x.data, '%d/%m/%Y') <= dataTermino1,
                       vendas))  # passamos como parametro a lista gerada pelo método DaoVenda.ler(), ue esta armazenada na variável vendas
            cont = 1  # contagem de vendas
            total = 0  # contagem do valor das vendas
            for i in vendasSelecionadas:
                print(f'==========Venda [{cont}]==========')
                print(f'Nome: {i.itensVendidos.nome}\n'
                      f'Categoria: {i.itensVendidos.categoria}\n'
                      f'Data: {i.data}\n'
                      f'Quantidade: {i.quantidadeVendida}\n'
                      f'Cliente: {i.comprador}\n'
                      f'Vendedor: {i.vendedor}\n')
                total == int(i.itensVendidos.preco) * int(i.quantidadeVendida)
                cont += 1

                print(f'Total Vendido: {total}')
#TODO: ADICIONAR MÉTODO PARA REMOVER VENDA, RECEBENDO UM ID COMO PARAMETRO

class ControllerFornecedor:

    def cadastrarFornecedor(self, nome, cnpj, telefone, categoria):
        x = DaoFornecedor.ler()
        listaCnpj = list(filter(lambda x: x.cnpj == cnpj, x))
        listaTelefone = list(filter(lambda x: x.telefone == telefone, x))
        if len(listaCnpj) > 0:
            print('O cnpj já existe')
        elif len(listaTelefone) > 0:
            print('O telefone já existe')
        else:
            if len(cnpj) == 14 and len(telefone) <= 11 and len(telefone) >=10:
                DaoFornecedor.salvar(Fornecedor(nome, cnpj, telefone, categoria))
            else:
                print('Digite um cnpj ou telefone válido')

    def alterarFornecedor(self, nomeAlterar, novoNome, novoCnpj, novoTelefone, novaCategoria):
        x = DaoFornecedor.ler()
        h = list(filter(lambda x: x.nome == nomeAlterar, x))                #verificar se o fornecedor já existe
        if len(h) > 0:
            y = list(filter(lambda x: x.nome == novoNome, x))                  #verficar se o fornecedor para o qual desejamos alterar já existe
            if len(y) == 0:
                z = list(map(lambda x: (Fornecedor(novoNome, novoCnpj, novoTelefone, novaCategoria) if (x.nome == novoNome) else(x), x)))
            else:
                print('O nome para o qual deseja alterar já existe')

            with open('estoque.txt') as arq:
                for i in x:
                    arq.writelines(i.nome + '|' + i.telefone + '|' +
                               i.cnpj + '|' + i.categoria)
        else:
             print('O fornecedor que deseja alterar não existe')


    def removerFornecedor(self, fornecedorRemover):
        x = DaoFornecedor.ler()
        est = list(filter(lambda x: x.nome == fornecedorRemover, x))      #verificar se o fornecedor existe
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == fornecedorRemover:
                    del x[i]
                    break
        else:
            print('O fornecedor que deseja remover não existe')

    def mostrarFornecedores(self):
        forn = DaoFornecedor.ler()
        if len(forn) == 0:
            print('Não há fornecedores cadastrados')
        else:
            print('=========Fornecedor=========')
            print('{}'.format(i.nome), '\n',
                  '{}'.format(i.cnpj), '\n' '{}'.format(i.categoria), '\n' 
                  '{}'.format(i.telefone), '\n')


class ControllerCliente:
    def cadastrarCliente(self, nomeCliente, cpf, email, endereco):
        x = Daopessoa.ler()
        listaCpf = list(filter(lambda x: x.cpf == cpf, x))                       #verificar se o cpf já existe
        if len(listaCpf) > 0:
            print('CPF já existente')
        else:
            if len(cpf) == 11 and len(telefone) >= 10 and len(telefone) <= 11:
                DaoPessoa.salvar(Pessoa(nome, telefone, cpf, endereco))
                print('Cliente cadastrado com sucesso')
            else:
                print('Digite um cpf ou telefone válido')

    def alterarCliente(self, clienteAlterar, clienteAlterado, novoNome, novoTelefone, novoCpf, novoEndereco, novoEmail):
        x = DaoPessoa.ler()
        y = list(filter(lambda x: x.nome == clienteAlterar, x))                  #verificar se o cliente existe
        if len(y) > 0:
            y = list(filter(lambda x: x.nome == clienteAlterado, x))             # verficar se o cliente para o qual desejamos alterar já existe
            if len(y) == 0:
                z = list(map(lambda x: (Pessoa(clienteAlterado, novoNome, novoTelefone, novoCpf, novoEndereco, novoEmail) if (x.nome == clienteAlterado) else (x), x)))
            else:
                print('O nome para o qual deseja alterar já existe')

            with open('clientes.txt') as arq:
                for i in x:
                    arq.writelines(i.nome + '|' + i.telefone + '|' +
                                   i.cpf + '|' + i.endereco + '|' + i.email)
        else:
            print('O cliente que deseja alterar não existe')

    def removerCliente(self, clienteRemover):
        x = DaoPessoa.ler()
        est = list(filter(lambda x: x.nome == clienteRemover, x))  # verificar se o cliente existe
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == clienteRemover:
                    del x[i]
                    break
        else:
            print('O fornecedor que deseja remover não existe')

    def mostrarClientes(self):
        cliente = DaoPessoa.ler()
        if len(cliente) == 0:
            print('Não há clientes cadastrados')
        else:
            print('=========Cliente=========')
            print('{}'.format(i.nome), '\n',
                  '{}'.format(i.telefone), '\n' '{}'.format(i.email), '\n' 
                  '{}'.format(i.cpf), '\n'
                  '{}'.format(i.endereco, '\n'))

class ControllerFuncionario:
    def cadastrarFuncionario(self,clt, nomeFuncionario, telefone, cpf, email, endereco):
        x = DaoFuncionario.ler()
        y = list(filter(lambda x: x.nome == nomeFuncionario, x))                      #verificar se o funcionario já existe
        if len(y) == 0:
            if len(cpf) == 11 and len(telefone) >= 10 and len(telefone) <= 11:
                DaoPessoa.salvar(Pessoa(nome, telefone, cpf, endereco))
                print('Cliente cadastrado com sucesso')
            else:
                print('Digite um cpf ou telefone válido')
        else:
            print('O funcionário que deseja cadastrar já existe')

    def alterarFuncionario(self,CPFALTERAR, CPFALTERADO, cltAlterar, cltAlterado, nomeAlterar, nomeAlterado, telefoneAlterar, telefoneAlterado, emailAlterar, emailAlterado, enderecoAlterar, enderecoAlterado):
        x = DaoPessoa.ler()
        y = list(filter(lambda x: x.nome == nomeAlterar))          #verificar se o funcionário já existe
        if len (y) > 0:
            z = list(map(lambda x: (Funcionario(cltAlterado, nomeAlterado, telefoneAlterado, NOVOCPF, novoEndereco, novoEmail) if (x.nome == nomeAlterado and x.cpf == NOVOCPF) else (x), x)))
        else:
            print('O nome que deseja alterar não existe')

        with open('estoque.txt') as arq:
            for i in x:
                arq.writelines(i.nome + '|' + i.telefone + '|' +
                               i.cnpj + '|' + i.categoria)

    def removerFuncionario(self, nome, cpf):
        x = DaoFuncionario.ler()
        est = list(filter(lambda x: x.nome == clienteRemover, x))  # verificar se o cliente existe
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == clienteRemover:
                    del x[i]
                    break
        else:
            print('O fornecedor que deseja remover não existe')

    def mostrarFuncionarios(self):
        func = DaoFuncionario.ler()
        if len(func) == 0:
            print('Não há nenhum funcioário cadastrado')
        else:
            print('=========Funcionário=========')
            print('{}'.format(i.nome), '\n',
                  '{}'.format(i.cpf), '\n' '{}'.format(i.clt), '\n' 
                  '{}'.format(i.telefone), '\n'
                  '{}'.format(i.email), '\n'
                  '{}'.format(i.endereco), '\n')



