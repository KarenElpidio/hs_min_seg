def conv_hms_a_seg(h, m, s):
    """ Calcula la cantidad de segundos de un tiempo dado en horas, minutos y segundos, y devuelve el resultado al programa principal. """
    return 3600 * h + 60 * m + s


def conv_seg_a_hms(segundos):
    """ Calcula un tiempos expresados en segundos y muestra en pantalla su conversión en horas, minutos y segundos. """
    horas = segundos//3600
    minutos = (segundos % 3600)//60
    segundos = (segundos % 3600) % 60
    return horas, minutos, segundos


def main():
    """ Lee dos tiempos ingresados por teclado expresados en horas, minutos y segundos, suma ambos tiempos y muestre por pantalla el resultado en horas, minutos y segundos. """
    h1 = int(input("Ingrese la primera cantidad de horas: "))
    m1 = int(input("Ingrese la primera cantidad de minutos: "))
    s1 = int(input("Ingrese la primera cantidad de segundos: "))

    sumaSegundos = conv_hms_a_seg(h1, m1, s1)

    h2 = int(input("Ingrese la segunda cantidad de horas: "))
    m2 = int(input("Ingrese la segunda cantidad de minutos: "))
    s2 = int(input("Ingrese la segunda cantidad de segundos: "))

    sumaSegundos = sumaSegundos + conv_hms_a_seg(h2,m2,s2)
    print('El resultado es %s horas %i minutos y %s segundos!' % conv_seg_a_hms(sumaSegundos))

main()
