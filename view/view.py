import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from bd.bd import *
from model.User import User
from model.Book import Book


# Configuração de cores
COR1 = "#fcbd00"  # AMARELO
COR2 = "#030303"  # PRETO
COR3 = "#2e2a2a"  # CINZA
COR4 = "#757272"  # CINZA CLARO
COR5 = "#fcfcfc"  # BRANCO

def criar_janela_principal():

    # Criando a janela principal
    janela = tk.Tk()
    janela.config(bg=COR2)
    janela.geometry("800x495")
    janela.title("Gerenciador de Livros")

    # Defina a configuração da coluna da janela principal para que o Frame janela_sub expanda
    janela.grid_columnconfigure(1, weight=1)

    # Crie o Frame de título e adicione o Label do título
    janela_titulo = tk.Frame(janela, width=800, height=100, bg=COR1)
    janela_titulo.grid(row=0, column=0, columnspan=2, sticky="nsew")
    titulo = tk.Label(janela_titulo, text="Sistema de Gerenciamento de Livros", font=('Ivy', 20, 'bold'), bg=COR1, fg=COR2)
    titulo.grid(row=0, column=0, padx=15, pady=32, sticky="w")

    # Crie o Frame do menu
    janela_menu = tk.Frame(janela, width=180, height=495, bg="#2e2a2a")  # Aqui você pode definir a cor diretamente
    janela_menu.grid(row=1, column=0, sticky="nsw")

    # Criando sub Frames
    janela_sub = tk.Frame(janela, width=620, height=495, bg=COR4)
    janela_sub.grid(row=1, column=1, sticky="nsew")  # Colocado à direita

    # Chame a função para criar os botões do menu
    criar_botoes_menu(janela_menu, janela_sub)

    return janela

def criar_botoes_menu(janela_menu, janela_sub):
    # Coloque a criação dos botões do menu aqui
    b_1 = tk.Button(janela_menu, text="Novo Usuário", width=25, height=2, bg=COR3,\
        font=('Ivy 13 bold'), relief="raised", overrelief="ridge", activebackground=COR3, command=lambda:funcao_novo_usuario(janela_sub))
    b_1.grid(row=0, column=0, padx=2, pady=2)

    b_2 = tk.Button(janela_menu, text="Cadastrar Livro", width=25, height=2, bg=COR3,\
        font=('Ivy 13 bold'), relief="raised", overrelief="ridge", activebackground=COR3, command=lambda:funcao_cadastrar_livro(janela_sub))
    b_2.grid(row=1, column=0, padx=2, pady=2)

    b_3 = tk.Button(janela_menu, text="Exibir Todos Livros", width=25, height=2,\
        bg=COR3, font=('Ivy 13 bold'), relief="raised", overrelief="ridge", activebackground=COR3, command=lambda:exibir_todos_livros(janela_sub))
    b_3.grid(row=2, column=0, padx=2, pady=2)

    b_4 = tk.Button(janela_menu, text="Exibir Todos Usuário", width=25, height=2,\
        bg=COR3, font=('Ivy 13 bold'), relief="raised", overrelief="ridge", activebackground=COR3, command=lambda:exibir_todos_usuarios(janela_sub))
    b_4.grid(row=3, column=0, padx=2, pady=2)

    b_5 = tk.Button(janela_menu, text="Realizar Empréstimo", width=25, height=2,\
        bg=COR3, font=('Ivy 13 bold'), relief="raised", overrelief="ridge", activebackground=COR3, command=lambda: fazer_emprestimo(janela_sub))
    b_5.grid(row=4, column=0, padx=2, pady=2)

    b_6 = tk.Button(janela_menu, text="Devolução Empréstimo", width=25, height=2,\
        bg=COR3, font=('Ivy 13 bold'), relief="raised", overrelief="ridge", activebackground=COR3, command=lambda: cadastrar_devolucao(janela_sub))
    b_6.grid(row=5, column=0, padx=2, pady=2)

    b_7 = tk.Button(janela_menu, text="Livros Emprestados", width=25, height=2,\
        bg=COR3, font=('Ivy 13 bold'), relief="raised", overrelief="ridge", activebackground=COR3, command=lambda: livros_emprestados(janela_sub))
    b_7.grid(row=6, column=0, padx=2, pady=2)

