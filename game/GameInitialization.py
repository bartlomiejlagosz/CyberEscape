from PIL import Image
import ctypes
from game.GroundGenerator import *
from game.Character import *
from game.Ground import *
import random
from opencv.detection import *

def get_screen_size():
    user32 = ctypes.windll.user32
    return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

def set_screen_prop():
    pygame.display.set_caption("Window")
    return pygame.display.set_mode(get_screen_size(),pygame.RESIZABLE)


def draw_runner():
    runner.display(game_window)


def draw_init_objects(objects):
    for i in range(0, 13):
        objects.append(Ground(i * 122 - 50, 598, 180, 180))

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
usr32 = ctypes.windll.user32
screen_width = usr32.GetSystemMetrics(1)
screen_height = usr32.GetSystemMetrics(0)
speed = 60
objects = []
run = True
frame_counter = 0
pygame.time.set_timer(pygame.USEREVENT + 1, 120000)
pygame.time.set_timer(pygame.USEREVENT + 2, random.randrange(6000,10000))
flag = 0
bg_speed = 1
runner = Character(200, 500, 100, 100)
game_window = set_screen_prop()
if len(os.listdir('../resources/background_fit')) == 0:
    for x in range(0, 60):
        img = Image.open('../resources/background/frame_' + str(x) + '_delay-0.03s.gif')
        img = img.resize((screen_height, screen_width), Image.ANTIALIAS)
        img.save('../resources/background_fit/frame_' + str(x) + '_delay-0.03s.gif')
background = [pygame.image.load(os.path.join('../resources/background_fit', 'frame_' + str(x) + '_delay-0.03s.gif'))
              for x in range(0, 60)]
aWeight = 0.5
camera = cv.VideoCapture(0)
top, right, bottom, left = 80, 350, 295, 590
num_frames = 0
calibrated = False
