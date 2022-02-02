from Models import *

class DaoCategoria:
    @classmethod
    def salvar(cls, categoria):
        with open('categoria.txt', 'a' ) as arq:
            arq.writelines(categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines()

        print(cls.categoria)

        cat = []
        for i in cls.categoria:       #referencia a o parametro da classe Categoria da models
            cat.append(Categoria(i))
        return cat

class DaoVenda:
    @classmethod
    def salvar(cls, venda : Venda):
        with open('vendas.txt', 'a') as arq:
            arq.writelines(venda.itensVendidos.nome + '|' + venda.itensVendidos.preco + '|' +
                           venda.itensVendidos.categoria + '|' + venda.vendedor + '|' +
                           venda.comprador + '|' + str(venda.quantidadeVendida) + '|' + venda.data)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('vendas.txt', 'r' ) as arq:
            cls.venda = arq.readlines()

        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda)) #nao mostrar o \n no terminal
        cls.venda = list(map(lambda x: x.split('|'), cls.venda)) #dividir a lista onde tiver |
        print(cls.venda)
        return cls.venda

class  DaoEstoque:
    @classmethod
    def salvar(cls, produto: Produtos, quantidade):
        with open('estoque.txt', 'a') as arq:
            arq.writelines(produto.nome + '|' + produto.preco + '|' +
                           produto.categoria + '|'
                            + str(quantidade)) 
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('estoque.txt', 'r' ) as arq:
            cls.estoque = arq.readlines()

        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque)) #nao mostrar o \n no terminal
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque)) #dividir a lista onde tiver |
        est = []
        for i in cls.estoque:
            est.append(Estoque(i[0], i[1], i[2], i[3]))


        return est

class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor : Fornecedor):
        with open('fornecedores.txt', 'a') as arq:
            arq.writelines(fornecedor.nome + '|' + fornecedor.cnpj + '|' +
                           fornecedor.categoria + '|' + fornecedor.telefone)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('fornecedores.txt', 'r') as arq:
            cls.fornecedores = arq.readlines()

        cls.fornecedores = list(map(lambda x: x.replace('\n', ''), cls.estoque))  # nao mostrar o \n no terminal
        cls.fornecedores = list(map(lambda x: x.split('|'), cls.estoque))  # dividir a lista onde tiver |
        forn = []
        for i in cls.fornecedores:
            forn.append(Fornecedor(i[0], i[1], i[2], i[3]))

        return forn


class DaoPessoa:
    @classmethod
    def salvar(cls, pessoas: Pessoa):
        with open('clientes.txt', 'a') as arq:
            arq.writelines(pessoas.nome + '|' + pessoas.cpf + '|' +
                          pessoas.email + '|' + pessoas.telefone + '|' + pessoas.endereco)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('clientes.txt', 'r') as arq:
            cls.clientes = arq.readlines()

        cls.clientes = list(map(lambda x: x.replace('\n', ''), cls.estoque))  # nao mostrar o \n no terminal
        cls.clientes = list(map(lambda x: x.split('|'), cls.estoque))  # dividir a lista onde tiver |
        client = []
        for i in cls.clientes:
            client.append(Pessoa(i[0], i[1], i[2], i[3]))

        return client

class DaoFuncionario:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('funcionarios.txt', 'a') as arq:
            arq.writelines(funcionario.clt + '|' + funcionario.nome + '|' +
                          funcionario.email + '|' + funcionario.telefone + '|' +
                           funcionario.endereco + '|' + funcionario.cpf)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('funcionarios.txt', 'r') as arq:
            cls.funcionarios = arq.readlines()

        cls.funcionarios = list(map(lambda x: x.replace('\n', ''), cls.estoque))  # nao mostrar o \n no terminal
        cls.funcionarios = list(map(lambda x: x.split('|'), cls.estoque))  # dividir a lista onde tiver |
        func = []
        for i in cls.funcionarios:
            func.append(Pessoa(i[0], i[1], i[2], i[3]))

        return func





x = Produtos('banana', '5', 'frutas')

y = Venda(x, 'caio', 'marcos', '3')

DaoVenda.salvar(y)
DaoVenda.ler()


