from settings import *
from ship import SHIP

class GAME:
    """
    Classe Game qui regroupe tout ce qui concerne l'affichage du jeu et les interactions.
    Permet d'initialiser une nouvelle partie gère les évenements utilisateurs.
    
    Attributs
    ----------

    screen : Surface object 
        affichage de l'écran de jeu 
    clock : Clock object 
        controle la génération des framesrates du jeu
    game_font : Font object 
        police d'écriture pour l'affichage des textes
    ship : Ship object
        représentation d'un objet de type bateau

    Methodes
    -------
    run
        Lance le jeu après initialisation et récupère les évenements utilisateurs en continu
        Met à jour l'écran de jeu en fonction des modifications sur le plateau de jeu
    draw_grid_and_ship
        Affiche les cellules du plateau de jeu en fonction de s'il y a un navire (touché ou non)
    check_tir
        Check si le tir de l'utilisateur a touché une cible ou non.


    """
    def __init__(self):

        # Initialisation de l'écran de jeu
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((SCREEN_SIZE,SCREEN_SIZE))
        
        # Configurations
        pygame.display.set_caption("Jeu de la bataille navale")
        self.screen.fill(BACKGROUND)
        self.clock = pygame.time.Clock()
        self.game_font = pygame.font.Font(FONT,20)

        # Création des bateaux
        ship1 = SHIP(size = 4, name = "Croiseur")
        ship2 = SHIP(size = 3, name = "Escorteur")
        ship3 = SHIP(size = 3, name = "Escorteur")
        ship4 = SHIP(size = 2, name = "Torpilleur")
        ship5 = SHIP(size = 2, name = "Torpilleur")
        ship6 = SHIP(size = 2, name = "Torpilleur")
        ship7 = SHIP(size = 1, name = "Sous-marin")
        ship8 = SHIP(size = 1, name = "Sous-marin")
        ship9 = SHIP(size = 1, name = "Sous-marin")
        ship10 = SHIP(size = 1, name = "Sous-marin")

        # Placement aléatoire des bateaux
        ship1.randomize_position()
        ship2.randomize_position()
        ship3.randomize_position()
        ship4.randomize_position()
        ship5.randomize_position()
        ship6.randomize_position()
        ship7.randomize_position()
        ship8.randomize_position()
        ship9.randomize_position()
        ship10.randomize_position()

        # Affichage de la grille
        self.draw_grid_and_ship()
        
    def run(self):
        """
        Le jeu tourne sans arrêt tant que l'utilisateur ne ferme pas le jeu.
        Récupère les évenements utilisateurs tel que le clique de la souris sur une case du jeu.
        """
        running = True
        while running:
            # Check les évenements utilisateurs
            for event in pygame.event.get():
                        # Si l'utilisateur clique sur la croix, le jeu se ferme
                        if event.type == pygame.QUIT:
                            running = False
                        # Si l'utilisateur clique dans une case, on vérifie une cible est touchée
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            pos_mouse = pygame.mouse.get_pos()
                            pos_y = pos_mouse[0] // (CELL_SIZE + BORDER)
                            pos_x = pos_mouse[1] // (CELL_SIZE + BORDER)

                            # Check si cible touchée
                            self.check_tir(pos_x,pos_y)
            
            # Update de la grille tant que le jeu tourne
            self.draw_grid_and_ship()
            
            # Met à jour l'écran
            pygame.display.flip()
            self.clock.tick(60)
        
        # Quitte le jeu
        pygame.quit()
        sys.exit()
    
    def draw_grid_and_ship(self):
        """
        Affiche les cellules en fonction de si la cellule contient un navire et qui est touché ou non.
        """

        # Lecture case par case
        for row in range(CELL_NUMBER):
            for column in range(CELL_NUMBER):

                # Case jamais touchée (intacte)
                if grid[row][column] == 0 or grid[row][column] == 1:
                    # Liste alphabétique qui sera affiché sur l'écran de jeu.
                    lettres = list(string.ascii_uppercase)
                    board_lettres = [[lettres[i]+str(j+1)for i in range(CELL_NUMBER)] for j in range(CELL_NUMBER)]

                    self.draw_case(row, column, BLACK)
                    text = self.game_font.render(board_lettres[row][column],True, WHITE)
                    self.screen.blit(text,((BORDER + CELL_SIZE) * column + 2* BORDER,(BORDER + CELL_SIZE) * row + 1.5* BORDER))

                # Navire touché
                elif grid[row][column] == 2:
                    self.draw_case(row, column, RED)
                    self.draw_cross(row, column)
                # Cible raté
                elif grid[row][column] == 4:
                    self.draw_case(row, column, BLACK)
                    self.draw_cross(row, column)


    def draw_cross(self, row, column):
        """
        Affichage d'une croix qui indique que le joueur a (déjà) tiré sur cette case
        """
        pygame.draw.line(self.screen, 
                                    BACKGROUND, 
                                    ((BORDER + CELL_SIZE) * column + BORDER, (BORDER + CELL_SIZE) * row + BORDER), 
                                    ((BORDER + CELL_SIZE) * column + BORDER + CELL_SIZE, (BORDER + CELL_SIZE) * row + BORDER + CELL_SIZE),
                                    6)
                    
        pygame.draw.line(self.screen, 
                                    BACKGROUND,
                                    ((BORDER + CELL_SIZE) * column + BORDER, (BORDER + CELL_SIZE) * row + BORDER + CELL_SIZE), 
                                    ((BORDER + CELL_SIZE) * column + BORDER + CELL_SIZE, (BORDER + CELL_SIZE) * row + BORDER), 
                                    6)
    
    def draw_case(self, row, column, color):
        """
        Affiche la cellule en fonction de si un navire a été touchée (ROUGE) ou non (NOIR)
        """
        pygame.draw.rect(self.screen, 
                                    color,
                                    [(BORDER + CELL_SIZE) * column + BORDER, 
                                    (BORDER + CELL_SIZE) * row + BORDER, 
                                    CELL_SIZE,
                                    CELL_SIZE])

    def check_tir(self, x, y):
        """
        Check si le tir effectué par l'utilisateur a touché un navire ou non et met à jour la grille en conséquence.
        """
        # Touché
        if grid[x][y] == 1:
            grid[x][y] = 2
        # Tir raté
        elif grid[x][y] == 0:
            grid[x][y] = 4