def funcao_novo_usuario(janela_sub):
    # Limpa o Frame janela_sub
    for widget in janela_sub.winfo_children():
        widget.destroy()

    l_titulo = tk.Label(
        janela_sub,
        text="Cadastrar novo Usuário:",
        font=('Arial', 15, 'bold'),
        width=620,
        height=1,
        anchor="w",
        padx=15,
        pady=12,
        bg=COR5
    )
    l_titulo.pack()

    # Espaço em branco entre o título e o frame
    espaco_branco = tk.Frame(
        janela_sub,
        width=800,
        height=15,
        bg=COR4,
    )
    espaco_branco.pack()

    janela_sub_info = tk.Frame(
        janela_sub,
        width=800,
        height=315,
        bg=COR5,
    )
    janela_sub_info.pack(side="bottom", fill="both", expand=True)

    l_nome = tk.Label(
        janela_sub_info,
        text="Nome:",
        font=('Arial', 10, 'bold'),
        height=1,
        bg=COR5
    )
    l_nome.grid(row=0, column=0, padx=15, pady=12, sticky="w")

    entry_nome = tk.Entry(
        janela_sub_info,
        font=('Arial', 10),
    )
    entry_nome.grid(row=0, column=1, padx=10, pady=12, sticky="w")

    l_sobrenome = tk.Label(
        janela_sub_info,
        text="Sobrenome:",
        font=('Arial', 10, 'bold'),
        height=1,
        bg=COR5
    )
    l_sobrenome.grid(row=1, column=0, padx=15, pady=12, sticky="w")

    entry_sobrenome = tk.Entry(
        janela_sub_info,
        font=('Arial', 10),
    )
    entry_sobrenome.grid(row=1, column=1, padx=10, pady=12, sticky="w")

    l_endereco = tk.Label(
        janela_sub_info,
        text="Endereço do Usuário:",
        font=('Arial', 10, 'bold'),
        height=1,
        bg=COR5
    )
    l_endereco.grid(row=2, column=0, padx=15, pady=12, sticky="w")

    entry_endereco = tk.Entry(
        janela_sub_info,
        font=('Arial', 10),
    )
    entry_endereco.grid(row=2, column=1, padx=10, pady=12, sticky="w")

    l_email = tk.Label(
        janela_sub_info,
        text="Endereço de Email:",
        font=('Arial', 10, 'bold'),
        height=1,
        bg=COR5
    )
    l_email.grid(row=3, column=0, padx=15, pady=12, sticky="w")

    entry_email = tk.Entry(
        janela_sub_info,
        font=('Arial', 10),
    )
    entry_email.grid(row=3, column=1, padx=10, pady=12, sticky="w")

    l_telefone = tk.Label(
        janela_sub_info,
        text="Número de Telefone: ",
        font=('Arial', 10, 'bold'),
        height=1,
        bg=COR5
    )
    l_telefone.grid(row=4, column=0, padx=15, pady=12, sticky="w")

    entry_telefone = tk.Entry(
        janela_sub_info,
        font=('Arial', 10),
    )
    entry_telefone.grid(row=4, column=1, padx=10, pady=12, sticky="w")

    def salvar_usuario():
        #pega os dados digitados
        nome = entry_nome.get()
        sobrenome = entry_sobrenome.get()
        endereco = entry_endereco.get()
        email = entry_email.get()
        telefone = entry_telefone.get()

        user = User(nome, sobrenome, endereco, email, telefone)

        # Verifique se o nome e sobrenome contêm apenas letras
        valida_string(user)
        #salva os valores digitados
        save_user(user)

        # Lista de campos Entry
        campos_entry = [entry_nome, entry_sobrenome, entry_endereco, entry_email, entry_telefone]

        # Limpar todos os campos Entry
        for campo in campos_entry:
            campo.delete(0, "end")

    b_salvar = tk.Button(
        janela_sub_info,
        command=salvar_usuario,
        text="Salvar",
        bg=COR4,
        fg=COR5,
        width=10,
        height=1
    )
    b_salvar.grid(row=5, column=1, padx=10, pady=12)

