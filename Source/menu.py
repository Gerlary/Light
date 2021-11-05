
import pygame as pg
from time import sleep, time
from os import system, path
from ctypes import windll
from math import *
from random import randint

BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
PURPLE = 255, 0, 255
YELLOW = 255, 255, 0
GRAY = 128, 128, 128
S_GRAY = 90, 90, 90
SS_GRAY = 64, 64, 64
ORANGE = 255, 128, 0
S_BLACK = 40, 40, 40
B_PURPLE = 128, 0, 128
L_BLUE = 0, 128, 255

block1 = block2 = block3 = False
mode = pg.FULLSCREEN
def0, def1 = windll.user32.GetSystemMetrics(0), windll.user32.GetSystemMetrics(1)
#def0, def1 = 1440, 810

hodi = 0

SIZE = [def0, def1]
o11 = o22 = o33 = o44 = o55 = BLACK
c11 = c22 = c33 = c44 = c55 = GREEN
scroll_c = GRAY
mn = True
mk = 1
s169 = [(1280,720), (1366, 768), (1440, 810), (1600, 900), (1920, 1080)]
if ((def0, def1) not in s169): mode = 0
for sz in s169:
    if (sz[0] <= def0):
        SIZE[0] = sz[0]
        SIZE[1] = sz[1]
