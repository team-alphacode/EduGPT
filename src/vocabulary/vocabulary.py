import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

class Vocabulary:
    def __init__(self):
        self.vocabulary_path = (
            BASE_DIR / "data" / "vocabulary" / "vocabulary.json"
        )
        self.token_to_id = {}
        self.id_to_token = {}

    def build(self, tokens):
        """
        Construye el vocabulario a partir de los tokens.
        """
        unique_tokens = sorted(set(tokens))
        self.token_to_id = {
            token: index
            for index, token in enumerate(unique_tokens)
        }
        self.id_to_token = {
            index: token
            for token, index in self.token_to_id.items()
        }
        return self.token_to_id

    def save(self):
        self.vocabulary_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )
        data = {
            "token_to_id": self.token_to_id,
            "id_to_token": self.id_to_token
        }
        with open(
            self.vocabulary_path,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4
            )
        print(f"\nVocabulario guardado en:")
        print(self.vocabulary_path)

    def encode(self, tokens):
        """
        Convierte tokens en IDs.
        """
        return [
            self.token_to_id[token]
            for token in tokens
        ]

    def decode(self, ids):
        """
        Convierte IDs nuevamente en tokens.
        """
        return [
            self.id_to_token[index]
            for index in ids
        ]

    def show_information(self):
        print()
        print("=" * 45)
        print("              VOCABULARIO")
        print("=" * 45)
        print(
            f"Palabras únicas..... {len(self.token_to_id)}"
        )
        print("\nPrimeros 20 elementos:\n")
        for token, index in list(
            self.token_to_id.items()
        )[:20]:
            print(f"{index:5} -> {token}")