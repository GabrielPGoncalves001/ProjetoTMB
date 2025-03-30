from time import sleep



def Dados():
    while True:
        try:
            
            idade = int(input("Digite sua idade:"))
            peso = float(input("Digite seu peso, sem o kg:"))
            altura = int(input("Digite sua altura em cm:"))

            if idade <= 0:
                print("Por favor, digite uma idade válida.")
                continue

            elif peso <= 0:
                print("Por favor, digite um peso válido.")
                continue

            elif altura <= 0:
                print("Por favor, digite uma altura válida.")    
                continue

            while True:
                genero = input("Digite seu gênero:").strip().lower()
                if genero.strip().lower() in ['masculino', 'feminino']:
                    break
                else:
                 print("Digite um gênero biológicamente válido, por favor.")
                continue

            return genero, idade, peso, altura
        
        except ValueError as e:
            print("Entrada inválida")

dados_user = Dados()    
genero, idade, altura, peso = dados_user        

print(f"Certo. De acordo com suas repostas, \nSua idade é {idade};\nSeu peso é {peso};\nSua altura é {altura};\nPor fim, seu gênero é {genero}.")
sleep(1)

print("Com estes dados coletados, vou fazer para você a fórmula do cálculo TMB (Taxa Metabólica Basal).\n Existem diversas fórmulas, a que vou u sar é a de Miffin-St Jeor, a mais recomendada para a sociedade atual.\n Mas óbviamente, somente um profissional da área de nutrição pode te dar resultados mais precisos.")
sleep(2)
print("Mulheres: TMB = (10 × peso em kg) + (6,25 × altura em cm) - (5 × idade em anos) - 161")
print("Homens: TMB = (10 × peso em kg) + (6,25 × altura em cm) - (5 × idade em anos) + 5")


def Masculino():
    print("Enfim, já que seu gênero é masculino, a fórmula para seu TMB será:")
    sleep(2)
    print(f'(10 x {peso}) + (6,25 x {altura}) - (5 x {idade}) + 5')
    
    resultado_peso = 10 * peso
    resultado_altura = 6.25 * altura
    resultado_idade = 5 * idade
    
    sleep(1.5)
    
    print(f"Aqui os resultados de cada etapa: \n{resultado_peso} + {resultado_altura} - {resultado_idade:.2f} + 5")
    
    resultado_final = resultado_peso + resultado_altura - resultado_idade + 5
    contador = 3
    print("Seu TMB é...")
    
    while contador >= 1:
        print(contador)
        sleep(1)
        contador -= 1
        
    print(f"Aproximadamente: {resultado_final:.2f}kcal/dia!")
    return resultado_final




def Feminino():
    print("Enfim, já que seu gênero é feminino, a fórmula para seu TMB será:")
    sleep(2)
    print(f'(10 x {peso}) + (6.25 x {altura}) - (5 x {idade}) - 161')
    
    resultado_peso = 10 * peso
    resultado_altura = 6.25 * altura
    
    sleep(1.5)
    
    print(f"Aqui os resultados de cada etapa: \n{resultado_peso} + {resultado_altura} - (5 * {idade:.2f}) - 161")
    
    resultado_final = resultado_peso + resultado_altura - (5 * idade) - 161
    
    contador = 3
    print("Seu TMB é...")
    while contador >= 1:
        print(contador)
        sleep(1)
        contador -= 1
        
    print(f"Aproximadamente: {resultado_final:.2f}kcal/dia!")
    return resultado_final
if genero == 'masculino':
    resultado_final = Masculino()
elif genero == 'feminino':
    resultado_final = Feminino()    

print("Existe também um calculo para saber quanto de calorias gastamos no dia a dia conforme nossa atividade física.")
print("Esse calculo tem 5 niveis, escolhendo o nível faremos o TMB x Nível de atividade q será = TDEE (Fator de Atividade Física)")

decisao = input("Deseja realizar o teste? (sim/não):").lower()

def CalcularTDEE(resultado_final):
    while True:
        try:
            print('1. Sedentário, Pouco ou nenhum exercício.')
            print("2. Atividade leve, exercícios leves ou esportes de 1 a 3 dias na semana.")
            print("3. Atividade moderada, exercícios ou esportes de 3 a 5 dias na semana.")
            print("4. Ativdade intensa, exercícios ou esportes de 6 a 7 dias na semana")
            print("5. Atividade muito intensa, exercício intenso diário ou treinamento físico extremo.")

            atividade = int(input("Digite uma das opções que mais se encaixa com o seu perfil:"))
            
            if atividade not in [1, 2, 3, 4, 5]:
                print("Digite uma opção válida.")
                continue

            elif atividade == 1:
                print(f"Seu calculo é: {resultado_final} x 1,2")
                tdee = resultado_final * 1.2
                print(f"Seu TDEE: {tdee:.2f}")
                break

            elif atividade == 2:
                print(f'Seu calculo é: {resultado_final} x 1,375')       
                tdee = resultado_final * 1.375
                print(f'Seu TDEE: {tdee:.2f}')  
                
            elif atividade == 3:
                print(f'Seu calculo é: {resultado_final} x 1,55')       
                tdee = resultado_final * 1.55
                print(f'Seu TDEE: {tdee:.2f}') 
                break
            elif atividade == 4:
                print(f'Seu calculo é: {resultado_final} x 1,725')       
                tdee = resultado_final * 1.725
                print(f'Seu TDEE: {tdee:.2f}')   
                break
            elif atividade == 5:
                print(f'Seu calculo é: {resultado_final} x 1,9')       
                tdee = resultado_final * 1.9
                print(f'Seu TDEE: {tdee:.2f}') 
                break
            else:
                print("Entrada invalida.")
        except ValueError:
            print("Entrada inválida, digite um número inteiro.")

if decisao == 'sim':
    CalcularTDEE(resultado_final)    
else:
    print("Tudo bem, até logo!")            
