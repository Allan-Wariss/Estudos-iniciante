import turtle
import time
import random
import math

tela = turtle.Screen()                   # Faz a tela do jogo
tela.title("Vrum Vrum THE GAME")         # Titulo da janela
tela.setup(1000, 750)                    # Resolução da tela em px
tela.bgcolor("black")                    # background para analisar o erro do fundo animado
tela.addshape("background-grande.gif")   # fundo animado
tela.addshape("sprite-mario-1.gif")      # Sprite jogador
tela.addshape("sprite-bowser-1.gif")     # Sprite inimigo 1
tela.addshape("sprite-luigi-1.gif")      # Sprite inimigo 2
tela.addshape("Combustivel-cheio.gif")   # Sprites Combustivel
tela.addshape("Combustivel-meio.gif")    # -
tela.addshape("Combustivel-baixo.gif")   # -
tela.addshape("Combustivel-zero.gif")    # -

#Velocidades
veloFundo = 0
veloInimigo = 0
andar = 0

# Configuração fundo
comeco = -560
fundo = turtle.Turtle()
fundo.speed(0)
fundo.penup()
fundo.shape("background-grande.gif")

#Combustivel
combustivel_valor = 300                   # Valor inicial do Combustivel
combustivel = turtle.Turtle()
combustivel.shape("Combustivel-cheio.gif")
combustivel.penup()
combustivel.speed(0)                      # Velocidade = 0 para teleportar sem ser visto
combustivel.setpos(400,350)               # Posição do Sprite

#Pontos
pontos_valor = 0         # Valor inicial dos Pontos
pontos = turtle.Turtle()
pontos.hideturtle()      # Esconde o shape do Turtle# Desenha o valor de pontos na tela
pontos.up()
pontos.speed(0)
pontos.setpos(-480,320)  # Pontos será mostrado no canto superior esquerdo
pontos.color("white")    # Cor dos Pontos



# Jogador
inicio_jogador = -270                    # Posição do Sprite
jogador = turtle.Turtle()
jogador.shape("sprite-mario-1.gif")
jogador.speed(0)                         # Velocidade = 0 para teleportar sem ser visto
jogador.penup()
jogador.sety(inicio_jogador)


#Variaveis de random
x1 = random.randint(-230, 100)            # Aleatoriedade do X inimigo 1
x2 = random.randint(-100, 250)            # Aleatoriedade do X inimigo 2
y1 = random.randint(700,1000)             # Aleatoriedade do Y inimigo 1
y2 = random.randint(500,800)              # Aleatoriedade do Y inimigo 2
# Inimigo
inicio_inimigo1Y = y1                     # Inimigo coordenada fora da tela
inicio_inimigo1X = x1                     # Inimigo coordenada gerada em lugar aleatorio no eixo X
inimigo1 = turtle.Turtle()
inimigo1.shape("sprite-bowser-1.gif")
inimigo1.penup()
inimigo1.speed(0)                          # Velocidade = 0 para teleportar sem ser visto
inimigo1.sety(inicio_inimigo1Y)            # Inimigo aparece fora da tela
inimigo1.setx(inicio_inimigo1X)            # Inimigo aparece em lugar aleatorio no eixo X


# Inimigo2
inicio_inimigo2Y = y2                       # Inimigo2 coordenada fora da tela
inicio_inimigo2X = x2                       # Inimigo 2coordenada gerada em lugar aleatorio no eixo X
inimigo2 = turtle.Turtle()
inimigo2.shape("sprite-luigi-1.gif")
inimigo2.penup()
inimigo2.speed(0)                           # Velocidade = 0 para teleportar sem ser visto
inimigo2.sety(inicio_inimigo2Y)             # Inimigo2 aparece fora da tela
inimigo2.setx(inicio_inimigo2X)             # Inimigo2 aparece em lugar aleatorio no eixo X


# Função Iniciar o jogo
def start():                                #Quando a função for chamada dará as velocidades iniciando o jogo
    global veloFundo, andar, veloInimigo
    veloFundo = 80
    veloInimigo = 20
    andar = 30
    return veloFundo, andar

def colisao():
    global combustivel_valor
    combustivel_valor -= 50         # Colisão com inimigo perde 50 de combustivel
    inimigo1.speed(10)              # Speed para animação suave do inimigo voltando quando colidir
    inimigo2.speed(10)              # Speed para animação suave do inimigo voltando quando colidir
    fundo.speed(5)                  # Speed para animação suave do inimigo voltando quando colidir
    fundo.sety(-comeco)             # Fundo volta na colisão (impressão que o carro voltou)
    fundo.speed(0)                  # Speed 0 para sincronizar com a animação padrão do fundo
    inimigo1.sety(inicio_inimigo1Y) # Teleportes dos inimigos quando houver colisão
    inimigo1.setx(inicio_inimigo1X) #-
    inimigo2.sety(inicio_inimigo2Y) #-
    inimigo2.setx(inicio_inimigo2X) #-
    inimigo1.speed(0)               # Speed 0 para sincronizar com a animação padrão
    inimigo2.speed(0)               # Speed 0 para sincronizar com a animação padrão
    time.sleep(0.5)                 # Jogo congela 0.5s para ocorrer essa função

