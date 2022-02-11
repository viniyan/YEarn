import Controller
import os.path

def criaArquivos(*nome):                            #para que o usário não precise criar os arquivos (banco de dados) à mão
    for i in nome:
        if not os.path.exists(i):
            with open('i', 'w') as arq:
                arq.write('')

criaArquivos('categoria.txt', 'clientes.txt', 'estoque.txt', 'fornecedores.txt', 'funcionarios.txt', 'vendas.txt')

if __name__ == '__main__':                         #essa condicao serve para que tudo dentro da funcao só seja executado dentro do arquivo View.py. Se tentarmos importar esse arquivo em outro, não vai rodar
    while True:
        local = int(input('Digite 1 para acessar ( Categorias )\n'
                          'Digite 2 para acessar ( Estoque )\n'
                          'Digite 3 para acessar ( Fornecedor )\n'
                          'Digite 4 para acessar ( Cliente )\n'
                          'Digite 5 para acessar ( Funcionario )\n'
                          'Digite 6 para acessar ( Vendas )\n'
                          'Digite 8 para sair\n'))

        if local == 1:
            cat = Controller.ControllerCategoria()
            while True:
                decidir = int(input('Digite 1 para cadastrar uma categoria\n'
                                    'Digite 2 para remover uma categoria\n'
                                    'Digite 3 para alterar uma categoria\n'
                                    'Digite 4 para ver as categorias\n'
                                    'Digite 5 para sair\n'))

                if decidir == 1:
                    categoria = input('Digite a categoria que deseja cadastrar\n')
                    cat.cadastrarCategoria(categoria)
                elif decidir == 2:
                    categoria = input('Digite a categoria que deseja remover\n')
                    cat.removerCategoria(categoria)
                elif decidir == 3:
                    categoria = input('Digite a categoria que deseja alterar\n')
                    novaCategoria = input('Digite o nome para o qual deseja alterar\n')
                    cat.alterarCategoria(categoria, novaCategoria)
                elif decidir == 4:
                    categoria = input('Estas são as categorias:\n')
                    cat.mostrarCategoria()
                else:
                    break

        if local == 2:
            cat = Controller.ControllerEstoque()
            while True:
                decidir = int(input('Digite 1 para cadastrar um produto'
                                    'Digite 2 para remover um produto\n'
                                    'Digite 3 para alterar um produto\n'
                                    'Digite 4 para ver o estoque\n'
                                    'Digite 5 para sair\n'))

                if decidir == 1:
                    nome = input('Digite o nome do produto que deseja cadastrar\n')
                    preco = int(input('Digite o valor do produto que deseja cadastrar'))
                    categoria = input('Digite a categoria do produto que deseja cadastrar')
                    quantidade = int(input('Digite a quantidade do produto que deseja cadastrar'))
                    cat.cadastrarProduto(nome, preco, categoria, quantidade)
                elif decidir == 2:
                    nome = input('Digite o nome do produto que deseja remover\n')
                    cat.removerProduto(nome)
                elif decidir == 3:
                    nomeAntes = input('Digite o produto que deseja alterar\n')
                    nomeDepois = input('Digite o nome para o qual deseja alterar\n')
                    novoPreco = float(input('Digite o preço deste produto'))
                    novaQuantidade = int(input('Digite a quantidade deste produto'))
                    novaCategoria = input('Digite a categoria deste produto')
                    cat.alterarProduto(nomeAntes, nomeDepois, novoPreco, novaQuantidade, novaCategoria)
                elif decidir == 4:
                    produto = input('Estes são os produtos em estoque:\n')
                    cat.mostrarEstoque()
                else:
                    break

        if local == 3:
            cat = Controller.ControllerFornecedor()
            while True:
                decidir = int(input('Digite 1 para cadastrar um fornecedor'
                                    'Digite 2 para remover um fornecedor\n'
                                    'Digite 3 para alterar um fornecedor\n'
                                    'Digite 4 para ver os fornecedores\n'
                                    'Digite 5 para sair\n'))

                if decidir == 1:
                    nome = input('Digite o nome do fornecedor que deseja cadastrar\n')
                    cnpj = input('Digite o cnpj do fornecedor que deseja cadastrar')
                    telefone = input('Digite o telefone do fornecedor')
                    categoria = input('Digite a categoria do fornecedor')
                    cat.cadastrarFornecedor(nome, cnpj, telefone, categoria)
                elif decidir == 2:
                    nome = input('Digite o fornecedor que deseja remover\n')
                    cat.removerFornecedor(fornecedor)
                elif decidir == 3:
                    nomeAntes = input('Digite o fornecedor que deseja alterar\n')
                    nomeDepois = input('Digite o nome para o qual deseja alterar\n')
                    novoCnpj = input('Digite o cnpj do fornecedor')
                    novoTelefone= input('Digite o telefone do fornecedor')
                    novaCategoria = input('Digite a categoria do fornecedor')
                    cat.alterarFornecedor(nomeAntes, nomeDepois, novoCnpj, novoTelefone, novaCategoria)
                elif decidir == 4:
                    fornecedor = input('Estes são os fornecedores cadastrados:\n')
                    cat.mostrarFornecedores()
                else:
                    break

        if local == 4:
            cat = Controller.ControllerCliente()
            while True:
                decidir = int(input('Digite 1 para cadastrar um cliente'
                                    'Digite 2 para remover um cliente\n'
                                    'Digite 3 para alterar um cliente\n'
                                    'Digite 4 para ver o cliente\n'
                                    'Digite 5 para sair\n'))

                if decidir == 1:
                    nome = input('Digite o nome do cliente que deseja cadastrar\n')
                    cpf = input('Digite o cpf do cliente que deseja cadastrar')
                    email = input('Digite o email do cliente que deseja cadastrar')
                    endereco = input('Digite o endereço do cliente que deseja cadastrar')
                    cat.cadastrarCliente(nome, cpf, email, endereco)
                elif decidir == 2:
                    nome = input('Digite o cliente que deseja remover\n')
                    cat.removerCliente(nome)
                elif decidir == 3:
                    nomeAntes = input('Digite o cliente que deseja alterar\n')
                    nomeDepis = input('Digite o nome para o qual deseja alterar\n')
                    novoTelefone = input('Digite o telefone do cliente')
                    novoCpf = input('Digite o cpf do cliente')
                    novoEndereco = input('Digite o endereço do cliente')
                    novoEmail = input('Digite o e-mail do cliente')
                    cat.alterarCliente(nomeAntes, nomeDepois, novoTelefone, novoCpf, novoEndereco, novoEmail)
                elif decidir == 4:
                    cliente = input('Estes são os clientes cadastrados:\n')
                    cat.mostrarClientes()
                else:
                    break

        if local == 5:
            cat = Controller.ControllerFuncionario()
            while True:
                decidir = int(input('Digite 1 para cadastrar um funcionario'
                                    'Digite 2 para remover um funcionario\n'
                                    'Digite 3 para alterar um funcionario\n'
                                    'Digite 4 para ver o funcionario\n'
                                    'Digite 5 para sair\n'))

                if decidir == 1:
                    nome = input('Digite o nome do funcionário que deseja cadastrar \n')
                    clt = input('Digite o número da carteira de trabalho')
                    telefone = input('Digite o funcionário que deseja alterar \n')
                    nomeAntes = input('Digite o nome atual do fute o telefone')
                    cpf = input('Digite o cpf')
                    email = input('Digite o email')
                    endereco = input('Digite o endereco')
                    cat.cadastrarFuncionario(nome, clt, telefone, cpf, email, endereco)
                elif decidir == 2:
                    func = input('Digite o cpf e nome do funcionário que deseja remover\n')
                    cat.removerFuncionario(func)
                elif decidir == 3:
                    nomeAntes = input('Digite o nome atual do funcionário')
                    nomeDepois = input('Digite o nome pretendido do funcionário')
                    telefoneAntes = input('Digite o telefone atual do funcionário')
                    telefoneDepois = input('Digite o telefone pretendido do funcionário')
                    emailAntes = input('Digite o email atual do funcionário')
                    emailDepois = input('Digite o email pretendido do funcionário')
                    enderecoAntes = input('Digite o endereço atual do funcionário')
                    enderecoDepois = input('Digite o endereço pretendido do funcionário')

                    cat.alterarFuncionario(nomeAntes, nomeDepois,telefoneAntes, telefonedepois, emailAntes, emailDepois, enderecoAntes, enderecoDepois)
                elif decidir == 4:
                    cliente = input('Estes são os clientes cadastrados:\n')
                    cat.mostrarFuncionarios()
                else:
                    break

        if local == 6:
            cat = Controller.ControllerVenda()
            while True:
                decidir = int(input('Digite 1 para cadastrar uma venda\n'
                                    'Digite 2 para ver os produtos mais vendidos\n'
                                    'Digite 3 para ver as vendas cadastradas\n'
                                    'Digite 4 para sair\n'))
#TODO: criar método na controllerVenda para possibilitar a remoção e alteração de uma venda
                if decidir == 1:
                    nomeProduto = input('Digite o nome do produto vendido que deseja cadastrar\n')
                    vendedor = input('Digite o nome do vendedor \n')
                    comprador = input('Digite o nome do comprador\n')
                    quantidadeVendida = input('Digite a quantidade vendida de cada produto\n')
                    cat.cadastrarVenda(nomeProduto, vendedor, comprador, quantidadeVendida)
                elif decidir == 2:
                    venda = print('Esses são os produtos mais vendidos:\n')
                    cat.relatorioProdutos()
                elif decidir == 3:
                    func = print('Essas são as vendas cadastradas\n')
                    dataInicio = input('Digite uma data de início no formato dd/mm/aaaa')
                    dataTermino = input('Digite uma data de início no formato dd/mm/aaaa')
                    cat.mostrarVenda(dataInicio, dataTermino)
                else:
                    break





