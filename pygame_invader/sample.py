import pygame
from pygame import mixer
import random
import math

pygame.init()
clock = pygame.time.Clock()
FPS = 60
screen = pygame.display.set_mode((800,600))    
# # 背景色の設定
# screen.fill((150, 150, 120))
# Windowに表示されるゲーム名
pygame.display.set_caption("Invader Game")


# Pleyer
playerImg = pygame.image.load("marmot.png")
playerX,playerY = 370,480
playerX_change = 0
playerY_change = 0
# Enemy
enemyImg = pygame.image.load("enemy.png")
enemyX = random.randint(0,736)
enemyY = random.randint(50,150)
enemyX_change,enemyY_change = 4, 40
# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 3
bullet_state = 'ready'
# Score 
scoreValue = 0
# Sound
mixer.init()
sound = mixer.Sound('laser.wav')

def player(x,y):
    screen.blit(playerImg,(x,y))
def enemy(x,y):
    screen.blit(enemyImg, (x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    # sound.play()s
    screen.blit(bulletImg,(x + 16, y + 10))
def isCollision(enemyX,enemyY,bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY -bulletY, 2))
    if distance < 27:
        return True
    else:
        return False
    
def show_fps():
    fps_font = pygame.font.SysFont(None, 24)
    fps_text = fps_font.render(f"FPS: {int(clock.get_fps())}", True, (255,255,255))
    screen.blit(fps_text, (10, 10))



# 音声ファイルの読み込みと再生を確認
# try:
#     sound = mixer.Sound('laser.wav')
#     sound.play()
#     print("音声ファイルの再生に成功")
# except pygame.error as e:
#     print("音声ファイルの再生に失敗:", e)

running = True
while running:
    clock.tick(FPS)
    screen.fill((150, 150, 120))
    
    for event in pygame.event.get():
        #閉じるボタン押下で終了
        if event.type == pygame.QUIT:
            running = False
        # キー操作
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 1.5
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LALT or pygame.K_RIGHT:
                playerX_change = 0
    # player_move
    playerX += playerX_change
    if playerX <=0:
        playerX = 0
    elif playerX >= 736:
        playerX =736


    #enemy_move
    if enemyY >440:
        break
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 4
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -4
        enemyY += enemyY_change
    collision = isCollision(enemyX,enemyY,bulletX,bulletY)
    if collision:
        bulletY = 480
        bullet_state ='ready'
        scoreValue += 1
        sound.play()
        enemyX = random.randint(0,736)
        enemyY = random.randint(50,150)
    
    # Bullet_move
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'
    if bullet_state == 'fire':
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change
    # score
    font = pygame.font.SysFont(None, 32)
    score =font.render(f"Score : {str(scoreValue)}",True,(255,255,255))
    screen.blit(score,(20,50))

    player(playerX,playerY)
    enemy(enemyX,enemyY)


    show_fps()  # FPSを表示
    # 画面を更新
    pygame.display.update()

# ゲーム終了時
pygame.quit()