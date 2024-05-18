import cv2
import pygame
import sys
import mediapipe as mp
import pyautogui
import random
from ball import Ball, AI_ball
from barrier import Barrier, Barrier2
from border import Border, Top_Border
from points import Point_Display
from menu.text import Menu_Text
from bg import Bg

pygame.init()

# Константы
WIDTH = 640
HEIGHT = 480
FPS = 60
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
cap = cv2.VideoCapture(1)
# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball test")
clock = pygame.time.Clock()

crash_sound = pygame.mixer.Sound("boing.mp3")

fingers_dict = []

def get_raised_fingers():
    global fingers_dict
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    index = 0
    data_stored = []
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for landmark in hand_landmarks.landmark:
                h, w, _ = frame.shape
                cx, cy = int(landmark.x * w), int(landmark.y * h)
                index += 1
                data_stored.append([cx, cy])



    list_ys = {}
    index = 0
    if data_stored:
        for x in data_stored:
            index += 1
            if index-1 in [4, 8, 12, 16, 20]:
                list_ys.update({x[1]:index-1})

        list_ys_sorted = sorted(list_ys)
        range_data = list_ys_sorted[-1] - list_ys_sorted[0]
        try:
            if not -30 < fingers_dict[0] - range_data < 30:
                for x in list_ys:
                    if x != list_ys_sorted[0]:
                        if x < list_ys_sorted[0] + 20:
                            print(x, list_ys_sorted[0])
                            return 2
                return 1
            else:
                fingers_dict.append(range_data)
        except IndexError:
            fingers_dict.append(range_data)
    else:
        return 0



def get_hand_data():
    hands_dict = {'0':[], '1':[], '2':[]}
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    index = 0
    hand_index = 0
    hs, ws = 0, 0
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for landmark in hand_landmarks.landmark:
                h, w, _ = frame.shape
                hs, hw = h, w
                if index in [6, 7]:
                    cx, cy = int(landmark.x * w), int(landmark.y * h)
                    hands_dict[f'{hand_index}'].append([cx, cy])
                index += 1

            hand_index += 1
            index = 0
    return [hands_dict, [hs, ws]]

