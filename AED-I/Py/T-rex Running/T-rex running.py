import time
import random
from graphics import *

def fundo(win):
    win.setBackground("White")
    chao = Line(Point(1, 400), Point(1000, 400))
    chao.setFill("gray")
    chao.draw(win)

def animafundo(win, x):
    y = random.randrange(30, 200) 
    # Para X criar váriavel fora decrementando e migrar para a função -5,-5,-5
    cloud = Image(Point(x, y), "scene/cloud.png")
    cloud.draw(win)
    cloud.move(-10, 0)
    time.sleep(.2)
    cloud.undraw()

def animaobs(win): 
    num = random.randrange(1, 4)
    if num == 1:
        obs = Image(Point(1050, 358), "scene/cactus1.png")
    elif num == 2:
        obs = Image(Point(1050, 358), "scene/cactus2.png")
    else:
        obs = Image(Point(1050, 358), "scene/cactus2.png")
    obs.draw(win)
    x = 0
    obs.move(-30, 0)
    time.sleep(.1)
    x += 30
       



def entrada(win):
    titulo = Image(Point(500,200), "scene/1.png")
    titulo.draw(win)
    rect = Rectangle(Point(200, 50), Point(800, 300))
    rect.draw(win)
    clique = Image(Point(500, 500), "scene/clique.png")
    cactu = Image(Point(800, 400), "scene/cactus1.png")
    cactu.draw(win)
    cactu1 = Image(Point(200, 500), "scene/cactus2.png")
    cactu1.draw(win)
    sun = Image(Point(800, 100), "scene/sun.png")
    sun.draw(win)
    cloud1 = Image(Point(800, 200), "scene/cloud.png")
    cloud1.draw(win)
    cloud2 = Image(Point(180, 100), "scene/cloud.png")
    cloud2.draw(win)
    rexent = Image(Point(500, 358), "rex/Run .png")
    rexent.draw(win)

    i = True
   
    while i:
        if (win.checkMouse() == None):
            update()
            clique.draw(win)
            time.sleep(0.5)
            update()
            clique.undraw()
            time.sleep(0.5)
        else:
            titulo.undraw()
            rect.undraw()
            cactu.undraw()
            cactu1.undraw()
            rexent.undraw()
            cloud1.undraw()
            cloud2.undraw()
            i = False
            




