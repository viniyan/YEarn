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

    def alterarCategoria(self, categoriaAlterar, categoriaAlterada):
        x = DaoCategoria.ler()

        cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))

        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))
            if len(cat) == 0:
                x = list(map(lambda x: Categoria(categoriaAlterada) if (x.categoria == categoriaAlterar) else [x], x))     #Categoria vira categoriaAlterada se x.categoria == categoriaAlterar

            else:
                print('O nome já existe')

        else:
            print('A categoria que deseja alterar nâo existe')

        #Para salvar na memória persistente

        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
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


class ControllerEstoque:
    def cadastrarProduto(self, nome, preco,categoria: Categoria, quantidade):      #parametros da models
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
