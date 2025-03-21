from time import sleep

def idade():
    while
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso (apenas o número, sem a unidade de medida): "))
altura = int(input("Digite sua altura em cm: "))
genero = str(input("Digite seu gênero: "))

print(f"Certo. De acordo com suas repostas, \nSua idade é {idade};\nSeu peso é {peso};\nSua altura é {altura};\nPor fim, seu gênero é {genero}.")
sleep(1)

print("Com estes dados coletados, vou fazer para você a fórmula do cálculo TMB (Taxa Metabólica Basal).\n Existem diversas fórmulas, a que vou u sar é a de Harris-Benedict, a mais usada.\n Mas óbviamente, só um profissional da área de nutrição pode te dar resultados mais precisos.")
sleep(2)
print("O calculo é: 655 + (9,56 x Peso em kg) + (1,85 x altura em cm) - (4,68 x idade) para mulheres")
print("Para homens seria 66 + (13,75 x Peso em kg) + (5 x altura em cm) - (6,75 x idade).")








def Masculino():
    print("Enfim, já que seu gênero é masculino, a fórmula para seu TMB será:")
    sleep(2)
    print(f'66 + (13,75 * {peso}) + (5 x {altura}) - (6,75 x {idade})')
    
    resultado_peso = 13.75 * peso
    resultado_altura = 5 * altura
    resultado_idade = 6.75 * idade
    
    sleep(1.5)
    
    print(f"Aqui os resultados de cada etapa: \n66 + {resultado_peso} + {resultado_altura} - {resultado_idade:.2f}")
    
    resultado_final = 66 + resultado_peso + resultado_altura - resultado_idade
    contador = 3
    print("Seu TMB é...")
    
    while contador >= 1:
        print(contador)
        sleep(1)
        contador -= 1
        
    print(f"Aproximadamente: {resultado_final:.2f}kcal/dia!")





def Feminino():
    print("Enfim, já que seu gênero é feminino, a fórmula para seu TMB será:")
    sleep(2)
    print(f'655 + (9,56 * {peso}) + (1,85 x {altura}) - (4,68 x {idade})')
    
    resultado_peso = 9.56 * peso
    resultado_altura = 1.85 * altura
    resultado_idade = 4.68 * idade
    
    sleep(1.5)
    
    print(f"Aqui os resultados de cada etapa: \n655 + {resultado_peso} + {resultado_altura} - {resultado_idade:.2f}")
    
    resultado_final = 655 + resultado_peso + resultado_altura - resultado_idade
    
    contador = 3
    print("Seu TMB é...")
    while contador >= 1:
        print(contador)
        sleep(1)
        contador -= 1
        
    print(f"Aproximadamente: {resultado_final:.2f}kcal/dia!")

if genero.lower() == 'masculino':
    Masculino()
elif genero.lower() == 'feminino':
    Feminino()    

    
