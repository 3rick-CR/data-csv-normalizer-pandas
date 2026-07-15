from pathlib import Path
import pandas as pd


def cargar_datos(archivo):
    """Carga un archivo en formato CSV y gestiona la excepción si no existe.

    Parameters:
    ----------
    archivo : str
        Ruta o nombre del archivo CSV a cargar.

    Returns:
    -------
    tuple (DataFrame, str) o (None, None)
        Retorna el DataFrame activo y la ruta original si la carga es exitosa,
        o (None, None) si ocurre un error de tipo FileNotFoundError.
    """
    try:
        df = pd.read_csv(archivo)
        print("Archivo cargado correctamente")
        return df, archivo

    except FileNotFoundError:
        print(f" Error al intentar cargar el archivo '{archivo}'")
        return None, None


def menu(df, nombre_original):
    """Controla el flujo de navegación principal de la aplicación mediante una

    interfaz de consola interactiva.

    Parameters:
    ----------
    df : DataFrame
        El DataFrame activo sobre el cual se ejecutarán las acciones del menú.
    nombre_original : str
        La ruta o nombre del archivo cargado inicialmente.
    """
    while True:

        print("\n--- Menu ---")
        print("1) Info data frame")
        print("2) Normalizar data frame")
        print("3) Generar el archivo limpio")
        print("4) Salir del programa")

        opc = input("Seleccione una opcion: ")

        if opc == "1":
            info(df)
        elif opc == "2":
            df = normalizar(df)
        elif opc == "3":
            generar_archivo(df, nombre_original)
        elif opc == "4":
            print("Saliendo del programa")
            exit()
        else:
            print("Por favor seleccione una opcion valida")


def info(df):
    """Muestra un diagnóstico inicial y resumen descriptivo del DataFrame en

    consola.
    """
    print("\n--- Informacion de dataset ---\n")

    print("Primeras 10 filas: \n")
    print(df.head(10))

    print(f"\nTotal-> Filas: {df.shape[0]}  Columnas: {df.shape[1]}\n")

    print("Nombre de columnas, tipo de dato y valores nulos:\n")
    for i in df.columns:
        print(f"{i}, Tipo: {df[i].dtype}, Cant nulos: {df[i].isna().sum()}")


