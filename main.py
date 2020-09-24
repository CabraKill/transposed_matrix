from src.controllers.read_input import Inputs


def main():
    print("Bem vindo")
    inputs = Inputs()
    while(True):
        try:
            inputs.get_inputs()
        except Exception as e:
            print("Erro:",end="")
            print(e)
        print("")


if __name__ == "__main__":
    main()
