import turtle
import time
import random
import math
import winsound

tela = turtle.Screen()                   # Faz a tela do jogo
tela.title("Vrum Vrum THE GAME")         # Titulo da janela
tela.setup(1000, 750)                    # Resolução da tela em px
tela.bgcolor("black")                    # background para analisar o erro do fundo animado
tela.addshape("background-grande.gif")   # fundo animado
tela.addshape("sprite-mario-1.gif")      # Sprites jogador
tela.addshape("sprite-mario-2.gif")      #-
tela.addshape("sprite-mario-3.gif")      #-
tela.addshape("sprite-mario-4.gif")      #-
tela.addshape("sprite-mario-5.gif")      #-
tela.addshape("sprite-mario-6.gif")      #-
tela.addshape("sprite-mario-7.gif")      #-
tela.addshape("sprite-mario-8.gif")      #-
tela.addshape("sprite-mario-9.gif")      #-
tela.addshape("sprite-mario-10.gif")     #-
tela.addshape("sprite-mario-11.gif")     #-
tela.addshape("sprite-mario-12.gif")     #-
tela.addshape("sprite-mario-13.gif")     #-
tela.addshape("sprite-bowser-1.gif")     # Sprite inimigo 1
tela.addshape("sprite-luigi-1.gif")      # Sprite inimigo 2
tela.addshape("cogumelo.gif")            # Sprite cogumelo
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

#Mensagem de iniciar o jogo
mensagem = turtle.Turtle()                # Mensagem para indicar o jogar que tecla apertar para iniciar
mensagem.hideturtle()
mensagem.color("white")
mensagem.up()
mensagem.write("APERTE ESPAÇO PARA INICIAR ", False,align="center", font=('impact', 50, 'normal'))

# Mensagem de fim de jogo
perdeu = turtle.Turtle()  # Mensagem para indicar fim de jogo
perdeu.hideturtle()
perdeu.color("red")
perdeu.up()


#Pontos
pontos_valor = 0         # Valor inicial dos Pontos
pontos = turtle.Turtle()
pontos.hideturtle()      # Esconde o shape do Turtle# Desenha o valor de pontos na tela
pontos.up()
pontos.speed(0)
pontos.setpos(-480,320)  # Pontos será mostrado no canto superior esquerdo
pontos.color("white")    # Cor dos Pontos

#Variaveis de random
xg = random.randint(-230, 230)            # Aleatoriedade do X cogumelo
yg = random.randint(1600,2000)            # Aleatoriedade do Y cogumelo
x1 = random.randint(-200, 200)            # Aleatoriedade do X inimigo 1
x2 = random.randint(-100, 200)            # Aleatoriedade do X inimigo 2
y1 = random.randint(700,1000)             # Aleatoriedade do Y inimigo 1
y2 = random.randint(500,800)              # Aleatoriedade do Y inimigo 2

# Cogumelo
inicio_coguY = yg                      # Cogumelo coordenada fora da tela
inicio_coguX = xg                      # Cogumelo coordenada gerada em lugar aleatorio no eixo X
cogumelo = turtle.Turtle()
cogumelo.penup()
cogumelo.speed(0)                      # Velocidade = 0 para teleportar sem ser visto
cogumelo.sety(inicio_coguY)            # Cogumelo aparece fora da tela
cogumelo.setx(inicio_coguX)            # Cogumelo aparece em lugar aleatorio no eixo X
cogumelo.shape("cogumelo.gif")

# Inimigo1
inicio_inimigo1Y = y1                     # Inimigo coordenada fora da tela
inicio_inimigo1X = x1                     # Inimigo coordenada gerada em lugar aleatorio no eixo X
inimigo1 = turtle.Turtle()
inimigo1.penup()
inimigo1.speed(0)                          # Velocidade = 0 para teleportar sem ser visto
inimigo1.sety(inicio_inimigo1Y)            # Inimigo aparece fora da tela
inimigo1.setx(inicio_inimigo1X)            # Inimigo aparece em lugar aleatorio no eixo X
inimigo1.shape("sprite-bowser-1.gif")

