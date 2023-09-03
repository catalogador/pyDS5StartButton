import pygame
import subprocess


pygame.init()

pycontroller = pygame.joystick.get_count()

epicPath = "C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe"


if(pycontroller >= 1):
    gamepad = pygame.joystick.Joystick(0)
    gamepad.init()

    print(f"Controle detectado: {gamepad.get_name()}")


    print(f"{gamepad.get_button(10)}")


    button_mapping = {
        6: 6,

    }

    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                xbox_button = button_mapping.get(event.button,None)
                if xbox_button is not None:
                    print(f"botão {xbox_button} pressionado")
                    subprocess.run([epicPath])




