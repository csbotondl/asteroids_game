from circleshape import *
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED,PLAYER_SHOOT_COOLDOWN_SECONDS
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen: pygame.Surface):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt: float) -> None:
        self.rotation += dt * PLAYER_TURN_SPEED

    def move(self, dt: float) -> None:
        self.position += pygame.Vector2(0,1).rotate(self.rotation)*PLAYER_SPEED*dt
    def shoot(self) -> None:
        bullet = Shot(self.position.x, self.position.y)
        bullet.velocity = pygame.Vector2(0,1).rotate(self.rotation)*PLAYER_SHOOT_SPEED


    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        self.cooldown -= dt
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if (self.cooldown > 0):
                pass
            else:
                self.cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
                self.shoot()
