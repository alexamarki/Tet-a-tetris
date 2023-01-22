import pygame
import constants, variables

with open("data/levels/input.txt", "r") as file:
    classicBase = [[x for x in line.split()] for line in file]
    gameHeight = len(classicBase)
    gameWidth = len(classicBase[0])


class tetrominoBlock(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, screen=True):
        super().__init__(variables.all_sprites)
        self.x = x
        self.y = y
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        if screen:
            self.x += variables.boardTopX
            self.y += variables.boardTopY
            self.rotationSit()

    def rotationSit(self):
        if variables.rotor % 4 == 1:
            pass
        elif variables.rotor % 4 == 2:
            self.x, self.y = constants.boardCentreX + constants.boardCentreY - self.y - 1, -constants.boardCentreX + constants.boardCentreY + self.x
        elif variables.rotor % 4 == 3:
            self.x, self.y = constants.boardCentreX * 2 - self.x - 1, constants.boardCentreY * 2 - self.y - 1
        else:
            self.x, self.y = constants.boardCentreX - constants.boardCentreY + self.y, constants.boardCentreX + constants.boardCentreY - self.x - 1

    def update(self, screen):
        screen.blit(self.image, ((self.x) * constants.blockScale, (self.y) * constants.blockScale))


class AnimationExc(pygame.sprite.Sprite):
    def blitIt(self):
        variables.screen.blit(pygame.image.load(f'data/exclamationAnimationFrames/frame{int(variables.framed % 11 // 1) + 1}.png').convert_alpha(),
                              (780, 30))
