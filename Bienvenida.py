print("")
print("Hola de nuevo")

a = 40
b = 30
c = 8

def suma():
    print("Suma total: ", a + b + c)

suma()

def generar_datos_ventas():
    dias = ["Lun", "Mar", "Mie", "Jue", "Vie"]
    ventas = [120, 500, 230, 289, 310]
    return dias, ventas

def resumen_analitica():
    dias, ventas = generar_datos_ventas()
    total = sum(ventas)
    promedio = total / len(ventas)
    return {
        "dias": dias, 
        "ventas": ventas,
        "total": total, 
        "promedio": promedio
    }

datos = resumen_analitica()
print("Total de ventas :", datos ["total"])
print("Promedio diario:", datos ["promedio"])
