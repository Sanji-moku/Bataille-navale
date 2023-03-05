from settings import *

class SHIP:
    """
    Classe Ship regroupe tout ce qui concerne les navires du jeu et notamment leur emplacement de manière aléatoire
    
    Attributs
    ----------

    size : int
        taille du bateau 
    name : str 
        nom du bateau
    destroyed : booleen 
        état du bateau (Coulé ou non)

    Methodes
    -------
    randomize_position
        Positionne de manière aléatoire le bateau sur le plateau de jeu en fonction de certains critères
    check_empty_horizontal_cells
        Vérifie si les cellules sont libres pour positionner le navire horizontalement
    check_empty_vertical_cells
        Vérifie si les cellules sont libres pour positionner le navire verticalement
    check_contact_cell
        Vérifie que le navire ne soit pas en contact avec un autre

    """

    def __init__(self, size, name):
        self.size = size
        self.name = name
        self.destroyed = False
    
    def randomize_position(self):
        """
        Positionne le navire de manière aléatoire sur la plateau de jeu.
        """
        horizontal = random.choice([True, False])
        if horizontal:
            
            # Check si les cellules sont libres pour placer le navire horizontalement
            result = self.check_empty_horizontal_cells()

            # Tant que les cellules aléaoirement choisies sont déjà utilisées, on relance.
            while(not result[0]):
                result = self.check_empty_horizontal_cells()

            # Les cellules sont libres, donc on peut les notifier dans la grille
            for i in range(self.size):
                    grid[result[1]][result[2] + i] = 1
        else:
            # Check si les cellules sont libres pour placer le navire verticalement
            result = self.check_empty_vertical_cells()

            # Tant que les cellules aléaoirement choisies sont déjà utilisées, on relance.
            while(not result[0]):
                result = self.check_empty_vertical_cells()

            # Les cellules sont libres, on peut donc les notifier dans la grille de jeu
            for i in range(self.size):
                    grid[result[1] + i][result[2]] = 1


    def check_empty_horizontal_cells(self):
        """
        Vérifies si les cellules contigus aléaoirement choisies et horizontalement sont libres
        """

        #
        random_x = random.randint(0,CELL_NUMBER - 1)
        if self.size > 1:
            random_y = random.randint(0,(CELL_NUMBER - 1) - (self.size - 1))
        else:
            random_y = random.randint(0,(CELL_NUMBER - 1) - self.size)

        for col in grid[random_x][random_y : random_y + self.size]:
            # Si la case est occupée
            if col != 0:
                return [False]
        
        
        # Stock les positions du navire sous forme de liste à position [ [posx, posy], ... , ... ]
        positions = list()
        for i in range(self.size):
            positions.append([random_x,random_y + i])
        
        # Les cellules sont libres, on vérifie maintenant si elles sont au contact d'autres navires

        if not self.check_contact_cell(positions):
            return [False]

        # Cellules libres et aucun contacts contact => OK
        return [True, random_x, random_y]

    def check_empty_vertical_cells(self):
        """
        Vérifie si les cellules contigus aléaoirement choisies et verticalement sont libres
        """
        random_y = random.randint(0, CELL_NUMBER - 1)
        if self.size > 1:
            random_x = random.randint(0,(CELL_NUMBER - 1) - (self.size - 1))
        else:
            random_x = random.randint(0,(CELL_NUMBER - 1) - self.size)
        
        for row in grid[random_x: random_x + self.size]:
            if row[random_y] != 0:
                return [False]
        
        # Les cellules sont libres, on vérifie maintenant si elles sont au contact d'autres navires
        positions = list()
        for i in range(self.size):
            positions.append([random_x + i,random_y])
        
        if not self.check_contact_cell(positions):
            return [False]

        # Les cellules sont libres et aucun autres navires n'est au contact => OK 
        return [True, random_x, random_y]
    
    def check_contact_cell(self, positions):
        """
        Vérifie si les cellules ne sont pas au contact d'un autre navire (diagonales incluses)
        """
        for pos in positions:
            # Cellules de dessus
            higher_row = 0 if pos[0] == 0 else pos[0] - 1
            # Cellules du dessous
            lower_row = 9 if pos[0] == 9 else pos[0] + 1

            # Si la cellule est dans la 1ère colonne
            if pos[1] == 0:
                if grid[higher_row][0] != 0 or grid[higher_row][1] != 0:
                    return False
                if grid[pos[0]][1] != 0:
                    return False
                if grid[lower_row][0] != 0 or grid[lower_row][1] != 0:
                    return False
                
            # Si la cellule est dans la dernière colonne
            elif pos[1] == 9:
                if grid[higher_row][8] != 0 or grid[higher_row][9] != 0:
                    return False
                if grid[pos[0]][8] != 0:
                    return False
                if grid[lower_row][8] != 0 or grid[lower_row] != 0:
                    return False
            
            # Si la cellule est sur l'une des autres colonnes
            else:
                if grid[higher_row][pos[1] - 1] != 0 or grid[higher_row][pos[1]] != 0 or grid[higher_row][pos[1] + 1] != 0:
                    return False
                if grid[pos[0]][pos[1] - 1] != 0 or grid[pos[0]][pos[1] + 1] != 0:
                    return False
                if grid[lower_row][pos[1] - 1] != 0 or grid[lower_row][pos[1]] != 0 or grid[lower_row][pos[1] + 1] != 0:
                    return False
        
        # Si aucun navire n'est autour des cellules, on retourne True
        return True 