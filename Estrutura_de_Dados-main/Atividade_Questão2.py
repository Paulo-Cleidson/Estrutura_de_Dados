class GerenciamntoPedidos:

    def __init__(self):
        self.pedidos = []
        self.acao_undo = []
        self.acao_redo = []
    
    def adicionar_pedido(self, pedido):
        self.pedidos.append(pedido)
        self.acao_undo.append("Pedido Adicionado")
    
    def atender_pedido(self):
        self.pedidos.pop()
        self.acao_undo.append("Pedido Entregue")
    
    def desfazer(self):
        if len(self.acao_undo) != 0:

            acao = self.acao_undo.pop()

            match acao:
                case "Pedido Adicionado":
                    self.pedidos.pop()
                
                case "Pedido Entregue":
                    self.pedidos.append(acao)
        else:
            print("Não há ações para desfazer.")
    
    def imprimir(self):
        print(self.pedidos)
        print(self.acao_undo)
        print(self.acao_redo)

Fip_Burguer = GerenciamntoPedidos()

Fip_Burguer.adicionar_pedido("Pedido 1")
Fip_Burguer.adicionar_pedido("Pedido 2")
Fip_Burguer.adicionar_pedido("Pedido 3")
Fip_Burguer.atender_pedido()
Fip_Burguer.imprimir
Fip_Burguer.desfazer()
Fip_Burguer.imprimir()