class sistema():
    def __init__(self):
       self.__lista_paciente=[]
       self.__numero_pacientes=len(self.__lista_paciente)
#Duda- ¿Por que no se asignan en el mismo init?
    
    #Setters
    def asignarNombre(self,nombre):
        self.__nombre=nombre
    def asignarCedula(self,cedula):
        self.__cedula=cedula
    def asignarGenero(self,genero):
        self.__genero=genero
    def asignarServicio(self,servicio):
        self.__servicio=servicio

    def IngresarPaciente(self):
        nombre=input('Ingrese nombre')
        cedula=int(input('Ingresar cedula'))
        genero=input('Ingresar genero')
        servicio=input('Ingrese servicio')

        p=paciente()
        p.asignarNombre(nombre)
        p.asignarCedula(cedula)
        p.asignarGenero(genero)
        p.asignarServicio(servicio)

        self.__lista_pacientes.append(p)
        self.__numero_pacientes=len(self.__lista_paciente)
#Tener en cuenta usar la funcion magica de string 
    #Getters
    def VerNombre(self):
        return self.__nombre
    def VerCedula(self):
        return self.__cedula
    def VerGenero(self):
        return self.__genero
    def VerServicio(self):
        return self.__servicio
    def VernumPacientes(self):
        return self.__numero_pacientes
    def VerdatosPacientes(self):
        cedula=

    
class paciente(sistema):
    def  __init__(self,nom, ced, gen, serv):
        sistema.__init__(self,nom, ced, gen)
        self.servicio=serv

class empleado(sistema):
    def  __init__(self,nom, ced, gen, turn):
        sistema.__init__(self,nom, ced, gen)
        self.turno=turn

class enfermeras(empleado):
    def  __init__(self,nom, ced, gen,turn,
                  rang):
        empleado.__init__(self,nom, ced, gen, turn)
        self.rango=rang

class medicos(empleado):
    def  __init__(self,nom, ced, gen, turn, esp):
        empleado.__init__(self,nom, ced, gen,turn)
        self.especialidad=esp

p1= paciente()
p2= paciente()
p1.asignarNombre('Maria Rosa')
p1.asignarCedula(1040570498)
p1.asignarGenero('Mujer')
print(p1.VerCedula())


def main():
    sis=sistema()

    while True:
        opcion=int(input('''
Ingrese:
                         0.Salir
                         1.Ingresar paciente
                         2.Ver pacientes
                         '''))
        if opcion==1:
            print('A continuacion Se solicitaran los datos:')

if __name__=='__main__':
    
