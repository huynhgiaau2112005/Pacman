from Config import Config
import pygame

BoxWidth = 400
BoxHeight = 220

boxX = (Config.width - BoxWidth) / 2
boxY = 100

ButtonWidth = (BoxWidth - 6 * 10) / 5
ButtonHeight = 30
ButtonX = boxX + 10
ButtonY = boxY + 22 + 160

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 32)

class ExperimentBox:
    def showResultBoard(self, algorithm, search_time, memory_usage , num_expanded_nodes):
        pygame.draw.rect(Config.screen, (255, 153, 51), (boxX, boxY, BoxWidth, BoxHeight), border_radius=15)

        algorithm_text = font.render(f"Algorithm: {algorithm}", True, BLACK)
        search_time_text = font.render(f"Search time: {search_time:.6f} seconds", True, BLACK)
        memory_usage_text = font.render(f"Memory usage: {memory_usage:.6f} MB", True, BLACK)
        num_expanded_nodes_text = font.render(f"Number of expanded nodes : {num_expanded_nodes}", True, BLACK)
        pick_testcase_text = font.render("Pick next testcase", True, BLACK)
            
        Config.screen.blit(algorithm_text, (boxX + 24, boxY + 22))
        Config.screen.blit(search_time_text, (boxX + 24, boxY + 22 + 30))
        Config.screen.blit(memory_usage_text, (boxX + 24, boxY + 22 + 60))
        Config.screen.blit(num_expanded_nodes_text, (boxX + 24, boxY + 22 + 90))
        pygame.draw.line(Config.screen, (0, 0, 0), (boxX + 24, boxY + 22 + 120), (boxX + BoxWidth - 24, boxY + 22 + 120), 2)
        Config.screen.blit(pick_testcase_text, (boxX + 100, boxY + 22 + 130))

        mouse_x, mouse_y = pygame.mouse.get_pos()

        for i in range(5):
            button_x = ButtonX + i * (10 + ButtonWidth)
            button_y = ButtonY
            button_color = 'WHITE'

            if button_x <= mouse_x <= button_x + ButtonWidth and button_y <= mouse_y <= button_y + ButtonHeight:
                button_color = (144, 238, 144) # Màu xanh lục nhạt
            
            pygame.draw.rect(Config.screen, 'BLACK', (button_x - 2, button_y - 2, ButtonWidth + 4, ButtonHeight + 4), border_radius=15)
            pygame.draw.rect(Config.screen, button_color, (button_x, button_y, ButtonWidth, ButtonHeight), border_radius=15)
            
            id = font.render(f"{i + 1}", True, BLACK)
            Config.screen.blit(id, (ButtonX + i * (10 + ButtonWidth) + ButtonWidth / 2 - 6, ButtonY + 5))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Config.running = False
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return -1 # quit level signal
                if event.key == pygame.K_q:
                    Config.running = False
                    return -1 # quit level ssignal
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # 1 là chuột trái
                print("Chuột trái được nhấn!")
                for i in range(5):
                    button_x = ButtonX + i * (10 + ButtonWidth)
                    button_y = ButtonY
                    if button_x <= mouse_x <= button_x + ButtonWidth and button_y <= mouse_y <= button_y + ButtonHeight:
                        return i
        
        return None
