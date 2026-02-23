class Livros:
    def __init__(self, titulo, autores):
        self.titulo = titulo
        self.autores = autores


class Biblioteca:
    def __init__(self):
        self.books = []

    def adicionar_books(self, titulo, autores):
        self.books.append(Livros(titulo, autores))

    def listar_books(self):

        largura_titulo = max(len(livro.titulo) for livro in self.books)

        print("\n" + "=" * (largura_titulo + 20))
        print(" BIBLIOTECA DO ERIK".center(largura_titulo + 20))
        print("=" * (largura_titulo + 20))

        for i, livro in enumerate(self.books, 1):
            print(f"{i:02d} | {livro.titulo:<{largura_titulo}} | {livro.autores}")

        print("=" * (largura_titulo + 20))


# Criando os livros
livro1 = Livros('Metamorfose','Franz Kafka')
livro2 = Livros('Noites Brancas', 'Fiódor Dostoiévski')
livro3 = Livros('A Morte de Ivan Ilitch', 'Liev Tolstoi')
livro4 = Livros('A Divina Comedia Inferno', 'Dante Alighieri')
livro5= Livros('A Divina Comedia Purgatório', 'Dante Alighieri')
livro6= Livros('A divina Comedia Paraiso', 'Dante Alighieri')


# Criar a biblioteca e adicionar o livro nela
biblioteca = Biblioteca()
biblioteca.adicionar_books(livro1.titulo, livro1.autores)
biblioteca.adicionar_books(livro2.titulo, livro2.autores)
biblioteca.adicionar_books(livro3.titulo, livro3.autores)
biblioteca.adicionar_books(livro4.titulo, livro4.autores)
biblioteca.adicionar_books(livro5.titulo, livro5.autores)
biblioteca.adicionar_books(livro6.titulo, livro6.autores)

# Listar os livros
biblioteca.listar_books()