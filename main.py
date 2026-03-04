import random
import string

def check_conf(config: list,size_password: int):
    """
    Valida la configuración ingresada por el usuario.

    Verifica que:
    - Al menos una opción esté marcada como "si".
    - El tamaño de la contraseña esté entre 1 y 24 caracteres.

    Args:
        config (list): Lista de opciones ingresadas por el usuario
                       (valores esperados: "si" o "no").
        size_password (int): Longitud deseada de la contraseña.

    Raises:
        ValueError: Si no se selecciona ninguna opción válida.
        ValueError: Si la longitud no está en el rango permitido.
    """
    if "si" not in config:
        raise ValueError("Debe elegir al menos una opcion con 'si'")
    if   size_password < 1 or size_password > 24:
        raise ValueError("La contraseña debe tener menos de 24 caracteres y mas de 1")      

def pass_conf():
    """
    Solicita al usuario la configuración para generar la contraseña.

    Pregunta si desea incluir:
    - Letras minúsculas
    - Letras mayúsculas
    - Números
    - Caracteres especiales
    - Longitud de la contraseña

    Returns:
        dict: Diccionario con la configuración seleccionada por el usuario.
              Contiene las claves:
              - lower_case
              - upper_case
              - nums
              - spec_char
              - size_password
    """
    lower_case = str(input("¿Quiere que la contraseña tenga letras minusculas?SI/NO: ")).lower()
    upper_case = str(input("¿Quiere que la contraseña tenga letras mayusculas?SI/NO: ")).lower()
    nums = str(input("¿Quieres que la contraseña tenga numeros?SI/NO: ")).lower()
    spec_char = str(input("¿Queres que la contraseña tenga caracteres especiales?SI/NO: ")).lower()
    size_password = int(input("Ingrese la longitud de la contraseña: "))
    
    options = [lower_case,upper_case,nums,spec_char]
    check_conf(options,size_password)
    
    config = {"lower_case": lower_case,
              "upper_case": upper_case,
              "nums": nums,
              "spec_char": spec_char,
              "size_password": size_password}
    return config


def generate_alphabet(conf:dict):
    """
    Genera el alfabeto base según la configuración elegida.

    Construye una cadena con los caracteres permitidos para la contraseña
    dependiendo de las opciones activadas.

    Args:
        conf (dict): Diccionario con la configuración del usuario.

    Returns:
        str: Cadena con todos los caracteres posibles que podrán
             usarse para generar la contraseña.
    """
    alphabet =""
    if conf["lower_case"] == "si":
        alphabet += string.ascii_lowercase
    if conf["upper_case"] == "si":
        alphabet += string.ascii_uppercase
    if conf["nums"] == "si":
        alphabet += string.digits
    if conf["spec_char"] == "si":
        alphabet += "+*-{}[]@_&%/()#$¿?¡!"
    return alphabet

def generate_password(alphabet:str, size_password:int):
    """
    Genera una contraseña aleatoria.

    Construye una cadena de longitud especificada seleccionando
    caracteres aleatorios del alfabeto proporcionado.

    Args:
        alphabet (str): Conjunto de caracteres permitidos.
        size_password (int): Longitud deseada de la contraseña.

    Returns:
        None: Imprime la contraseña generada en pantalla.
    """
    password = ""
    for _ in range (size_password):
        password += random.choice(alphabet)
    print(f"Contraseña generada: {password}")
    


def main():
    """
    Función principal del programa.

    Controla el flujo general:
    - Solicita la configuración al usuario.
    - Genera el alfabeto correspondiente.
    - Genera la contraseña.
    - Maneja posibles errores de validación.
    """
    try:
        config = pass_conf()
        alphabet = generate_alphabet(config)
        generate_password(alphabet,config["size_password"])
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()