def funcao_cadastrar_livro(janela_sub):
    for widget in janela_sub.winfo_children():
        widget.destroy()

    l_titulo = tk.Label(
        janela_sub,
        text="Cadastrar novo Livro:",
        font=('Arial', 15, 'bold'),
        width=620,
        height=1,
        anchor="w",
        padx=15,
        pady=12,
        bg=COR5
    )
    l_titulo.pack()

    # Espaço em branco entre o título e o frame
    espaco_branco = tk.Frame(
        janela_sub,
        width=800,
        height=15,
        bg=COR4,
    )
    espaco_branco.pack()

    janela_sub_info = tk.Frame(
        janela_sub,
        width=800,
        height=315,
        bg=COR5,
    )
    janela_sub_info.pack(side="bottom", fill="both", expand=True)

    l_titulo = tk.Label(
        janela_sub_info,
        text="Título: ",
        font=('Arial', 10, 'bold'),
        height=1,
        bg=COR5
    )
    l_titulo.grid(row=0, column=0, padx=15, pady=12, sticky="w")

    entry_titulo = tk.Entry(
        janela_sub_info,
        font=('Arial', 10),
    )
    entry_titulo.grid(row=0, column=1, padx=10, pady=12, sticky="w")

    l_autor = tk.Label(
        janela_sub_info,
        text="Autor: ",
        font=('Arial', 10, 'bold'),
        height=1,
        bg=COR5
    )
    l_autor.grid(row=1, column=0, padx=15, pady=12, sticky="w")

    entry_autor = tk.Entry(
        janela_sub_info,
        font=('Arial', 10),
    )
    entry_autor.grid(row=1, column=1, padx=10, pady=12, sticky="w")

    l_editora = tk.Label(
        janela_sub_info,
        text="Editora: ",
        font=('Arial', 10, 'bold'),
        height=1,
        bg=COR5
    )
    l_editora.grid(row=2, column=0, padx=15, pady=12, sticky="w")

    entry_editora = tk.Entry(
        janela_sub_info,
        font=('Arial', 10),
    )
    entry_editora.grid(row=2, column=1, padx=10, pady=12, sticky="w")

    l_ano_publicacao = tk.Label(
        janela_sub_info,
        text="Ano publicação: ",
        font=('Arial', 10, 'bold'),
        height=1,
        bg=COR5
    )
    l_ano_publicacao.grid(row=3, column=0, padx=15, pady=12, sticky="w")

    entry_ano_publicacao = tk.Entry(
        janela_sub_info,
        font=('Arial', 10),
    )
    entry_ano_publicacao.grid(row=3, column=1, padx=10, pady=12, sticky="w")

    l_isbn = tk.Label(
        janela_sub_info,
        text="ISBN: ",
        font=('Arial', 10, 'bold'),
        height=1,
        bg=COR5
    )
    l_isbn.grid(row=4, column=0, padx=15, pady=12, sticky="w")

    entry_isbn = tk.Entry(
        janela_sub_info,
        font=('Arial', 10),
    )
    entry_isbn.grid(row=4, column=1, padx=10, pady=12, sticky="w")

    def salvar_livro():
        #pega os dados digitados
        titulo = entry_titulo.get()
        autor = entry_autor.get()
        editora = entry_editora.get()
        ano_publicacao = entry_ano_publicacao.get()
        isbn = entry_isbn.get()

            # Verifique se o nome e sobrenome contêm apenas letras
        if not titulo.isalpha():
            messagebox.showerror("Erro", "Nome deve conter apenas letras.")
            return

        if not autor.isalpha():
            messagebox.showerror("Erro", "Sobrenome deve conter apenas letras.")
            return

        book = Book(titulo, autor, editora, ano_publicacao, isbn)
        #salva os valores digitados
        save_book(book)

        # Lista de campos Entry
        campos_entry = [entry_titulo,entry_autor,entry_editora,entry_ano_publicacao,entry_isbn]

        # Limpar todos os campos Entry
        for campo in campos_entry:
            campo.delete(0, "end")

    b_salvar = tk.Button(
        janela_sub_info,
        command=salvar_livro,
        text="Salvar",
        bg=COR4,
        fg=COR5,
        width=10,
        height=1
    )
    b_salvar.grid(row=5, column=1, padx=10, pady=12)

