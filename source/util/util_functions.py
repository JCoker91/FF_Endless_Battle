import os
import pygame


def load_image_folder(folder_path: str):
    images = []
    for file in sorted(os.listdir(folder_path)):
        if file.endswith('.png') or file.endswith('.jpeg'):
            _image = pygame.image.load(
                os.path.join(folder_path, file)).convert_alpha()
            images.append(_image)
    return images


def draw_text_wrap(string: str,font: pygame.font.Font, wrap_width: int, x_pos: int, y_pos: int, text_color: pygame.Color = 'White'):    
    words = string.split(' ')
    display_surface = pygame.display.get_surface()
    line_count = 0
    current_line_length = 0
    words_per_line = []
    for word in words:
        rendered_text = font.render(word, False, text_color)
        rendered_width = rendered_text.get_width()
        heigth = rendered_text.get_height()
        if current_line_length + rendered_width < wrap_width:
            line_count += 1 
            current_line_length += rendered_width 
        else:
            words_per_line.append(line_count) 
            line_count = 1 
            current_line_length = rendered_width
    words_per_line.append(line_count)

    start_index = 0
    line_index = 0
    for line in words_per_line:
        line_index += line
        line_words = ' '.join(words[start_index:start_index + line])
        rendered_text = font.render(line_words, False, text_color)
        display_surface.blit(rendered_text, (x_pos, y_pos))
        y_pos += heigth
        start_index = line_index


if __name__ == '__main__':
    pygame.init()
    MENU_COLOR = "Blue"
    MENU_SECONDARY_COLOR = "DarkBlue"
    MENU_TEXT_COLOR = "White"
    MENU_BORDER_COLOR = 'White'
    MENU_PADDING = 20
    MENU_BORDER_WIDTH = 3
    MENU_BORDER_RADIUS = 3
    screen = pygame.display.set_mode((500, 500))
    screen_w = screen.get_width()
    screen_h = screen.get_height()
    display_area = pygame.surface.Surface((300, 300))
    display_area.fill('Blue')
    display_area_rect = display_area.get_rect(center=(screen_w/2, screen_h/2))
    clock = pygame.time.Clock()

    def process_events():
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
        pygame.display.update()
        clock.tick(60)

    while True:
        screen.blit(display_area, display_area_rect)
        pygame.draw.rect(screen, MENU_BORDER_COLOR, display_area_rect,
                         MENU_BORDER_WIDTH, MENU_BORDER_RADIUS)
        text_string = 'Breaks the target and gains increased stats for 5 turns. Afterward, becomes sleepy and does zero damage for 56 turns. Then dies. Then gets reborn. Then dies again and that is all folks'
        test_width = 300 - 60
        x_pos = display_area_rect.left + MENU_PADDING
        font = pygame.font.Font('resources/fonts/Pixeltype/Pixeltype.ttf', 24)
        draw_text_wrap(text_string, font, test_width, x_pos, display_area_rect.top + MENU_PADDING, (255,0,255))

        process_events()
