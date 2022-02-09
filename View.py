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
                          'Digite 7 para ver os produtos mais vendidos\n'
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
                    produto = input('Digite o produto que deseja cadastrar\n')
                    cat.cadastrarProduto(produto)
                elif decidir == 2:
                    produto = input('Digite o produto que deseja remover\n')
                    cat.removerProduto(produto)
                elif decidir == 3:
                    produto = input('Digite o produto que deseja alterar\n')
                    novoProduto = input('Digite o nome para o qual deseja alterar\n')
                    cat.alterarProduto(produto, novoProduto)
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
                    fornecedor = input('Digite o fornecedor que deseja cadastrar\n')
                    cat.cadastrarFornecedor(fornecedor)
                elif decidir == 2:
                    fornecedor = input('Digite o fornecedor que deseja remover\n')
                    cat.removerFornecedor(fornecedor)
                elif decidir == 3:
                    fornecedor = input('Digite o fornecedor que deseja alterar\n')
                    novoFornecedor = input('Digite o nome para o qual deseja alterar\n')
                    cat.alterarFornecedor(fornecedor, novoFornecedor)
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
                    cliente = input('Digite o cliente que deseja cadastrar\n')
                    cat.cadastrarCliente(cliente)
                elif decidir == 2:
                    cliente = input('Digite o cliente que deseja remover\n')
                    cat.removerCliente(cliente)
                elif decidir == 3:
                    cliente = input('Digite o cliente que deseja alterar\n')
                    novoCliente = input('Digite o nome para o qual deseja alterar\n')
                    cat.alterarCliente(cliente, novoCliente)
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
                    func = input('Digite o funcionário que deseja cadastrar (clt, nome do funcionário, telefone, cpf, email, endereco)\n')
                    cat.cadastrarFuncionario(func)
                elif decidir == 2:
                    func = input('Digite o cpf e nome do funcionário que deseja remover\n')
                    cat.removerFuncionario(func)
                elif decidir == 3:
                    func = input('Digite o funcionário que deseja alterar (CPFALTERAR, CPFALTERADO, cltAlterar, cltAlterado, nomeAlterar, nomeAlterado, telefoneAlterar, telefoneAlterado, emailAlterar, emailAlterado, enderecoAlterar, enderecoAlterado)\n')
                    novoFunc = input('Digite os dados para os quais deseja alterar\n')
                    cat.alterarCliente(func, novoFunc)
                elif decidir == 4:
                    cliente = input('Estes são os clientes cadastrados:\n')
                    cat.mostrarFuncionarios()
                else:
                    break

        if local == 6:
            cat = Controller.ControllerVenda()
            while True:
                decidir = int(input('Digite 1 para cadastrar uma venda'
                                    'Digite 2 para remover uma venda\n'
                                    'Digite 3 para alterar uma venda\n'
                                    'Digite 4 para ver as vendas cadastradas\n'
                                    'Digite 5 para sair\n'))

                if decidir == 1:
                    venda = input('Digite o funcionário que deseja cadastrar\n')
                    cat.cadastrarVenda(venda)
                elif decidir == 2:
                    func = input('Digite o func que deseja remover\n')
                    cat.remover(func)
                elif decidir == 3:
                    func = input('Digite o funcionário que deseja alterar\n')
                    novoFunc = input('Digite o nome para o qual deseja alterar\n')
                    cat.alterarCliente(func, novoFunc)
                elif decidir == 4:
                    cliente = input('Estes são os clientes cadastrados:\n')
                    cat.mostrarFuncionarios()
                else:
                    break





