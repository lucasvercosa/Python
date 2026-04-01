import pygame #Usado para jogos
pygame.init() #Inicia o pygame
pygame.mixer.init() #Inicializar o mixer (importante!)
pygame.mixer.music.load('') #Carrega a música
pygame.mixer.music.play() #Toca a música
input() #Pausa o programa até você apertar Enter dando tempo do pygame inicializar corretamente
pygame.event.wait()