def exibir_todos_livros(janela_sub):
    for widget in janela_sub.winfo_children():
        widget.destroy()

    l_titulo = tk.Label(
        janela_sub,
        text="Lista de Livros Cadastrados",
        font=('Arial', 15, 'bold'),
        width=620,
        height=1,
        anchor="w",
        padx=15,
        pady=12,
        bg=COR5
    )
    l_titulo.pack()

    # Crie um Frame para conter o Treeview e a barra de rolagem
    frame_treeview = ttk.Frame(janela_sub)
    frame_treeview.pack(padx=15, pady=10, fill="both", expand=True)

    # Crie um Treeview para exibir a lista de livros
    colunas = ("Id","Título", "Autor", "Editora", "Ano de Publicação", "ISBN")
    lista_livros = ttk.Treeview(frame_treeview, columns=colunas, show="headings")
    lista_livros.pack(fill="both", expand=True)

    # Defina o cabeçalho da tabela
    for coluna in colunas:
        lista_livros.heading(coluna, text=coluna)
        lista_livros.column(coluna, width=120)  # Ajuste a largura das colunas conforme necessário

    # Preencha a tabela com os livros cadastrados
    livros = read_book()
    
    for livro in livros:
        lista_livros.insert("", "end", values=(livro[0], livro[1], livro[2], livro[3], livro[4], livro[5]))

    # Crie uma barra de rolagem vertical
    scrollbar_vertical = ttk.Scrollbar(lista_livros, orient="vertical", command=lista_livros.yview)
    scrollbar_vertical.pack(side="right", fill="y")

    # Crie uma barra de rolagem horizontal
    scrollbar_horizontal = ttk.Scrollbar(lista_livros, orient="horizontal", command=lista_livros.xview)
    scrollbar_horizontal.pack(side="bottom", fill="x")

    # Configure as barras de rolagem
    lista_livros.configure(yscrollcommand=scrollbar_vertical.set, xscrollcommand=scrollbar_horizontal.set)

    # Adicione um botão para fechar a lista de livros
    b_fechar = tk.Button(
        janela_sub,
        text="Fechar",
        command="",
        bg=COR4,
        fg=COR5,
        width=10,
        height=1
    )
    b_fechar.pack(pady=10)

def exibir_todos_usuarios(janela_sub):
    for widget in janela_sub.winfo_children():
        widget.destroy()

    l_titulo = tk.Label(
        janela_sub,
        text="Lista de Usuários Cadastrados",
        font=('Arial', 15, 'bold'),
        width=620,
        height=1,
        anchor="w",
        padx=15,
        pady=12,
        bg=COR5
    )
    l_titulo.pack()

    # Crie um Frame para conter o Treeview e a barra de rolagem
    frame_treeview = ttk.Frame(janela_sub)
    frame_treeview.pack(padx=15, pady=10, fill="both", expand=True)

    # Crie um Treeview para exibir a lista de livros
    colunas = ("Id","Nome", "Sobrenome", "Endereço", "Email", "Telefone")
    lista_usuarios = ttk.Treeview(frame_treeview, columns=colunas, show="headings")
    lista_usuarios.pack(fill="both", expand=True)

    # Defina o cabeçalho da tabela
    for coluna in colunas:
        lista_usuarios.heading(coluna, text=coluna)
        lista_usuarios.column(coluna, width=120)  # Ajuste a largura das colunas conforme necessário

    # Preencha a tabela com os livros cadastrados
    usuarios = read_user()
    for user in usuarios:
        lista_usuarios.insert("", "end", values=(user[0], user[1], user[2], user[3], user[4], user[5]))

    # Crie uma barra de rolagem vertical
    scrollbar_vertical = ttk.Scrollbar(lista_usuarios, orient="vertical", command=lista_usuarios.yview)
    scrollbar_vertical.pack(side="right", fill="y")

    # Crie uma barra de rolagem horizontal
    scrollbar_horizontal = ttk.Scrollbar(lista_usuarios, orient="horizontal", command=lista_usuarios.xview)
    scrollbar_horizontal.pack(side="bottom", fill="x")

    # Configure as barras de rolagem
    lista_usuarios.configure(yscrollcommand=scrollbar_vertical.set, xscrollcommand=scrollbar_horizontal.set)

    # Adicione um botão para fechar a lista de livros
    b_fechar = tk.Button(
        janela_sub,
        text="Fechar",
        command="",
        bg=COR4,
        fg=COR5,
        width=10,
        height=1
    )
    b_fechar.pack(pady=10)

