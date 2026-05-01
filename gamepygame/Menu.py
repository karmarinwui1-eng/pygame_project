import pygame, sys

class Button:
    def __init__(self, path, x,y,size):
        self.image = pygame.transform.scale(
            pygame.image.load(path).convert_alpha(), size)
        self.rect = self.image.get_rect(center=(x,y))

    def draw(self,screen):
        screen.blit(self.image,self.rect)

    def click(self,event):
        return event.type==pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)

class Menu:
    def __init__(self,screen,W,H):
        self.screen=screen
        self.W=W; self.H=H

        self.bg=pygame.transform.scale(
            pygame.image.load("menu assets/bg.jpg"), (W,H))
        self.gobg=pygame.transform.scale(
            pygame.image.load("menu assets/gameovermenu.png"), (W,H))

        self.start=Button("menu assets/startbtn.png",W//2,260,(250,90))
        self.exit=Button("menu assets/exitbtn.png",W//2,380,(250,90))
        self.again=Button("menu assets/try-againbtn.png",W//2,320,(270,90))

    def main(self):
        while True:
            self.screen.blit(self.bg,(0,0))
            self.start.draw(self.screen)
            self.exit.draw(self.screen)

            for e in pygame.event.get():
                if e.type==pygame.QUIT: pygame.quit(); sys.exit()
                if self.start.click(e): return "start"
                if self.exit.click(e): pygame.quit(); sys.exit()

            pygame.display.update()

    def gameover(self):
        font=pygame.font.SysFont("Arial",60)
        while True:
            self.screen.blit(self.gobg,(0,0))
            txt=font.render("GAME OVER",True,(255,80,80))
            self.screen.blit(txt, txt.get_rect(center=(self.W//2,150)))

            self.again.draw(self.screen)
            self.exit.draw(self.screen)

            for e in pygame.event.get():
                if e.type==pygame.QUIT: pygame.quit(); sys.exit()
                if self.again.click(e): return "restart"
                if self.exit.click(e): pygame.quit(); sys.exit()

            pygame.display.update()