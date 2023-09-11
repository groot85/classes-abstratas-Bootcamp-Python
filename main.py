#Exercicio 2 - classes abstratas

#Regras: 
# O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres (-- > class Cliente)
# Modele um sistema orientado a objetos para representar contas correntes do Banco Delas seguindo os requisitos abaixo.

# 1. Cada [conta corrente] pode ter um ou mais [clientes] como titular. - os requisitos para criar classe
# 2. O banco controla apenas o [nome], o [telefone] e a [renda mensal] de cada cliente.
# 3. A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos. [atributo] Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela fizer um depósito, aumentaremos o saldo. SACAR/DEPOSITAR
# 4. [Clientes mulheres] possuem em suas contas um cheque especial de valor igual à sua renda mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até -renda_mensal. [logica que faz relaçao com o saque]
# 5. [Clientes homens] por enquanto não têm direito a cheque especial. - dois tipos de clientes tem comportamento dif
# Para modelar seu sistema, utilize obrigatoriamente os conceitos:
# "classe"
#"herança"
#"propriedades"
#"encapsulamento"
#"classe abstrata"
     
#obs.: classe abstrata possui metodos abstratos, não tem implementacao. Funciona como se fosse um "template" para a classe filha).
#cliente homem e cliente mulher serão herdeiros de Clientes
#@property #a propriedade serve para acessar pelo mundo externo a variável que está escondida, que so tem no mundo interno ex:  _variavel ex _nome

from abc import ABC, abstractmethod

class Cliente (ABC):
    def __init__ (self, nome, telefone, renda_mes):
        self._nome = nome #(protegido)
        self._telefone = telefone #(protegido)
        self.__renda_mes = renda_mes #(privado)

    @property 
    def nome (self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        if type(novo_nome) != str:
            raise TypeError ("A variável deve ser str ")
        self._nome = novo_nome

    @property 
    def telefone (self):
        return self._telefone

    @telefone.setter
    def telefon(self, novo_telefone):
        if type(novo_telefone) != str:
            raise TypeError ("A variável deve ser str")
        self._telefone = novo_telefone

    @property 
    def renda_mes(self):
        return self.__renda_mes 

    @abstractmethod
    def cheque_especial (self):
        pass

class ClienteMulher (Cliente):
    def __init__(self, nome, telefone, renda_mes):
        super().__init__(nome, telefone, renda_mes)
    
    def cheque_especial (self):
        return True
      
class ClienteHomem (Cliente):
    def __init__(self, nome, telefone, renda_mes):
        super().__init__(nome, telefone, renda_mes)
    
    def cheque_especial (self):
        return False

class ContaCorrente:
    def __init__(self, titular):
        self.__saldo = 0.0
        self.__operacoes = []
        self.__titulares = []
        self.adicionar_titular(titular)

    def adicionar_titular (self, titular):
        self.__titulares.append(titular)

    def depositar (self, valor: float):
        self.__saldo += valor 
        self.__operacoes.append(f"Depósito realizado de R$ {valor:.2f}")

    def sacar (self, valor: float):
        titular = self.__titulares[0]
        if titular.cheque_especial() == False:
            if valor <= self.__saldo:
                self.__saldo -= valor
                self.__operacoes.append(f"Saque de R$ {valor:.2f}")
            else:
                raise ValueError("Saldo Insuficiente")
        else:
            if valor <= self.__saldo or (self.__saldo - valor) >= -titular.renda_mes:
                self.__saldo -= valor
                self.__operacoes.append(f"Saque de R${valor:.2f}")
            else:
                raise ValueError("Saldo Insuficiente")

    @property
    def saldo (self):
        return self.__saldo

    @property
    def operacoes (self):
        return self.__operacoes

  
cliente_mulher = ClienteMulher ("Ana", "999999", 25000)
cliente_homem = ClienteHomem ("Cesar", "888888", 3000)

conta1 = ContaCorrente (cliente_mulher)
conta2 = ContaCorrente (cliente_homem)

print(conta1.saldo)
print(conta2.saldo)
print()

conta1.depositar(250.0)
conta2.depositar(350.0)

print(conta1.operacoes)
print(conta2.operacoes)

conta1.sacar(3000.0)
conta2.sacar(300.0)
print()

print(conta1.saldo)
print(conta2.saldo)
print()

print(conta1.operacoes)
print(conta2.operacoes)

# saque sem tratar a mensagem de erro
# conta1.sacar(3000.0)
# conta2.sacar(300.0)
# print()

#como fazer uma mensagem de erro APÓS a ação DO CLIENTE sem aparecer o detalhamento de erro do sistema

try:
  conta1.sacar(3000.0)
  conta2.sacar(100.0)
except ValueError as e:
  print (f"Erro durante a execução: {e}")