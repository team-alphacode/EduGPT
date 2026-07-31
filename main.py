from src.models.model import EduGPT
from src.datasets.corpus_builder import CorpusBuilder
from src.tokenizer.tokenizer import Tokenizer

def main():
    model = EduGPT()
    builder = CorpusBuilder()
    tokenizer = Tokenizer()
    while True:
        option = model.show_menu()
        if option == "1":
            builder.build_corpus()
        elif option == "2":
            model.train()
        elif option == "3":
            model.show_information()
        elif option == "4":
            corpus = builder.load_corpus()
            tokenizer.run(corpus, "manual")
        elif option == "5":
            corpus = builder.load_corpus()
            tokenizer.run(corpus, "nltk")
        elif option == "6":
            corpus = builder.load_corpus()
            tokenizer.run(corpus, "tiktoken")
        elif option == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()