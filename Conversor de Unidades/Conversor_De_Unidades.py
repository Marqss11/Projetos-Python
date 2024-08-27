from time import sleep
from Menus import *

while True:
    print(main_menu)
    option = int(input("Informe a opção desejada: "))
    if option == 1:
        print(temperature_menu)
        temperature_option = int(input("Informe a opção que deseja utilizar: "))
        if temperature_option == 1:
            temperature_value = float(input("Informe a temperatura em Celsius: "))
            result_temperature_fahrenheit = (temperature_value * 1.8) + 32
            print("="*40)
            print(f"RESULTADO:\nValor em Celsius: {temperature_value}\nValor em Fahrenheit: {result_temperature_fahrenheit}")
            print("="*40)
            sleep(2)
            print(exit_menu)
            exit_option = int(input("Informe a opção desejada: "))
            if exit_option == 1:
                continue
            elif exit_option == 2:
                break
            else:
                print("Opção Invalida!")
        elif temperature_option == 2:
            temperature_value = float(input("Informe a temperatura em Fahrenheit: "))
            result_temperature_celsius = (temperature_value - 32) / 1.8
            print("="*40)
            print(f"RESULTADO:\nValor em Fahrenheit: {temperature_value}\nValor em Celsius: {result_temperature_celsius}")
            print("="*40)
            sleep(2)
            print(exit_menu)
            exit_option = int(input("Informe a opção desejada: "))
            if exit_option == 1:
                continue
            elif exit_option == 2:
                break
            else:
                print("Opção Invalida!")
    
    elif option == 2:
        print("Encerrado...")
        break

    else:
        print("Opção Invalida!")
        sleep(1)