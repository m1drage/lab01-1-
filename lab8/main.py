import pygame
import random
import sys
pygame.init()
class ThemeError(Exception):
    pass

class FactGenerator:
    def __init__(self):
        self.__themes = {
            "Кошки": [
                "Рисунок носа кошки индивидуален, как отпечаток пальца у человека.",
                "Кошки не чувствуют сладкого вкуса. ",
                "Древние египтяне брили брови в знак траура по кошке.",
                "Мозг кошки на 90% похож на человеческий.",
                "Чувствуют землетрясения за 10–15 минут до толчков."
            ],
            "Хомяки": [
                "Слышат ультразвук – общаются на частотах, недоступных человеческому уху.",
                "Рождаются сразу с зубами. ",
                "В Швейцарии запрещено держать одного хомяка – только парами, иначе штраф.",
                "Они близоруки и различают только оттенки серого и зеленого.",
                "Если хомячок родился слабым или больным – мать его съест."
            ],
            "Попугаи": [
                "У них почти нет вкусовых рецепторов – жуют всё подряд, даже острый перец.",
                "Попугаи спят, как летучие мыши – повисают вниз головой.",
                "Сердце бьется 300 раз в минуту.",
                "В средневековой Европе говорящих попугаев сжигали как ведьм.",
                "Африканский серый Жако знает до 1500 слов, понимает вопросы и даже шутит. "
            ],
            "Кролики": [
                "Узнают хозяина, откликаются на кличку и даже приносят мячик.",
                "Без сородичей впадают в депрессию, перестают есть и гибнут. ",
                "В Древнем Риме кроликов разводили только для меха и магических ритуалов.",
                "Могут грызть бетон и прыгать в длину на 3 метра",
                "Одна крольчиха может произвести до 800 потомков всего за 2 года."
            ],
            "Курицы": [
                "Чувствуют магнитное поле Земли.",
                "У кур более 30 звуковых сигналов для разных ситуаций.",
                "Различают ультрафиолет и оттенки, недоступные нашему глазу.",
                "Куры запоминают до 100 человеческих лиц и различают эмоции.",
                "Прямые потомки динозавров, их ДНК совпадает с древними ящерами на 60%."
            ]
        }
    
    def get_random_fact(self, theme):
        if theme not in self.__themes:
            raise ThemeError(f"Тема '{theme}' не найдена")
        return random.choice(self.__themes[theme])
    
    def get_themes(self):
        return list(self.__themes.keys())

class SimpleButton:
    def __init__(self, x, y, width, height, text, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.font = pygame.font.SysFont('Arial', 24)
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=10)
        pygame.draw.rect(surface, (0, 0, 0), self.rect, 2, border_radius=10)
        
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
    
    def is_clicked(self, pos, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(pos)
        return False

class FactApp:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Генератор фактов по выбранной теме")
        self.clock = pygame.time.Clock()
        self.running = True
        self.bg_color = (243, 234, 214)
        self.fact_generator = FactGenerator()
        self.current_fact = "Нажмите на кнопку темы, чтобы увидеть случайный факт"
        self.current_theme = None
        self.theme_buttons = []
        self.create_buttons()
        self.font = pygame.font.SysFont('Arial', 28)
        self.small_font = pygame.font.SysFont('Arial', 24)
    
    def create_buttons(self):
        themes = self.fact_generator.get_themes()
        button_width = 200
        button_height = 50
        start_y = 150
        spacing = 20
        
        colors = [
            (246, 182, 167),  
            (210, 201, 138),  
            (246, 182, 167),   
            (210, 201, 138),  
            (246, 182, 167)   
        ]
        
        for i, theme in enumerate(themes):
            y = start_y + i * (button_height + spacing)
            button = SimpleButton(
                self.screen_width // 2 - button_width // 2,
                y,
                button_width,
                button_height,
                theme,
                colors[i % len(colors)]  
            )
            self.theme_buttons.append(button)
    
    def handle_events(self):
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            for button in self.theme_buttons:
                if button.is_clicked(mouse_pos, event):
                    try:
                        self.current_fact = self.fact_generator.get_random_fact(button.text)
                        self.current_theme = button.text
                    except ThemeError as e:
                        self.current_fact = f"Ошибка: {str(e)}"
                        self.current_theme = None
    
    def draw(self):
        self.screen.fill(self.bg_color) 
        # заголовок
        title = self.font.render("Генератор фактов по выбранной тематике", True, (166, 109, 69))
        title_rect = title.get_rect(center=(self.screen_width // 2, 50))
        self.screen.blit(title, title_rect)
         # тема
        if self.current_theme:
            theme_text = self.small_font.render(f"Тема: {self.current_theme}", True, (167, 161, 85))
            theme_rect = theme_text.get_rect(center=(self.screen_width // 2, 100))
            self.screen.blit(theme_text, theme_rect)
        
        # Кнопки
        for button in self.theme_buttons:
            button.draw(self.screen)
        
        # Факт 
        fact_y = 150 + len(self.theme_buttons) * (50 + 20) + 50
        fact_text = self.small_font.render(self.current_fact, True, (166, 109, 69))
        self.screen.blit(fact_text, (50, fact_y))
        
        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    app = FactApp()
    app.run()