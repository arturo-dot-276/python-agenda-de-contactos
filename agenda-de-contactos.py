import os

CARPETA = 'contactos/'
EXTENSION = '.txt'

class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():
    crear_directorio()
    mostrar_menu()
    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opción: \r\n')
        opcion = int(opcion)
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print('Opción no válida, intente de nuevo!')

def eliminar_contacto():
    nombre = input('Seleccione el contacto que desea eliminar: \r\n')
    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('Contacto eliminado correctamente!')
    except IOError:
        print('El archivo no existe!')
        print(IOError)
    app()

def buscar_contacto():
    nombre = input('Seleccione el contacto que desea buscar: \r\n')
    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('Información del contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El archivo no existe!')
        print(IOError)
    app()

def mostrar_contactos():
    archivos = os.listdir(CARPETA)

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]
    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')

def editar_contacto():
    print('Escribe el nombre del contacto a editar')
    nombre_anterior = input('Nombre del contacto que desea editar: \r\n')
    existe = existe_contacto(nombre_anterior)
    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:
            nombre_contacto = input('Agrega el Nuevo Nombre: \r\n')
            telefono_contacto = input('Agrega el Nuevo Teléfono: \r\n')
            categoria_contacto = input('Agrega la Nueva Categoría: \r\n')
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Telefono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')
            os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)
            print('Contacto editado exitosamente! \r\n')
    else:
        print('Ese contacto no existe!')
    app()

def agregar_contacto():
    print('Escribe los datos del Nuevo Contacto')
    nombre_contacto = input('Nombre del Contacto: \r\n')
    existe = existe_contacto(nombre_contacto)
    if not existe:
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:
            telefono_contacto = input('Agrega el Telédono: \r\n')
            categoria_contacto = input('Categoría Contacto: \r\n')
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Telefono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')
            print('Contacto creado exitosamente! \r\n')
    else:
        print('Ese contacto ya existe. SUGERENCIA: Asigna un nomre diferente! \r\n')
    app()

def mostrar_menu():
    print('Seleccione del Menú lo que desea hacer:')
    print('1) Agregar Nuevo Contacto')
    print('2) Editar Contacto')
    print('3) Ver Contacto')
    print('4) Buscar Contacto')
    print('5) Eliminar Contacto')

def crear_directorio():
    if not os.path.exists(CARPETA):
        # Crear la carpeta si no existe
        os.makedirs(CARPETA)

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

app()
