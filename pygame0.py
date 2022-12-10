import pygame
pygame.init()

screen = pygame.display.set_mode((500,600))
WHITE =(255,255,255)
YELLOW =(252, 215, 3)
BLACK= (0,0,0)
RED = (255,0,0)

running = True
font = pygame.font.SysFont('Arial',50)
text1 = font.render("+",True,BLACK)
text2 = font.render("+",True,BLACK)
text3 = font.render("start",True,BLACK)
text4 = font.render("-",True,BLACK)
text5 = font.render("-",True,BLACK)
text6 = font.render("Reset",True,BLACK)
while running:
	#lap day man hinh
	screen.fill(YELLOW)
	#vi tri con chuot
	
	#ve hinh chu nhat
	pygame.draw.rect(screen,WHITE,(100,50,50,50))
	pygame.draw.rect(screen,WHITE,(200,50,50,50))
	pygame.draw.rect(screen,WHITE,(300,50,150,50))
	pygame.draw.rect(screen,WHITE,(100,200,50,50))
	pygame.draw.rect(screen,WHITE,(200,200,50,50))
	pygame.draw.rect(screen,WHITE,(300,200,150,50))
	pygame.draw.rect(screen,BLACK,(50,520,400,50))
	pygame.draw.rect(screen,WHITE,(60,530,380,30))

	# text
	screen.blit(text1,(112,47))
	screen.blit(text2,(212,47))
	screen.blit(text3,(320,55))
	screen.blit(text4,(118,197))
	screen.blit(text5,(218,197))
	screen.blit(text6,(312,205))
	# hinh tron
	pygame.draw.circle(screen, BLACK , ( 250,400), 100)
	pygame.draw.circle(screen, WHITE , ( 250.5,400), 95)
	# kim
	pygame.draw.line(screen, RED, (250,400),(250,350))
#	pygame.draw.line(screen, BLACK,(250,400),(250,310))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				print("chuot trai")
			elif event.button == 3:
				print("chuot phai")
			elif event.button == 2:
				print("chuot giua")
	pygame.display.flip()

pygame.quit()
