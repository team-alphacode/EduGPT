class EduGPT:
    def __init__(self):
        self.name = "EduGPT"
        self.version = "0.0.2"
        self.vocabulary = set()
        self.total_words = 0

    def train(self, trainer):
        trainer.train()

    def show_information(self):
        print()
        print("=" * 45)
        print(
            f"        {self.name} v{self.version}"
        )
        print("=" * 45)

    def show_menu(self):
        self.show_information()
        print("1. Construir corpus")
        print("2. Preparar modelo")
        print("3. Información del modelo")
        print("4. Tokenizador Manual")
        print("5. Tokenizador NLTK")
        print("6. Tokenizador TikToken")
        print("0. Salir")
        print()
        return input(
            "Seleccione una opción: "
        )