def fazer_emprestimo(janela_sub):
    # Limpa o Frame janela_sub
    for widget in janela_sub.winfo_children():
        widget.destroy()

    l_titulo = tk.Label(
        janela_sub,
        text="Cadastrar Emprestimo:",
        font=('Arial', 15, 'bold'),
        width=620,
        height=1,
        anchor="w",
        padx=15,
        pady=12,
        bg=COR5
    )
    l_titulo.pack()

    # Espaço em branco entre o título e o frame
    espaco_branco = tk.Frame(
        janela_sub,
        width=800,
        height=15,
        bg=COR4,
    )
    espaco_branco.pack()

    janela_sub_info = tk.Frame(
        janela_sub,
        width=800,
        height=315,
        bg=COR5,
    )
    janela_sub_info.pack(side="bottom", fill="both", expand=True)

    l_id_emprestimo = tk.Label(
        janela_sub_info,
        text="Id do livro:",
        font=('Arial', 10, 'bold'),
        height=1,
        bg=COR5
    )
    l_id_emprestimo.grid(row=0, column=0, padx=15, pady=12, sticky="w")

    entry_id_livro = tk.Entry(
        janela_sub_info,
        font=('Arial', 10),
    )
    entry_id_livro.grid(row=0, column=1, padx=10, pady=12, sticky="w")

    l_id_usuario = tk.Label(
        janela_sub_info,
        text="Id do usuário:",
        font=('Arial', 10, 'bold'),
        height=1,
        bg=COR5
    )
    l_id_usuario.grid(row=1, column=0, padx=15, pady=12, sticky="w")

    entry_id_usuario = tk.Entry(
        janela_sub_info,
        font=('Arial', 10),
    )
    entry_id_usuario.grid(row=1, column=1, padx=10, pady=12, sticky="w")

    l_data_emprestimo = tk.Label(
        janela_sub_info,
        text="Data do empréstimo:",
        font=('Arial', 10, 'bold'),
        height=1,
        bg=COR5
    )
    l_data_emprestimo.grid(row=2, column=0, padx=15, pady=12, sticky="w")

    entry_data_emprestimo = tk.Entry(
        janela_sub_info,
        font=('Arial', 10),
    )
    entry_data_emprestimo.grid(row=2, column=1, padx=10, pady=12, sticky="w")

    l_data_devolucao = tk.Label(
        janela_sub_info,
        text="Data da devolução:",
        font=('Arial', 10, 'bold'),
        height=1,
        bg=COR5
    )
    l_data_devolucao.grid(row=3, column=0, padx=15, pady=12, sticky="w")

    entry_data_devolucao = tk.Entry(
        janela_sub_info,
        font=('Arial', 10),
    )
    entry_data_devolucao.grid(row=3, column=1, padx=10, pady=12, sticky="w")

    def fazer_emprestimo():
        id_livro = entry_id_livro.get()
        id_usuario = entry_id_usuario.get()
        data_emprestimo = entry_data_emprestimo.get()
        data_devolucao = entry_data_devolucao.get()

        # Verificar se o campo data_devolucao está vazio (string vazia)
        if not data_devolucao:
            data_devolucao = None

        loan = Loan(id_livro, id_usuario, data_emprestimo, data_devolucao)

        insert_loan(loan)

        # Lista de campos Entry
        campos_entry = [entry_id_usuario, entry_id_livro, entry_data_emprestimo, entry_data_devolucao]

        # Limpar todos os campos Entry
        for campo in campos_entry:
            campo.delete(0, "end")

    b_salvar = tk.Button(
        janela_sub_info,
        command=fazer_emprestimo,
        text="Salvar",
        bg=COR4,
        fg=COR5,
        width=10,
        height=1
    )
    b_salvar.grid(row=5, column=1, padx=10, pady=12)