# Inimigo2
inicio_inimigo2Y = y2                       # Inimigo2 coordenada fora da tela
inicio_inimigo2X = x2                       # Inimigo 2coordenada gerada em lugar aleatorio no eixo X
inimigo2 = turtle.Turtle()
inimigo2.penup()
inimigo2.speed(0)                           # Velocidade = 0 para teleportar sem ser visto
inimigo2.sety(inicio_inimigo2Y)             # Inimigo2 aparece fora da tela
inimigo2.setx(inicio_inimigo2X)             # Inimigo2 aparece em lugar aleatorio no eixo X
inimigo2.shape("sprite-luigi-1.gif")

# Jogador
inicio_jogador = -270                    # Posição do Sprite
jogador = turtle.Turtle()
jogador.speed(0)                         # Velocidade = 0 para teleportar sem ser visto
jogador.penup()
jogador.sety(inicio_jogador)
jogador.shape("sprite-mario-1.gif")

#winsound.PlaySound('som_game.wav', winsound.SND_FILENAME)
# Função Iniciar o jogo
def start():                                # Quando chamada iniciará ou reiniciará o jogo
    mensagem.clear()                        # Quando o jogo iniciar a mensagem é apagada
    perdeu.clear()                          # Caso a função seja usada para reiniciar, apaga a mensagem de fim de jogo
    global veloFundo, andar, veloInimigo, pontos_valor, combustivel_valor # Pega as globais
    pontos_valor = 0         # Pontos inicia ou reinicia para
    combustivel_valor = 300  # Combustivel fica = 300
    veloFundo = 80           # velocidade do fundo fica = 80
    veloInimigo = 20         # velocidade dos inimigos fica = 20
    andar = 30               # velocidade do jogador = 30
    pontos.clear()           # pontos apaga para ser desenhado de novo
    pontos.write(f"Pontos: {pontos_valor} ", False, font=('Arial', 30, 'normal'))  # Desenha os pontos na tela
    cogumelo.sety(inicio_coguY)     # Reinicia a posição de todos
    cogumelo.setx(inicio_coguX)     # -
    inimigo1.sety(inicio_inimigo1Y) # -
    inimigo1.setx(inicio_inimigo1X) # -
    inimigo2.sety(inicio_inimigo2Y) # -
    inimigo2.setx(inicio_inimigo2X) # -
    jogador.setx(0)                 # -
    fundo.sety(-comeco)             # -
    perdeu.clear() # Caso a função seja usada para reiniciar, apaga a mensagem de fim de jogo



