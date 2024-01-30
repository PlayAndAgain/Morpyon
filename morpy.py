import pyxel
TITLE = "Morpy"
WIDTH = 50
HEIGHT = 59
pyxel.init(WIDTH, HEIGHT, title=TITLE)
pyxel.load("morpy.pyxres")
tour = 1
victoire = False
egalite = False
pyxel.mouse(True)

class case:
    '''crée une classe case avec
        - la position x de son coin supérieur gauche sur la fenetre
        - la position y de son coin supérieur gauche sur la fenetre
        - son appartenance (0 si libre, 1 si elle est au joueur 1 et 2 si elle est au joueur 2'''
    def __init__(self, a, b, c):
        self.x_window = a
        self.y_window = b
        self.player = c
    
    def attribution_case(self, p):
            self.player = p
            pyxel.play(0, tour)
        
haut_gauche = case(0, 9, 0)
haut_milieu = case(17, 9, 0)
haut_droit = case(34, 9, 0)
milieu_gauche = case(0, 26, 0)
centre = case(17,26,0)
milieu_droit = case(34, 26, 0)
bas_gauche = case(0, 43, 0)
bas_milieu = case(17,43,0)
bas_droit = case(34, 43, 0)

grille = [haut_gauche, haut_milieu, haut_droit,
          milieu_gauche, centre, milieu_droit,
          bas_gauche, bas_milieu, bas_droit    ]

def test_ligne(case1, case2, case3):
    '''Test si 3 case appartienne a l'un des joueurs et si oui renvoie ce joueur'''
    if case1.player == 1 and case2.player == 1 and case3.player == 1:
        return 1
    elif case1.player == 2 and case2.player == 2 and case3.player == 2:
        return 2
    else : 
        return 0
def test_grille(g):
    global victoire
    if test_ligne(g[0], g[1], g[2]) != 0:
        victoire = True
        pyxel.play(1, 3)
    
    if test_ligne(g[3], g[4], g[5]) != 0:
        victoire = True
        pyxel.play(1, 3)
    
    if test_ligne(g[6], g[7], g[8]) != 0:
        victoire = True
        pyxel.play(1, 3)
    
    if test_ligne(g[0], g[3], g[6]) != 0:
        victoire = True
        pyxel.play(1, 3)
    
    if test_ligne(g[1], g[4], g[7]) != 0:
        victoire = True
        pyxel.play(1, 3)
        
    if test_ligne(g[2], g[5], g[8]) != 0:
        victoire = True
        pyxel.play(1, 3)
        
    if test_ligne(g[0], g[4], g[8]) != 0:
        victoire = True
        pyxel.play(1, 3)
        
    if test_ligne(g[2], g[4], g[6]) != 0:
        victoire = True
        pyxel.play(1, 3)
        
def test_egalite(tab):
    global egalite
    for case in tab:
        if case.player == 0:
            return None 
    egalite = True
    pyxel.play(1,4)


def clic_sur(self, x,y)-> bool:
        if pyxel.mouse_x >= x and pyxel.mouse_x <= x+16 and pyxel.mouse_y >= y and pyxel.mouse_y <= y+16 and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            return True
        else:
            return False

def draw():
    global tour
    global egalite
    
    pyxel.cls(0)
    pyxel.text(16, 1, "Morpy", 7)
    pyxel.line(16, 9, 16, 59, 7)
    pyxel.line(33, 9, 33, 59, 7)
    pyxel.line(0, 25, 50, 25, 7)
    pyxel.line(0, 42, 50, 42, 7)
    
    if tour == 1:
        pyxel.blt(1,1, 0, 32,0, 8, 8)
    else :
        pyxel.blt(1,1, 0, 40,0, 8, 8)
        
    for case in grille :
        if case.player == 1:
            pyxel.blt(case.x_window, case.y_window, 0, 0, 0, 16, 16, 0)
        if case.player == 2:
            pyxel.blt(case.x_window, case.y_window, 0, 16, 0, 16, 16, 0)
            
    if victoire == True :
        pyxel.rect(3, 24, 46, 24, 13)
        pyxel.text(6, 27, "Le joueur " + str(tour), 11)
        pyxel.text(11, 33, "a gagne !", 11)
        pyxel.text(5, 26, "Le joueur " + str(tour), 3)
        pyxel.text(10, 32, "a gagne !", 3)

        
    if egalite == True :
        pyxel.rect(6, 24, 39, 24, 13)
        pyxel.text(9, 27, "Egalite !", 2)
        pyxel.text(8, 26, "Egalite !", 1)
        
    if victoire == True or egalite == True:
        pyxel.blt(21, 38, 0, 32, 8, 8, 8, 0)
    
                    
def update():
    global tour
    global victoire
    global egalite
    for case in grille :
        if clic_sur(case, case.x_window, case.y_window):
            if case.player == 0 and victoire == False:
                case.attribution_case(tour)
                test_grille(grille)
                if victoire == False and egalite == False:
                    test_egalite(grille)
                    if tour == 1:
                       tour = 2
                    elif tour == 2:
                       tour = 1

                
    if (pyxel.mouse_x >= 21 and pyxel.mouse_x <= 28 and pyxel.mouse_y >= 38 and pyxel.mouse_y <= 46 and pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT) )and (victoire == True or egalite == True):
        tour = 1
        for case in grille:
            case.attribution_case(0)
        victoire = False
        egalite = False 
                    
                        
pyxel.run(update, draw)