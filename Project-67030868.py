import pygame
import sys

pygame.init()

#ตัวหน้าจอแสดงผล
WIDTH, HEIGHT = 1200, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Vocabwordly")

#ภาพ
try:
    background_image = pygame.image.load('background.jpg')
    IMG_1845 = pygame.image.load('IMG_1845.png')
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
    t_bg = pygame.image.load('IMG_1848.png')
    w_bg = pygame.image.load('IMG_1849.png')
    wood_bg = pygame.image.load('IMG_1850.png')
except pygame.error as e:
    print("Could not load background image:", e)
    sys.exit()

#ตัวข้อมูลด่าน ตัวอักษร คำศัพท์
levels = {
    1: (['b', 'a', 't'], ['bat', 'tab', 'ab', 'at']),
    2: (['d', 'o', 'f', 'e', 'g'], ['fed', 'god', 'of', 'fog', 'dog']),
    3: (['w', 'h', 'i', 't', 'e'], ['hit', 'it', 'with','wet','tie','wit','hi','white','he']),
    #4 : (['a','l','b','i','o','n'], ['lion','ab','albino','bin','lab','lib','ab','ban','lan','bon','boil']),
}

#สีตามค่า RGB
WHITE = (255, 255, 255)
LIGHT_GRAY = (240, 240, 240)
DARK_GRAY = (50, 50, 50)
SOFT_BLUE = (106, 196, 255)
SOFT_PURPLE = (160, 106, 255)
SOFT_GREEN = (144, 238, 144)
SOFT_RED = (255, 102, 102)
BLACK = (0, 0, 0)
LIGHT_BROWN = (211, 185, 144)
MEDIUM_BROWN = (165, 125, 85)
DARK_BROWN = (101, 67, 33)

#การตั้งค่าฟ้อนท์
font = pygame.font.SysFont('Roboto', 80)
small_font = pygame.font.SysFont('Roboto', 30)

