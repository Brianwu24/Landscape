import pygame
from pygame import *
import math as mth
import random
import glob

pygame.init()
pygame.mixer.init()

music_file_list = []
for file in glob.glob('music/*'):
    music_file_list.append(file)

def load_music():
    choice = random.choice(music_file_list)
    pygame.mixer.music.load(choice)
    mixer.music.set_volume(.3)

def unload_music():
    pygame.mixer.music.unload()

load_music()
pygame.mixer.music.play()

# setting screen size
size = (1920, 1080)

# loading the grass animation and mountain image which were all rendered in Blender
screen = pygame.display.set_mode(size, vsync=1)
clock = pygame.time.Clock()
file_list = glob.glob('grass/*')
grass_image = []
for file in file_list:
    image = pygame.image.load(file).convert_alpha()
    grass_image.append(image)

mountain_image = pygame.image.load('mountain.png').convert_alpha()

fire_image = pygame.image.load('fire.png').convert_alpha()
# defining colors in RGB
WHITE = (255, 255, 255)

BLACK = (0, 0, 0)
GREY = (40, 40, 40)

GREEN = (0, 255, 0)

SUN_YELLOW = (50, 50, 50)

BROWN = (139, 69, 19)
RED = (255, 0, 0)

LASER_BLUE = (63, 94, 249)

MOON = (150, 150, 150)
SILVER = (192, 192, 192)

# speed of each cycle
speed = 1


def draw_sun(position, color=WHITE):
    pygame.draw.circle(screen, color, position, radius=60)


def draw_moon(position, color=MOON):
    pygame.draw.circle(screen, color, position, radius=50)

    x, y = position
    pygame.draw.circle(screen, SILVER, (x + 10, y + 10), radius=10)
    pygame.draw.circle(screen, SILVER, (x - 25, y - 19), radius=10)
    pygame.draw.circle(screen, SILVER, (x + 15, y - 19), radius=6)
    pygame.draw.circle(screen, SILVER, (x - 25, y + 15), radius=6)
    pygame.draw.circle(screen, SILVER, (x + 35, y), radius=6)


def draw_clouds_1(position, colour):
    x, y = position
    pygame.draw.circle(screen, colour, (x - 30, y), radius=20)
    pygame.draw.circle(screen, colour, (x, y - 15), radius=30)
    pygame.draw.circle(screen, colour, (x + 10, y - 10), radius=30)
    pygame.draw.circle(screen, colour, (x - 10, y - 5), radius=30)
    pygame.draw.circle(screen, colour, (x + 30, y), radius=20)


def draw_clouds_2(position, colour):
    x, y = position
    pygame.draw.circle(screen, colour, (x - 50, y), radius=30)
    pygame.draw.circle(screen, colour, (x, y - 20), radius=40)
    pygame.draw.circle(screen, colour, (x + 20, y - 10), radius=40)
    pygame.draw.circle(screen, colour, (x - 30, y - 5), radius=40)
    pygame.draw.circle(screen, colour, (x + 40, y), radius=25)


def draw_star(position, color, radius):
    pygame.draw.circle(screen, color, position, radius)


def draw_glow(colour, radius):
    surf = pygame.Surface((radius * 2, radius * 2))
    pygame.draw.circle(surf, colour, (radius, radius), radius)
    surf.set_colorkey((0, 0, 0))
    return surf


def draw_background(color):
    surf = pygame.Surface((1920, 1080))
    pygame.draw.rect(surf, color, ((0, 0), (1920, 1080)))
    return surf


class fire_glow():
    def __init__(self):
        self.amount = 5
        self.random_y = []
        self.y = []
        self.x = []
        self.circle_info = []

        for i in range(self.amount):
            y = random.randrange(0, 31, 3)
            self.random_y.append(y)

        self.y = self.random_y.copy()

    def reset(self):
        for i in self.y:
            if self.pos_y + i < 600:
                self.y[self.y.index(i)] = random.choice(self.random_y)

    def draw_fire_glow(self, position):
        self.pos_x, self.pos_y = position
        for y in self.y:
            color = (255, 0, 0)
            glow_radius = 10
            screen.blit(draw_glow(color, glow_radius), (self.pos_x - glow_radius, (self.pos_y + y) - glow_radius),
                        special_flags=BLEND_RGB_ADD)
        self.y = [y - 2 * speed for y in self.y]
        self.reset()


