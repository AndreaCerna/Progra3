class Alumno():

    def info(self):
        lista =[]
        cont = int(input("Ingrese la cantidad de alumnos a Inscribir:  "))

        while (cont>0):
            NombreAlumno = input("Ingrese Su nombre Completo:  ")
            lista.append(NombreAlumno)
            cont-=1

        print(lista)


alumno=Alumno()
alumno.info()


class Curso():

    def info(self):
        lista =[]
        cont = int(input("¿Cuantos cursos se asignará?:  "))

        while (cont>0):
            NombreCurso = input("Nombre del Curso:  ")
            lista.append(NombreCurso)
            cont-=1

        print(lista)


cursos=Curso()
cursos.info()

class Ciclo():

    def info(self):
        lista =[]
        cont = int(input("¿Cuántos ciclos lleva?:  "))

        while (cont>0):
            NombreCiclo = input("¿Nombre del Ciclo(s) Cursando?:  ")
            lista.append(NombreCiclo)
            cont-=1

        print(lista)


ciclos=Ciclo()
ciclos.info()


class Seccion():

    def info(self):
        SeccionAlumno = input("¿Sección Asignada?:  ")


seccion=Seccion()
seccion.info()

datos = [Alumno,Curso,Ciclo,Seccion]
for i in range(0,3):
    print ( datos[i] , end="  " )
print()

