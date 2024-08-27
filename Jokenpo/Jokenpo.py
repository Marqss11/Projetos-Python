from random import randint
from time import sleep


print("="*30)
print("Selecione uma das opções")
print("1) Pedra\n2) Papel\n3) Tesoura")
print("="*30)

choice = int(input("Informe sua opção de escolha: ")) # Escolha do player referente as opções
machine = randint(1,3) # Maquina selecionará qual opção desejada entre 1 e 3

if choice == 1:
    player_choice = "Pedra"

elif choice == 2:
    player_choice = "Papel"

else:
    player_choice = "Tesoura"

if machine == 1:
    machine_choice = "Pedra"

elif machine == 2:
    machine_choice = "Papel"

else:
    machine_choice = "Tesoura"

print(f"Você escolhe a opção: {player_choice}.\nQue os jogos comecem!")
print("Jo...")
sleep(1)
print("Ken...")
sleep(1)
print("Po!...")
sleep(1)
print("="*30)
if player_choice == machine_choice:
    print(f"Olha só... ambos escolheram {machine_choice}!\n Acho que deu empate...")

elif player_choice == "Pedra" and machine_choice == "Tesoura":
    print(f"Sua escolha: {player_choice}\nEscolha da maquina: {machine_choice}\nVocê venceu!")

elif player_choice == "Papel" and machine_choice == "Pedra":
    print(f"Sua escolha: {player_choice}\nEscolha da maquina: {machine_choice}\nVocê venceu!")

elif player_choice == "Tesoura" and machine_choice == "Papel":
    print(f"Sua escolha: {player_choice}\nEscolha da maquina: {machine_choice}\nVocê venceu!")

else:
    print(f"Sua escolha: {player_choice}\nEscolha da maquina: {machine_choice}\nA maquina venceu!")
print("="*30)

