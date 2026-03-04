import random
import string

#TO DO: hacer el docstring
def pass_conf():
    lower_case = str(input("¿Quiere que la contraseña tenga letras minusculas?SI/NO: ")).lower()
    upper_case = str(input("¿Quiere que la contraseña tenga letras mayusculas?SI/NO: ")).lower()
    nums = str(input("¿Quieres que la contraseña tenga numeros?SI/NO: ")).lower()
    spec_char = str(input("¿Queres que la contraseña tenga caracteres especiales?SI/NO: ")).lower()
    config = {"lower_case": lower_case,
              "upper_case": upper_case,
              "nums": nums,
              "spec_char": spec_char}
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
    confg = pass_conf()
    alfhabet = generate_alfhabet(confg)



if __name__ == "__main__":
    main()