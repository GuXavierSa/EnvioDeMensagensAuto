#Tarefas:
#   Abrir o WhatsApp com o Iniciar
#   Entrar e copiar a atividade no grupo de Mensagens
#   Entrar no último grupo
#   Digitar e enviar a mensagem

#Importando bibliotecas

from ssl import AlertDescription
import pyautogui
import time
import random

#Funções

def random_num ():
    x = random.randint(0,5)
    return x

#Definição de listas para as posições
# conversas = ["Rob. Bas. A", "Rob. Bas. B", "Rob. Auto. A", "Rob. Auto. B", "Info. Bas. A", "Info. Bas. B", "Info. Apl. A", "Info. Apl. B", "Cri. Ino.", "1SAT", "2SAT", "3SAT", "4SAT", "1SIT", "2SIT", "3SIT", "4SIT", "1SRT", "2SRT", "3SRT", "4SRT"] 
conversas = ["Xavier CEAP"]
pesquisa_x = [270, 271, 272, 273, 274, 275]
pesquisa_y = [104, 105, 106, 107, 108, 109]

#mensagem = pyautogui.prompt(text='Digite a mensagem que será enviada.', title='Envio de Atividades', default=' ')
mensagem = "adsadas\nasdasdas\nasdasda\nsdasda"
confirmação = pyautogui.confirm(text="O programa de envio de mensagens automatizadas irá começar, porfavor, tire suas mãos do teclado e mouse, a partir de agora seu computador será controlado pelo sistema", title="Envio de Mensagens", buttons=["Ok", "Cancelar"])


if confirmação == "Ok":

    #Inicializar o WhatsApp desktop
    time.sleep(2)
    pyautogui.hotkey("winleft")
    time.sleep(0.3)
    pyautogui.write("WhatsApp")
    time.sleep(0.3)
    pyautogui.press("enter")
    time.sleep(4) #Esperar carregar a janela
    pyautogui.press("f11")

    # Envio de mensagem
    for i in range(len(conversas)):
        x = random_num()
        y = random_num()
        #Pesquisar o grupo
        time.sleep(1)
        pyautogui.click(pesquisa_x[x], pesquisa_y[y])
        time.sleep(1)
        pyautogui.write(conversas[i])
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)

        #Enviando a mensagem
        pyautogui.write(mensagem)
        time.sleep(1.5)
        pyautogui.press("enter")
        i =+ 1

        
else:
    exit()