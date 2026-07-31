import nltk
import tiktoken
from nltk.tokenize import word_tokenize

class Tokenizer:
    def __init__(self):
        pass

    def run(self, corpus, tokenizer_type):
        if tokenizer_type == "manual":
            return self.manual_tokenizer(corpus)
        elif tokenizer_type == "nltk":
            return self.nltk_tokenizer(corpus)
        elif tokenizer_type == "tiktoken":
            return self.tiktoken_tokenizer(corpus)
        else:
            print("Tipo de tokenizador no válido.")
            return []

    def manual_tokenizer(self, corpus):
        print("\n========== TOKENIZER MANUAL ==========\n")
        tokens = corpus.split()
        self.show_information(tokens)
        return tokens

    def nltk_tokenizer(self, corpus):
        print("\n========== TOKENIZER NLTK ==========\n")
        tokens = word_tokenize(corpus)
        self.show_information(tokens)
        return tokens

    def tiktoken_tokenizer(self, corpus):
        print("\n========== TOKENIZER TIKTOKEN ==========\n")
        encoding = tiktoken.get_encoding("cl100k_base")
        token_ids = encoding.encode(corpus)
        self.show_information(token_ids)
        print("\nReconvirtiendo los primeros 30 tokens:\n")
        print(encoding.decode(token_ids[:30]))
        return token_ids

    def show_information(self, tokens):
        print(f"Cantidad de tokens... {len(tokens)}")
        print(f"Tipo devuelto........ {type(tokens)}")
        print("\nPrimeros 30 tokens:\n")
        print(tokens[:30])