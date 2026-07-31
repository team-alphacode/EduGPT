from src.edugpt.model import EduGPT

def main():
    model = EduGPT()
    while True:
        option = model.show_menu()
        if option == "1":
            model.build_corpus()
        elif option == "2":
            model.train()
        elif option == "3":
            model.show_information()
        elif option == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()