def draw_bush(position, num_berry):
    x, y = position
    pygame.draw.rect(screen, BROWN, ((x, y), (40, 15)))
    pygame.draw.circle(screen, GREEN, (x - 10, y - 10), 20)
    pygame.draw.circle(screen, GREEN, (x + 20, y - 15), 25)
    pygame.draw.circle(screen, GREEN, (x + 5, y - 40), 16)

    pygame.draw.circle(screen, GREEN, (x + 40, y - 15), 25)
    pygame.draw.circle(screen, GREEN, (x + 25, y - 40), 17)

    # Berries
    if num_berry <= 3:
        pygame.draw.circle(screen, RED, (x + 40, y - 13), 5)
        pygame.draw.circle(screen, RED, (x - 10, y - 10), 5)
        pygame.draw.circle(screen, RED, (x, y - 40), 5)
    if num_berry == 4:
        pygame.draw.circle(screen, RED, (x, y - 40), 5)
        pygame.draw.circle(screen, RED, (x - 10, y - 10), 5)
        pygame.draw.circle(screen, RED, (x + 40, y - 13), 5)
        pygame.draw.circle(screen, RED, (x + 30, y - 40), 5)
    if num_berry == 5:
        pygame.draw.circle(screen, RED, (x + 40, y - 13), 5)
        pygame.draw.circle(screen, RED, (x - 10, y - 10), 5)
        pygame.draw.circle(screen, RED, (x + 20, y - 15), 5)
        pygame.draw.circle(screen, RED, (x + 30, y - 40), 5)
        pygame.draw.circle(screen, RED, (x, y - 40), 5)


def draw_tree(position, width, height):
    x, y = position
    pygame.draw.rect(screen, BROWN, ((x, y), (width, height)))
    pygame.draw.circle(screen, GREEN, (x - 10, y - 10), 20)
    pygame.draw.circle(screen, GREEN, (x + 20, y - 15), 25)
    pygame.draw.circle(screen, GREEN, (x + 5, y - 40), 16)

    pygame.draw.circle(screen, GREEN, (x + 40, y - 15), 25)
    pygame.draw.circle(screen, GREEN, (x + 25, y - 40), 17)


