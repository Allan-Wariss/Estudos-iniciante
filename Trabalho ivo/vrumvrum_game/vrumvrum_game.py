import turtle
import time

tela = turtle.Screen()                   # Faz a tela do jogo
tela.title("Vrum Vrum THE GAME")         # Titulo da janela
tela.setup(1000, 750)                    # Resolução da tela em px
tela.bgcolor("black")                    # background para analisar o erro do fundo animado
tela.addshape("background-grande.gif")   # fundo animado
tela.addshape("sprite-mario-1.gif")      # Sprite jogador
tela.addshape("Combustivel-cheio.gif")   # Sprites Combustivel
tela.addshape("Combustivel-meio.gif")    # -
tela.addshape("Combustivel-baixo.gif")   # -
tela.addshape("Combustivel-zero.gif")    # -

#Velocidades
veloFundo = 0
andar = 0

# Configuração fundo
comeco = -580
fundo = turtle.Turtle()
fundo.speed(10)
fundo.penup()
fundo.shape("background-grande.gif")

#Combustivel
combustivel_valor = 300                   # Valor inicial do Combustivel
combustivel = turtle.Turtle()
combustivel.shape("Combustivel-cheio.gif")
combustivel.penup()
combustivel.speed(0)
combustivel.setpos(400,350)               # Posição do Sprite

#Pontos
pontos_valor = 0

# Jogador
inicio_jogador = -210                    # Posição do Sprite
jogador = turtle.Turtle()
jogador.speed(0)
jogador.penup()
jogador.sety(inicio_jogador)
jogador.shape("sprite-mario-1.gif")

# Função Iniciar o jogo
def start():                  #Quando a função for chamada dará as velocidades iniciando o jogo
    global veloFundo, andar
    veloFundo = 20
    andar = 30
    return veloFundo, andar

# Funções jogador
def direita():
    global veloFundo
    if jogador.xcor() < 240:  # Limite de onde pode andar DIREITA
        jogador.fd(andar)

def esquerda():
    global veloFundo
    if jogador.xcor() > -260:  # Limite de onde pode andar ESQUERDA
        jogador.bk(andar)
def addGas():                  # Adicionar Combustivel
    global combustivel_valor
    combustivel_valor = 300
    return combustivel_valor


# Mover Jogador
tela.onkey(direita, "Right")
tela.onkey(esquerda, "Left")
tela.onkey(start, "space")
tela.onkey(addGas, "f")
tela.listen()

while True:
    # Loop do fundo infinito em movimento e suas regras
    fundo.goto(0, fundo.ycor() - veloFundo)
    if fundo.ycor() < comeco:
        combustivel_valor -= 10         # Conforme o fundo vai passando o combustivel diminue
        pontos_valor += 20              # Conforme o fundo vai passando os Pontos Aumentam 20
        fundo.speed(0)
        fundo.sety(-comeco)
        fundo.speed(10)
        if jogador.xcor() < -259:       # Colidir na calçada da Esquerda perde Gasolina
            time.sleep(0.001)
            combustivel_valor -= 30
        if jogador.xcor() > 239:        # Colidir na calçada da Direita perde Gasolina
            time.sleep(0.001)
            combustivel_valor -= 30
        print(f"Gasolina: {combustivel_valor}")
        print(f"Pontos: {pontos_valor}")

    #Regra se o combustivel acabar
    if combustivel_valor < 1000 and combustivel_valor >=300 :      # Combustivel muda de sprite
        combustivel.shape("Combustivel-cheio.gif")
        combustivel_valor = 290                                    # Quando entra na condição o jogo fica lento, isso resolve o problema, pois em seguida ele sai da condição

    if combustivel_valor <= 250 and combustivel_valor >= 220:      # Combustivel muda de sprite
        combustivel.shape("Combustivel-meio.gif")
        combustivel_valor = 210                                    # Resolve problema da condição

    if combustivel_valor <= 120 and combustivel_valor >=80:        # Combustivel muda de sprite
        combustivel.shape("Combustivel-baixo.gif")
        combustivel_valor = 70                                     # Resolve problema da condição

    if combustivel_valor <= 0:                                     # Combustivel zerado o Jogo para
        combustivel.shape("Combustivel-zero.gif")
        veloFundo = 0
        andar = 0
        #Velocidade inimigo = 0
        #Velocidade Gasolina = 0


tela.mainloop()
