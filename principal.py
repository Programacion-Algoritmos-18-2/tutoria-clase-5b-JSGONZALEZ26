from paquete_academico.metodos import *
#Creacion del objeto pais, y inicialización de atributos de la Clase Pais
p = Pais()
p.setCapital("Quito")
p.setPais("Ecuador")
#Creacion del objeto Estudiante, atributos setters del objeto
est1 = EstudianteDistancia()
est1.setNombre("Jose")
est1.setApellido("Diaz")
est1.setCodigo("11012")
est1.setNumMaterias(5)
est1.setModulo("Noveno")
est1.setPais(p)
#Presentación del objeto 
print(est1.presentarInformacion())