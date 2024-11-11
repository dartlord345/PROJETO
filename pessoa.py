class Pessoa:
    def __init__(self, nome, istId,padrinhos):
        self.nome = nome
        self.istId = istId
        self,padrinhos = padrinhos
        self.pseudos = []

    def __str__(self):
        return f'{self.nome} tem {self.idade} anos'
    
    def adicionar_pseudoPadrinho(self, pseudo):
        self.pseudos.append(pseudo)

    def remover_pseudoPadrinho(self, pseudo):
        self.pseudos.remove(pseudo)
    