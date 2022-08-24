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


def text_wrap(string: str, width: int, x_pos: int, y_pos: int, display_surface: pygame.Surface, text_size: int = 24):
    font = pygame.font.Font(
        'resources/fonts/Pixeltype/Pixeltype.ttf', text_size)
    words = string.split(' ')

    line_count = 0
    current_line_length = 0
    words_per_line = []
    for word in words:
        rendered_width = font.render(word, False, 'White')
        rendered_width = rendered_width.get_width()
        if current_line_length + rendered_width < width:
            line_count += 1
            current_line_length += rendered_width
        else:
            words_per_line.append(line_count)
            line_count = 0
            current_line_length = 0
    words_per_line.append(line_count)

    start_index = 0
    line_index = 0
    for line in words_per_line:
        line_index += line
        line_words = ' '.join(words[start_index:start_index + line])
        rendered_text = font.render(line_words, False, 'White')
        display_surface.blit(rendered_text, (x_pos, y_pos))
        y_pos += text_size
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
        test_width = 300 - (MENU_PADDING * 2)
        x_pos = display_area_rect.left + MENU_PADDING
        text_wrap(text_string, test_width,
                  x_pos, display_area_rect.top + MENU_PADDING, screen)

        process_events()