def colisao():
    global combustivel_valor, inicio_inimigo1X, inicio_inimigo1Y, inicio_inimigo2X, inicio_inimigo2Y, andar
    andar = 0                           # Jogador não ande durante a colisão
    combustivel_valor -= 50             # Colisão com inimigo perde 50 de combustivel
    #Animação da colisão
    jogador.shape("sprite-mario-2.gif") # Sprite que mudará
    time.sleep(0.01)                    # Tempo que de um sprite para o outro
    jogador.shape("sprite-mario-3.gif")
    time.sleep(0.01)
    jogador.shape("sprite-mario-4.gif")
    time.sleep(0.01)
    jogador.shape("sprite-mario-5.gif")
    time.sleep(0.01)
    jogador.shape("sprite-mario-6.gif")
    time.sleep(0.1)
    jogador.shape("sprite-mario-7.gif")
    time.sleep(0.01)
    jogador.shape("sprite-mario-8.gif")
    time.sleep(0.01)
    jogador.shape("sprite-mario-9.gif")
    time.sleep(0.1)
    jogador.shape("sprite-mario-10.gif")
    time.sleep(0.01)
    jogador.shape("sprite-mario-11.gif")
    time.sleep(0.01)
    jogador.shape("sprite-mario-12.gif")
    time.sleep(0.01)
    jogador.shape("sprite-mario-13.gif")
    time.sleep(0.01)
    jogador.shape("sprite-mario-1.gif")
    time.sleep(0.01)
    inicio_inimigo1X = random.randint(-230, 200)  #Sorteia de novo a posição
    inicio_inimigo1Y = random.randint(700,1000)   #Sorteia de novo a posição
    inicio_inimigo2X = random.randint(-100, 210)  #Sorteia de novo a posição
    inicio_inimigo2Y = random.randint(500,800)    #Sorteia de novo a posição
    inimigo1.speed(10)              # Speed para animação suave do inimigo voltando quando colidir
    inimigo2.speed(10)              # Speed para animação suave do inimigo voltando quando colidir
    fundo.speed(5)                  # Speed para animação suave do inimigo voltando quando colidir
    fundo.sety(-comeco)             # Fundo volta na colisão (impressão que o carro voltou)
    fundo.speed(0)                  # Speed 0 para sincronizar com a animação padrão do fundo
    cogumelo.sety(inicio_coguY)     # Teleportes dos cogumelo quando houver colisão
    cogumelo.setx(inicio_coguX)     # -
    inimigo1.sety(inicio_inimigo1Y) # Teleportes dos inimigos quando houver colisão
    inimigo1.setx(inicio_inimigo1X) # -
    inimigo2.sety(inicio_inimigo2Y) # -
    inimigo2.setx(inicio_inimigo2X) # -
    inimigo1.speed(0)               # Speed 0 para sincronizar com a animação padrão
    inimigo2.speed(0)               # Speed 0 para sincronizar com a animação padrão
    andar = 30                      # Jogador volta a andar

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
    global combustivel_valor, inicio_coguX, inicio_coguY
    combustivel_valor = 300
    inicio_coguX = random.randint(-230, 230) # Quando colidir e adicionar o combustivel sorteia de novo o eixo X
    inicio_coguY = random.randint(1700,1900) # Quando colidir e adicionar o combustivel sorteia de novo o eixo Y
    cogumelo.sety(inicio_coguY)  # Teleportes dos cogumelo quando houver colisão
    cogumelo.setx(inicio_coguX)  # -
    return combustivel_valor


