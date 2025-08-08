import pygame
import time

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Rosto Eletrônico")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_face(expression="neutral"):
    screen.fill(WHITE)

    # Cabeça
    pygame.draw.circle(screen, (255, 220, 180), (200, 200), 150)

    # Olhos
    pygame.draw.circle(screen, BLACK, (140, 150), 20)
    pygame.draw.circle(screen, BLACK, (260, 150), 20)

    # Boca
    if expression == "neutral":
        pygame.draw.line(screen, BLACK, (150, 260), (250, 260), 5)
    elif expression == "happy":
        pygame.draw.arc(screen, BLACK, pygame.Rect(150, 230, 100, 50), 0, 3.14, 5)
    elif expression == "sad":
        pygame.draw.arc(screen, BLACK, pygame.Rect(150, 260, 100, 50), 3.14, 6.28, 5)
    elif expression == "surprised":
        pygame.draw.circle(screen, BLACK, (200, 260), 20, 5)

    pygame.display.flip()

running = True
expressions = ["neutral", "happy", "sad", "surprised"]
idx = 0
last_change = time.time()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Troca expressão a cada 2 segundos
    if time.time() - last_change > 2:
        idx = (idx + 1) % len(expressions)
        draw_face(expressions[idx])
        last_change = time.time()

pygame.quit()