from os import system

import pygame

import ocr
from poke_utils import Pokemon

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
                for pokemon in oponnent:
                    enemy = Pokemon(pokemon)
                    if enemy.exists():
                        # name
                        print(f"Name: {enemy.get_name().upper()}")
                        # type
                        print("\nType: ", end="")
                        for type in enemy.get_types():
                            print(f"| {type} | ", end="")
                        # weaknesses
                        print("\nWeaknesses: ", end="")
                        for weakness in enemy.get_weakness():
                            print(f"| {weakness} | ", end="")
                        # normal attacks i.e. not weakness, resistant, or immine
                        # not yet implemented
                    else:
                        print("Pokemon not detected")
