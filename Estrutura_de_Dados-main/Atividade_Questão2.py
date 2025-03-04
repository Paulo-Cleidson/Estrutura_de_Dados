class GerenciamntoPedidos:

    def __init__(self):
        self.pedidos = []
        self.acao_undo = []
        self.acao_redo = []
    

    def adicionar_pedido(self, pedido):
        self.pedidos.append(pedido)
        self.acao_undo.append(pedido)
        self.acao_undo.append("Adicionado")
    

    def atender_pedido(self):
        self.acao_undo.append(self.pedidos[0])
        self.pedidos.remove(self.pedidos[0])
        self.acao_undo.append("Atendido")
    

    def desfazer(self):
        if len(self.acao_undo) != 0:

            acao = self.acao_undo.pop()
            pedido = self.acao_undo.pop()
            self.acao_redo.clear()
            self.acao_redo.append(pedido)
            self.acao_redo.append(acao)

            match acao:
                case "Adicionado":
                    self.pedidos.pop()
                
                case "Atendido":
                    self.pedidos.insert(0, pedido)
        else:
            print("Não há ações para desfazer.")


    def refazer(self):
        if len(self.acao_redo) != 0:

            acao = self.acao_redo.pop()
            pedido = self.acao_redo.pop()

            match acao:
                case "Adicionado":
                    self.adicionar_pedido(pedido)
                
                case "Atendido":
                    self.atender_pedido()
        else:
            print("Não há ações para refazer.")
    

    def imprimir(self):
        print("lista de pedidos: ", self.pedidos)
        print("lista undo: ", self.acao_undo)
        print("lista redo: ", self.acao_redo)

# teste adicionar pedidos
Fip_Burguer = GerenciamntoPedidos()
Fip_Burguer.adicionar_pedido("Pedido 1")
Fip_Burguer.adicionar_pedido("Pedido 2")
Fip_Burguer.adicionar_pedido("Pedido 3")
Fip_Burguer.imprimir()

# teste atender pedidos
Fip_Burguer.atender_pedido()
Fip_Burguer.imprimir()

# teste desfazer
Fip_Burguer.desfazer()
Fip_Burguer.imprimir()

# teste refazer
Fip_Burguer.refazer()
Fip_Burguer.imprimir()
