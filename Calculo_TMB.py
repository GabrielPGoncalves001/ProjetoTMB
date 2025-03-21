from time import sleep

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso (apenas o número, sem a unidade de medida): "))
altura = int(input("Digite sua altura em cm: "))
genero = str(input("Digite seu gênero: "))

print(f"Certo. De acordo com sua resposta, seu nome é {nome};\nSua idade é {idade};\nSeu peso é {peso};\nSua altura é {altura};\nPor fim, seu gênero é {genero}.")
sleep(1)

print("Com estes dados coletados, vou fazer para você a fórmula do cálculo TMB (Taxa Metabólica Basal).\n Existem diversas fórmulas, a que vou usar é a de Harris-Benedict, a mais usada.\n Mas óbviamente, só um profissional da área de nutrição pode te dar resultados mais precisos.\n O calculo é: 655 + (9,6 x Peso em kg) + (1,8 x altura em cm) - (4,7 x idade) para MULHERES\n Para homens seria 66 + (13,7 x Peso em kg) + (5 x altura em cm) - (6,8 x idade).\n Bom, bora lá")
sleep(1)

def Masculino():
    print(f'66 + (13,7 * {peso}) + (5 x {altura}) - (6,8 x {idade})')
    resultado_peso = 13.7 * peso
    resultado_altura 5 * altura
    resultado_idade = 6.8 * idade
    sleep(1)
    sleep(1.5)
    print(f"65 + {resultado_peso} + {resultado_altura} - {resultado_idade}")
    resultado_final = 66 + resultado_peso + resultado_altura - resultado_idade
    print(f"Seu TMB é: {round(resultado_final, 2)}!")


if genero.lower() == 'masculino':
    Execut Masculino
    