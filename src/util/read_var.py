def read_number(text: str, integer: bool = False):
    try:
        value = float(input("{}".format(text)))
        return int(value) if integer else value
    except:
        print("Insira um número válido!!!")
        raise Exception("Insira um número válido!")
