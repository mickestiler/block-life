from wall import Wall

class GameMap:
    def __init__(self):
        self.walls = [
            Wall(50, 100, breakable=True),
            Wall(200, 150, breakable=True),
            Wall(300, 300, breakable=False),
            # Add more walls as needed
        ]

    def draw(self, win):
        for wall in self.walls:
            wall.draw(win)

    def update(self, player):
        walls_to_keep = []
        for wall in self.walls:
            if not wall.is_collision(player.rect) or (wall.is_collision(player.rect) and not wall.breakable):
                walls_to_keep.append(wall)

        self.walls = walls_to_keep
