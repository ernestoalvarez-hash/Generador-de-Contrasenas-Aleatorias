#TO DO: hacer el docstring
def pass_conf():
    strings = str(input("¿Quiere que la contraseña tenga letras?SI/NO: ")).lower()
    nums = str(input("¿Quieres que la contraseña tenga numeros?SI/NO: ")).lower()
    spec_char = str(input("¿Queres que la contraseña tenga caracteres especiales?SI/NO: ")).lower()
    config = {"strings": strings,
              "nums": nums,
              "spec_char": spec_char}
    return config
    
#TO DO: hacer el docstring
def main():
    confg = pass_conf() 

if __name__ == "__main__":
    main()