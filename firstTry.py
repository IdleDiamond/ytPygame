#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 21:08:41 2024

@author: joaking
"""

import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/Pixeltype.ttf',50)


sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/Ground.png').convert()

score_surf = test_font.render('My Game', False, (64,64,64))
score_rect = score_surf.get_rect(center = (400, 50))

snail_surface = pygame.image.load('graphics/Snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600, 300))

player_surf = pygame.image.load('graphics/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity  = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_gravity = -20
            
        if event.type == pygame.KEYUP:
            print("Key up")

           
            
            """
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("mouse down")
            """
            
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    
    pygame.draw.rect(screen, 0xc0e8ec , score_rect)
    pygame.draw.rect(screen, 0xc0e8ec , score_rect, 10)
    screen.blit(score_surf,(score_rect))
    
    
    
    """
    snail_x_pos -= 4
    if snail_x_pos < -50:
        snail_x_pos = 775
    screen.blit(snail_surface, (snail_x_pos,250))
    """
    
    snail_rect.right -= 4
    if snail_rect.right < 0:
        snail_rect.right = 850
    screen.blit(snail_surface, snail_rect)
    
    #player
    player_gravity += 1
    player_rect.y += player_gravity
    screen.blit(player_surf, player_rect)
    
    
    
    """
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        print("jump")
    """
    
    """
    if player_rect.colliderect(snail_rect):
        print("collision")
    """
    
    """
    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        print(pygame.mouse.get_pressed())
    """
    
    pygame.display.update()
    clock.tick(60)
    
    
    
    
    
    
    
    
    
    
    
    
    