k = SIZE[0]/1280
if (SIZE[0] == 1366): k = 1.0625
otverx = 100
cletki = (def1-otverx*k)//9
otbok = (def0-def1)//2
scroll_y = 0
zvuk_y = int(50*k)
og_y = int(130*k)
gm_y = int(200*k)
ge_y = int(270*k)
iz_y = int(373*k)
rez_y = int(453*k)
ar_y = int(523*k)
br_y = int(593*k)
ch_y = int(696*k)
re1_y = int(30*k)
re2_y = int(SIZE[1]*1.5) - int(62*k)
steps = [zvuk_y, og_y, gm_y, ge_y, iz_y, ch_y, re1_y, re2_y, rez_y, ar_y, br_y]
rdx_1 = rdx_2 = rdx_3 = rdx_4 = SIZE[0]-int(700*k)
pdx_1 = pdx_2 = pdx_3 = pdx_4 = 100
step = (SIZE[1]//5*3-int(40*k))//4

pg.init()
pg.font.init()
Impact = pg.font.SysFont("Impact", int(30*k))
Impact_s = pg.font.SysFont("Impact", int(25*k))

gifn = 0

DG = Impact.render("Гапонов Дмитрий   aka   Jay T. Doggzone III", True, BLACK)
vkDG = Impact.render("VK:    https://vk.com/jay_t_doggzone_iii", True, BLACK)
DA = Impact.render("Антипин Данила   aka   danan", True, BLACK)
vkDA = Impact.render("VK:    https://vk.com/danan2", True, BLACK)
to_cb1 = Impact.render("Скопировать", True, B_PURPLE)
to_cb2 = Impact.render("Скопировать", True, PURPLE)
back = Impact.render("Назад в Меню", True, B_PURPLE)
back1 = Impact.render("Назад в Меню", True, PURPLE)
pr1 = Impact.render("Применить", True, B_PURPLE)
pr2 = Impact.render("Применить", True, PURPLE)
zvuk = Impact.render("Звук", True, BLACK)
iz = Impact.render("Изображение", True, BLACK)
ch = Impact.render("Параметры Игры", True, BLACK)


screen = pg.display.set_mode(SIZE,mode,32)
pg.display.set_caption("by JTD_III")
clock = pg.time.Clock()

pg.mixer.music.load(path.join("music","b_music.ogg"))

click_sound = pg.mixer.Sound(path.join("music","click.wav"))

my_face1 = pg.image.load(path.join('image','me500x500.jpg')) 
my_face2 = pg.transform.scale(my_face1,(416,416))
my_face3 = pg.transform.scale(my_face1,(375,375)) 
my_face4 = pg.transform.scale(my_face1,(355,355))
my_face5 = pg.transform.scale(my_face1,(333,333))


danya_face1 = pg.image.load(path.join('image','danya500x500.jpg')) 
danya_face2 = pg.transform.scale(danya_face1,(416,416))
danya_face3 = pg.transform.scale(danya_face1,(375,375))
danya_face4 = pg.transform.scale(danya_face1,(355,355))
danya_face5 = pg.transform.scale(danya_face1,(333,333))


how_i = pg.image.load(path.join('image','KaK_igratt.png'))
how_i1 = pg.transform.scale(how_i,(1920,1080))
how_i2 = pg.transform.scale(how_i,(1600,900))
how_i3 = pg.transform.scale(how_i,(1440,810))
how_i4 = pg.transform.scale(how_i,(1366,768))
how_i5 = pg.transform.scale(how_i,(1280,720))


winb = pg.image.load(path.join('image','Win_bl.png'))
winb1 = pg.transform.scale(winb,(1920,1080))
winb2 = pg.transform.scale(winb,(1600,900))
winb3 = pg.transform.scale(winb,(1440,810))
winb4 = pg.transform.scale(winb,(1366,768))
winb5 = pg.transform.scale(winb,(1280,720))

winw = pg.image.load(path.join('image','Win_w.png'))
winw1 = pg.transform.scale(winw,(1920,1080))
winw2 = pg.transform.scale(winw,(1600,900))
winw3 = pg.transform.scale(winw,(1440,810))
winw4 = pg.transform.scale(winw,(1366,768))
winw5 = pg.transform.scale(winw,(1280,720))


crsr1 = True
crsr2 = crsr3 = crsr4 = False
colvo = 0

pg.mixer.music.play()
'''
class button:
    color = GREEN
    rcolor = BLACK
    
    def __init__(this,text:str = "", x:int = 0, y:int = 0, f) -> None:
        this.text = text
        this.f = f
    t_down = Impact.render(text, True, B_PURPLE)
    t_up = Impact.render(text, True, PURPLE)
    
    def draw(this) -> None:
        pg.draw.rect(screen,this.color,[this.x,this.y,int(200*k),int(40*k)])
        pg.draw.rect(screen,this.rcolor,[this.x,this.y,int(200*k),int(40*k)],int(2*k))
        screen.blit(this.t_down, this.t_down.get_rect(center = (this.x,this.y+int(20*k))))
        screen.blit(this.t_up, this.t_up.get_rect(center = (this.x-int(2*k),this.y+int(18*k))))
    def check(this) -> None:
        mouse_x, mouse_y = pg.mouse.get_pos()
        if (this.x <= mouse_x <= this.x + int(200*k) and this.y <= mouse_y <= this.y + int(40*k)):
            this.rcolor = WHITE
            if (pg.mouse.get_pressed()[0]):
                this.color = BLUE
                f()
            else:
                this.color = GREEN
        else:
            this.rcolor = BLACK
'''
gif = [pg.image.load(path.join('gif','frame_%i_delay-0.04s.gif'%i)) for i in range(48)]
def cb(s:str) -> None:
    system("echo " + s + "| clip")
    return;

def draw_menu169(o1:tuple, o2:tuple, o3:tuple, o4:tuple, o5:tuple, c1:tuple, c2:tuple, c3:tuple, c4:tuple, c5:tuple) -> None:
    pg.draw.rect(screen,c1,[SIZE[0]//2-int(100*k),SIZE[1]//5,int(200*k),int(40*k)])
    pg.draw.rect(screen,o1,[SIZE[0]//2-int(100*k),SIZE[1]//5,int(200*k),int(40*k)],int(2*k))
    start_game1 = Impact.render("Начать Игру", True, B_PURPLE)
    screen.blit(start_game1,(SIZE[0]//2 - int(75*k), SIZE[1]//5))
    start_game2 = Impact.render("Начать Игру", True, PURPLE)
    screen.blit(start_game2,(SIZE[0]//2-int(77*k), SIZE[1]//5-int(2*k)))
    
    pg.draw.rect(screen,c2,[SIZE[0]//2-int(100*k),SIZE[1]//5+step,int(200*k),int(40*k)])
    pg.draw.rect(screen,o2,[SIZE[0]//2-int(100*k),SIZE[1]//5+step,int(200*k),int(40*k)],int(2*k))
    how_play1 = Impact.render("Как Играть", True, B_PURPLE)
    screen.blit(how_play1,(SIZE[0]//2-int(70*k), SIZE[1]//5 + step))
    how_play2 = Impact.render("Как Играть", True, PURPLE)
    screen.blit(how_play2,(SIZE[0]//2-int(72*k), SIZE[1]//5 + step - int(2*k)))
    
    pg.draw.rect(screen,c3,[SIZE[0]//2-int(100*k),SIZE[1]//5+2*step,int(200*k),int(40*k)])
    pg.draw.rect(screen,o3,[SIZE[0]//2-int(100*k),SIZE[1]//5+2*step,int(200*k),int(40*k)],int(2*k))
    authors1 = Impact.render("Авторы", True, B_PURPLE)
    screen.blit(authors1,(SIZE[0]//2-int(50*k), SIZE[1]//5 + 2*step))
    authors1 = Impact.render("Авторы", True, PURPLE)
    screen.blit(authors1,(SIZE[0]//2-int(50*k)-int(2*k), SIZE[1]//5 + 2*step - int(2*k)))
    
    pg.draw.rect(screen,c4,[SIZE[0]//2-int(100*k),SIZE[1]//5+3*step,int(200*k),int(40*k)])
    pg.draw.rect(screen,o4,[SIZE[0]//2-int(100*k),SIZE[1]//5+3*step,int(200*k),int(40*k)],int(2*k))
    preferences1 = Impact.render("Настройки", True, B_PURPLE)
    screen.blit(preferences1,(SIZE[0]//2-int(70*k), SIZE[1]//5 + 3*step))
    preferences2 = Impact.render("Настройки", True, PURPLE)
    screen.blit(preferences2,(SIZE[0]//2-int(70*k) - int(2*k), SIZE[1]//5 + 3*step - int(2*k)))
    
    pg.draw.rect(screen,c5,[SIZE[0]//2-int(100*k),SIZE[1]//5+4*step,int(200*k),int(40*k)])
    pg.draw.rect(screen,o5,[SIZE[0]//2-int(100*k),SIZE[1]//5+4*step,int(200*k),int(40*k)],int(2*k))
    quit_game1 = Impact.render("Выйти", True, B_PURPLE)
    screen.blit(quit_game1,(SIZE[0]//2-int(42*k), SIZE[1]//5 + 4*step))
    quit_game2 = Impact.render("Выйти", True, PURPLE)
    screen.blit(quit_game2,(SIZE[0]//2-int(42*k) - int(2*k), SIZE[1]//5 + 4*step - int(2*k)))
    
        

def menu() -> None:
    
    global o11, o22, o33, o44, o55, c11, c22, c33, c44, c55, gifn
    o11 = o22 = o33 = o44 = o55 = BLACK
    c11 = c22 = c33 = c44 = c55 = GREEN
    pr = False
    h = False
    a = False
    g = False    
    while (mn):
        pr = False
        h = False
        a = False
        g = False
        gifn = (gifn+1)%48
        for event in pg.event.get():
            if (event.type == pg.QUIT):
                pg.quit()
                return;
            x,y = pg.mouse.get_pos()
            if (SIZE[0]//2 - int(100*k) <= x <= SIZE[0]//2 + int(100*k) and SIZE[1]//5 <= y <= SIZE[1]//5 + int(40*k)):
                o11 = WHITE
                if (pg.mouse.get_pressed()[0]):
                    c11 = BLUE
                    g = True
                    click_sound.play()
                else:
                    c11 = GREEN
            elif (SIZE[0]//2 - int(100*k) <= x <= SIZE[0]//2 + int(100*k) and SIZE[1]//5+step <= y <= SIZE[1]//5+step + int(40*k)):
                o22 = WHITE
                if (pg.mouse.get_pressed()[0]):
                    c22 = BLUE
                    h = True
                    click_sound.play()
                else:
                    c22 = GREEN                
            elif (SIZE[0]//2 - int(100*k) <= x <= SIZE[0]//2 + int(100*k) and SIZE[1]//5+2*step <= y <= SIZE[1]//5+2*step + int(40*k)):
                o33 = WHITE
                if (pg.mouse.get_pressed()[0]):
                    c33 = BLUE
                    a = True
                    click_sound.play()
                else:
                    c33 = GREEN               
                
            elif (SIZE[0]//2 - int(100*k) <= x <= SIZE[0]//2 + int(100*k) and SIZE[1]//5+3*step <= y <= SIZE[1]//5+3*step + int(40*k)):
                o44 = WHITE
                if (pg.mouse.get_pressed()[0]):
                    c44 = BLUE
                    pr = True
                    click_sound.play()
                else:
                    c44 = GREEN               
            elif (SIZE[0]//2 - int(100*k) <= x <= SIZE[0]//2 + int(100*k) and SIZE[1]//5 + 4*step<= y <= SIZE[1]//5+4*step + int(40*k)):
                o55 = WHITE
                if (pg.mouse.get_pressed()[0]):
                    c55 = BLUE
                    click_sound.play()
                else:
                    c55 = GREEN                
            else:
                o11 = o22 = o33 = o44 = o55 = BLACK
        screen.fill(GRAY)
        
              
        clock.tick(26)
        screen.blit(pg.transform.scale(gif[gifn],(int(SIZE[1]/1080*1080),int(SIZE[1]/1080*1080))),((SIZE[0] - SIZE[1])//2,0))
        draw_menu169(o11,o22,o33,o44,o55,c11,c22,c33,c44,c55)
        pg.display.update()  
        '''pg.draw.line(screen,WHITE,(640,0),(640,720))
        pg.draw.line(screen,WHITE,(0,360),(1280,360))
        pg.draw.line(screen,GREEN,(0,144),(1280,144))'''
        pg.display.update()
        
        if (c55 == BLUE):
            pg.quit()
            return;
        if (g):
            sleep(0.125)
            game()
            c11 = GREEN
        if (h):
            sleep(0.125)
            how()
            c22 = GREEN
        if (a): 
            sleep(0.125)
            author()
            c33 = GREEN
        if (pr): 
            sleep(0.125)
            pref()
            c44 = GREEN        
    return;


def pref() -> None:
    global SIZE, s169, k, rdx_1, rdx_2, rdx_3, rdx_4, pdx_1, pdx_2, pdx_3, pdx_4, block1, block2, block3, mk, zvuk_y, og_y, gm_y, ge_y, iz_y, rez_y, ar_y, br_y, ch_y, re1_y, re2_y, steps, r1, r2, r3,r4 , scroll_y, mode, screen, scroll_c, crsr1 ,crsr2, crsr3, crsr4, colvo
    c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = c10 = c11 = GREEN
    o1 = o2 = o3 = o4 = o5 = o6 = o7 = o8 = o9 = o10 = o11 = BLACK
    cu1 = cu2 = cu3 = cu4 = BLACK
    ko1 = ko2 = ko3 = ko4 = BLACK
    col_block = False
    scroll_c = GRAY
    oo1 = oo2 = oo3 = oo4 = oo5 = oo6 = oo7 = BLACK
    l1 = l2 = l3 = l4 = l5 = BLACK
    ri1 = ri2 = ri3 = ri4 = ri5 = False
    rmf = rm0 = False
    cu_block = False
    pcrsr1,pcrsr2,pcrsr3,prcr4 = crsr1 ,crsr2, crsr3, crsr4
    pcolvo = colvo
    if (mode): rmf = True
    if (not mode): rm0 = True
    if (SIZE[0] == 1280): ri1 = True
    if (SIZE[0] == 1366): ri2 = True
    if (SIZE[0] == 1440): ri3 = True
    if (SIZE[0] == 1600): ri4 = True
    if (SIZE[0] == 1920): ri5 = True
    scroll_y = 0
    zvuk_y = int(50*k)
    og_y = int(130*k)
    gm_y = int(200*k)
    ge_y = int(270*k)
    iz_y = int(373*k)
    rez_y = int(453*k)
    ar_y = int(523*k)
    br_y = int(593*k)
    ch_y = int(696*k)
    re1_y = int(30*k)
    re2_y = int(SIZE[1]*1.5) - int(62*k)
    steps = [zvuk_y, og_y, gm_y, ge_y, iz_y, ch_y, re1_y, re2_y, rez_y, ar_y, br_y]
    r1, r2, r3, r4 = rdx_1, rdx_2, rdx_3, rdx_4
    br1, br2, br3, br4, br5 = ri1, ri2, ri3, ri4, ri5
    block1 = block2 = block3 = False
    rblock1 = rblock2 = rblock3 = rblock4 = rblock5 = False
    mx,my = pg.mouse.get_pos()
    notin = True    
    while (True):
        for event in pg.event.get():
            if (event.type == pg.QUIT):
                pg.quit()
                global mn
                mn = False
                return;
            x,y = pg.mouse.get_pos()
            if (notin or scroll_c == GRAY): mx, my = pg.mouse.get_pos()
            if (SIZE[0]//2+int(500*k)-int(100*k) <= x <= SIZE[0]//2+int(500*k)+int(100*k) and re2_y <= y <= re2_y + int(40*k)):
                o1 = WHITE
                if (pg.mouse.get_pressed()[0]):
                    c1 = BLUE
                    click_sound.play()
                else:
                    c1 = GREEN
            else:
                o1 = BLACK
            if (SIZE[0]//2-int(100*k) <= x <= SIZE[0]//2+int(100*k) and SIZE[1] - int(50*k) <= y <= SIZE[1] - int(50*k) + int(40*k)):
                o2 = WHITE
                if (pg.mouse.get_pressed()[0]):
                    c2 = BLUE
                    
                    mode = pg.FULLSCREEN
                    if ((def0, def1) not in s169): mode = 0
                    if (mode):
                        rmf = True
                        rm0 = False
                    else:
                        rmf = False
                        rm0 = True
                    for sz in s169:
                        if (sz[0] <= def0):
                            SIZE[0] = sz[0]
                            SIZE[1] = sz[1]
                    changerez(SIZE)
                    screen = pg.display.set_mode(SIZE,mode,32)
                    ri1 = ri2 = ri3 = ri4 = ri5 = False
                    if (SIZE[0] == 1280): ri1 = True
                    if (SIZE[0] == 1366): ri2 = True
                    if (SIZE[0] == 1440): ri3 = True
                    if (SIZE[0] == 1600): ri4 = True
                    if (SIZE[0] == 1920): ri5 = True                    
                    rdx_1 = rdx_2 = rdx_3 = rdx_4 = SIZE[0]-int(700*k)
                    pdx_1 = pdx_2 = pdx_3 = pdx_4 = 100*(rdx_1/(SIZE[0] - int(700*k)))
                    r1, r2, r3, r4 = rdx_1, rdx_2, rdx_3, rdx_4
                    block1 = block2 = block3 = rblock1 = rblock2 = False
                    mk = 1
                    changebr(1)
                    c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = c10 = c11 = GREEN
                    o1 = o2 = o3 = o4 = o5 = o6 = o7 = o8 = o9 = o10 = o11 = BLACK
                    oo1 = oo2 = oo3 = oo4 = oo5 = BLACK
                    l1 = l2 = l3 = l4 = BLACK
                    pg.mouse.set_cursor(*pg.cursors.arrow)
                    crsr1 = True
                    crsr2 = crsr3 = crsr4 = False
                    colvo = 0
                    pg.mixer.music.set_volume(1)
                    click_sound.set_volume(1)
                    click_sound.play()
                else:
                    c2 = GREEN
            else:
                o2 = BLACK
                
            if (SIZE[0]-int(240*k) <= x <= SIZE[0]-int(40*k) and og_y <= y <= og_y + int(40*k)):
                o3 = WHITE
                if (pg.mouse.get_pressed()[0]):
                    c3 = BLUE
                    block1 = True
                    mk = pdx_1/100
                    pg.mixer.music.set_volume(mk*pdx_2/100)
                    click_sound.set_volume(mk*pdx_3/100)
                    click_sound.play()
                else:
                    c3 = GREEN
            else:
                o3 = BLACK
            
            if (SIZE[0]-int(240*k) <= x <= SIZE[0]-int(40*k) and og_y + int(70*k) <= y <= og_y + int(110*k)):
                o4 = WHITE
                if (pg.mouse.get_pressed()[0]):
                    c4 = BLUE
                    block2 = True
                    pg.mixer.music.set_volume(pdx_2/100*mk)
                    click_sound.play()
                else:
                    c4 = GREEN
            else:
                o4 = BLACK
            
            if (SIZE[0]-int(240*k) <= x <= SIZE[0]-int(40*k) and og_y + int(140*k) <= y <= og_y + int(180*k)):
                o5 = WHITE
                if (pg.mouse.get_pressed()[0]):
                    c5 = BLUE
                    block3 = True
                    click_sound.set_volume(pdx_3/100*mk)
                    click_sound.play()
                else:
                    c5 = GREEN
            else:
                o5 = BLACK
            if (SIZE[0]-int(240*k) <= x <= SIZE[0]-int(40*k) and iz_y+int(80*k) <= y <= iz_y+int(120*k)):
                o6 = WHITE
                if (pg.mouse.get_pressed()[0]):
                    c6 = BLUE
                    rblock1 = True
                    click_sound.play()
                    
                else:
                    c6 = GREEN
            else:
                o6 = BLACK
            if (SIZE[0]-int(240*k) <= x <= SIZE[0]-int(40*k) and iz_y+int(220*k) <= y <= iz_y+int(260*k)):
                o7 = WHITE
                if (pg.mouse.get_pressed()[0]):
                    c7 = BLUE
                    rblock2 = True
                    click_sound.play()
                    
                else:
                    c7 = GREEN
            else:
                o7 = BLACK
            if (SIZE[0]-int(240*k) <= x <= SIZE[0]-int(40*k) and iz_y+int(150*k) <= y <= iz_y+int(190*k)):
                o8 = WHITE
                if (pg.mouse.get_pressed()[0]):
                    c8 = BLUE
                    click_sound.play()
                    
                else:
                    c8 = GREEN
            else:
                o8 = BLACK 
                if (def0 >= 1280 and int(400*k) < x < int(516*k) and iz_y+int(80*k) <= y <= iz_y + int(120*k)):
                    oo1 = WHITE
                    l1 = WHITE
                    if (pg.mouse.get_pressed()[0]):
                        ri1 = True
                        ri2 = ri3 = ri4 = ri5 = False
                        click_sound.play()
                else:
                    oo1 = BLACK
                    l1 = BLACK
                if (def0 >= 1366 and int(516*k) < x < int(632*k) and iz_y+int(80*k) <= y <= iz_y + int(120*k)):
                    oo2 = WHITE
                    l1 = l2 = WHITE
                    if (pg.mouse.get_pressed()[0]):
                        ri2 = True
                        ri1 = ri3 = ri4 = ri5 = False
                        click_sound.play()
                else:
                    oo2 = BLACK
                    l2 = BLACK
                    l1 = oo1
                if (def0 >= 1440 and int(632*k) < x < int(748*k) and iz_y+int(80*k) <= y <= iz_y + int(120*k)):
                    oo3 = WHITE
                    l2 = l3 = WHITE
                    if (pg.mouse.get_pressed()[0]):
                        ri3 = True
                        ri2 = ri1 = ri4 = ri5 = False
                        click_sound.play()
                else:
                    oo3 = BLACK
                    l3 = BLACK
                    l2 = oo2
                
                if (def0 >= 1600 and int(748*k) < x < int(864*k) and iz_y+int(80*k) <= y <= iz_y + int(120*k)):
                    oo4 = WHITE
                    l3 = l4 = WHITE
                    if (pg.mouse.get_pressed()[0]):
                        ri4 = True
                        ri2 = ri3 = ri1 = ri5 = False
                        click_sound.play()
                else:
                    oo4 = BLACK
                    l4 = BLACK
                    l3 = oo3
                if (def0 >= 1920 and int(864*k) < x < int(960*k) and iz_y+int(80*k) <= y <= iz_y + int(120*k)):
                    oo5 = WHITE
                    l4 = WHITE
                    if (pg.mouse.get_pressed()[0]):
                        ri5 = True
                        ri2 = ri3 = ri4 = ri1 = False
                        click_sound.play()
                else:
                    oo5 = BLACK
                    l4 = oo4
                if (int(400*k) < x < int(690*k) and iz_y+int(150*k) <= y <= iz_y + int(190*k)):
                    oo6 = WHITE
                    l5 = WHITE
                    if (pg.mouse.get_pressed()[0]):
                        rm0 = True
                        rmf = False
                        click_sound.play()
                else:
                    oo6 = BLACK
                    l5 = BLACK
                
                if (int(690*k) < x < int(980*k) and iz_y+int(150*k) <= y <= iz_y + int(190*k)):
                    oo7 = WHITE
                    l5 = WHITE
                    if (pg.mouse.get_pressed()[0]):
                        rm0 = False
                        rmf = True
                        click_sound.play()
                else:
                    oo7 = BLACK
                    l5 = oo6
                
                if (int(400*k) < x < int(544*k) and ch_y+int(80*k) <= y <= ch_y+int(120*k)):
                    cu1 = WHITE
                    if (pg.mouse.get_pressed()[0]):
                        crsr1 = True
                        crsr2 = crsr3 = crsr4 = False
                        click_sound.play()
                else:
                    cu1 = BLACK
                if (int(545*k) < x < int(689*k) and ch_y+int(80*k) <= y <= ch_y+int(120*k)):
                    cu2 = WHITE
                    if (pg.mouse.get_pressed()[0]):
                        crsr2 = True
                        crsr1 = crsr3 = crsr4 = False
                        click_sound.play()
                else:
                    cu2 = BLACK
                if (int(690*k) < x < int(834*k) and ch_y+int(80*k) <= y <= ch_y+int(120*k)):
                    cu3 = WHITE
                    if (pg.mouse.get_pressed()[0]):
                        crsr3 = True
                        crsr1 = crsr2 = crsr4 = False
                        click_sound.play()
                else:
                    cu3 = BLACK
                if (int(835*k) < x < int(979*k) and ch_y+int(80*k) <= y <= ch_y+int(120*k)):
                    cu4 = WHITE
                    if (pg.mouse.get_pressed()[0]):
                        crsr4 = True
                        crsr1 = crsr3 = crsr2 = False
                        click_sound.play()
                else:
                    cu4 = BLACK
                if (SIZE[0] - int(240*k) <= x <= SIZE[0] - int(40*k) and ch_y+int(80*k) <= y <= ch_y+int(120*k)):
                    o9 = WHITE
                    if (pg.mouse.get_pressed()[0]):
                        c9 = BLUE
                        cu_block = True
                        if (crsr1): pg.mouse.set_cursor(*pg.cursors.arrow)
                        if (crsr2): pg.mouse.set_cursor(*pg.cursors.diamond)
                        if (crsr3): pg.mouse.set_cursor(*pg.cursors.broken_x)
                        if (crsr4): pg.mouse.set_cursor(*pg.cursors.tri_left)
                        click_sound.play()
                        
                else:
                    o9 = BLACK
                
                if (int(400*k) < x < int(544*k) and ch_y+int(150*k) <= y <= ch_y+int(190*k)):
                    ko1 = WHITE
                    if (pg.mouse.get_pressed()[0]):
                        colvo = 0
                        click_sound.play()
                else:
                    ko1 = BLACK
                if (int(545*k) < x < int(689*k) and ch_y+int(150*k) <= y <= ch_y+int(190*k)):
                    ko2 = WHITE
                    if (pg.mouse.get_pressed()[0]):
                        colvo = 4
                        click_sound.play()                    
                else:
                    ko2 = BLACK
                if (int(690*k) < x < int(834*k) and ch_y+int(150*k) <= y <= ch_y+int(190*k)):
                    ko3 = WHITE
                    if (pg.mouse.get_pressed()[0]):
                        colvo = 8
                        click_sound.play()                    
                else:
                    ko3 = BLACK
                if (int(835*k) < x < int(979*k) and ch_y+int(150*k) <= y <= ch_y+int(190*k)):
                    ko4 = WHITE
                    if (pg.mouse.get_pressed()[0]):
                        colvo = 16
                        click_sound.play()                    
                else:
                    ko4 = BLACK
            
                if (SIZE[0] - int(240*k) <= x <= SIZE[0] - int(40*k) and ch_y+int(150*k) <= y <= ch_y+int(190*k)):
                    o10 = WHITE
                    if (pg.mouse.get_pressed()[0]):
                        c10 = BLUE
                        col_block = True
                        click_sound.play()
                else:
                    o10 = BLACK
            if (int(400*k) <= x <= SIZE[0]-int(300*k) and og_y+int(10*k) <= y <= og_y + int(30*k)):
                if (pg.mouse.get_pressed()[0]):
                    rdx_1 = x - int(400*k)
                    pdx_1 = 100*(rdx_1/(SIZE[0] - int(700*k)))
            
            if (int(400*k) <= x <= SIZE[0]-int(300*k) and og_y+int(80*k) <= y <= og_y + int(110*k)):
                if (pg.mouse.get_pressed()[0]):
                    rdx_2 = x - int(400*k)
                    pdx_2 = 100*(rdx_2/(SIZE[0] - int(700*k)))
            if (int(400*k) <= x <= SIZE[0]-int(300*k) and og_y+int(150*k) <= y <= og_y + int(180*k)):
                if (pg.mouse.get_pressed()[0]):
                    rdx_3 = x - int(400*k)
                    pdx_3 = 100*(rdx_3/(SIZE[0] - int(700*k)))

            if (int(400*k) <= x <= SIZE[0]-int(300*k) and br_y+int(10*k) <= y <= br_y + int(30*k)):
                if (pg.mouse.get_pressed()[0]):
                    rdx_4 = x - int(400*k)
                    pdx_4 = 100*(rdx_4/(SIZE[0] - int(700*k)))
                
            if (event.type == pg.MOUSEBUTTONDOWN or event.type == pg.MOUSEBUTTONUP):
                if (event.button == 5):
                    if (scroll_y <= SIZE[1]//2 - int(15*k)):
                        scroll_y += int(15*k)
                        for i in range(len(steps)): 
                            steps[i] -= int(15*k)
                        pg.event.post(pg.event.Event(pg.KEYDOWN))
                    if (SIZE[1]//2 - scroll_y < int(15*k)):
                        for i in range(len(steps)): 
                            steps[i] -= SIZE[1]//2 - scroll_y                        
                        scroll_y = SIZE[1]//2  
                    
                if (event.button == 4):
                    if (scroll_y >= int(15*k)):
                        scroll_y -= int(15*k)
                        for i in range(len(steps)):
                            steps[i] += int(15*k)
                        pg.event.post(pg.event.Event(pg.KEYDOWN))
                    if (scroll_y < int(15*k)): 
                        for i in range(len(steps)):
                            steps[i] += scroll_y                           
                        scroll_y = 0
               
               
            if (SIZE[0] - int(20*k) <= mx <= SIZE[0] and scroll_y <= my <= scroll_y + SIZE[1]//2):
                scroll_c = S_GRAY
                if (pg.mouse.get_pressed()[0]):
                    scroll_c = SS_GRAY
                    mx1, my1 = pg.mouse.get_pos()
                    notin = False
                    dy = my1 - my
                    if (scroll_y <= SIZE[1]//2 - dy and dy >= 0 or dy <= scroll_y and dy < 0):
                        scroll_y += dy
                        for i in range(len(steps)):
                            steps[i] -= dy                  
                    my = my1
                    mx = mx1
                else: 
                    scroll_c = S_GRAY
                    notin = True                    
            else:
                scroll_c = GRAY
        zvuk_y = steps[0]
        og_y = steps[1]
        gm_y = steps[2]
        ge_y = steps[3]
        iz_y = steps[4]
        ch_y = steps[5]
        re1_y = steps[6]
        re2_y = steps[7]
        rez_y = steps[8]
        ar_y = steps[9]
        br_y = steps[10]
        clock.tick(144)
        screen.fill(S_BLACK)
        pg.draw.rect(screen, scroll_c, (SIZE[0] - int(20*k), scroll_y, SIZE[0], SIZE[1]//2))
        pg.draw.rect(screen,BLACK,(int(30*k),re1_y+int(323*k), SIZE[0] - int(60*k), int(313*k)), int(5*k))
        pg.draw.rect(screen,BLACK,(int(30*k),re1_y+int(646*k), SIZE[0] - int(60*k), int(313*k)), int(5*k))
        pg.draw.rect(screen,BLACK,(int(30*k),re1_y, SIZE[0] - int(60*k), int(313*k)), int(5*k))        
        
        pg.draw.rect(screen,c1,[SIZE[0]//2+int(500*k)-int(100*k),re2_y,int(200*k),int(40*k)])
        pg.draw.rect(screen,o1,[SIZE[0]//2+int(500*k)-int(100*k),re2_y,int(200*k),int(40*k)],int(2*k))
        
        pg.draw.rect(screen,c2,[SIZE[0]//2-int(100*k),re2_y,int(200*k),int(40*k)])
        pg.draw.rect(screen,o2,[SIZE[0]//2-int(100*k),re2_y,int(200*k),int(40*k)],int(2*k))        
        
        back1 = Impact.render("Назад в Меню", True, B_PURPLE)
        screen.blit(back1,(SIZE[0]//2+int(410*k), re2_y))
        back2 = Impact.render("Назад в Меню", True, PURPLE)
        screen.blit(back2,(SIZE[0]//2+int(410*k) - int(2*k), re2_y - int(2*k)))
        
        de1 = Impact.render("Сброс", True, B_PURPLE)
        screen.blit(de1,(SIZE[0]//2 - int(37*k), re2_y))
        de2 = Impact.render("Сброс", True, PURPLE)
        screen.blit(de2,(SIZE[0]//2 - int(37*k) - int(2*k), re2_y - int(2*k)))
        
        
        
        screen.blit(zvuk,(SIZE[0]//2-int(30*k), zvuk_y))
        
        og = Impact.render("Общая Громкость", True, BLACK)
        screen.blit(og,(int(70*k), og_y))
        pg.draw.rect(screen,L_BLUE,(int(400*k),og_y+int(10*k), rdx_1, int(20*k)))
        pg.draw.rect(screen,BLACK,(int(400*k),og_y+int(10*k), SIZE[0]-int(700*k), int(20*k)),int(2*k))
        pd1 = Impact_s.render("%i%%"%(ceil(pdx_1) if (pdx_1 > 50) else int(pdx_1)), True, BLACK)
        screen.blit(pd1,(SIZE[0]//2, og_y+int(5*k)))
        
        pg.draw.rect(screen,c3,[SIZE[0]-int(240*k),og_y,int(200*k),int(40*k)])
        pg.draw.rect(screen,o3,[SIZE[0]-int(240*k),og_y,int(200*k),int(40*k)],int(2*k))        

        screen.blit(pr1,(SIZE[0]-int(210*k), og_y))
        screen.blit(pr2,(SIZE[0]-int(210*k) - int(2*k), og_y - int(2*k)))
                
        
        pg.draw.rect(screen,c4,[SIZE[0]-int(240*k),og_y+int(70*k),int(200*k),int(40*k)])
        pg.draw.rect(screen,o4,[SIZE[0]-int(240*k),og_y+int(70*k),int(200*k),int(40*k)],int(2*k))        
        gm = Impact.render("Громкость Музыки", True, BLACK)
        screen.blit(gm,(int(70*k), gm_y))
        pg.draw.rect(screen,L_BLUE,(int(400*k),og_y+int(80*k), rdx_2, int(20*k)))
        pg.draw.rect(screen,BLACK,(int(400*k),og_y+int(80*k), SIZE[0]-int(700*k), int(20*k)),int(2*k))
        screen.blit(pr1,(SIZE[0]-int(210*k), og_y+int(70*k)))
        screen.blit(pr2,(SIZE[0]-int(210*k) - int(2*k), og_y +int(70*k) - int(2*k)))      
        pd2 = Impact_s.render("%i%%"%(ceil(pdx_2) if (pdx_2 > 50) else int(pdx_2)), True, BLACK)
        screen.blit(pd2,(SIZE[0]//2, og_y+int(75*k)))        
        
        pg.draw.rect(screen,c5,[SIZE[0]-int(240*k),og_y+int(140*k),int(200*k),int(40*k)])
        pg.draw.rect(screen,o5,[SIZE[0]-int(240*k),og_y+int(140*k),int(200*k),int(40*k)],int(2*k))        
        ge = Impact.render("Громкость Эффектов", True, BLACK)
        screen.blit(ge,(int(70*k), ge_y))
        pg.draw.rect(screen,L_BLUE,(int(400*k),og_y+int(150*k), rdx_3, int(20*k)))
        pg.draw.rect(screen,BLACK,(int(400*k),og_y+int(150*k), SIZE[0]-int(700*k), int(20*k)),int(2*k))
        screen.blit(pr1,(SIZE[0]-int(210*k), og_y+int(140*k)))
        screen.blit(pr2,(SIZE[0]-int(210*k) - int(2*k), og_y +int(140*k) - int(2*k)))        
        pd3 = Impact_s.render("%i%%"%(ceil(pdx_3) if (pdx_3 > 50) else int(pdx_3)), True, BLACK)
        screen.blit(pd3,(SIZE[0]//2, og_y+int(145*k)))  
        
        
        
        screen.blit(iz,(SIZE[0]//2-int(87*k), iz_y))
        
        
        
        pg.draw.rect(screen,c6,[SIZE[0]-int(240*k),iz_y+int(80*k),int(200*k),int(40*k)])
        pg.draw.rect(screen,o6,[SIZE[0]-int(240*k),iz_y+int(80*k),int(200*k),int(40*k)],int(2*k))        

        screen.blit(pr1,(SIZE[0]-int(210*k), iz_y+int(80*k)))
        screen.blit(pr2,(SIZE[0]-int(210*k) - int(2*k), iz_y+int(80*k) - int(2*k)))
        
        
        
        if (ri1): pg.draw.rect(screen,GREEN,(int(400*k),iz_y+int(80*k),int(116*k),int(40*k)))
        if (ri2): pg.draw.rect(screen,GREEN,(int(516*k),iz_y+int(80*k),int(116*k),int(40*k)))
        if (ri3): pg.draw.rect(screen,GREEN,(int(632*k),iz_y+int(80*k),int(116*k),int(40*k)))
        if (ri4): pg.draw.rect(screen,GREEN,(int(748*k),iz_y+int(80*k),int(116*k),int(40*k)))
        if (ri5): pg.draw.rect(screen,GREEN,(int(864*k),iz_y+int(80*k),int(116*k),int(40*k)))
        if (rm0): pg.draw.rect(screen,GREEN,(int(400*k),iz_y+int(150*k),int(290*k),int(40*k)))
        if (rmf): pg.draw.rect(screen,GREEN,(int(690*k),iz_y+int(150*k),int(290*k),int(40*k)))
        
        if (def0 < 1366): pg.draw.rect(screen,RED,(int(516*k),iz_y+int(80*k),int(116*k),int(40*k)))
        if (def0 < 1440): pg.draw.rect(screen,RED,(int(632*k),iz_y+int(80*k),int(116*k),int(40*k)))
        if (def0 < 1600): pg.draw.rect(screen,RED,(int(748*k),iz_y+int(80*k),int(116*k),int(40*k)))
        if (def0 < 1920): pg.draw.rect(screen,RED,(int(864*k),iz_y+int(80*k),int(116*k),int(40*k)))
        
       
        #pg.draw.rect(screen,BLACK,(int(400*k),iz_y+int(80*k), SIZE[0]-int(700*k), int(40*k)),int(2*k))
        pg.draw.rect(screen,oo1,(int(400*k),iz_y+int(80*k),int(116*k),int(40*k)),int(2*k))
        _640x360 = Impact_s.render("1280x720", True, BLACK)
        screen.blit(_640x360,(int(411*k),iz_y+int(84*k)))           
        pg.draw.rect(screen,oo2,(int(516*k),iz_y+int(80*k),int(116*k),int(40*k)),int(2*k))
        _960x540 = Impact_s.render("1366x768", True, BLACK)
        screen.blit(_960x540,(int(527*k),iz_y+int(84*k)))        
        pg.draw.rect(screen,oo3,(int(632*k),iz_y+int(80*k),int(116*k),int(40*k)),int(2*k))
        _1280x720 = Impact_s.render("1440x810", True, BLACK)
        screen.blit(_1280x720,(int(642*k),iz_y+int(84*k)))                
        pg.draw.rect(screen,oo4,(int(748*k),iz_y+int(80*k),int(116*k),int(40*k)),int(2*k))
        _1600x900 = Impact_s.render("1600x900", True, BLACK)
        screen.blit(_1600x900,(int(755*k),iz_y+int(84*k)))                
        pg.draw.rect(screen,oo5,(int(864*k),iz_y+int(80*k),int(116*k),int(40*k)),int(2*k))
        _1920x1080 = Impact_s.render("1920x1080", True, BLACK)
        screen.blit(_1920x1080,(int(868*k),iz_y+int(84*k)))
        
        pg.draw.line(screen,l1,(int(516*k),iz_y+int(80*k)),(int(516*k),iz_y+int(120*k)),int(2*k))
        pg.draw.line(screen,l2,(int(632*k),iz_y+int(80*k)),(int(632*k),iz_y+int(120*k)),int(2*k))
        pg.draw.line(screen,l3,(int(748*k),iz_y+int(80*k)),(int(748*k),iz_y+int(120*k)),int(2*k))
        pg.draw.line(screen,l4,(int(864*k),iz_y+int(80*k)),(int(864*k),iz_y+int(120*k)),int(2*k))
        
        
        
        rez = Impact.render("Разрешение Экрана", True, BLACK)
        screen.blit(rez,(int(70*k), rez_y))
        
        ar = Impact.render("Режим Отображения", True, BLACK)
        screen.blit(ar,(int(70*k), ar_y))
        
        
        pg.draw.rect(screen,c8,[SIZE[0]-int(240*k),iz_y+int(150*k),int(200*k),int(40*k)])
        pg.draw.rect(screen,o8,[SIZE[0]-int(240*k),iz_y+int(150*k),int(200*k),int(40*k)],int(2*k))        
        
        screen.blit(pr1,(SIZE[0]-int(210*k), iz_y+int(150*k)))
        
        screen.blit(pr2,(SIZE[0]-int(210*k) - int(2*k), iz_y+int(150*k) - int(2*k)))
        
        
        #pg.draw.rect(screen,BLACK,(int(400*k),iz_y+int(150*k), SIZE[0]-int(700*k), int(40*k)),int(2*k))
        pg.draw.rect(screen,oo6,(int(400*k),iz_y+int(150*k),int(290*k),int(40*k)),int(2*k))
        window = Impact_s.render("В Окне", True, BLACK)
        screen.blit(window,(int(515*k),iz_y+int(154*k)))
        naves = Impact_s.render("На Весь Экран", True, BLACK)
        screen.blit(naves,(int(760*k),iz_y+int(154*k)))
        pg.draw.rect(screen,oo7,(int(690*k),iz_y+int(150*k),int(290*k),int(40*k)),int(2*k))
        pg.draw.line(screen,l5,(int(690*k),iz_y+int(150*k)),(int(690*k),iz_y+int(190*k)),int(2*k))
        
        
        
        
        
        br = Impact.render("Яркость", True, BLACK)
        screen.blit(br,(int(70*k), br_y))
        
        
        pg.draw.rect(screen,WHITE,(int(400*k),br_y+int(10*k), rdx_4, int(20*k)))
        pg.draw.rect(screen,BLACK,(int(400*k),br_y+int(10*k), SIZE[0]-int(700*k), int(20*k)),int(2*k))        
        pg.draw.rect(screen,c7,[SIZE[0]-int(240*k),iz_y+int(220*k),int(200*k),int(40*k)])
        pg.draw.rect(screen,o7,[SIZE[0]-int(240*k),iz_y+int(220*k),int(200*k),int(40*k)],int(2*k))
        
        pd4 = Impact_s.render("%i%%"%(ceil(pdx_4) if (pdx_4 > 50) else int(pdx_4)), True, BLACK)
        screen.blit(pd4,(SIZE[0]//2, iz_y+int(225*k)))
        
        screen.blit(pr1,(SIZE[0]-int(210*k), iz_y+int(220*k)))

        screen.blit(pr2,(SIZE[0]-int(210*k) - int(2*k), iz_y+int(220*k) - int(2*k)))
        
        if (crsr1): pg.draw.rect(screen,GREEN,(int(400*k),ch_y+int(80*k),int(144*k),int(40*k)))
        if (crsr2): pg.draw.rect(screen,GREEN,(int(545*k),ch_y+int(80*k),int(144*k),int(40*k)))
        if (crsr3): pg.draw.rect(screen,GREEN,(int(690*k),ch_y+int(80*k),int(144*k),int(40*k)))
        if (crsr4): pg.draw.rect(screen,GREEN,(int(835*k),ch_y+int(80*k),int(144*k),int(40*k)))        
        
        cur = Impact.render("Курсор", True, BLACK)
        screen.blit(cur,(int(70*k),int(80*k)+ch_y))
        pg.draw.rect(screen,cu1,(int(400*k),int(80*k)+ch_y,int(144*k),int(40*k)),int(2*k))
        screen.blit(Impact_s.render("Стрелка", True, BLACK),(int(425*k),int(84*k)+ch_y))
        pg.draw.rect(screen,cu2,(int(545*k),int(80*k)+ch_y,int(144*k),int(40*k)),int(2*k))
        screen.blit(Impact_s.render("Кристалл", True, BLACK),(int(565*k),int(84*k)+ch_y))
        pg.draw.rect(screen,cu3,(int(690*k),int(80*k)+ch_y,int(144*k),int(40*k)),int(2*k))
        screen.blit(Impact_s.render("Прицел", True, BLACK),(int(722*k),int(84*k)+ch_y))
        pg.draw.rect(screen,cu4,(int(835*k),int(80*k)+ch_y,int(144*k),int(40*k)),int(2*k))
        screen.blit(Impact_s.render("Угол", True, BLACK),(int(880*k),int(84*k)+ch_y))
        
        pg.draw.rect(screen,c9,[SIZE[0]-int(240*k),ch_y+int(80*k),int(200*k),int(40*k)])
        pg.draw.rect(screen,o9,[SIZE[0]-int(240*k),ch_y+int(80*k),int(200*k),int(40*k)],int(2*k))        
        screen.blit(pr1,(SIZE[0]-int(210*k), ch_y+int(80*k)))
        screen.blit(pr2,(SIZE[0]-int(210*k) - int(2*k), ch_y+int(80*k) - int(2*k)))        
        
        if (colvo == 0): pg.draw.rect(screen,GREEN,(int(400*k),ch_y+int(150*k),int(144*k),int(40*k)))
        if (colvo == 4): pg.draw.rect(screen,GREEN,(int(545*k),ch_y+int(150*k),int(144*k),int(40*k)))
        if (colvo == 8): pg.draw.rect(screen,GREEN,(int(690*k),ch_y+int(150*k),int(144*k),int(40*k)))
        if (colvo == 16): pg.draw.rect(screen,GREEN,(int(835*k),ch_y+int(150*k),int(144*k),int(40*k)))         
        
        kol = Impact.render("Кол-во шашек вначале", True, BLACK)
        screen.blit(kol,(int(70*k),int(150*k)+ch_y))
        pg.draw.rect(screen,ko1,(int(400*k),int(150*k)+ch_y,int(144*k),int(40*k)),int(2*k))
        screen.blit(Impact_s.render("0", True, BLACK),(int(465*k),int(154*k)+ch_y))
        pg.draw.rect(screen,ko2,(int(545*k),int(150*k)+ch_y,int(144*k),int(40*k)),int(2*k))
        screen.blit(Impact_s.render("4", True, BLACK),(int(610*k),int(154*k)+ch_y))
        pg.draw.rect(screen,ko3,(int(690*k),int(150*k)+ch_y,int(144*k),int(40*k)),int(2*k))
        screen.blit(Impact_s.render("8", True, BLACK),(int(755*k),int(154*k)+ch_y))
        pg.draw.rect(screen,ko4,(int(835*k),int(150*k)+ch_y,int(144*k),int(40*k)),int(2*k))
        screen.blit(Impact_s.render("16", True, BLACK),(int(895*k),int(154*k)+ch_y))
        
        
               
        
        
        pg.draw.rect(screen,c10,[SIZE[0]-int(240*k),ch_y+int(150*k),int(200*k),int(40*k)])
        pg.draw.rect(screen,o10,[SIZE[0]-int(240*k),ch_y+int(150*k),int(200*k),int(40*k)],int(2*k))        
        screen.blit(pr1,(SIZE[0]-int(210*k), ch_y+int(150*k)))
        screen.blit(pr2,(SIZE[0]-int(210*k) - int(2*k), ch_y+int(150*k) - int(2*k)))         
        
        screen.blit(ch,(SIZE[0]//2-int(105*k), ch_y))

        clock.tick(144)
        pg.display.update()
        if (c1 == BLUE):
            sleep(0.125)
            break;
        if (c6 == BLUE): 
            sleep(0.125)
            if (ri1): changerez([1280,720])
            if (ri2): changerez([1366,768])
            if (ri3): changerez([1440,810])
            if (ri4): changerez([1600,900])
            if (ri5): changerez([1920,1080])            
            c6 = GREEN
        if (c7 == BLUE):
            sleep(0.125)
            changebr(pdx_4/100)
            c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = c10 = c11 = GREEN
            o1 = o2 = o3 = o4 = o5 = o6 = o7 = o8 = o9 = o10 = o11 = BLACK
            oo1 = oo2 = oo3 = oo4 = oo5 = oo6 = oo7 = BLACK
            l1 = l2 = l3 = l4 = l5 = BLACK
            cu1 = cu2 = cu3 = cu4 = BLACK
            c7 = GREEN
            scroll_c = GRAY
        if (c8 == BLUE):
            sleep(0.125)
            if (rm0):
                mode = 0
                screen = pg.display.set_mode(SIZE,mode,32)
            if (rmf):
                mode = pg.FULLSCREEN
                screen = pg.display.set_mode(SIZE,mode,32)
            c8 = GREEN
        if (c9 == BLUE):
            sleep(0.125)
            c9 = GREEN
        if (c10 == BLUE):
            sleep(0.125)
            c10 = GREEN
    if (not block1):
        rdx_1 = r1
        pdx_1 = 100*(rdx_1/(SIZE[0] - int(700*k)))
    if (not block2):
        rdx_2 = r2
        pdx_2 = 100*(rdx_2/(SIZE[0] - int(700*k)))
    if (not block3):
        rdx_3 = r3
        pdx_3 = 100*(rdx_3/(SIZE[0] - int(700*k)))
    if (not rblock1):
        ri1, ri2, ri3, ri4, ri5 = br1, br2, br3, br4, br5
    if (not rblock2):
        rdx_4 = r4
        pdx_4 = 100*(rdx_4/(SIZE[0] - int(700*k)))
    if (not cu_block):
        crsr1 ,crsr2, crsr3, crsr4 = pcrsr1,pcrsr2,pcrsr3,prcr4
    if (not col_block):
        colvo = pcolvo
    return;

def how() -> None:
    c1 = GREEN
    o1 = BLACK
    
    while (True):
        screen.fill(BLACK)
        for event in pg.event.get():
            if (event.type == pg.QUIT):
                pg.quit()
                global mn
                mn = False
                return;
            x,y = pg.mouse.get_pos()
            if (SIZE[0]//2+int(500*k)-int(100*k) <= x <= SIZE[0]//2+int(500*k)+int(100*k) and SIZE[1] - int(100*k) <= y <= SIZE[1] - int(100*k) + int(40*k)):
                o1 = WHITE
                if (pg.mouse.get_pressed()[0]):
                    c1 = BLUE
                    click_sound.play()
                else:
                    c1 = GREEN
            else:
                o1 = BLACK
        if (SIZE[0] == 1920):
            screen.blit(how_i1,(0,0))
        if (SIZE[0] == 1600):
            screen.blit(how_i2,(0,0))
        if (SIZE[0] == 1440):
            screen.blit(how_i3,(0,0))
        if (SIZE[0] == 1366):
            screen.blit(how_i4,(0,0))
        if (SIZE[0] == 1280):
            screen.blit(how_i5,(0,0))
        pg.draw.rect(screen,c1,[SIZE[0]//2+int(500*k)-int(100*k),SIZE[1] - int(100*k),int(200*k),int(40*k)])
        pg.draw.rect(screen,o1,[SIZE[0]//2+int(500*k)-int(100*k),SIZE[1] - int(100*k),int(200*k),int(40*k)],int(2*k))
        screen.blit(back,(SIZE[0]//2+int(500*k) - int(90*k), SIZE[1] - int(100*k)))
        screen.blit(back1,(SIZE[0]//2+int(500*k) - int(90*k)-int(2*k), SIZE[1] - int(100*k)-int(2*k)))
        clock.tick(144)
        pg.display.update()
        if (c1 == BLUE):
            sleep(0.125)
            c1 = GREEN
            return
    return;

def changerez(sz:list) -> None:
    global screen, k, SIZE, Impact, Impact_s, step, rdx_1, rdx_2, rdx_3, rdx_4, pdx_1, pdx_2, pdx_3, pdx_4, mode, zvuk_y, og_y, gm_y, ge_y, iz_y, rez_y, ar_y, br_y, ch_y, re1_y, re2_y,steps, r1, r2, r3, r4, scroll_y, DG, vkDG, DA, vkDA, to_cb1, to_cb2, back, back1, pr1, pr2, zvuk, iz, ch
    k = sz[0]/1280
    if (sz[0] == 1366): k = 1.0625
    SIZE[0], SIZE[1] = sz[0], sz[1]
    screen = pg.display.set_mode(SIZE,mode,32)
    Impact = pg.font.SysFont("Impact", int(30*k))
    Impact_s = pg.font.SysFont("Impact", int(25*k))
    step = (SIZE[1]//5*3-int(40*k))//4
    rdx_1 = int(pdx_1/100*(SIZE[0] - int(700*k)))
    rdx_2 = int(pdx_2/100*(SIZE[0] - int(700*k)))
    rdx_3 = int(pdx_3/100*(SIZE[0] - int(700*k)))
    rdx_4 = int(pdx_4/100*(SIZE[0] - int(700*k)))
    zvuk_y = int(50*k)
    og_y = int(130*k)
    gm_y = int(200*k)
    ge_y = int(270*k)
    iz_y = int(373*k)
    rez_y = int(453*k)
    ar_y = int(523*k)
    br_y = int(593*k)
    ch_y = int(696*k)
    re1_y = int(30*k)
    re2_y = int(SIZE[1]*1.5) - int(62*k)
    steps = [zvuk_y, og_y, gm_y, ge_y, iz_y, ch_y, re1_y, re2_y, rez_y, ar_y, br_y]
    r1, r2, r3, r4 = rdx_1, rdx_2, rdx_3, rdx_4
    scroll_y = 0
    DG = Impact.render("Гапонов Дмитрий   aka   Jay T. Doggzone III", True, BLACK)
    vkDG = Impact.render("VK:    https://vk.com/jay_t_doggzone_iii", True, BLACK)
    DA = Impact.render("Антипин Данила   aka   danan", True, BLACK)
    vkDA = Impact.render("VK:    https://vk.com/danan2", True, BLACK)
    to_cb1 = Impact.render("Скопировать", True, B_PURPLE)
    to_cb2 = Impact.render("Скопировать", True, PURPLE)
    back = Impact.render("Назад в Меню", True, B_PURPLE)
    back1 = Impact.render("Назад в Меню", True, PURPLE)
    pr1 = Impact.render("Применить", True, B_PURPLE)
    pr2 = Impact.render("Применить", True, PURPLE)
    zvuk = Impact.render("Звук", True, BLACK)
    iz = Impact.render("Изображение", True, BLACK)
    ch = Impact.render("Параметры Игры", True, BLACK)
    return;

def changebr(brk:float) -> None:
    global WHITE, RED, GREEN, BLUE, PURPLE, YELLOW, GRAY, ORANGE, S_BLACK, B_PURPLE, L_BLUE, S_GRAY, SS_GRAY, o11, o22, o33, o44, o55, c11, c22, c33, c44, c55, DG, vkDG, DA, vkDA, to_cb1, to_cb2, back, back1, pr1, pr2, zvuk, iz, ch, scroll_c
    WHITE = int(255*brk), int(255*brk), int(255*brk)
    RED = int(255*brk), 0, 0
    GREEN = 0, int(255*brk), 0
    BLUE = 0, 0, int(255*brk)
    PURPLE = int(255*brk), 0, int(255*brk)
    YELLOW = int(255*brk), int(255*brk), 0
    GRAY = int(128*brk), int(128*brk), int(128*brk)
    ORANGE = int(255*brk), 128*brk, 0
    S_BLACK = int(40*brk), int(40*brk), int(40*brk)
    B_PURPLE = int(128*brk), 0, int(128*brk)
    L_BLUE = 0, int(128*brk), int(255*brk)
    S_GRAY = int(90*brk), int(90*brk), int(90*brk)
    SS_GRAY = int(64*brk), int(64*brk), int(64*brk)    
    o11 = o22 = o33 = o44 = o55 = BLACK
    c11 = c22 = c33 = c44 = c55 = GREEN
    scroll_c = GRAY
    DG = Impact.render("Гапонов Дмитрий   aka   Jay T. Doggzone III", True, BLACK)
    vkDG = Impact.render("VK:    https://vk.com/jay_t_doggzone_iii", True, BLACK)
    DA = Impact.render("Антипин Данила   aka   danan", True, BLACK)
    vkDA = Impact.render("VK:    https://vk.com/danan2", True, BLACK)
    to_cb1 = Impact.render("Скопировать", True, B_PURPLE)
    to_cb2 = Impact.render("Скопировать", True, PURPLE)
    back = Impact.render("Назад в Меню", True, B_PURPLE)
    back1 = Impact.render("Назад в Меню", True, PURPLE)
    pr1 = Impact.render("Применить", True, B_PURPLE)
    pr2 = Impact.render("Применить", True, PURPLE)
    zvuk = Impact.render("Звук", True, BLACK)
    iz = Impact.render("Изображение", True, BLACK)
    ch = Impact.render("Параметры Игры", True, BLACK)
    return;

def author() -> None:
    c1 = c2 = c3 = c4 = c5 = GREEN
    o1 = o2 = o3 = o4 = o5 = BLACK
    
    while (True):
        for event in pg.event.get():
            if (event.type == pg.QUIT):
                pg.quit()
                global mn
                mn = False
                return;
            x,y = pg.mouse.get_pos()
            if (SIZE[0]//2+int(500*k)-int(100*k) <= x <= SIZE[0]//2+int(500*k)+int(100*k) and SIZE[1] - int(100*k) <= y <= SIZE[1] - int(100*k) + int(40*k)):
                o1 = WHITE
                if (pg.mouse.get_pressed()[0]):
                    c1 = BLUE
                    click_sound.play()
                else:
                    c1 = GREEN
            else:
                o1 = BLACK
            if (int(50*k) + int(600*k) <= x <= int(50*k) + int(600*k)+int(200*k) and int(50*k) <= y <= int(50*k) + int(40*k)):
                o2 = WHITE
                if (pg.mouse.get_pressed()[0]):
                    c2 = BLUE
                    click_sound.play()
                else:
                    c2 = GREEN
            else:
                o2 = BLACK
            if (int(50*k) + int(600*k) <= x <= int(50*k) + int(600*k)+int(200*k) and int(100*k) <= y <= int(100*k) + int(40*k)):
                o3 = WHITE
                if (pg.mouse.get_pressed()[0]):
                    c3 = BLUE
                    click_sound.play()
                else:
                    c3 = GREEN
            else:
                o3 = BLACK
            if (int(50*k) + int(600*k) <= x <= int(50*k) + int(600*k)+int(200*k) and SIZE[1]//2+int(50*k) <= y <= SIZE[1]//2+int(50*k) + int(40*k)):
                o4 = WHITE
                if (pg.mouse.get_pressed()[0]):
                    c4 = BLUE
                    click_sound.play()
                else:
                    c4 = GREEN
            else:
                o4 = BLACK
            if (int(50*k) + int(600*k) <= x <= int(50*k) + int(600*k)+int(200*k) and SIZE[1]//2+int(100*k) <= y <= SIZE[1]//2+int(100*k) + int(40*k)):
                o5 = WHITE
                if (pg.mouse.get_pressed()[0]):
                    c5 = BLUE
                    click_sound.play()
                else:
                    c5 = GREEN
            else:
                o5 = BLACK
        
        pg.draw.rect(screen, RED, (0,0,SIZE[0],SIZE[1]//2))
        pg.draw.rect(screen, BLACK, (0,0,SIZE[0],SIZE[1]//2),int(4*k))
        pg.draw.rect(screen, ORANGE, (0,SIZE[1]//2,SIZE[0],SIZE[1]//2))
        pg.draw.rect(screen, BLACK, (0,SIZE[1]//2,SIZE[0],SIZE[1]//2),int(4*k))
        
       
        
        
        
        
        
        pg.draw.rect(screen,c2,[int(50*k) + int(600*k),int(50*k),int(200*k),int(40*k)])
        pg.draw.rect(screen,o2,[int(50*k) + int(600*k),int(50*k),int(200*k),int(40*k)],int(2*k))
        screen.blit(to_cb1,(int(50*k) + int(600*k) + int(15*k), int(50*k)))
        screen.blit(to_cb2,(int(50*k) + int(600*k) + int(15*k) - int(2*k), int(50*k) - int(2*k)))
        pg.draw.rect(screen,c3,[int(50*k) + int(600*k),int(100*k),int(200*k),int(40*k)])
        pg.draw.rect(screen,o3,[int(50*k) + int(600*k),int(100*k),int(200*k),int(40*k)],int(2*k))    
        screen.blit(to_cb1,(int(50*k) + int(600*k) + int(15*k), int(100*k)))
        screen.blit(to_cb2,(int(50*k) + int(600*k) + int(15*k) - int(2*k), int(100*k) - int(2*k)))
        
        pg.draw.rect(screen,c4,[int(50*k) + int(600*k),SIZE[1]//2 + int(50*k),int(200*k),int(40*k)])
        pg.draw.rect(screen,o4,[int(50*k) + int(600*k),SIZE[1]//2 + int(50*k),int(200*k),int(40*k)],int(2*k))    
        screen.blit(to_cb1,(int(50*k) + int(600*k) + int(15*k), SIZE[1]//2 + int(50*k)))
        screen.blit(to_cb2,(int(50*k) + int(600*k) + int(15*k) - int(2*k), SIZE[1]//2 + int(50*k) - int(2*k)))
        pg.draw.rect(screen,c5,[int(50*k) + int(600*k),SIZE[1]//2 + int(100*k),int(200*k),int(40*k)])
        pg.draw.rect(screen,o5,[int(50*k) + int(600*k),SIZE[1]//2 + int(100*k),int(200*k),int(40*k)],int(2*k))    
        screen.blit(to_cb1,(int(50*k) + int(600*k) + int(15*k), SIZE[1]//2 + int(100*k)))
        screen.blit(to_cb2,(int(50*k) + int(600*k) + int(15*k) - int(2*k), SIZE[1]//2 + int(100*k) - int(2*k)))

        
        
        screen.blit(DG,(int(50*k),int(50*k)))
        screen.blit(vkDG,(int(50*k),int(100*k)))
        
        if (SIZE[0] == 1920):
            screen.blit(my_face1,(int(900*k),int(15*k)))
            pg.draw.rect(screen,BLACK,(int(900*k),int(15*k),500,500),int(10*k))
        elif (SIZE[0] == 1600):
            screen.blit(my_face2,(int(900*k),int(15*k)))
            pg.draw.rect(screen,BLACK,(int(900*k),int(15*k),416,416),int(10*k))
        elif (SIZE[0] == 1440):
            screen.blit(my_face3,(int(900*k),int(15*k)))
            pg.draw.rect(screen,BLACK,(int(900*k),int(15*k),375,375),int(10*k))
        elif (SIZE[0] == 1366):
            screen.blit(my_face4,(int(900*k),int(15*k)))
            pg.draw.rect(screen,BLACK,(int(900*k),int(15*k),355,355),int(10*k))
        else:
            screen.blit(my_face5,(int(900*k),int(15*k)))
            pg.draw.rect(screen,BLACK,(int(900*k),int(15*k),333,333),int(10*k))            
        
        
        screen.blit(DA,(int(50*k),SIZE[1]//2 + int(50*k)))
        screen.blit(vkDA,(int(50*k),SIZE[1]//2 + int(100*k)))
        
        if (SIZE[0] == 1920):
            screen.blit(danya_face1,(int(900*k),SIZE[1]//2 +int(15*k)))
            pg.draw.rect(screen,BLACK,(int(900*k),SIZE[1]//2 +int(15*k),500,500),int(10*k))
        elif (SIZE[0] == 1600):
            screen.blit(danya_face2,(int(900*k),SIZE[1]//2 +int(15*k)))
            pg.draw.rect(screen,BLACK,(int(900*k),SIZE[1]//2 +int(15*k),416,416),int(10*k))
        elif (SIZE[0] == 1440):
            screen.blit(danya_face3,(int(900*k),SIZE[1]//2 +int(15*k)))
            pg.draw.rect(screen,BLACK,(int(900*k),SIZE[1]//2 +int(15*k),375,375),int(10*k))
        elif (SIZE[0] == 1366):
            screen.blit(danya_face4,(int(900*k),SIZE[1]//2 +int(15*k)))
            pg.draw.rect(screen,BLACK,(int(900*k),SIZE[1]//2 +int(15*k),355,355),int(10*k))
        else:
            screen.blit(danya_face5,(int(900*k),SIZE[1]//2 +int(15*k)))
            pg.draw.rect(screen,BLACK,(int(900*k),SIZE[1]//2 +int(15*k),333,333),int(10*k))   
        
        pg.draw.rect(screen,c1,[SIZE[0]//2+int(500*k)-int(100*k),SIZE[1] - int(100*k),int(200*k),int(40*k)])
        pg.draw.rect(screen,o1,[SIZE[0]//2+int(500*k)-int(100*k),SIZE[1] - int(100*k),int(200*k),int(40*k)],int(2*k))
        
        screen.blit(back,(SIZE[0]//2+int(500*k) - int(90*k), SIZE[1] - int(100*k)))
        
        screen.blit(back1,(SIZE[0]//2+int(500*k) - int(90*k)-int(2*k), SIZE[1] - int(100*k)-int(2*k)))
        
        clock.tick(144)
        pg.display.update()
        if (c1 == BLUE):
            sleep(0.125)
            break;
        if (c2 == BLUE):
            sleep(0.125)
            cb("Гапонов Дмитрий   aka   Jay T. Doggzone III")
            c2 = GREEN
        if (c3 == BLUE):
            sleep(0.125)
            cb("https://vk.com/jay_t_doggzone_iii")
            c3 = GREEN
        if (c4 == BLUE):
            sleep(0.125)
            cb("Антипин Данила   aka   danan")
            c4 = GREEN
        if (c5 == BLUE):
            sleep(0.125)
            cb("https://vk.com/danan2")
            c5 = GREEN
    return;


class fig:
    x = 0
    y = 0
    color = WHITE
    ocolor = BLACK
    def __init__(this, color:tuple = WHITE, x:int = 0, y:int = 0) -> None:
        this.x = x
        this.y = y
        this.color = color
        this.ocolor = BLACK if (this.color == WHITE) else WHITE
        
    def draw(this) -> None:
        pg.draw.circle(screen, this.color, (this.x, this.y), (SIZE[1]-int(300*k))//16)
        pg.draw.circle(screen, this.ocolor, (this.x, this.y), (SIZE[1]-int(250*k))//16, int(4*k))
        pg.draw.circle(screen, this.ocolor, (this.x, this.y), (SIZE[1]-int(250*k))//32, int(4*k))

def game() -> None:
    global colvo, hodi
    hodi = 0
    plusb = plusw = False
    colvo_b = 32
    colvo_ch = 32  
    sx, sy = -1, -1
    kw = 0
    kb = 0
    c1 = GREEN
    o1 = BLACK
    save = [[0]*10 for i in range(10)]
    shashki = [[None]*8 for i in range(8)]
    derz = False
    may = False
    white_s = fig(WHITE, int(100*k),int(250*k))
    
    black_s = fig(BLACK, SIZE[0]-int(100*k),int(250*k))    
    for i in range(colvo):
        koef = randint(0,1)
        yy,xx = 2*randint(0,3) + koef, 2*randint(0,3)+ koef
        while (save[yy][xx]):
            koef = randint(0,1)
            yy,xx = 2*randint(0,3)+ koef, 2*randint(0,3)+ koef
        shashki[yy][xx] = fig(WHITE, (int(10*k)+(SIZE[0]-SIZE[1])//2+(SIZE[1] - int(150*k))//8+(SIZE[1] - int(150*k))//16+(SIZE[1] - int(150*k))//8*xx), (SIZE[1] - int(150*k))//8+ (SIZE[1] - int(150*k))//16+(SIZE[1] - int(150*k))//8*yy)
        save[yy][xx] = True
    for i in range(colvo):
        yy,xx = 2*randint(0,3)+1, 2*randint(0,3)
        while (save[yy][xx]):
            yy,xx = 2*randint(0,3)+1, 2*randint(0,3)
            if (randint(0,32000)&1):
                yy,xx = xx,yy            
        shashki[yy][xx] = fig(BLACK, (int(10*k)+(SIZE[0]-SIZE[1])//2+(SIZE[1] - int(150*k))//8+(SIZE[1] - int(150*k))//16+(SIZE[1] - int(150*k))//8*xx), (SIZE[1] - int(150*k))//8+ (SIZE[1] - int(150*k))//16+(SIZE[1] - int(150*k))//8*yy)        
        save[yy][xx] = True
    while (True):
        screen.fill(S_GRAY)
        
        
        for event in pg.event.get():
            if (event.type == pg.QUIT):
                pg.quit()
                return;
        x,y = pg.mouse.get_pos()
        if (SIZE[0]//2+int(400*k) <= x <= SIZE[0]//2+int(600*k) and SIZE[1] - int(100*k) <= y <= SIZE[1] + int(100*k)):
            o1 = WHITE
            if (pg.mouse.get_pressed()[0]):
                c1 = BLUE
                click_sound.play()
        else:
            o1 = BLACK
        
        x,y = pg.mouse.get_pos()   
        if (not derz):
            for yy in range(8):
                for xx in range(8):
                    if (hodi&1):
                        if (yy&1 and xx&1 or not xx&1 and not yy&1): continue;
                    else:
                        if (not (yy&1 and xx&1 or not xx&1 and not yy&1)): continue;
                    if (save[yy][xx]):
                        if (10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*xx < x < 10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//4+(SIZE[1] - 150*k)//8*xx and (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*yy < y < (SIZE[1] - 150*k)//4+(SIZE[1] - 150*k)//8*yy):
                            shashki[yy][xx].color = GREEN
                            if (event.type == pg.MOUSEBUTTONDOWN and event.button == 1):
                                derz = True
                                sy,sx = yy,xx
                                pg.mouse.get_rel()
                                click_sound.play()
                                sleep(0.125)
                                break;
                                
                        else:
                            shashki[yy][xx].color = WHITE if (yy&1 and xx&1 or not yy&1 and not xx&1) else BLACK            
        
            
                
        for y in range(8):
            for i in range(8):
                if (y&1 and i&1 or not y&1 and not i&1):
                    pg.draw.rect(screen, GRAY, (10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*y,(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*i, (SIZE[1] - 150*k)//8,(SIZE[1] - 150*k)//8))
                    pg.draw.rect(screen, BLACK, (10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*y,(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*i, (SIZE[1] - 150*k)//8,(SIZE[1] - 150*k)//8),int(2*k))
                else:
                    pg.draw.rect(screen, SS_GRAY, (10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*y,(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*i, (SIZE[1] - 150*k)//8,(SIZE[1] - 150*k)//8))
                    pg.draw.rect(screen, BLACK, (10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*y,(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*i, (SIZE[1] - 150*k)//8,(SIZE[1] - 150*k)//8),int(2*k))
                   

        for y in range(8):
            for i in range(8):
                if (shashki[y][i]):
                    shashki[y][i].draw()
        if (derz):
            if (not may):
                mx,my = (sx, sy)
                may = True
            
            shashki[sy][sx].x, shashki[sy][sx].y = pg.mouse.get_pos()
            verh = vniz = vprav = vlev = True
            if (save[my][mx-2] and (mx - 2 >= 0) or not (10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*0 <= 10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(mx-2) <= 10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(7) and (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*0 <= (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*my <= (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*7)): vlev = False

            if (save[my][mx+2] or not (10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*0 <= 10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(mx+2) <= 10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(7) and (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*0 <= (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*my <= (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*7 )): vprav = False
            if (save[my-2][mx] and (my - 2 >= 0) or not (10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*0 <= 10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(mx) <= 10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(7) and (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*0 <= (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(my-2) <= (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*7 )): verh = False
            if (save[my+2][mx] or not (10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*0 <= 10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(mx) <= 10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(7) and (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*0 <= (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(my+2) <= (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*7)): vniz = False
            pg.draw.rect(screen, PURPLE, (10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(mx),(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*my, (SIZE[1] - 150*k)//8,(SIZE[1] - 150*k)//8))
            pg.draw.rect(screen, BLACK, (10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(mx),(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*my, (SIZE[1] - 150*k)//8,(SIZE[1] - 150*k)//8),int(2*k))            
            if (vprav):
                pg.draw.rect(screen, PURPLE, (10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(mx+2),(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*my, (SIZE[1] - 150*k)//8,(SIZE[1] - 150*k)//8))
                pg.draw.rect(screen, BLACK, (10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(mx+2),(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*my, (SIZE[1] - 150*k)//8,(SIZE[1] - 150*k)//8),int(2*k))
            if (vlev):
                pg.draw.rect(screen, PURPLE, (10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(mx-2),(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*my, (SIZE[1] - 150*k)//8,(SIZE[1] - 150*k)//8))
                pg.draw.rect(screen, BLACK, (10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(mx-2),(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*my, (SIZE[1] - 150*k)//8,(SIZE[1] - 150*k)//8),int(2*k))
            if (vniz):
                pg.draw.rect(screen, PURPLE, (10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*mx,(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(my+2), (SIZE[1] - 150*k)//8,(SIZE[1] - 150*k)//8))
                pg.draw.rect(screen, BLACK, (10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*mx,(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(my+2), (SIZE[1] - 150*k)//8,(SIZE[1] - 150*k)//8),int(2*k))
            if (verh):
                pg.draw.rect(screen, PURPLE, (10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*mx,(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(my-2), (SIZE[1] - 150*k)//8,(SIZE[1] - 150*k)//8))
                pg.draw.rect(screen, BLACK, (10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*mx,(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(my-2), (SIZE[1] - 150*k)//8,(SIZE[1] - 150*k)//8),int(2*k))
            if (verh and 10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*mx <= pg.mouse.get_pos()[0] <= 10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(mx+1) and (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(my-2) <= pg.mouse.get_pos()[1] <= (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(my-1)):
                pg.draw.rect(screen, WHITE, (10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*mx,(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(my-2), (SIZE[1] - 150*k)//8,(SIZE[1] - 150*k)//8),int(2*k))
            if (vlev and 10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(mx-2) <= pg.mouse.get_pos()[0] <= 10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(mx-1) and (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(my) <= pg.mouse.get_pos()[1] <= (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(my+1)):
                pg.draw.rect(screen, WHITE, (10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(mx-2),(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(my), (SIZE[1] - 150*k)//8,(SIZE[1] - 150*k)//8),int(2*k))
            if (vprav and 10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(mx+2) <= pg.mouse.get_pos()[0] <= 10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(mx+3) and (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(my) <= pg.mouse.get_pos()[1] <= (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(my+1)):
                pg.draw.rect(screen, WHITE, (10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(mx+2),(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(my), (SIZE[1] - 150*k)//8,(SIZE[1] - 150*k)//8),int(2*k))
            if (vniz and 10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*mx <= pg.mouse.get_pos()[0] <= 10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(mx+1) and (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(my+2) <= pg.mouse.get_pos()[1] <= (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(my+3)):
                pg.draw.rect(screen, WHITE, (10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*mx,(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(my+2), (SIZE[1] - 150*k)//8,(SIZE[1] - 150*k)//8),int(2*k))
            if (10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*mx <= pg.mouse.get_pos()[0] <= 10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(mx+1) and (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(my) <= pg.mouse.get_pos()[1] <= (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(my+1)):
                pg.draw.rect(screen, WHITE, (10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*mx,(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(my), (SIZE[1] - 150*k)//8,(SIZE[1] - 150*k)//8),int(2*k))
            shashki[sy][sx].draw()
            if (pg.mouse.get_pressed()[0]):
                    if (vniz and 10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*mx <= pg.mouse.get_pos()[0] <= 10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(mx+1) and (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(my+2) <= pg.mouse.get_pos()[1] <= (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(my+3)):
                        click_sound.play()
                        derz = False
                        may = False
                        pg.event.post(pg.event.Event(pg.KEYDOWN))
                        if (save[my+1][mx]):
                            save[my+1][mx] = 0
                            shashki[my+1][mx] = None
                            if (my&1 and mx&1 or not my&1 and not mx&1):
                                colvo_ch -=1
                            else:
                                colvo_b -= 1                            
                        save[my][mx] = 0
                        save[my+2][mx] = 1
                        shashki[my+2][mx] = shashki[my][mx]
                        shashki[my][mx] = None
                        shashki[my+2][mx].x, shashki[my+2][mx].y = int(10*k)+(SIZE[0]-SIZE[1])//2+(SIZE[1] - int(150*k))//8+(SIZE[1] - int(150*k))//8*mx + (SIZE[1] - int(150*k))//16, (SIZE[1] - int(150*k))//8+(SIZE[1] - int(150*k))//8*(my+2) + (SIZE[1] - int(150*k))//16
                        hodi += 1
                        shashki[my+2][mx].color = WHITE if (my&1 and mx&1 or not my&1 and not mx&1) else BLACK
                    if (verh and 10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*mx <= pg.mouse.get_pos()[0] <= 10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(mx+1) and (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(my-2) <= pg.mouse.get_pos()[1] <= (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(my-1)):
                        click_sound.play()
                        derz = False
                        may = False
                        pg.event.post(pg.event.Event(pg.KEYDOWN))
                        if (save[my-1][mx]):
                            save[my-1][mx] = 0
                            shashki[my-1][mx] = None
                            if (my&1 and mx&1 or not my&1 and not mx&1):
                                colvo_ch -=1
                            else:
                                colvo_b -= 1                            
                        save[my][mx] = 0
                        save[my-2][mx] = 1
                        shashki[my-2][mx] = shashki[my][mx]
                        shashki[my][mx] = None
                        shashki[my-2][mx].x, shashki[my-2][mx].y = int(10*k)+(SIZE[0]-SIZE[1])//2+(SIZE[1] - int(150*k))//8+(SIZE[1] - int(150*k))//8*mx + (SIZE[1] - int(150*k))//16, (SIZE[1] - int(150*k))//8+(SIZE[1] - int(150*k))//8*(my-2) + (SIZE[1] - int(150*k))//16
                        hodi += 1
                        shashki[my-2][mx].color = WHITE if (my&1 and mx&1 or not my&1 and not mx&1) else BLACK
                    if (vprav and 10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(mx+2) <= pg.mouse.get_pos()[0] <= 10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(mx+3) and (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(my) <= pg.mouse.get_pos()[1] <= (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(my+1)):
                        click_sound.play()
                        derz = False
                        may = False
                        pg.event.post(pg.event.Event(pg.KEYDOWN))
                        if (save[my][mx+1]):
                            save[my][mx+1] = 0
                            shashki[my][mx+1] = None
                            if (my&1 and mx&1 or not my&1 and not mx&1):
                                colvo_ch -=1
                            else:
                                colvo_b -= 1                            
                        save[my][mx] = 0
                        save[my][mx+2] = 1
                        shashki[my][mx+2] = shashki[my][mx]
                        shashki[my][mx] = None
                        shashki[my][mx+2].x, shashki[my][mx+2].y = int(10*k)+(SIZE[0]-SIZE[1])//2+(SIZE[1] - int(150*k))//8+(SIZE[1] - int(150*k))//8*(mx+2) + (SIZE[1] - int(150*k))//16, (SIZE[1] - int(150*k))//8+(SIZE[1] - int(150*k))//8*(my) + (SIZE[1] - int(150*k))//16
                        hodi += 1
                        shashki[my][mx+2].color = WHITE if (my&1 and mx&1 or not my&1 and not mx&1) else BLACK
                    if (vlev and 10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(mx-2) <= pg.mouse.get_pos()[0] <= 10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(mx-1) and (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(my) <= pg.mouse.get_pos()[1] <= (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(my+1)):
                        click_sound.play()
                        derz = False
                        may = False
                        pg.event.post(pg.event.Event(pg.KEYDOWN))
                        if (save[my][mx-1]):
                            save[my][mx-1] = 0
                            shashki[my][mx-1] = None
                            if (my&1 and mx&1 or not my&1 and not mx&1):
                                colvo_ch -=1
                            else:
                                colvo_b -= 1
                        save[my][mx] = 0
                        save[my][mx-2] = 1
                        shashki[my][mx-2] = shashki[my][mx]
                        shashki[my][mx] = None
                        shashki[my][mx-2].x, shashki[my][mx-2].y = int(10*k)+(SIZE[0]-SIZE[1])//2+(SIZE[1] - int(150*k))//8+(SIZE[1] - int(150*k))//8*(mx-2) + (SIZE[1] - int(150*k))//16, (SIZE[1] - int(150*k))//8+(SIZE[1] - int(150*k))//8*(my) + (SIZE[1] - int(150*k))//16
                        hodi += 1
                        shashki[my][mx-2].color = WHITE if (my&1 and mx&1 or not my&1 and not mx&1) else BLACK
                    if (pg.mouse.get_rel() != (0,0) and 10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(mx) <= pg.mouse.get_pos()[0] <= 10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(mx+1) and (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(my) <= pg.mouse.get_pos()[1] <= (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(my+1)):
                        click_sound.play()
                        derz = False
                        may = False
                        pg.event.post(pg.event.Event(pg.KEYDOWN))
                        save[my][mx] = 1
                        
    
                        shashki[my][mx].x, shashki[my][mx].y = int(10*k)+(SIZE[0]-SIZE[1])//2+(SIZE[1] - int(150*k))//8+(SIZE[1] - int(150*k))//8*(mx) + (SIZE[1] - int(150*k))//16, (SIZE[1] - int(150*k))//8+(SIZE[1] - int(150*k))//8*(my) + (SIZE[1] - int(150*k))//16                
                        hodi += 1
                        shashki[my][mx].color = WHITE if (my&1 and mx&1 or not my&1 and not mx&1) else BLACK

        pg.draw.rect(screen,c1,[SIZE[0]//2+int(500*k)-int(100*k),SIZE[1] - int(100*k),int(200*k),int(40*k)])
        pg.draw.rect(screen,o1,[SIZE[0]//2+int(500*k)-int(100*k),SIZE[1] - int(100*k),int(200*k),int(40*k)],int(2*k))
        
        screen.blit(back,(SIZE[0]//2+int(500*k) - int(90*k), SIZE[1] - int(100*k)))
        screen.blit(back1,(SIZE[0]//2+int(500*k) - int(90*k)-int(2*k), SIZE[1] - int(100*k)-int(2*k)))        
        clock.tick(144)
        
        winds = Impact.render('Ходит Белый' if (not hodi&1) else 'Ходит Чёрный',True, BLACK)
        screen.blit(winds,(SIZE[0]//2-80*k,20*k))
        
        colvo_left = Impact.render('Количество белых: '+str(colvo_b),True,WHITE)
        colvo_right = Impact.render('Количество черных: '+ str(colvo_ch),True,WHITE)
        screen.blit(colvo_left, (40*k,150*k))
        screen.blit(colvo_right, (SIZE[0]-310*k,150*k))
        
        
        
                
        
        m_x, m_y = pg.mouse.get_pos()
        if (SIZE[0]-int(100*k)-(SIZE[1]-int(300*k))//16 < m_x < SIZE[0]-int(100*k)+(SIZE[1]-int(300*k))//16 and int(250*k)-(SIZE[1]-int(300*k))//16 < m_y < int(250*k)+(SIZE[1]-int(300*k))//16 and hodi&1):
            black_s.color = GREEN
            if (pg.mouse.get_pressed()[0]):
                plusb = True
                pg.mouse.get_rel()
                sleep(0.125)                
                       
        else:
            black_s.color = BLACK
            
        if (int(100*k)-(SIZE[1]-int(300*k))//16 < m_x < int(100*k)+(SIZE[1]-int(300*k))//16 and int(250*k)-(SIZE[1]-int(300*k))//16 < m_y < int(250*k)+(SIZE[1]-int(300*k))//16 and not hodi&1):
            white_s.color = GREEN
            if (pg.mouse.get_pressed()[0]):
                plusw = True
                pg.mouse.get_rel()
                sleep(0.125)
            
        else:
            white_s.color = WHITE  
        white_s.draw()
        black_s.draw()
        
        if (plusb):
            for yy in range(8):
                for xx in range(8):
                    if (not save[yy][xx] and not (yy&1 and xx&1 or not yy&1 and not xx&1)):
                        pg.draw.rect(screen, PURPLE, (10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*xx,(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*yy, (SIZE[1] - 150*k)//8,(SIZE[1] - 150*k)//8))
                        pg.draw.rect(screen, BLACK, (10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*xx,(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*yy, (SIZE[1] - 150*k)//8,(SIZE[1] - 150*k)//8),int(2*k))
                        m__x, m__y = pg.mouse.get_pos()
                        if (10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*xx < m__x < 10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(xx+1) and (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*yy < m__y < (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(yy+1)):
                            pg.draw.rect(screen, WHITE, (10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*xx,(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*yy, (SIZE[1] - 150*k)//8,(SIZE[1] - 150*k)//8),int(2*k))
                            if (pg.mouse.get_pressed()[0]):
                                shashki[yy][xx] = fig(BLACK,int(10*k)+(SIZE[0]-SIZE[1])//2+(SIZE[1] - int(150*k))//8 + (SIZE[1] - int(150*k))//16 +(SIZE[1] - int(150*k))//8*xx, (SIZE[1] - int(150*k))//8+(SIZE[1] - int(150*k))//8*yy + (SIZE[1] - int(150*k))//16)
                                save[yy][xx] = 1
                                hodi += 1
                                plusb = False                            
            pg.draw.circle(screen, BLACK, pg.mouse.get_pos(), (SIZE[1]-int(300*k))//16)
            pg.draw.circle(screen, WHITE, pg.mouse.get_pos(), (SIZE[1]-int(250*k))//16, int(4*k))
            pg.draw.circle(screen, WHITE, pg.mouse.get_pos(), (SIZE[1]-int(250*k))//32, int(4*k))
        if (plusw):
            for yy in range(8):
                for xx in range(8):
                    if (not save[yy][xx] and (yy&1 and xx&1 or not yy&1 and not xx&1)):
                        pg.draw.rect(screen, PURPLE, (10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*xx,(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*yy, (SIZE[1] - 150*k)//8,(SIZE[1] - 150*k)//8))
                        pg.draw.rect(screen, BLACK, (10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*xx,(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*yy, (SIZE[1] - 150*k)//8,(SIZE[1] - 150*k)//8),int(2*k))
                        m__x, m__y = pg.mouse.get_pos()
                        if (10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*xx < m__x < 10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(xx+1) and (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*yy < m__y < (SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*(yy+1)):
                            pg.draw.rect(screen, WHITE, (10*k+(SIZE[0]-SIZE[1])//2+(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*xx,(SIZE[1] - 150*k)//8+(SIZE[1] - 150*k)//8*yy, (SIZE[1] - 150*k)//8,(SIZE[1] - 150*k)//8),int(2*k))
                            if (pg.mouse.get_pressed()[0]):
                                shashki[yy][xx] = fig(WHITE,int(10*k)+(SIZE[0]-SIZE[1])//2+(SIZE[1] - int(150*k))//8 + (SIZE[1] - int(150*k))//16 +(SIZE[1] - int(150*k))//8*xx, (SIZE[1] - int(150*k))//8+(SIZE[1] - int(150*k))//8*yy + (SIZE[1] - int(150*k))//16)
                                save[yy][xx] = 1
                                hodi += 1
                                plusw = False
                                
                        

            
            pg.draw.circle(screen, WHITE, pg.mouse.get_pos(), (SIZE[1]-int(300*k))//16)
            pg.draw.circle(screen, BLACK, pg.mouse.get_pos(), (SIZE[1]-int(250*k))//16, int(4*k))
            pg.draw.circle(screen, BLACK, pg.mouse.get_pos(), (SIZE[1]-int(250*k))//32, int(4*k))            
        pg.display.update()
        if (c1 == BLUE):
            sleep(0.125)
            c1 = GREEN
            return;
        if (colvo_b == 0):
            screen.fill(BLACK)
            if (SIZE[0] == 1920):
                screen.blit(winb1,(0,0))
            if (SIZE[0] == 1600):
                screen.blit(winb2,(0,0))
            if (SIZE[0] == 1440):
                screen.blit(winb3,(0,0))
            if (SIZE[0] == 1366):
                screen.blit(winb4,(0,0))
            if (SIZE[0] == 1280):
                screen.blit(winb5,(0,0))
            pg.display.update()
            sleep(3)
            return
        if (colvo_ch == 0):
            screen.fill(BLACK)
            if (SIZE[0] == 1920):
                screen.blit(winw1,(0,0))
            if (SIZE[0] == 1600):
                screen.blit(winw2,(0,0))
            if (SIZE[0] == 1440):
                screen.blit(winw3,(0,0))
            if (SIZE[0] == 1366):
                screen.blit(winw4,(0,0))
            if (SIZE[0] == 1280):
                screen.blit(winw5,(0,0))
            pg.display.update()
            sleep(3)
            return        
    return;
def main() -> int:
    menu()
    
    return 0;

if (__name__ == "__main__"):
    main()