def cadastrar_devolucao(janela_sub):
    # Limpa o Frame janela_sub
    for widget in janela_sub.winfo_children():
        widget.destroy()

    l_titulo = tk.Label(
        janela_sub,
        text="Cadastrar Devolução:",
        font=('Arial', 15, 'bold'),
        width=620,
        height=1,
        anchor="w",
        padx=15,
        pady=12,
        bg=COR5
    )
    l_titulo.pack()

    # Espaço em branco entre o título e o frame
    espaco_branco = tk.Frame(
        janela_sub,
        width=800,
        height=15,
        bg=COR4,
    )
    espaco_branco.pack()

    janela_sub_info = tk.Frame(
        janela_sub,
        width=800,
        height=315,
        bg=COR5,
    )
    janela_sub_info.pack(side="bottom", fill="both", expand=True)

    l_id_emprestimo = tk.Label(
        janela_sub_info,
        text="Id do livro:",
        font=('Arial', 10, 'bold'),
        height=1,
        bg=COR5
    )
    l_id_emprestimo.grid(row=0, column=0, padx=15, pady=12, sticky="w")

    entry_id_emprestimo = tk.Entry(
        janela_sub_info,
        font=('Arial', 10),
    )
    entry_id_emprestimo.grid(row=0, column=1, padx=10, pady=12, sticky="w")

    l_data_devolucao = tk.Label(
        janela_sub_info,
        text="Data da devolução:",
        font=('Arial', 10, 'bold'),
        height=1,
        bg=COR5
    )
    l_data_devolucao.grid(row=3, column=0, padx=15, pady=12, sticky="w")

    entry_data_devolucao = tk.Entry(
        janela_sub_info,
        font=('Arial', 10),
    )
    entry_data_devolucao.grid(row=3, column=1, padx=10, pady=12, sticky="w")

    def cadastrar_devolucao():
        id_emprestimo = entry_id_emprestimo.get()
        data_devolucao = entry_data_devolucao.get()

        update_loan_return_date(data_devolucao, id_emprestimo)

        # Lista de campos Entry
        campos_entry = [entry_id_emprestimo, entry_data_devolucao]

        # Limpar todos os campos Entry
        for campo in campos_entry:
            campo.delete(0, "end")

    b_salvar = tk.Button(
        janela_sub_info,
        command=cadastrar_devolucao,
        text="Salvar",
        bg=COR4,
        fg=COR5,
        width=10,
        height=1
    )
    b_salvar.grid(row=5, column=1, padx=10, pady=12)

def livros_emprestados(janela_sub):
    # Limpa o Frame janela_sub
    for widget in janela_sub.winfo_children():
        widget.destroy()

    l_titulo = tk.Label(
        janela_sub,
        text="Cadastrar Devolução:",
        font=('Arial', 15, 'bold'),
        width=620,
        height=1,
        anchor="w",
        padx=15,
        pady=12,
        bg=COR5
    )
    l_titulo.pack()

    # Crie um Frame para conter o Treeview e a barra de rolagem
    frame_treeview = ttk.Frame(janela_sub)
    frame_treeview.pack(padx=15, pady=10, fill="both", expand=True)

    # Crie um Treeview para exibir a lista de livros
    colunas = ("Título", "Nome", "Sobrenome", "Data empréstimo", "Data devolução")
    lista_livros = ttk.Treeview(frame_treeview, columns=colunas, show="headings")
    lista_livros.pack(fill="both", expand=True)

    # Defina o cabeçalho da tabela
    for coluna in colunas:
        lista_livros.heading(coluna, text=coluna)
        lista_livros.column(coluna, width=120)  # Ajuste a largura das colunas conforme necessário

    # Preencha a tabela com os livros cadastrados
    livros = get_books_on_loan()

    for livro in livros:
        lista_livros.insert("", "end", values=(livro[0], livro[1], livro[2], livro[3], livro[4]))

    # Crie uma barra de rolagem vertical
    scrollbar_vertical = ttk.Scrollbar(lista_livros, orient="vertical", command=lista_livros.yview)
    scrollbar_vertical.pack(side="right", fill="y")

    # Crie uma barra de rolagem horizontal
    scrollbar_horizontal = ttk.Scrollbar(lista_livros, orient="horizontal", command=lista_livros.xview)
    scrollbar_horizontal.pack(side="bottom", fill="x")

    # Configure as barras de rolagem
    lista_livros.configure(yscrollcommand=scrollbar_vertical.set, xscrollcommand=scrollbar_horizontal.set)

    # Adicione um botão para fechar a lista de livros
    b_fechar = tk.Button(
        janela_sub,
        text="Fechar",
        command="",
        bg=COR4,
        fg=COR5,
        width=10,
        height=1
    )
    b_fechar.pack(pady=10)

def valida_string(User):
    if not User.nome.isalpha():
        messagebox.showerror("Erro", "Nome deve conter apenas letras.")
        return

    if not User.sobrenome.isalpha():
        messagebox.showerror("Erro", "Sobrenome deve conter apenas letras.")
        return