def main():
    # Спрайты

    ball = Ball()
    barrier = Barrier()
    barrier2 = Barrier2()
    ai_ball = AI_ball(ball)
    border = Border()
    menu_text = Menu_Text()
    bg = Bg()
    top_border = Top_Border()
    point_display = Point_Display('0', '0')

    collisions = []
    collisions2 = []

    points1, points2 = 0, 0
    tick = 0

    barrier1_hidden, barrier2_hidden = False, False

    running = True
    menu = True
    ai_enabled = True
    ai_calculate = False
    if ai_enabled:
        barrier2.update(WIDTH - 60, 300 - 150)
    updating_all = True
    while running:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        cv2.imwrite("cur_image.png", frame)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))
        if not menu:
            bg.draw(screen)
            barrier.draw(screen)
            barrier2.draw(screen)
            border.draw(screen)
            top_border.draw(screen)
            point_display.draw(screen, points1, points2)
            ball.draw(screen)
            # ai_ball.draw(screen)

            if not barrier1_hidden or not barrier2_hidden:
                ball.update()
                if ai_enabled and not ai_calculate:
                    ai_ball.reset(ball)
                elif ai_calculate:
                    ai_ball.update()


            base = get_hand_data()
            dictionary = base[0]
            dimentions = base[1]
            dictionary_counter = 0
            if dictionary['0']:
                dictionary_counter += 1
            if dictionary['1']:
                dictionary_counter += 1

            try:
                if not barrier1_hidden:
                    barrier.update(dictionary['0'][1][0]*(WIDTH/640), dictionary['0'][1][1]*(HEIGHT/440)-50)

            except IndexError:
                pass
            try:
                if not barrier2_hidden and not ai_enabled:
                    barrier2.update(dictionary['1'][1][0]*(700/640), dictionary['1'][1][1]*(600/440)-50)
                elif ai_enabled and barrier2.target != 0:
                    barrier2.move()
            except IndexError:
                pass

            if points1 == 10:
                print("PLAYER 1 WON")
                quit()
            if points2 == 10:
                print("PLAYER 2 WON")
                quit()

            # Ball movement

            if ball.rect.bottom > screen.get_rect().bottom:
                ball.hit_wall(0)
            if ball.rect.right > screen.get_rect().right:
                points1 += 1
                ai_calculate = False
                ball.rect.center = screen.get_rect().center
                ball.move = [random.choice([-10, 10, -15, 15]), random.choice([-10, 10, -15, 15])]

            if ball.rect.top < screen.get_rect().top+50:
                ball.hit_wall(2)
            if ball.rect.left < screen.get_rect().left:
                points2 += 1
                ai_calculate = False
                ball.rect.center = screen.get_rect().center
                ball.move = [random.choice([-10, 310, -15, 15]), random.choice([-10, 10, -15, 15])]

            if ai_calculate:
                if ai_ball.rect.bottom > screen.get_rect().bottom:
                    ai_ball.hit_wall(0)

                if ai_ball.rect.top < screen.get_rect().top+50:
                    ai_ball.hit_wall(2)



            if not ai_calculate and ai_enabled:
                ai_ball.reset(ball)
            if ai_calculate and ai_enabled:
                if ai_ball.rect.x >= WIDTH-70:
                    barrier2.reach(ai_ball.rect.y-150)
                    ai_ball.move = ai_ball.move2
                    ai_ball.reset(ball)
                    ai_calculate = False

            temp_group = pygame.sprite.Group()
            temp_group.add(ball)
            # AI
            if ball.move[0] > 0 and pygame.sprite.spritecollide(border, temp_group, False):
                ai_calculate = True
                ai_ball.move1 = [ball.move[0]*2, ball.move[1]*2]
                ai_ball.move = ai_ball.move1
            if pygame.key.get_pressed()[pygame.K_r]:
                return main()

            if pygame.sprite.spritecollide(barrier, temp_group, False):
                collisions2.append(True)
                boole = False
                try:
                    if collisions2[-1] == collisions2[-2]:
                        ball.rect.y -= 3
                    else:
                        boole = True
                except:
                    boole = True

                if boole:
                    crash_sound.play()
                    if ball.rect.bottom > barrier.rect.bottom:
                        ball.hit_wall(0)

                    if ball.rect.right > barrier.rect.right:
                        ball.hit_wall(1)

                    if ball.rect.top < barrier.rect.top:
                        ball.hit_wall(2)

                    if ball.rect.left < barrier.rect.left:
                        ball.hit_wall(3)

            else:
                collisions2.append(False)

            if pygame.sprite.spritecollide(barrier2, temp_group, False):
                collisions.append(True)
                boole = False
                try:
                    if collisions[-1] == collisions[-2]:
                        ball.rect.y -= 3
                    else:
                        boole = True
                except:
                    boole = True

                if boole:
                    crash_sound.play()

                    if ball.rect.bottom > barrier2.rect.bottom:
                        ball.hit_wall(0)
                    if ball.rect.right > barrier2.rect.right:
                        ball.hit_wall(1)
                    if ball.rect.top < barrier2.rect.top:
                        ball.hit_wall(2)
                    if ball.rect.left < barrier2.rect.left:
                        ball.hit_wall(3)


            else:
                collisions.append(False)

            if not ai_enabled:
                if dictionary_counter == 2:
                    barrier1_hidden, barrier2_hidden = False, False
                if dictionary_counter == 1:
                    barrier1_hidden, barrier2_hidden = True, False

            if screen.get_width()/2+20 > barrier.rect.x > screen.get_width()/2-20:
                barrier.originate()

            if screen.get_width()/2+20 > barrier2.rect.x > screen.get_width()/2-20:
                barrier2.originate()

            try:
                del collisions[-3]
            except:
                pass
            try:
                del collisions2[-3]
            except:
                pass
            # Обновление экрана
        else:
            tick += 1
            menu_text.draw(screen)
            if get_raised_fingers() == 1 and (tick%20) == 0:
                menu = False
                ai_enabled = True
            elif get_raised_fingers() == 2:
                menu = False
                ai_enabled = False

        pygame.display.update()


if __name__ == "__main__":
    main()
