class Fila:
    def __init__(self):
        self.lista_da_fila = []

    def inserir(self, item):
        self.lista_da_fila.append(item)
    
    def remover(self):
        removido = self.lista_da_fila.pop(0)
        print("Item removido:", removido)
    
    def esta_vazia(self):
        if len(self.lista_da_fila) == 0:
             return True
        else:
             return False


class Pilha:
    def __init__(self):
        self.lista_da_pilha = []
    
    def empilhar(self, item):
        self.lista_da_pilha.append(item)
    
    def desempilhar(self):
        desempilhado = self.lista_da_pilha.pop()
        print("Item desempilhado: ", desempilhado)

    def esta_vazia(self):
        if len(self.lista_da_pilha) == 0:
                return True
        else:
                return False
        
    def imprimir(self):
        print(self.lista_da_pilha)
    
#testes da Fila:
fila = Fila()

fila.inserir("primeiro")
fila.inserir("segundo")
fila.inserir("terceiro")

print(fila.lista_da_fila)
print(fila.esta_vazia())

fila.remover()
fila.remover()
fila.remover()

print(fila.esta_vazia())

# #testes da Pilha
pilha = Pilha()

pilha.empilhar("Prato 1")
pilha.empilhar("Prato 2")
pilha.empilhar("Prato 3")

pilha.imprimir()
print(pilha.esta_vazia())

pilha.desempilhar()
pilha.desempilhar()
pilha.desempilhar()

print(pilha.esta_vazia())

