class Vehicle:     #define la clase vehiculo

    seller = "Avila Cars C.A."     #Todos los carros de este programa pertenecen a Avila Cars

    def __init__(self, brand, model, color, year): #define los atributos del vehiculo
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year

    def show_att(self): #construye un string que representa el vehiculo
        return "Marca: {}, Modelo: {}, Color: {}, Año: {}".format(self.brand, \
            self.model, self.color, self.year)
        