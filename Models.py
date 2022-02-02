from datetime import datetime

class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria

class Produtos:
    def __init__(self, nome, preco, categoria: Categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

class Estoque:
    def __init__(self, produto: Produtos, quantidade):
        self.produto = produto
        self.quantidade= quantidade

class Venda:
    def __init__(self, itensVendidos: Produtos, vendedor, comprador, quantidadeVendida, data = datetime.now().strftime('%d/%m/%Y')):
        self.itensVendidos = itensVendidos
        self.vendedor = vendedor
        self.comprador = comprador
        self.quantidadeVendida = quantidadeVendida
        self.data = data

class Fornecedor:
    def __init__(self, nome, cnpj, telefone, categoria):
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.categoria = categoria

class Pessoa:
    def __init__(self, nome, telefone, cpf, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.email = email
        self.endereco = endereco

class Funcionario(Pessoa):
    def __init__(self, clt, nome, telefone, cpf, email, endereco):
        self.clt = clt
        super(Funcionario, self).__init__(nome, telefone, cpf, email, endereco)

#class Impostos:
#    def __init__(self, entidade, vencimento):
#        self.entidade = entidade
#        self.vencimento = vencimento

#class SimplesNacional(Impostos):
#    def __init__(self, entidade, classificacao, aliquota, vencimento):
#        self.entidade = entidade
#        self.classificacao = classificacao
#        self.aliquota = aliquota
 #       self.vencimento = vencimento

#class Iof:
 #   def __init__(self):
  #      return True



#class ValorMonetario(Iof):
 #   def __init__(self):
  #      return True

#class PessoaFisica(ValorMonetario):
 #   def __init__(self, tipodeOperacao, prazo, aliquota):
  #      self.tipodeOperacao = tipodeOperacao
   #     self.prazo = prazo
    #    self.aliquota = aliquota

#class PessoaJuridica(ValorMonetario):
 #   super(PessoaFisica, self).__init__(tipodeOperacao, prazo, aliquota)




#class Bens(Iof):
 #   def __init__(self):
  #      return True

#class PessoaFisica(Bens):
 #   def __init__(self):
  #      return True

#class PessoaJuridica(Bens):
 #   def __init__(self):
  #      return True

