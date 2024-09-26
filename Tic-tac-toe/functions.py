import pygame
def play_audio(audio):
    pygame.mixer.init()
    pygame.mixer.music.load('d:\python-for-devops\Tic-tac-toe\Audios\\'+audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  
        pygame.time.Clock().tick(5)

def position_choice():
    choice = ''
    patience_counter = 0
    rascal_flag = False
    while choice not in ['0','1','2']:
        choice = input("Pick a position(0,1,2): ")
        if choice not in ['0','1','2']:
            if patience_counter >=3:
                play_audio("kalikkunnoda_myre.mp3")
                patience_counter =0
                rascal_flag = True
                continue
            play_audio("Appo_naan_pottana.mp3")
            patience_counter +=1
    if rascal_flag: play_audio("Bloody_rascal.mp3")
            
    return int(choice)

def start_game():
    choice = ''
    patience_counter = 0
    while choice != 'Y':
        choice = input("Start game(Y,N)?")
        if  choice == 'N':
             play_audio("Poda_punda.mp3")
        elif choice == 'Y':
            play_audio("Adichu_keri_vaa.mp3")
        else:
            play_audio("Mudra_sradhikkanam.mp3")
    return choice

def play_user_turn():
    choice = ''
    while choice not in ['Y','N']:
        choice = input("Play your turn?[Y or N]")
        if choice not in ['Y','N']:
           play_audio("Velachil.mp3")  
    if choice == 'Y'
    return True

