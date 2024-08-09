import funciones.globales as fg

def mainMenu(op):
    title = """
****************************
* MENU PRINCIPAL DE PANCAM *
****************************
    """
    fg.borrar_pantalla()
    mainMenuOp = "1. Compras \n2. Ventas \n3. Gestión de Informes \n4. Salir"
    if(op != 4):
        print(title)
        print(mainMenuOp)
        try:
            opcion = int(input(':) '))
        except ValueError:
            print("Error en la opcion ingresada")
            mainMenu(0)
        else:
            match (opcion):
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    print("Regrese pronto ....")
                    fg.pausar_pantalla
                case _:
                    print('Opcion ingresada no pertenece al menu de opciones')
                    fg.pausar_pantalla()                    
                    mainMenu(0)
                    
if __name__ == '__main__':
    
    mainMenu(0)