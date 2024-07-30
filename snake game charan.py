import pygame
import random

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.width, self.height = 600, 400
        self.game_screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")
        
        self.snake_x, self.snake_y = self.width / 2, self.height / 2
        self.change_x, self.change_y = 0, 0
        self.food_pos = [random.randrange(0, self.width) // 10 * 10, random.randrange(0, self.height) // 10 * 10]
        self.clock = pygame.time.Clock()
        self.snake_body = [[self.snake_x, self.snake_y]]
        self.game_over = False
        self.score = 0  # Initialize score

    def display_snake_and_food(self):
        self.snake_x += self.change_x
        self.snake_y += self.change_y

        # Check if the snake collides with itself
        if [self.snake_x, self.snake_y] in self.snake_body[1:]:
            self.game_over = True
            return

        # Check if the snake hits the borders (x-axis and y-axis)
        if self.snake_x < 0 or self.snake_x >= self.width or self.snake_y < 0 or self.snake_y >= self.height:
            self.game_over = True
            return

        self.snake_body.append([self.snake_x, self.snake_y])

        if self.food_pos == [self.snake_x, self.snake_y]:
            self.food_pos = [random.randrange(0, self.width) // 10 * 10, random.randrange(0, self.height) // 10 * 10]
            self.score += 1  # Increment score when food is eaten
        else:
            del self.snake_body[0]

        self.game_screen.fill((0, 0, 0))
        pygame.draw.rect(self.game_screen, (0, 255, 0), [self.food_pos[0], self.food_pos[1], 10, 10])
        for segment in self.snake_body:
            pygame.draw.rect(self.game_screen, (255, 255, 255), [segment[0], segment[1], 10, 10])
        
        # Display the score
        self.display_score()

        pygame.display.update()

    def display_score(self):
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.game_screen.blit(score_text, (10, 10))  # Position the score at the top left

    def show_game_over(self):
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over!", True, (255, 0, 0))
        text_rect = text.get_rect(center=(self.width/2, self.height/2))
        self.game_screen.blit(text, text_rect)
        self.display_score()  # Display score on game over screen
        pygame.display.update()
        pygame.time.delay(2000)  # Delay to show the message for 2 seconds
        pygame.quit()  # Quit the game after showing the message
        quit()

    def run(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN and not self.game_over:
                    if event.key == pygame.K_LEFT:
                        self.change_x = -10
                        self.change_y = 0
                    elif event.key == pygame.K_RIGHT:
                        self.change_x = 10
                        self.change_y = 0
                    elif event.key == pygame.K_UP:
                        self.change_x = 0
                        self.change_y = -10
                    elif event.key == pygame.K_DOWN:
                        self.change_x = 0
                        self.change_y = 10

            if not self.game_over:
                self.display_snake_and_food()
            else:
                self.show_game_over()

            self.clock.tick(15)

if __name__ == "__main__":
    game = SnakeGame()
    game.run()