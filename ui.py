import pygame as pg, customLib as cl

class clickThing(pg.sprite.Sprite):
    def __init__(self, image, imageSize):
        super().__init__()

        self.unclickedDonutImage = cl.img.load(image, imageSize)
        self.clickedDonutImage = cl.img.load(image, (imageSize[0] // 1.2, imageSize[1] // 1.2))

        self.donutImage = self.unclickedDonutImage

        self.imageRect = self.donutImage.get_rect()

    def blit(self, dis, x, y, center=True):

        if center:
            self.imageRect.center = (x, y)

        else:
            self.imageRect.topright = (x, y)

        self.lastBlit = x, y

        dis.blit(self.donutImage, self.imageRect)
    
    def updateClicks(self, events):
        if events.type == pg.MOUSEBUTTONDOWN:
            if self.imageRect.collidepoint(events.pos):
                self.donutImage = self.clickedDonutImage
                self.imageRect.size = self.donutImage.get_rect().size

        if events.type == pg.MOUSEBUTTONUP:
            if self.imageRect.collidepoint(events.pos):
                self.donutImage = self.unclickedDonutImage
                self.imageRect.size = self.donutImage.get_rect().size
                return True

class upgradeCard(pg.sprite.Sprite):
    def __init__(self, image, imageSize, disText, descText):
        super().__init__()

        self.font = pg.font.Font("assets/UpgradeFont.ttf", 28)
        self.text = self.font.render(disText, True, (255, 255, 255))
        self.desc = self.font.render(descText, True, (255, 255, 255))

        self.cardImage = cl.img.load(image, imageSize)
        self.imageRect = self.cardImage.get_rect()

    def blit(self, dis, coords, center=True):
        self.imageRect.topleft = (coords[0]+10, coords[1]+10)

        self.totRect = pg.Rect(coords[0], coords[1], coords[0]+400, coords[1]+120)

        pg.draw.rect(dis, (70, 150, 130), self.totRect)

        dis.blit(self.text, (coords[0]+120, coords[1]+10))
        dis.blit(self.desc, (coords[0]+120, coords[1]+35))
        dis.blit(self.cardImage, self.imageRect)
    
    def updateClicks(self, events):
        if events.type == pg.MOUSEBUTTONDOWN:
            pass

        if events.type == pg.MOUSEBUTTONUP:
            if self.totRect.collidepoint(events.pos):
                return True

