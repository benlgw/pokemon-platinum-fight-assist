import pokemon_stats
from os import system

import pygame

import ocr
import pokemon_stats

# --------------------

pygame.init()

controllers = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYDEVICEADDED:
            print('Controller Detected')
            controller = pygame.joystick.Joystick(event.device_index)
            controllers.append(controller)
        elif event.type == pygame.JOYDEVICEREMOVED:
            print('Controller Removed')
            controllers.pop()

        '''
        Controller Mappings:
        0 = A
        1 = B
        3 = X
        4 = Y
        6 = LB
        7 = RB
        10 = LEFT MENU
        11 = RIGHT MENU
        15 = MIDDLE MENU
        '''

        for controller in controllers:
            if controller.get_button(11):  # Right Menu Button
                system('clear||cls')
                oponnent = ocr.get_opponent_pokemon()
                # try:
                for pokemon in oponnent:
                    if pokemon == None:
                        continue
                    oponnent = pokemon_stats.pokemon[pokemon] if type(oponnent) == str else pokemon_stats.pokemon[pokemon[0]]
                    print(f'Name: {oponnent['name'].upper()}')
                    print(f'\nType: {oponnent['type']}')
                    # for pokemon_type in oponnent['type']:
                    #     print(f'{pokemon_type}')
                    print(f'\nWeakness: {oponnent['weakness']}')
                    # for pokemon_weakness in oponnent['weakness']:
                    #     print(f'{pokemon_weakness}')
                    print(f'\nNormal: {oponnent['normal_attack']}')
                    # print(f'\nInnefective: {oponnent['innefective']}')
                    # print(f'\nImmune: {oponnent['immune']}')
                # except:
                #     print(f'Pokemon Not Detected (Recieved: {oponnent})')