def normalizar(df):
    """Ejecuta el submenú de limpieza, estandarización y transformación de tipos

    de datos del DataFrame.
    """
    while True:

        print("\n--- Normalizacion y limpieza de datos ---\n")
        print(
            "1) Estandarizar nombres de columnas , modificar nombres o eliminacion"
        )
        print("2) Tratamiento de valores nulos")
        print("3) Cambiar tipos de datos")
        print("4) Volver al menú principal")

        opc = input("Seleccione una opcion: ").lower().strip()

        if opc == "1":

            print(
                "=== Estandarizar nombres de columnas , modificar y eliminacion === "
            )

            # Estandarización de cadenas
            df.columns = (
                df.columns.str.strip().str.lower().str.replace(" ", "_")
            )
            print("\nNombres de columnas normalizados correctamente: ")

            for i in df.columns:
                print(i)

            borrar = (
                input(
                    "\nDesea eliminar o cambiar el nombre de alguna columna s / n: "
                )
                .lower()
                .strip()
            )

            if borrar == "s":

                while True:

                    if len(df.columns) == 0:
                        print("\n¡Error no quedan más columnas en el DataFrame.")
                        break

                    num_col = None
                    lista_columnas = list(df.columns)

                    for idx, col in enumerate(lista_columnas, start=1):
                        print(f"{idx}) {col}")

                    while True:
                        try:
                            num_col = int(
                                input(
                                    "Ingrese el numero de columna para eliminarla o cambiar su nombre en el dataframe: "
                                )
                            )
                            if num_col < 1 or num_col > len(df.columns):
                                print("Ingrese una opcion valida por favor")
                            else:
                                break
                        except ValueError:
                            print(
                                "Ingrese los datos en un formato numerico por favor"
                            )

                    print("1) Borrar columna")
                    print("2) Modificar nombre")
                    opc_usr = input("Seleccione una opcion: ").strip()

                    if opc_usr == "1":

                        if len(df.columns) <= 1:
                            print(
                                "\n Error: No puedes eliminar la última columna. El DataFrame quedaría vacío."
                            )
                            continue

                        col_a_borrar = lista_columnas[num_col - 1]
                        df.drop(columns=[col_a_borrar], inplace=True)
                        print(
                            f"Se elimino la columna: {col_a_borrar} exitosamente"
                        )

                    elif opc_usr == "2":

                        col_a_renombrar = lista_columnas[num_col - 1]
                        nuevo_nombre = (
                            input("Escriba el nuevo nombre: ")
                            .strip()
                            .lower()
                            .replace(" ", "_")
                        )
                        df.rename(
                            columns={col_a_renombrar: nuevo_nombre},
                            inplace=True,
                        )
                        print(
                            f"Se cambio el nombre de columna: {col_a_renombrar} por {nuevo_nombre} exitosamente"
                        )

                    else:
                        print("opcion invalida regresando al menu")
                        break

                    while True:
                        otra_col = (
                            input(
                                "Desea eliminar o modificar el nombre de otra columna s/n: "
                            )
                            .lower()
                            .strip()
                        )
                        if otra_col in ["s", "n"]:
                            break
                        else:
                            print("Seleccione una opcion valida")

                    if otra_col == "n":
                        break

            elif borrar == "n":
                print("Regresando al menu")
            else:
                print("Opcion invalida regresando al menu")

        elif opc == "2":

            print("\n=== Tratamiento de valores nulos ===\n")

            print("Filtro inicial: ")
            while True:
                try:
                    total_columnas = len(df.columns)
                    nan_permitidos = int(
                        input(
                            f"\nEl dataset tiene un total de {total_columnas} columnas ingresa el numero maximo de NaN permitidos por fila para conservarla: "
                        )
                    )
                    if nan_permitidos < 0 or nan_permitidos >= total_columnas:
                        print(
                            f"Error: El número debe estar entre 0 y {total_columnas - 1}."
                        )
                    else:
                        break
                except ValueError:
                    print("Error: Por favor ingresa un número entero válido.")

            filas_antes = df.shape[0]
            valores_minimos = total_columnas - nan_permitidos
            df.dropna(thresh=valores_minimos, inplace=True)

            filas_eliminadas = filas_antes - df.shape[0]
            print(
                f"-> Se eliminaron {filas_eliminadas} filas basura que superaban los {nan_permitidos} NaN."
            )
            print(f"-> Filas restantes para procesar: {df.shape[0]}\n")

            nulos_restantes = df.isna().sum().sum()
            if nulos_restantes == 0:
                print(
                    "\n¡Perfecto! El filtro inicial eliminó todos los nulos. Volviendo al menú principal."
                )
                break

            else:
                lista_nulos = []
                count = 0
                for i in df.columns:
                    nulos = df[i].isna().sum()
                    if nulos != 0:
                        count += 1
                        lista_nulos.append(i)
                        print(f"{count}) {i} -> nulos: {nulos}")

            print("\n=== Opciones para valores nulos === ")
            print("1) Eliminar todos los NaN del dataset (elimina filas)")
            print("2) Sustituir los NaN de forma personalizada (recomendado)")
            print("3) Regresar al menú principal")

            opc_limpieza = input("Ingrese una opcion: ").strip().lower()

            if opc_limpieza == "1":
                df.dropna(inplace=True)
                print("\nFilas con nulos restantes eliminadas exitosamente.")
                break

            elif opc_limpieza == "2":

                opciones_validas = {
                    "1": "eliminar",
                    "2": "moda",
                    "3": "promedio",
                    "4": "mediana",
                    "5": "fijo",
                    "6": "manual",
                    "7": "saltar",
                }

                def func_eliminar(nombre_columna):
                    df.dropna(subset=[nombre_columna], inplace=True)
                    print(
                        f"¡Filas con NaN en '{nombre_columna}' eliminadas correctamente!"
                    )
                    return

                def func_moda(nombre_columna):
                    if df[nombre_columna].mode().empty:
                        print(
                            "\nNo se puede calcular la moda (la columna no tiene valores válidos). Por favor, elige otra opción del menú."
                        )
                        return
                    valor_moda = df[nombre_columna].mode()[0]
                    df[nombre_columna] = df[nombre_columna].fillna(valor_moda)
                    print(
                        f"¡NaN en '{nombre_columna}' reemplazados con la moda: {valor_moda}!"
                    )

                def func_promedio(nombre_columna):
                    valor_promedio = df[nombre_columna].mean()
                    df[nombre_columna] = df[nombre_columna].fillna(
                        valor_promedio
                    )
                    print(
                        f"¡NaN en '{nombre_columna}' reemplazados con el promedio: {valor_promedio:.2f}!"
                    )
                    return

                def func_mediana(nombre_columna):
                    valor_mediana = df[nombre_columna].median()
                    df[nombre_columna] = df[nombre_columna].fillna(
                        valor_mediana
                    )
                    print(
                        f"¡NaN en '{nombre_columna}' reemplazados con la mediana: {valor_mediana}!"
                    )
                    return

                def func_fijo(nombre_columna, es_fecha):
                    valor_fijo = input(
                        f"Ingrese el valor fijo para '{nombre_columna}': "
                    ).strip()

                    if es_fecha:
                        try:
                            valor_fijo = pd.to_datetime(
                                valor_fijo, dayfirst=True, format="mixed"
                            )
                            print(
                                f"-> Fecha interpretada correctamente como: {valor_fijo.strftime('%Y-%m-%d')}"
                            )
                        except Exception:
                            print(
                                "Formato de fecha no reconocido. Se guardará como texto."
                            )
                    else:
                        try:
                            if "." in valor_fijo:
                                valor_fijo = float(valor_fijo)
                            else:
                                valor_fijo = int(valor_fijo)
                        except ValueError:
                            pass

                    df[nombre_columna] = df[nombre_columna].fillna(valor_fijo)
                    print(
                        f"¡NaN en '{nombre_columna}' reemplazados con: {valor_fijo}!"
                    )
                    return

                def func_manual(nombre_columna):
                    indices_nan = df[df[nombre_columna].isna()].index
                    total_nan = len(indices_nan)

                    if total_nan == 0:
                        print(
                            f"No hay valores nulos en la columna '{nombre_columna}'."
                        )
                        return

                    print(
                        f"\nIniciando sustitución manual para {total_nan} valores nulos."
                    )

                    for idx in indices_nan:
                        print(f"\n--> Editando fila con índice original: [{idx}]")
                        valor = input(
                            f"Ingresa el nuevo valor para la columna '{nombre_columna}': "
                        ).strip()

                        try:
                            if "." in valor:
                                valor = float(valor)
                            else:
                                valor = int(valor)
                        except ValueError:
                            pass

                        df.at[idx, nombre_columna] = valor
                        print("Se agregó el valor correctamente")
                    return

                for nombre_columna in lista_nulos:

                    es_numerica = pd.api.types.is_numeric_dtype(
                        df[nombre_columna]
                    )
                    es_fecha = pd.api.types.is_datetime64_any_dtype(
                        df[nombre_columna]
                    ) or any(
                        kw in nombre_columna.lower()
                        for kw in ["date", "fecha", "dia", "año", "mes"]
                    )
                    es_id = (
                        any(
                            kw in nombre_columna.lower()
                            for kw in ["id", "codigo", "code", "matricula", "key"]
                        )
                        or (
                            df[nombre_columna].dropna().nunique()
                            == len(df[nombre_columna].dropna())
                        )
                    ) and not es_fecha

                    print(
                        f"\nColumna: {nombre_columna} Tipo actual en Pandas: {df[nombre_columna].dtype} Nulos: {df[nombre_columna].isna().sum()} "
                    )

                    if es_id:
                        print(
                            " ⚠️ [ALERTA]: Detectada como columna de Identificadores (ID/Matrícula)."
                        )
                    elif es_fecha:
                        print(" 📅 [INFO]: Detectada como columna de FECHAS (Datetime).")

                    if es_id and not es_fecha:
                        print(
                            "\n1) Eliminar filas donde en esta columna los valores sean NaN"
                        )
                        print(
                            "5) Sustituir los NaN de la columna por un valor fijo"
                        )
                        print("6) Sustituir los NaN manualmente 1x1")
                        print("7) Saltar columna (No hacer cambios)")
                    else:
                        print(
                            "\n1) Eliminar filas donde en esta columna los valores sean NaN"
                        )
                        print(
                            "2) Sustituir los NaN de la columna por la Moda (valor mas común)"
                        )

                        if es_numerica and not es_id and not es_fecha:
                            print(
                                "3) Sustituir los NaN de la columna por el PROMEDIO (Media aritmética)"
                            )
                            print(
                                "4) Sustituir los NaN de la columna por la MEDIANA (Ideal contra outliers)"
                            )

                        print(
                            "5) Sustituir los NaN de la columna por un valor fijo"
                        )
                        print("6) Sustituir los NaN manualmente 1x1")
                        print("7) Saltar columna (No hacer cambios)")

                    while df[nombre_columna].isna().sum() != 0:
                        while True:
                            user_opc = (
                                input("Seleccione una opcion: ").lower().strip()
                            )
                            if user_opc not in opciones_validas.keys():
                                print(
                                    "Seleccione una opcion valida para continuar"
                                )
                                continue
                            break

                        accion = opciones_validas[user_opc]

                        if accion == "eliminar":
                            func_eliminar(nombre_columna)
                        elif accion == "moda":
                            func_moda(nombre_columna)
                        elif accion == "promedio":
                            func_promedio(nombre_columna)
                        elif accion == "mediana":
                            func_mediana(nombre_columna)
                        elif accion == "fijo":
                            func_fijo(nombre_columna, es_fecha)
                        elif accion == "manual":
                            func_manual(nombre_columna)
                        elif accion == "saltar":
                            print("Cambiando de columna..")
                            break

                nulos_restantes = df.isna().sum().sum()
                if nulos_restantes == 0:
                    print(
                        "\n¡Perfecto! el dataframe esta limpio de valores nulos. Volviendo al menú."
                    )
                    continue

            elif opc_limpieza == "3":
                print("\nRegresando al menú")
                break
            else:
                print("Error selecciona una opcion valida por favor")

        elif opc == "3":

            print("\n=== Cambiar tipo de dato ===\n")
            print(
                "Nota: Para usar esta funcion el dataframe tiene que estar sin valores NaN o nulos\n"
            )
            print("Comprobacion: ")
            total_nulos = df.isna().sum().sum()

            if total_nulos != 0:
                print(
                    f"Error el dataframe aun contiene {total_nulos} valores nulos. Primero utiliza las opciones para limpiar"
                )
                print("Regresando al menu")
                continue
            else:
                print("Correcto sin valores nulos!\n")

            while True:
                lista_columnas = list(df.columns)
                print("\n--- Columnas disponibles y su tipo actual ---")
                for idx, col in enumerate(lista_columnas, start=1):
                    print(f"{idx}) {col} -> Tipo actual: {df[col].dtype}")
                print(
                    f"{len(lista_columnas) + 1}) Volver al menú de normalización"
                )

                try:
                    num_col = int(input("\nSeleccione el número de la columna: "))
                    if num_col == len(lista_columnas) + 1:
                        break
                    if num_col < 1 or num_col > len(lista_columnas):
                        print("Error: Ingrese una opción válida.")
                        continue
                except ValueError:
                    print("Error: Por favor ingresa un formato numérico.")
                    continue

                col_seleccionada = lista_columnas[num_col - 1]
                print(
                    f"\n¿A qué tipo de dato deseas convertir '{col_seleccionada}'?"
                )
                print("1) Entero (int64)")
                print("2) Decimal / Flotante (float64)")
                print("3) Texto / Objeto (str/object)")
                print("4) Booleano (bool)")
                print("5) Fecha (datetime64)")
                print("6) Cancelar selección")

                opc_tipo = input("Seleccione una opción: ").strip()

                if opc_tipo == "6":
                    print("Selección cancelada.")
                    continue

                elif opc_tipo == "5":
                    try:
                        df[col_seleccionada] = pd.to_datetime(
                            df[col_seleccionada],
                            dayfirst=True,
                            format="mixed",
                            errors="raise",
                        )
                        print(
                            f"\n¡Éxito! Columna '{col_seleccionada}' convertida a datetime64."
                        )
                    except Exception as e:
                        print(f"\n Error de formato de fecha: {e}")

                elif opc_tipo in ["1", "2", "3", "4"]:
                    tipos_mapeo = {
                        "1": "int64",
                        "2": "float64",
                        "3": "object",
                        "4": "bool",
                    }
                    tipo_destino = tipos_mapeo[opc_tipo]
                    try:
                        df[col_seleccionada] = df[col_seleccionada].astype(
                            tipo_destino
                        )
                        print(
                            f"\n¡Éxito! Columna '{col_seleccionada}' convertida a {tipo_destino}."
                        )
                    except Exception as e:
                        print(f"\nError crítico de conversión: {e}")
                else:
                    print("Opción inválida. Intente de nuevo.")

                otra_conversion = (
                    input("\n¿Deseas cambiar el tipo de otra columna? s/n: ")
                    .lower()
                    .strip()
                )
                if otra_conversion != "s":
                    break

        elif opc == "4":
            break
        else:
            print("Seleccione una opcion valida por favor")
    return df


def generar_archivo(df, nombre_original):
    """Exporta el DataFrame actual a un archivo CSV en el disco local

    añadiendo el sufijo '_clean' dinámicamente al nombre original.
    """
    if df is not None:
        # Usamos Path para separar el nombre base de la extensión .csv de manera limpia
        ruta = Path(nombre_original)
        nuevo_nombre = f"{ruta.stem}_clean{ruta.suffix}"

        df.to_csv(nuevo_nombre, index=False)
        print(
            f"\nCambios guardados exitosamente en tu directorio como: '{nuevo_nombre}'."
        )
    else:
        print("\n Error: El DataFrame está vacío o no se ha cargado.")


if __name__ == "__main__":
    
    archivo_usr = input("Ingresa exactamente el nombre de tu archivo csv: ")
    tipo = ".csv"
    archivo_objetivo = archivo_usr + tipo
    
    df, nombre_archivo = cargar_datos(archivo_objetivo)
    
    if df is not None:
        menu(df, nombre_archivo)