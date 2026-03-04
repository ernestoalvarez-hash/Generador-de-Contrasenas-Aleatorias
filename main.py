import random
import string

#TO DO: hacer el docstring
def check_conf(config: list,size_password: int):
    if "si" not in config:
        raise ValueError("Debe elegir al menos una opcion con 'si'")
    if  0 > size_password or size_password > 24:
        raise ValueError("La contraseña debe tener menos de 24 caracteres y mas de 1")      

#TO DO: hacer el docstring
def pass_conf():
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

#TO DO: hacer el docstring
def generate_alfhabet(conf:dict):
    alfhabet =""
    if conf["lower_case"] == "si":
        alfhabet += string.ascii_lowercase
    if conf["upper_case"] == "si":
        alfhabet += string.ascii_uppercase
    if conf["nums"] == "si":
        alfhabet += string.digits
    if conf["spec_char"] == "si":
        alfhabet += "+*-{}[]@_&%/()#$¿?¡!"
    return alfhabet
    
#TO DO: hacer el docstring
def main():
    try:
        config = pass_conf()
        alfhabet = generate_alfhabet(config)

    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()