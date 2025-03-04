class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __str__(self):
        return f"{self.titulo} ({self.autor}, {self.ano})"
    
    def imprimir_informacoes(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}"

class Pessoa:
    def __init__(self, nome, idade, livro):
        self.nome = nome
        self.idade = idade
        self.livro = livro

    def imprimir_informacoes(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, {self.livro.imprimir_informacoes}"

livro1 = Livro("Silencio", "Patrick R.", 2010)

pessoa1 = Pessoa("Paulo", 35, livro1)
print(pessoa1.imprimir_informacoes())

pessoa2 = Pessoa("Edy", 35, livro1)
print(pessoa2.imprimir_informacoes())

lista = []

lista.append("primeiro")
lista.append("segundo")
lista.append("terceiro")

print(lista)
lista.remove(lista[0])
print(lista)
lista.remove(lista[0])
print(lista)
