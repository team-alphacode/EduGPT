from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

class EduGPT:
    def __init__(self):
        self.name = "EduGPT"
        self.version = "0.0.2"
        self.corpus = ""
        self.vocabulary = set()
        self.total_words = 0
        
        self.books_path = BASE_DIR / "data" / "books"
        self.processed_path = BASE_DIR / "data" / "processed"
        self.corpus_path = self.processed_path / "corpus.txt"

    def show_information(self):
        print()
        print("=" * 45)
        print(f"        {self.name} v{self.version}")
        print("=" * 45)

    def find_books(self):
        """
        Busca todos los archivos de texto
        dentro de la carpeta books.
        """
        books = list(self.books_path.glob("*.txt"))
        return books

    def read_books(self, books):
        """
        Lee todos los libros encontrados y
        devuelve un único texto.
        """
        corpus = ""
        print("\nLeyendo libros...\n")
        for book in books:
            print(f" > Leyendo: {book.name}")
            with open(book, "r", encoding="utf-8") as file:
                corpus += file.read()
                corpus += "\n"
        return corpus

    def save_corpus(self, corpus):
        """
        Guarda el corpus procesado.
        """
        self.processed_path.mkdir(exist_ok=True)
        with open(self.corpus_path, "w", encoding="utf-8") as file:
            file.write(corpus)

    def show_corpus_information(self, books, corpus):
        total_books = len(books)
        total_characters = len(corpus)
        total_lines = len(corpus.splitlines())
        total_words = len(corpus.split())
        print("Corpus construido exitosamente.")
        print(f"Libros procesados..... {total_books}")
        print(f"Caracteres............ {total_characters}")
        print(f"Líneas................ {total_lines}")
        print(f"Palabras.............. {total_words}")
        print()
        print(f"Archivo generado...... {self.corpus_path}")

    def build_corpus(self):
        books = self.find_books()
        print("\n**********  CONSTRUCCIÓN DEL CORPUS **********")
        if not books:
            print("\nNo se encontraron libros.")
            return
        print("\nLibros encontrados:\n")
        for book in books:
            print(f"✓ {book.name}")
        corpus = self.read_books(books)
        self.save_corpus(corpus)
        self.show_corpus_information(books, corpus)

        def show_menu(self):
        self.show_information()
        print("1. Construir corpus")
        print("2. Entrenar modelo")
        print("3. Información del modelo")
        print("0. Salir")
        print()
        return input("Seleccione una opción: ")

    def train(self):
        print()
        print("=" * 45)
        print("           ENTRENAMIENTO")
        print("=" * 45)
        print()
        print("Esta función estará disponible próximamente")