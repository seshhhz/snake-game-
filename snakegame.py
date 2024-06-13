# configurações iniciais
import pygame  # importando biblioteca
import random
pygame.init()  # rodando biblioteca pygame

pygame.display.set_caption('snake game')
# definindo variáveis do tamanho da tela
largura, altura = 1280, 720
# sempre usar tupla para definir informações da tela
tela = pygame.display.set_mode((largura, altura))  # variável global
relogio = pygame.time.Clock()
# definir cores do jogo
preto = (0, 0, 0)  # fundo da tela
branco = (255, 255, 255)  # cor da cobra
vermelho = (255, 0, 0)  # cor da pontuação
verde = (0, 255, 0)  # comida

# parâmetro da cobra
tamanho_quadrado = 20
velocidade_jogo = 15  # funciona em função do tempo


def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 20.0) * 20.0
    return comida_x, comida_y


def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])

    
def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela,branco,[pixel[0], pixel[1] ,tamanho, tamanho])    

        
def  desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Anonymous Pro",48)
    texto = fonte.render(f"Pontos: {pontuacao}", True, vermelho)#parametro True serve para ''arredondar'' a fonte se false deixa pixelado
    tela.blit(texto, [1,1])


def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0 

    return velocidade_x , velocidade_y

def rodar_jogo():
    fim_jogo = False

    x = largura / 2
    y = altura / 2

    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1
    pixels = []

    comida_x, comida_y = gerar_comida()

    # loop principal/eventos 
    while not fim_jogo:
        tela.fill(preto)  # Passando cor em formato de "variável"

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)



        # 'desenhar' os objetos do jogo na tela
        
        
        # comida
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)
        
      
        
        #atualizar a posicao da cobra 
        x += velocidade_x
        y += velocidade_y



        # cobra = lista de pixels 
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
             del pixels[0] # cria px um na frente e deleta o primeiro 

        #se cobra bater nela msm fim do jogo 
        for pixel in pixels[:-1]: 
            if pixel == [x,y]:
                fim_jogo = True 
        
        desenhar_cobra(tamanho_quadrado, pixels)

        # pontuação
        desenhar_pontuacao(tamanho_cobra- 1)



        # Atualização da tela
        pygame.display.update()     
    
        #criar nova comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1 
            comida_x, comida_y = gerar_comida()


        relogio.tick(velocidade_jogo)  # Utilizando o relogio para controlar a taxa de atualização


# criar a lógica de término do jogo
# cobra colidir com a parede
# cobra colidir nela mesma

# pegar as interações do usuário
# fechar tela
# ou apertar as teclas de ações no jogo

rodar_jogo()
