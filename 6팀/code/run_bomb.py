import pygame #1. pygame 선언
import random
import os

pygame.init()  # 2. pygame 초기화

# 3. 게임환경 전역변수 설정
BLACK = (0, 0, 0)
size = [600, 800]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

#게임 실행 무한루프
def runGame():

    #폭탄 이미지 설정
    bomb_image = pygame.image.load("./bombgame/bomb.png")
    bomb_image = pygame.transform.scale(bomb_image, (50, 50))
    bombs = []


    for i in range(5):                              #한번에 다섯개의 폭탄 생성
        rect = pygame.Rect(bomb_image.get_rect())   #폭탄 이미지 생성
        rect.left = random.randint(0, size[0])      #폭탄 사각형의 좌측 위를 좌표로 설정
        rect.top = -100
        dy = random.randint(12, 15)   #떨어지는 속도
        bombs.append({'rect': rect, 'dy': dy})  

    #캐릭터 이미지 설정
    person_image = pygame.image.load("./bombgame/person.png")
    person_image = pygame.transform.scale(person_image, (100, 100))
    person = pygame.Rect(person_image.get_rect())

    #캐릭터 위치 설정
    person.left = size[0] // 2 - person.width // 2
    person.top = size[1] - person.height
    person_dx = 0   #이동속도
    person_dy = 0

    global done
    while not done:
        clock.tick(30)
        screen.fill(BLACK)

    #조작키 설정
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    person_dx = -10
                elif event.key == pygame.K_RIGHT:
                    person_dx = 10
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    person_dx = 0
                elif event.key == pygame.K_RIGHT:
                    person_dx = 0

    #폭탄 생성
        for bomb in bombs:
            bomb['rect'].top += bomb['dy']      #폭탄이 낙하하도록 함
            if bomb['rect'].top > size[1]:      #폭탄이 바닥에 닿을 경우 삭제 후 재생성
                bombs.remove(bomb)
                rect = pygame.Rect(bomb_image.get_rect())
                rect.left = random.randint(0, size[0])
                rect.top = -100
                dy = random.randint(3, 9)
                bombs.append({'rect': rect, 'dy': dy})

        person.left = person.left + person_dx

        if person.left < 0:
            person.left = 0
        elif person.left > size[0] - person.width:
            person.left = size[0] - person.width

        screen.blit(person_image, person)

        #폭탄과 캐릭터 접촉 판정
        for bomb in bombs:
            if bomb['rect'].colliderect(person):    #bomb과 person이 겹칠 경우(colliderect)
                done = True
            screen.blit(bomb_image, bomb['rect'])

        pygame.display.update()


runGame()
pygame.quit()