def Main (Titulo: str, W: int, H:int):
    #Cria tela
    
        win = GraphWin(Titulo, W, H, autoflush=False)

        #Cria lista imagens
        corre = ["rex/Run (1).png", "rex/Run (2).png"]
        pula = ["rex/Run (1).png", "rex/Run (2).png"]
        pontos = ["score/0.png", "score/1.png", "score/2.png", "score/3.png", "score/4.png", "score/5.png", "score/6.png", "score/7.png", "score/8.png", "score/9.png"]
        #Cria variáveis
        framerate = 1/60.0
        cont_correndo = 0
        cont_pulando = 0
        centro = Point(500,358)
        x = 500
        cont_x_obs = 0
        cont_x_cloud1 = 0
        cont_x_cloud2 = 0
        cont_pulo = 0
        gameover = False
        pontuacao = 0
        pontlist = [0, 0, 0, 0]
        num0 = "score/0.png"
        num1 = "score/1.png"
        num2 = "score/2.png"
        num3 = "score/3.png"
        num4 = "score/4.png"
        num5 = "score/5.png"
        num6 = "score/6.png"
        num7 = "score/7.png"
        num8 = "score/8.png"
        num9 = "score/9.png"
        posnumum = Point(800,30)
        posnumdois = Point(810,30)
        posnumtres = Point(820,30)
        posnumquatro = Point(830,30)
        
        numum = Image(posnumum, num0)
        numum.draw(win)
        numdois = Image(posnumdois, num0)
        numdois.draw(win)
        numtres = Image(posnumtres, num0)
        numtres.draw(win)
        numquatro = Image(posnumquatro, num0)
        numquatro.draw(win)

        obs = Image(Point(1050, 385), "scene/cactus2.png")
        obs.draw(win)

        cloud1 = Image(Point(1300, 200), "scene/cloud.png")
        cloud1.draw(win)
        cloud2 = Image(Point(2300, 100), "scene/cloud.png")
        cloud2.draw(win)


        imagem = Image(centro, "rex/Run .png")
        imagem.draw(win)

        #chama funções
        fundo(win)
        entrada(win)

        #Animação de personagem para ponto de partida
        i = True
        while i:
        
            imagem.undraw()
            
            t = str(imagem.getAnchor())
            strsplit = t.split(",")
            
            
            if (strsplit[0] == "Point(100.0"):
                imagem.draw(win)
                i = False
                centro = imagem.getAnchor()
            else:
                x -= 20
                imagem = Image(Point(x, 358), corre[cont_correndo])
                imagem.draw(win)
                time.sleep(.1)
                cont_correndo += 1
                if cont_correndo >= 2:
                    cont_correndo = 0
            update()
            time.sleep(framerate)
        #Começa jogo
        #Equanto a janela não for fechada
        while win.closed == False:
            #Movimento personagem
            verifica = win.checkKey()
            imagem.undraw()
            numum.undraw()
            numdois.undraw()
            numtres.undraw()
            numquatro.undraw()


            pontuacao += 1
            pontstr = str(pontuacao)
            print(pontstr)
            if pontuacao > 1000:
                pontlist[0] = pontstr[0]
                pontlist[1] = pontstr[1]
                pontlist[2] = pontstr[2]
                pontlist[3] = pontstr[3]
            elif pontuacao > 99:
                pontlist[0] = "0"
                pontlist[1] = pontstr[0]
                pontlist[2] = pontstr[1]
                pontlist[3] = pontstr[2]
            elif pontuacao > 9:
                pontlist[0] = "0"
                pontlist[1] = "0"
                pontlist[2] = pontstr[0]
                pontlist[3] = pontstr[1]
            elif pontuacao > 0:
                pontlist[0] = "0"
                pontlist[1] = "0"
                pontlist[2] = "0"
                pontlist[3] = pontstr[0]

            if (pontlist[0] == "0"):
                numum = Image(posnumum, num0)
                numum.draw(win)
            elif (pontlist[0] == "1"):
                numum = Image(posnumum, num1)
                numum.draw(win)
            elif (pontlist[0] == "2"):
                numum = Image(posnumum, num2)
                numum.draw(win)
            elif (pontlist[0] == "3"):
                numum = Image(posnumum, num3)
                numum.draw(win)
            elif (pontlist[0] == "4"):
                numum = Image(posnumum, num4)
                numum.draw()
            elif (pontlist[0] == "5"):
                numum = Image(posnumum, num5)
                numum.draw(win)
            elif (pontlist[0] == "6"):
                numum = Image(posnumum, num6)
                numum.draw(win)
            elif (pontlist[0] == "7"):
                numum = Image(posnumum, num7)
                numum.draw(win)
            elif (pontlist[0] == "8"):
                numum = Image(posnumum, num8)
                numum.draw(win)
            elif (pontlist[0] == "9"):
                numum = Image(posnumum, num9)
                numum.draw(win)

            if (pontlist[1] == "0"):
                numdois = Image(posnumdois, num0)
                numdois.draw(win)
            elif (pontlist[1] == "1"):
                numdois = Image(posnumdois, num1)
                numdois.draw(win)
            elif (pontlist[1] == "2"):
                numdois = Image(posnumdois, num2)
                numdois.draw(win)
            elif (pontlist[1] == "3"):
                numdois = Image(posnumdois, num3)
                numdois.draw(win)
            elif (pontlist[1] == "4"):
                numdois = Image(posnumdois, num4)
                numdois.draw(win)
            elif (pontlist[1] == "5"):
                numdois = Image(posnumdois, num5)
                numdois.draw(win)
            elif (pontlist[1] == "6"):
                numdois = Image(posnumdois, num6)
                numdois.draw(win)
            elif (pontlist[1] == "7"):
                numdois = Image(posnumdois, num7)
                numdois.draw(win)
            elif (pontlist[1] == "8"):
                numdois = Image(posnumdois, num8)
                numdois.draw(win)
            elif (pontlist[1] == "9"):
                numdois = Image(posnumdois, num9)
                numdois.draw(win)

            if (pontlist[2] == "0"):
                numtres = Image(posnumtres, num0)
                numtres.draw(win)
            elif (pontlist[2] == "1"):
                numtres = Image(posnumtres, num1)
                numtres.draw(win)
            elif (pontlist[2] == "2"):
                numtres = Image(posnumtres, num2)
                numtres.draw(win)
            elif (pontlist[2] == "3"):
                numtres = Image(posnumtres, num3)
                numtres.draw(win)
            elif (pontlist[2] == "4"):
                numtres = Image(posnumtres, num4)
                numtres.draw(win)
            elif (pontlist[2] == "5"):
                numtres = Image(posnumtres, num5)
                numtres.draw(win)
            elif (pontlist[2] == "6"):
                numtres = Image(posnumtres, num6)
                numtres.draw(win)
            elif (pontlist[2] == "7"):
                numtres = Image(posnumtres, num7)
                numtres.draw(win)
            elif (pontlist[2] == "8"):
                numtres = Image(posnumtres, num8)
                numtres.draw(win)
            elif (pontlist[2] == "9"):
                numtres = Image(posnumtres, num9)
                numtres.draw(win)
            
            if (pontlist[3] == "0"):
                numquatro = Image(posnumquatro, num0)
                numquatro.draw(win)
            elif (pontlist[3] == "1"):
                numquatro = Image(posnumquatro, num1)
                numquatro.draw(win)
            elif (pontlist[3] == "2"):
                numquatro = Image(posnumquatro, num2)
                numquatro.draw(win)
            elif (pontlist[3] == "3"):
                numquatro = Image(posnumquatro, num3)
                numquatro.draw(win)
            elif (pontlist[3] == "4"):
                numquatro = Image(posnumquatro, num4)
                numquatro.draw(win)
            elif (pontlist[3] == "5"):
                numquatro = Image(posnumquatro, num5)
                numquatro.draw(win)
            elif (pontlist[3] == "6"):
                numquatro = Image(posnumquatro, num6)
                numquatro.draw(win)
            elif (pontlist[3] == "7"):
                numquatro = Image(posnumquatro, num7)
                numquatro.draw(win)
            elif (pontlist[3] == "8"):
                numquatro = Image(posnumquatro, num8)
                numquatro.draw(win)
            elif (pontlist[3] == "9"):
                numquatro = Image(posnumquatro, num9)
                numquatro.draw(win)



            if (cont_pulo >= 0):
                if (cont_pulo > 4):
                    centro = imagem.getAnchor()
                    imagem = Image(centro, pula[cont_pulando])
                    imagem.draw(win)
                    time.sleep(.1)
                    imagem.move(10, -50)
                    cont_pulando += 1
                    if cont_pulando >= 2:
                            cont_pulando = 0 
                    cont_pulo -= 1
                elif (cont_pulo > 0):
                    centro = imagem.getAnchor()
                    imagem = Image(centro, pula[cont_pulando])
                    imagem.draw(win)
                    time.sleep(.1)
                    imagem.move(-10, 50)
                    cont_pulando += 1
                    if cont_pulando >= 2:
                            cont_pulando = 0 
                    cont_pulo -= 1
                else:  
                    imagem.undraw()
                    cont_pulo -= 1
        

            


            if (verifica == "Up") and (cont_pulo == -1):
                cont_pulo = 8   
            elif (verifica == "") and (cont_pulo == -1):
                centro = imagem.getAnchor()
                imagem = Image(centro, corre[cont_correndo])
                imagem.draw(win)
                time.sleep(.1)
                cont_correndo += 1
                if cont_correndo >= 2:
                    cont_correndo = 0
            
            
            #Animação obstáculo
            if cont_x_obs > 1050:
                cont_x_obs = 0
                obs.move(1050, 0)
            else:
                obs.move(-30, 0)
                cont_x_obs += 30

    

            centro_obsx = int(obs.getAnchor().getX())
            centro_obsy = int(obs.getAnchor().getY())
            bordax_obs = centro_obsx - 35
            borday_obs = centro_obsy - 85

            centro_rexx = int(imagem.getAnchor().getX())
            centro_rexy = int(imagem.getAnchor().getY())
            bordax_rex = centro_rexx + 30
            borday_rex = centro_rexy + 30

            

            if cont_x_cloud1 >= 1300:
                cont_x_cloud1 = 0
                cloud1.move(1300, 0)
            else:
                cloud1.move(-10, 0)
                cont_x_cloud1 += 10
            
            if cont_x_cloud2 >= 2300:
                cont_x_cloud2 = 0
                cloud2.move(2300, 0)
            else:
                cloud2.move(-20, 0)
                cont_x_cloud2 += 20
        
            

            if bordax_obs < bordax_rex and bordax_obs >= 75 and borday_rex >= borday_obs:
                againb = Image(Point(500, 280), "scene/playagain.png")
                againb.draw(win)
                gameover = Image(Point(500, 250), "scene/gameover.png")
                gameover.draw(win)
                click = win.getMouse()
                xm = click.x
                ym = click.y
                if (483<xm<518) and (267<ym<296):
                    cont_x_obs = 0
                    obs.undraw()
                    obs = Image(Point(1050, 385), "scene/cactus2.png")
                    obs.draw(win)
                    gameover.undraw()
                    againb.undraw()
                    pontuacao = 0
                else:
                    win.close()



        #Este comando faz a janela ser atualizada a cada frame
        update()
        #Este comando faz com que o framerate fique sempre abaixo de 60fps
        time.sleep(framerate)




Main("T-rex running", 1000, 600)
