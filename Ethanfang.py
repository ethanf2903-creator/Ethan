import pygame, math, sys

W, H = 900, 600
CENTER = (W//2, H//2)
G = 0.5
DT = 0.1

BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255,230,0)
BLUE = (80,160,255)

pygame.init()
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("行星")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,24)

sx, sy = CENTER
smass = 5000
sradius = 18

dist = 180
speed = 7.0
ex, ey = sx+dist, sy
evx, evy = 0, -speed
emass = 5
eradius = 7
trail = []

while True:
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    dx = sx - ex
    dy = sy - ey
    r2 = dx*dx + dy*dy
    r = math.sqrt(r2) + 1e-6
    F = G * smass * emass / r2
    ax = F * dx / r / emass
    ay = F * dy / r / emass

    evx += ax * DT
    evy += ay * DT
    ex += evx * DT
    ey += evy * DT

    trail.append((int(ex), int(ey)))
    if len(trail) > 400:
        trail.pop(0)

    screen.fill(BLACK)
    if len(trail)>1:
        pygame.draw.lines(screen, BLUE, False, trail, 1)
    pygame.draw.circle(screen, YELLOW, (int(sx),int(sy)), sradius)
    pygame.draw.circle(screen, BLUE, (int(ex),int(ey)), eradius)

   
    pygame.display.flip()

    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
