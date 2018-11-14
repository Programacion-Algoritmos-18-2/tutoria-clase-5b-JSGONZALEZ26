class Persona(object):#Clase Padre
	def __init__(self):

		self.nombre = ""
		self.apellido = ""
		self.pais = Pais()
	pass

	def setNombre(self, m):
		self.nombre = m

	def getNombre(self):
		return self.nombre

	def setApellido(self, m):
		self.apellido = m

	def getApellido(self):
		return self.apellido

	def setPais(self, m):
		self.pais = m

	def getPais(self):
		return self.pais

	

class Estudiante(Persona): #Creacion de clase hija de Persona

	def __init__(self):
		super(Estudiante, self).__init__()
		self.codigo = ""

	def setCodigo(self, m):
		self.codigo = m

	def getCodigo(self):
		return self.codigo

	def presentarInformacion(self):
		cadena = "Informacion\n\tNombre Completo: %s %s\n\tProcedencia:\n\t\tPais: %s\n\t\tCapital: %s\n" % (self.getNombre(), self.getApellido(), self.pais.getPais(), self.pais.getCapital())
		return cadena

	pass

class EstudiantePresencial(Estudiante): #Creacion de clase heredada de Estudiante
#Constructor
	def __init__(self):
		super(EstudiantePresencial, self).__init__()
		self.numCreditos = 0
		self.ciclo = ""
#Getters & Setters
	def setNumCreditos(self, m):
		self.numCreditos = m

	def getNumCreditos(self):
		return self.numCreditos

	def setCiclo(self, m):
		self.ciclo = m

	def getCiclo(self):
		return self.ciclo

	def presentarInformacion(self):
		cadena ="%s\tCodigo: %s\n\tCiclo: %s\n\tNumero de creditos: %d\n" % (super(EstudiantePresencial, self).presentarInformacion(), self.getCodigo(), self.getCiclo(), self.getNumCreditos())
		return cadena

	pass

class EstudianteDistancia(Estudiante): #Clase heredada de Estudiante
#Constructor
	def __init__(self):
		super(EstudianteDistancia, self).__init__()
		self.numMaterias = 0
		self.modulo = ""

	def setNumMaterias(self, m):
		self.numMaterias = m

	def getNumMaterias(self):
		return self.numMaterias

	def setModulo(self, m):
		self.modulo = m

	def getModulo(self):
		return self.modulo

	def presentarInformacion(self):
		cadena ="%s\tCodigo: %s\n\tMódulo: %s\n\tNumero de materias: %d\n" % (super(EstudianteDistancia, self).presentarInformacion(), self.getCodigo(), self.getModulo(), self.getNumMaterias())
		return cadena

	pass
#Clase Pais, usada para el atributo pais en la clase Persona
class Pais(object):

	def __init__(self):
		self.pais = ""
		self.capital = ""

	def setPais(self, m):
		self.pais = m

	def getPais(self):
		return self.pais

	def setCapital(self, m):
		self.capital = m

	def getCapital(self):
		return self.capital
	pass	