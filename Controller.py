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
            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(categoriaAlterada) if (x.categoria == categoriaAlterar) else [x], x))

            else:
                print('O nome já existe')

        else:
            print('A categoria que deseja alterar nâo existe')

        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.write(i.categoria)
                arq.writelines('\n')
                
        def mostrarCategoria(self):
            categorias = DaoCategoria.ler()
            if len(categorias) == 0:
                 print('Categoria vazia')
            else:
                for i in categorias:
                    print('Categoria {}'.format(i.categoria))

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







