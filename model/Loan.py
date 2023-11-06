class Loan:
    """class emprestimos"""

    def __init__(self, id_livro, id_usuario, data_emprestimo, data_devolucao):
        self.id = None
        self.id_livro = id_livro
        self.id_usuario = id_usuario
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
