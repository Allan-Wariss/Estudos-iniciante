import turtle
tela = turtle.Screen()             # Faz a tela do jogo
tela.title("Vrum Vrum THE GAME")   # Titulo da janela
tela.setup(1000,600)               # Resolução da tela em px
tela.bgcolor("black")              # background para analisar o erro do fundo animado
tela.addshape("background.gif")    # fundo animado
tela.addshape("sprite-mario-1.gif")# Sprite jogador

#Configuração fundo
fundo = turtle.Turtle()
fundo.speed(10)
fundo.penup()
fundo.shape("background.gif")

comeco = -580                     # Indica a coordenada Y do Fundo 2
fundo2 = turtle.Turtle()
fundo2.penup()
fundo2.speed(0)
fundo2.sety(-comeco)
fundo2.speed(10)
fundo2.shape("background.gif")


#Jogador
inicio_jogador = -170
jogador = turtle.Turtle()
jogador.penup()
jogador.speed(0)
jogador.sety(inicio_jogador)
jogador.shape("sprite-mario-1.gif")

# Mover jogador
def direita():
    if jogador.xcor() < 245:
        jogador.fd(25)
def esquerda():
    if jogador.xcor() > -250:
        jogador.bk(25)
tela.onkeypress(direita,"Right")
tela.onkeypress(esquerda,"Left")
tela.listen()



while True:
    #Loop do fundo infinito
    fundo.goto(0, fundo.ycor()-20)
    fundo2.goto(0, fundo2.ycor()-20)
    if fundo.ycor() < comeco:
        fundo.speed(0)
        fundo.sety(-comeco)
        fundo.speed(10)
    if fundo2.ycor() < comeco:
        fundo2.speed(0)
        fundo2.sety(-comeco)
        fundo2.speed(10)







tela.mainloop()