def draw_smol_tree(position, width, height):
    x, y = position
    pygame.draw.rect(screen, BROWN, ((x + width // 1.5, y), (width, height)))
    pygame.draw.circle(screen, GREEN, (x - 10, y - 10), 20)
    pygame.draw.circle(screen, GREEN, (x + 20, y - 15), 25)
    pygame.draw.circle(screen, GREEN, (x + 5, y - 40), 16)

    pygame.draw.circle(screen, GREEN, (x + 40, y - 15), 25)
    pygame.draw.circle(screen, GREEN, (x + 25, y - 40), 17)


def draw_UFO(position):
    x, y = position
    pygame.draw.circle(screen, (0, 106, 78), (x + 100, y), 60)
    pygame.draw.ellipse(screen, (150, 150, 150), ((x, y), (200, 80)))
    for i in range(5):
        pygame.draw.ellipse(screen, (255, 255, 255), ((x + 16 * (i + 1), y + 25 - 2 * i), (10, 30 + 5 * i)))
    for i in range(6):
        pygame.draw.ellipse(screen, (255, 255, 255), ((x + 80 + (16 * (i + 1)), y + 15 + 2 * i), (10, 55 - 5 * i)))


def draw_laser_beam(height):
    surf = pygame.Surface((600, 900))
    #drawing trapazoid thus 4 points
    #300 is the midpoint of the x, 600/2 = 300
    top_length = 30
    bottom_length = 180
    pygame.draw.polygon(surf, LASER_BLUE, ((300 - top_length, 10), (300 + top_length, 10), (300+bottom_length, height), (300-bottom_length, height)))
    return surf

def draw_sheep():
    surf = pygame.Surface((180, 100))
    x, y = 55, 40

    # legs
    def draw_legs(position, length):
        x, y = position
        pygame.draw.rect(surf, BROWN, ((x, y), (5, length)))
        pygame.draw.rect(surf, GREY, ((x, y + length), (5, 5)))

    #drawing legs from left to right
    draw_legs((x - 10, y + 15), 30)
    draw_legs((x + 10, y + 15), 25)
    draw_legs((x + 30, y + 15), 30)
    draw_legs((x + 50, y + 15), 25)

    #wool
    pygame.draw.circle(surf, WHITE, (x, y), 20)
    pygame.draw.circle(surf, WHITE, (x + 20, y - 5), 23)
    pygame.draw.circle(surf, WHITE, (x + 40, y), 20)

    #head
    pygame.draw.circle(surf, WHITE, (x + 60, y - 3), 25)
    pygame.draw.circle(surf, BROWN, (x+60, y - 3), 15)

    #eyes
    pygame.draw.circle(surf, BLACK, (x + 55, y - 6), 2)
    pygame.draw.circle(surf, BLACK, (x + 65, y - 6), 2)
    return surf

def draw_sheep_RGB(position):
    x, y = position

    # legs
    def draw_legs(position, length):
        x, y = position
        pygame.draw.rect(screen, BROWN, ((x, y), (5, length)))
        pygame.draw.rect(screen, GREY, ((x, y + length), (5, 5)))

    #drawing legs from left to right
    draw_legs((x - 10, y + 15), 30)
    draw_legs((x + 10, y + 15), 25)
    draw_legs((x + 30, y + 15), 30)
    draw_legs((x + 50, y + 15), 25)

    #wool
    pygame.draw.circle(screen, WHITE, (x, y), 20)
    pygame.draw.circle(screen, WHITE, (x + 20, y - 5), 23)
    pygame.draw.circle(screen, WHITE, (x + 40, y), 20)

    #head
    pygame.draw.circle(screen, WHITE, (x + 60, y - 3), 25)
    pygame.draw.circle(screen, BROWN, (x+60, y - 3), 15)

    #eyes
    pygame.draw.circle(screen, BLACK, (x + 55, y - 6), 2)
    pygame.draw.circle(screen, BLACK, (x + 65, y - 6), 2)

# game loop
cycles = 0
sun_x = 0  # 0-1920
moon_x = 0  # 0-1920

# cycles of the day
cycle_morning = True
cycle_afternoon = False
cycle_night = False
cycle_midnight = False

background_color = (47, 79, 79)

# cloud generator
# morning
day_gen_y = False
day_cloud_y_speed = []
day_amount = 0
day_cloud_prev_x = 0
day_cloud_offset = []
day_cloud_rgb = (200, 200, 200)

night_gen_y = False
night_cloud_rgb = (50, 50, 50)
night_cloud_y_speed = []
night_amount = 0
night_cloud_prev_x = 0
night_cloud_offset = []
night_cloud_rgb = (40, 40, 40)

star_list = []
draw_star_night = False
clock = pygame.time.Clock()

# num of berries
bush_berry = []
for i in range(20):
    berry = random.randrange(1, 6)
    bush_berry.append(berry)

UFO_y = 0
UFO_cycles = 0

fire_class = fire_glow()

song_end = False

running = True
while running:
    #music

    if not pygame.mixer.music.get_busy():
        unload_music()
        load_music()
        pygame.mixer.music.play()

    # background loop
    # morning
    if cycle_morning and sun_x < 960:  # 960 is 1920/2 half way so afternoon
        prev_r, prev_g, prev_b = background_color
        r, g, b = .17 * speed, .17 * speed, -.16 * speed
        background_color = (prev_r + r, prev_g + g, prev_g + b)
    if round(sun_x) == 960:
        cycle_morning = False
        cycle_afternoon = True

    # afternoon
    if cycle_afternoon and sun_x > 960:
        prev_r, prev_g, prev_b = background_color
        r, g, b = -.17 * speed, -.17 * speed, .16 * speed
        background_color = (prev_r + r, prev_g + g, prev_g + b)
    if round(sun_x) == 1920:
        cycle_afternoon = False
        cycle_night = True

    # night
    if cycle_night:
        prev_r, prev_g, prev_b = background_color
        r, g, b = -.035 * speed, -.07 * speed, -.07 * speed
        background_color = (prev_r + r, prev_g + g, prev_g + b)
    if round(moon_x) == 960:
        cycle_night = False
        cycle_midnight = True

    # Midnight
    if cycle_midnight and moon_x > 960:
        prev_r, prev_g, prev_b = background_color
        r, g, b = .035 * speed, .07 * speed, .07 * speed
        background_color = (prev_r + r, prev_g + g, prev_g + b)
    if round(moon_x) == 1920:
        background_color = (47, 79, 79)  # reset background colour in case that the values overflow
        cycle_midnight = False
        cycle_morning = True

    # drawing background,grass, and mountain
    screen.blit(draw_background(background_color), (0, 0))
    screen.blit(mountain_image, (0, 200))
    screen.blit(grass_image[round(cycles)], (0, 0))

    reduced_r, reduced_g, reduced_b = background_color
    if cycle_morning or cycle_afternoon:
        reduced_r, reduced_g, reduced_b = reduced_r ** 0.6, reduced_g ** 0.6, reduced_b ** 0.6
    else:
        reduced_r, reduced_g, reduced_b = 0, 0, 0
    screen.blit(draw_background((reduced_r, reduced_b, reduced_g)), (0, 0), special_flags=BLEND_RGB_ADD)

    # sun loop
    if (sun_x < 1920) and ((cycle_morning is True) or (cycle_afternoon is True)):
        sun_y = ((300 / 1500000) * ((sun_x - 100) * (sun_x - 1720))) + 300
        for i in range(0, 52, 15):
            radius = 20 + (i * 2)
            r, g, b = SUN_YELLOW
            r, g, b = r + i * 3, g + i * 2, b - i * .10

            # credit to https://www.youtube.com/watch?v=NGFk44fY0O4&ab_channel=DaFluffyPotato for this idea
            screen.blit(draw_glow((r, g, b), radius), (sun_x - radius, sun_y - radius), special_flags=BLEND_RGB_ADD)
        draw_sun((sun_x, sun_y))
        sun_x += speed
    else:
        # reset the sun_x value to 0 which makes the sun start the loop over
        sun_x = 0

    # moon loop
    if moon_x < 1920 and ((cycle_morning is False) and (cycle_afternoon is False)):
        if draw_star_night == False:
            for _ in range(5, 30):
                x = random.randrange(50, 1900)
                y = random.randrange(10, 300)

                star_list.append((x, y))
            draw_star_night = True

        for i in star_list:
            x, y = i
            color = [(255, 166, 81), (255, 199, 142), (255, 217, 178), (255, 229, 207), (255, 244, 243),
                     (199, 216, 255), (175, 201, 255)]
            color = random.choice(color)
            random_radius = random.randrange(1, 3)
            glow_radius = random_radius * 2
            screen.blit(draw_glow(color, glow_radius), (x - glow_radius, y - glow_radius),
                        special_flags=BLEND_RGB_ADD)
            draw_star(i, color, random_radius)

        moon_y = ((300 / 1500000) * ((moon_x - 100) * (moon_x - 1720))) + 300
        for i in range(0, 30, 5):
            radius = 25 + (i * 2)
            r, g, b = GREY
            r, g, b = r - i * .2, g - i * .5, b + i * .07

            screen.blit(draw_glow((r, g, b), radius), (moon_x - radius, moon_y - radius), special_flags=BLEND_RGB_ADD)
        draw_moon((moon_x, moon_y))
        moon_x += speed

    else:
        # reset the sun_x value to 0 which makes the sun start the loop over
        moon_x = 0
        star_list = []
        draw_star_night = False

    # main loop

    if day_gen_y is False:
        day_amount = random.randrange(2, 10)
        for i in range(day_amount):
            y = random.randrange(150, 200)
            day_cloud_y_speed.append(y)

            day_x_offset = random.randrange(200, 600)
            day_cloud_offset.append(day_x_offset)
        day_gen_y = True

    if cycle_morning or cycle_afternoon:
        day_cloud_x = day_cloud_prev_x + speed
        day_cloud_prev_x = day_cloud_x

        for i in range(day_amount):
            draw_clouds_1((day_cloud_x + day_cloud_offset[i] + 100, day_cloud_y_speed[i]), day_cloud_rgb)
            draw_clouds_2((day_cloud_x - day_cloud_offset[i] + 400, day_cloud_y_speed[i] + 200), day_cloud_rgb)

    if cycle_midnight:
        day_gen_y = False
        day_cloud_y_speed = []
        day_amount = 0
        day_cloud_prev_x = 0
        day_cloud_offset = []

    if night_gen_y is False:
        night_amount = random.randrange(2, 5)
        for i in range(night_amount):
            y = random.randrange(150, 200)
            night_cloud_y_speed.append(y)

            night_x_offset = random.randrange(400, 600)
            night_cloud_offset.append(night_x_offset)
        night_gen_y = True

    if cycle_night or cycle_midnight:
        night_cloud_x = night_cloud_prev_x + speed
        night_cloud_prev_x = night_cloud_x

        for i in range(night_amount):
            draw_clouds_1((night_cloud_x + night_cloud_offset[i] + 100, night_cloud_y_speed[i]), night_cloud_rgb)
            draw_clouds_2((night_cloud_x - night_cloud_offset[i] + 400, night_cloud_y_speed[i] + 200), night_cloud_rgb)

    # reset values for night cycle
    if cycle_afternoon:
        night_gen_y = False
        night_cloud_y_speed = []
        night_amount = 0
        night_cloud_prev_x = 0
        night_cloud_offset = []

    # things in the scene
    draw_tree((400, 650), 30, 200)
    draw_tree((600, 850), 30, 100)
    draw_tree((1000, 800), 30, 60)

    draw_smol_tree((1400, 450), 15, 500)

    draw_bush((500, 740), bush_berry[0])
    draw_bush((200, 840), bush_berry[1])
    draw_bush((700, 900), bush_berry[2])
    draw_bush((1200, 810), bush_berry[3])
    draw_bush((1600, 850), bush_berry[4])

    screen.blit(fire_image, (830, 800))

    for i in range(0, 51, 15):
        fire_class.draw_fire_glow((855 + i, 860))

    UFO_y = 15 * mth.sin(UFO_cycles / 15 - speed) + 400

    # draw_sheep((820, UFO_y + 200))
    sheep = draw_sheep()
    rotated_sheep = pygame.transform.rotate(sheep, UFO_cycles)
    screen.blit(pygame.transform.rotate(sheep, UFO_cycles / 2), (770, 700), special_flags=BLEND_RGB_ADD)
    screen.blit(pygame.transform.rotate(sheep, UFO_cycles * 2), (850, 700), special_flags=BLEND_RGB_ADD)
    screen.blit(pygame.transform.rotate(sheep, UFO_cycles * 3), (820, 550), special_flags=BLEND_RGB_ADD)

    UFO_y = 15 * mth.sin(UFO_cycles/15-speed) + 400
    screen.blit(draw_laser_beam(500), (600, UFO_y + 50), special_flags=BLEND_RGB_ADD)
    draw_UFO((800, UFO_y))

    draw_sheep_RGB((300, 900))
    draw_sheep_RGB((1200, 900))
    draw_sheep_RGB((600, 700))
    draw_sheep_RGB((1600, 700))
    draw_sheep_RGB((1550, 850))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)  # frames/ticks per second

    if cycles >= 120:
        cycles = 0
    cycles += 2

    UFO_cycles += 1

    pygame.display.flip()

pygame.quit()