# Mover Jogador
tela.onkey(direita, "Right")
tela.onkey(esquerda, "Left")
tela.onkey(start, "space")
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

    if jogador.xcor() < -225:       # Colidir na calçada da Esquerda perde Gasolina
        colisao()
        jogador.speed(10)
        jogador.setx(0)
        jogador.speed(0)
    if jogador.xcor() > 210:        # Colidir na calçada da Direita perde Gasolina
        colisao()
        jogador.speed(10)
        jogador.setx(0)
        jogador.speed(0)

    #Movimento inimigo1
    inimigo1.goto(inicio_inimigo1X, inimigo1.ycor() - veloInimigo) # Regra de movimento
    if inimigo1.ycor() < comeco:                                   # Se sair do limite da tela volta para cima com um novo valor de X
        inicio_inimigo1X = random.randint(-200, 100)               # Tira aleatoriedade X de novo quando sair da tela
        inimigo1.speed(0)
        inimigo1.sety(inicio_inimigo1Y)
        inimigo1.setx(inicio_inimigo1X)

    # Movimento inimigo2
    inimigo2.goto(inicio_inimigo2X, inimigo2.ycor() - veloInimigo)  # Regra de movimento
    if inimigo2.ycor() < comeco:                                    # Se sair do limite da tela volta para cima com um novo valor de X
        inicio_inimigo2X = random.randint(-100, 200)                # Tira aleatoriedade X de novo quando sair da tela
        inimigo2.speed(0)
        inimigo2.sety(inicio_inimigo2Y)
        inimigo2.setx(inicio_inimigo2X)

    # Movimento cogumelo
    cogumelo.goto(inicio_coguX, cogumelo.ycor() - veloInimigo)  # Regra de movimento
    if cogumelo.ycor() < comeco:  # Se sair do limite da tela volta para cima com um novo valor de X
        inicio_coguX = random.randint(-100, 250)  # Tira aleatoriedade X de novo quando sair da tela
        cogumelo.speed(0)
        cogumelo.sety(inicio_coguY)
        cogumelo.setx(inicio_coguX)


    #Colisão
    di1 = math.sqrt((jogador.xcor() - inimigo1.xcor())**2 + (jogador.ycor() - inimigo1.ycor())**2)       # Colisao com inimigo1
    di2 = math.sqrt((jogador.xcor() - inimigo2.xcor()) ** 2 + (jogador.ycor() - inimigo2.ycor()) ** 2)   # Colisao com inimigo2
    dg = math.sqrt((jogador.xcor() - cogumelo.xcor()) ** 2 + (jogador.ycor() - cogumelo.ycor()) ** 2)    # Colisao com Cogumelo
    dii = math.sqrt((inimigo2.xcor() - inimigo1.xcor()) ** 2 + (inimigo2.ycor() - inimigo1.ycor()) ** 2) # Colisao inimigo com inimigo,nao nascem juntos
    dgi1 = math.sqrt((cogumelo.xcor() - inimigo1.xcor()) ** 2 + (cogumelo.ycor() - inimigo1.ycor()) ** 2)# Colisao cogumelo com inimigo1,nao nascem juntos
    dgi2 = math.sqrt((cogumelo.xcor() - inimigo2.xcor()) ** 2 + (cogumelo.ycor() - inimigo2.ycor()) ** 2)# Colisao cogumelo com inimigo2,nao nascem juntos

    distancia = 130           # O quanto cada objeto deve obedecer a esta distância
    if di1 <= distancia:      # Colisão jogador e inimigo1
        colisao()
    if di2 <= distancia:      # Colisão jogador e inimigo2
        colisao()
    if dg <= distancia:       # Colisão jogador e Cogumelo
        addGas()
    if dii <= distancia + 20: # Colisão entre inimigos, evitar que nasçam em cima do outro
        inicio_inimigo2X = x2
        inicio_inimigo2Y = y2
        inimigo2.sety(inicio_inimigo2Y)
        inimigo2.setx(inicio_inimigo2X)
    if dgi1 <= distancia:    # Colisão entre cogumelo e inimigo1, evitar que nasçam em cima do outro
        inicio_coguX = xg
        inicio_coguY = yg
        cogumelo.sety(inicio_coguY)
        cogumelo.setx(inicio_coguX)
    if dgi2 <= distancia:    # Colisão entre cogumelo e inimigo2, evitar que nasçam em cima do outro
        inicio_coguX = xg
        inicio_coguY = yg
        cogumelo.sety(inicio_coguY)
        cogumelo.setx(inicio_coguX)

    #Regra se o combustivel acabar
    if combustivel_valor < 1000 and combustivel_valor >=300 :      # Combustivel muda de sprite
        combustivel.shape("Combustivel-cheio.gif")
        combustivel_valor = 290 # Quando entra na condição o jogo fica lento, isso resolve o problema, pois em seguida ele sai da condição

    if combustivel_valor <= 220 and combustivel_valor >= 190:      # Combustivel muda de sprite
        combustivel.shape("Combustivel-meio.gif")
        combustivel_valor = 180                                    # Resolve problema da condição

    if combustivel_valor <= 150 and combustivel_valor >=90:        # Combustivel muda de sprite
        combustivel.shape("Combustivel-baixo.gif")
        combustivel_valor = 80                                     # Resolve problema da condição

    if combustivel_valor <= 0:                                     # Combustivel zerado o Jogo para
        combustivel.shape("Combustivel-zero.gif")
        perdeu.write("         Gasolina ACABOU ;-; \n Reinicie o jogo no ESPAÇO ", False, align="center", font=('impact', 50, 'normal'))
        veloFundo = 0                   # Combustivel acabar o fundo para
        andar = 0                       # Combustivel acabar o jogador para
        veloInimigo = 0                 # Combustivel acabar os inimigos param
        combustivel_valor = 2000        # Desbuga a função start() quando usada para reiniciar quando o combustivel adiquirir valor negativo

tela.mainloop()
