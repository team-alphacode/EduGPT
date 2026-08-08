from src.preprocessing.text_cleaner import TextCleaner
from src.tokenizer.tokenizer import Tokenizer
from src.vocabulary.vocabulary import Vocabulary
from src.embeddings.embedding import Embedding

class Trainer:
    def __init__(self, corpus_builder):
        self.corpus_builder = corpus_builder
        self.cleaner = TextCleaner()
        self.tokenizer = Tokenizer()
        self.vocabulary = Vocabulary()
        self.embedding = None

    def train(self):
        print()
        print("=" * 45)
        print("        PIPELINE DE ENTRENAMIENTO")
        print("=" * 45)

        # 1. Cargar corpus
        print("\n[1] Cargando corpus...")
        corpus = self.corpus_builder.load_corpus()
        print(f"Caracteres cargados: {len(corpus)}")

        # 2. Limpiar texto
        print("\n[2] Limpiando texto...")
        cleaned_text = self.cleaner.clean(corpus)
        print(f"Caracteres después de limpiar: {len(cleaned_text)}")

        # 3. Tokenizar
        print("\n[3] Tokenizando...")
        tokens = self.tokenizer.manual_tokenizer(cleaned_text)
        print(f"Tokens generados: {len(tokens)}")

        # 4. Construir vocabulario
        print("\n[4] Construyendo vocabulario...")
        self.vocabulary.build(tokens)
        self.vocabulary.show_information()
        self.vocabulary.save()

        # 5. Convertir tokens a IDs
        print("\n[5] Convirtiendo tokens a IDs...")
        token_ids = self.vocabulary.encode(tokens)
        print(f"Cantidad de IDs: {len(token_ids)}")
        print("\nPrimeros 30 IDs:")
        print(token_ids[:30])

        # 6. Crear embeddings
        print("\n[6] Creando embeddings...")
        vocabulary_size = len(self.vocabulary.token_to_id)
        self.embedding = Embedding(
            vocabulary_size=vocabulary_size,
            embedding_dimension=50
        )
        self.embedding.initialize()
        self.embedding.save()

        # 7. Mostrar ejemplo
        first_token = tokens[0]
        first_token_id = self.vocabulary.token_to_id[first_token]
        self.embedding.show_example(first_token_id, first_token)

        print()
        print("=" * 45)
        print("   PREPARACIÓN COMPLETADA")
        print("=" * 45)
        print()
        print("EduGPT ya tiene vocabulario e embeddings.")
        print("El entrenamiento de los pesos comenzará en la siguiente etapa.")