#ปุ่ม
class Button:
    def __init__(self, text, pos, size, color, hover_color, text_color=BLACK, border_radius=10):
        self.text = text
        self.pos = pos
        self.size = size
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.border_radius = border_radius

    def draw(self, window):
        mouse_pos = pygame.mouse.get_pos()
        rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        pygame.draw.rect(window, self.hover_color if rect.collidepoint(mouse_pos) else self.color, rect, border_radius=self.border_radius)
        text_surface = small_font.render(self.text, True, self.text_color)
        window.blit(text_surface, (self.pos[0] + (self.size[0] - text_surface.get_width()) // 2,
                                   self.pos[1] + (self.size[1] - text_surface.get_height()) // 2))

    def is_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        return rect.collidepoint(mouse_pos)

#คำสั่งปุ่มต่าง ๆ ในหน้าเมนู
def main_menu():
    play_button = Button("Play", (WIDTH // 2 - 100, HEIGHT // 2 - 40), (200, 60), LIGHT_BROWN, DARK_BROWN)
    tutorial_button = Button("Tutorial", (WIDTH // 2 - 100, HEIGHT // 2 + 40), (200, 60), LIGHT_BROWN, DARK_BROWN)
    select_level_button = Button("Level", (WIDTH // 2 - 100, HEIGHT // 2 + 140), (200, 60), LIGHT_BROWN, DARK_BROWN)

    while True:
        WIN.blit(IMG_1845, (0, 0))

        #ตัวขอบชื่อเกม
        title_text_border = font.render("Vocabwordly", True, WHITE)
        title_text = font.render("Vocabwordly", True, DARK_GRAY)
        WIN.blit(title_text_border, (WIDTH // 2 - title_text_border.get_width() // 2 + 2, HEIGHT // 4 + 2)) 
        WIN.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))

        play_button.draw(WIN)
        tutorial_button.draw(WIN)
        select_level_button.draw(WIN)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.is_clicked():
                    level_selection()
                elif tutorial_button.is_clicked():
                    show_tutorial()
                elif select_level_button.is_clicked():
                    level_selection()

#คำสั่งเลือกด่าน
def level_selection():
    level_buttons = [
        Button("Level 1", (WIDTH // 2 - 100, HEIGHT // 2 - 40), (200, 60), LIGHT_BROWN, DARK_BROWN),
        Button("Level 2", (WIDTH // 2 - 100, HEIGHT // 2 + 40), (200, 60), LIGHT_BROWN, DARK_BROWN),
        Button("Level 3", (WIDTH // 2 - 100, HEIGHT // 2 + 120), (200, 60), LIGHT_BROWN, DARK_BROWN),
        Button("Back", (WIDTH // 2 - 100, HEIGHT // 2 + 200), (200, 60), MEDIUM_BROWN, SOFT_PURPLE),
    ]

    while True:
        WIN.blit(wood_bg,(0,0))
        title_text = font.render("Select Level", True, DARK_GRAY)
        WIN.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))

        for button in level_buttons:
            button.draw(WIN)

        pygame.display.flip() #เพื่ออัปเดทข้อมูลเกมในส่วนของหน้าจอ

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, button in enumerate(level_buttons):
                    if button.is_clicked():
                        if i < 3:  
                            Vocabwordly(i + 1)
                        else:  #ปุ่มกลับ
                            return  

#คำสั่งหน้าสอนเล่น
def show_tutorial():
    back_button = Button("Back", (WIDTH // 2 - 100, HEIGHT - 80), (200, 60), MEDIUM_BROWN, SOFT_PURPLE)

    while True:
        WIN.blit(t_bg,(0,0))
        tutorial_text = font.render("Tutorial", True, DARK_GRAY)
        instructions = [
            "Form words by connecting letters.",
            "To select a letter, click on it. Click a selected letter again to deselect it.",
        ]

        WIN.blit(tutorial_text, (WIDTH // 2 - tutorial_text.get_width() // 2, HEIGHT // 4))
        for i, line in enumerate(instructions):
            instruction_surface = small_font.render(line, True, DARK_GRAY)
            WIN.blit(instruction_surface, (WIDTH // 2 - instruction_surface.get_width() // 2, HEIGHT // 2 + i * 30))

        back_button.draw(WIN)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and back_button.is_clicked():
                return 

#แก้ว
def draw_glass_shape(x, y, width, height):
    pygame.draw.rect(WIN, WHITE, (x - width // 2, y - height, width, height), border_radius=10)
    pygame.draw.rect(WIN, WHITE, (x - width // 2, y - height, width, height), 5, border_radius=10)  #ขอบขาว

#คำสั่งตัวแสดงอนิเมชั่นตัวคำที่ถูกเติม
def display_glass(found_words, total_words):
    glass_height = 360  
    glass_width = 140   
    glass_x = WIDTH // 2
    glass_y = HEIGHT // 2 + 50

    draw_glass_shape(glass_x, glass_y, glass_width, glass_height)

    #ตัวคำสั่งเติมแก้ว
    if found_words:
        fill_ratio = len(found_words) / total_words
        fill_height = int((glass_height - 20) * fill_ratio)
        fill_rect = pygame.Rect(glass_x - glass_width // 2 + 10, glass_y - fill_height, glass_width - 20, fill_height)
        pygame.draw.rect(WIN, SOFT_GREEN, fill_rect, border_radius=10)  #ตัวคำที่ถูกเติมไป

    #คำสั่งคำที่เหลือ
    words_left = total_words - len(found_words)
    words_left_surface = small_font.render(f"Words left: {words_left}", True, DARK_GRAY)
    WIN.blit(words_left_surface, (WIDTH // 2 - words_left_surface.get_width() // 2, glass_y + 10))

#คำที่เชื่อมได้
def display_found_words(found_words):

    #คำสั่งแสดงคำที่เชื่อมได้
    glass_width = 140 
    distance_from_glass = 70 
    start_x = (WIDTH // 2) + (glass_width // 2) + distance_from_glass 
    start_y = HEIGHT // 2 - 180 

    words_surface = small_font.render("Found Words:", True, DARK_GRAY)
    WIN.blit(words_surface, (start_x, start_y))

    for i, word in enumerate(found_words):
        word_surface = small_font.render(word, True, DARK_GRAY)
        WIN.blit(word_surface, (start_x, start_y + 30 + i * 30)) 


#คำสั่งการเคลื่อนไหวของคำไปในแก้ว
def animate_word_in_glass(word, found_words, total_words):
    word_surface = small_font.render(word, True, DARK_GRAY)
    word_x = WIDTH // 2 - word_surface.get_width() // 2
    word_y = HEIGHT // 2 + 20  

    for _ in range(30):  #ตัวอนิเมชั่น
        WIN.fill(LIGHT_BROWN)
        display_glass(found_words, total_words)
        WIN.blit(word_surface, (word_x, word_y))
        word_y -= 2  #ขยับ

        pygame.display.flip()
        pygame.time.delay(30)

#คำสั่งตัวเกม
def Vocabwordly(start_level):
    clock = pygame.time.Clock()
    level = start_level

    while level in levels:  #มีไว้เพื่อให้เล่นในตัวเลเวลต่อไปเพื่อกันไม่ให้มีข้อผิดพลาดที่ข้ามไปข้ออื่น
        letters, possible_words = levels[level]
        found_words = []
        selected_letters = []

        back_button = Button("Back", (WIDTH // 2 - 100, HEIGHT - 80), (200, 60), MEDIUM_BROWN, SOFT_PURPLE)

        while True:
            WIN.blit(w_bg, (0, 0))
            display_glass(found_words, len(possible_words))
            letter_buttons = []
            for index, letter in enumerate(letters):
                button_rect = pygame.Rect(WIDTH // 2 - (len(letters) * 70) // 2 + index * (70 + 10), HEIGHT // 2 + 100, 60, 60)
                letter_buttons.append((button_rect, letter))

                if letter in selected_letters:
                    pygame.draw.rect(WIN, SOFT_GREEN, button_rect, border_radius=15)
                else:
                    pygame.draw.rect(WIN, LIGHT_BROWN, button_rect, border_radius=15)

                letter_surface = font.render(letter, True, WHITE)
                WIN.blit(letter_surface, (button_rect.x + (60 - letter_surface.get_width()) // 2,
                                          button_rect.y + (60 - letter_surface.get_height()) // 2))

            back_button.draw(WIN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button_rect, letter in letter_buttons:
                        if button_rect.collidepoint(pygame.mouse.get_pos()):
                            if letter in selected_letters:
                                selected_letters.remove(letter)
                            else:
                                selected_letters.append(letter)

                            selected_word = ''.join(selected_letters)
                            if selected_word in possible_words and selected_word not in found_words:
                                found_words.append(selected_word)
                                animate_word_in_glass(selected_word, found_words, len(possible_words))
                                selected_letters.clear()

                    if back_button.is_clicked():
                        return  

            display_found_words(found_words)

            if len(found_words) == len(possible_words):
                break

            pygame.display.flip()
            clock.tick(60)

        level += 1  #เพื่อล็อคให้มันเล่นไปต่อในเลเวลถัดไปหลังจากที่สำเร็จเลเวลก่อนหน้า



main_menu()
pygame.exit()