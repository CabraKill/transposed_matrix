from src.util.read_var import read_number


class Inputs():
    def __init__(self):

        self.axis = 0  # [0:"X",1:"Y",2:"Z"]
        self.system = 0  # 0 for rad - 1 for degree
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.angle = 0

    def get_inputs(self):
        print("     Selcione o eixo")
        print("x-0\ny-1\nz-2")
        self.axis = read_number(text="Eixo: ", integer=True)
        print("     Selcione o sistema de medida:")
        print("1- rad")
        print("2- deg")
        self.system = read_number("System:")
        print("     Insira os valores x,y,z:")
        self.x = read_number("X: ")
        self.y = read_number("Y: ")
        self.z = read_number("Z: ")
        print("P=[{},{},{}]".format(self.x, self.y, self.z))

        self.angle_x = read_number("^X:")
        self.angle_y = read_number("^Y:")
        self.angle_z = read_number("^Z:")