# Funções jogador
def direita():
    global veloFundo
    if jogador.xcor() < 240:  # Limite de onde pode andar DIREITA
        jogador.fd(andar)

def esquerda():
    global veloFundo
    if jogador.xcor() > -260:  # Limite de onde pode andar ESQUERDA
        jogador.bk(andar)

# Adicionar Combustivel
def addGas():
    global combustivel_valor
    combustivel_valor = 300
    return combustivel_valor


# Mover Jogador
tela.onkey(direita, "Right")
tela.onkey(esquerda, "Left")
tela.onkey(start, "space")
tela.onkey(addGas, "f")
tela.listen()

#loop do jogo
while True:
    # Loop do fundo infinito em movimento e suas regras
    fundo.goto(0, fundo.ycor() - veloFundo)
    if fundo.ycor() < comeco:
        combustivel_valor -= 10                 # Conforme o fundo vai passando o combustivel diminue
        pontos_valor += 20                      # Conforme o fundo vai passando os Pontos Aumentam 20
        fundo.sety(-comeco)
        print(f"Gasolina: {combustivel_valor}") # Print combustivel no console
        print(f"Pontos: {pontos_valor}")        # Print pontos no console
        pontos.clear()                          # Apaga desenho dos pontos anteriores, para não ficar sobreposto
        pontos.write(f"Pontos: {pontos_valor} ", False, font=('Arial', 30, 'normal')) # Desenha os pontos na tela

        if jogador.xcor() < -259:       # Colidir na calçada da Esquerda perde Gasolina
            time.sleep(0.01)
            combustivel_valor -= 30
        if jogador.xcor() > 239:        # Colidir na calçada da Direita perde Gasolina
            time.sleep(0.01)
            combustivel_valor -= 30


    #Movimento inimigo1
    inimigo1.goto(inicio_inimigo1X, inimigo1.ycor() - veloInimigo) # Regra de movimento
    if inimigo1.ycor() < comeco:                                   # Se sair do limite da tela volta para cima com um novo valor de X
        inicio_inimigo1X = random.randint(-230, 100)               # Tira aleatoriedade X de novo quando sair da tela
        inimigo1.speed(0)
        inimigo1.sety(inicio_inimigo1Y)
        inimigo1.setx(inicio_inimigo1X)


    # Movimento inimigo2
    inimigo2.goto(inicio_inimigo2X, inimigo2.ycor() - veloInimigo)  # Regra de movimento
    if inimigo2.ycor() < comeco:                                    # Se sair do limite da tela volta para cima com um novo valor de X
        inicio_inimigo2X = random.randint(-100, 250)                # Tira aleatoriedade X de novo quando sair da tela
        inimigo2.speed(0)
        inimigo2.sety(inicio_inimigo2Y)
        inimigo2.setx(inicio_inimigo2X)


    #Colisão
    di1 = math.sqrt((jogador.xcor() - inimigo1.xcor())**2 + (jogador.ycor() - inimigo1.ycor())**2)       # Colisao com inimigo1
    di2 = math.sqrt((jogador.xcor() - inimigo2.xcor()) ** 2 + (jogador.ycor() - inimigo2.ycor()) ** 2)   # Colisao com inimigo2
    dii = math.sqrt((inimigo2.xcor() - inimigo1.xcor()) ** 2 + (inimigo2.ycor() - inimigo1.ycor()) ** 2) # Colisao inimigo com inimigo,nao nascem juntos
    if di1 <= 95:
        colisao()
    if di2 <= 95:
        colisao()
    if dii <= 200:
        inicio_inimigo2X = x2
        inicio_inimigo2Y = y2
        inimigo2.sety(inicio_inimigo1Y)
        inimigo2.setx(inicio_inimigo1X)

    #Regra se o combustivel acabar
    if combustivel_valor < 1000 and combustivel_valor >=300 :      # Combustivel muda de sprite
        combustivel.shape("Combustivel-cheio.gif")
        combustivel_valor = 290 # Quando entra na condição o jogo fica lento, isso resolve o problema, pois em seguida ele sai da condição

    if combustivel_valor <= 250 and combustivel_valor >= 220:      # Combustivel muda de sprite
        combustivel.shape("Combustivel-meio.gif")
        combustivel_valor = 210                                    # Resolve problema da condição

    if combustivel_valor <= 150 and combustivel_valor >=90:        # Combustivel muda de sprite
        combustivel.shape("Combustivel-baixo.gif")
        combustivel_valor = 80                                     # Resolve problema da condição

    if combustivel_valor <= 0:                                     # Combustivel zerado o Jogo para
        combustivel.shape("Combustivel-zero.gif")
        veloFundo = 0
        andar = 0
        veloInimigo = 0
        #Velocidade Gasolina = 0



tela.mainloop()
