import matplotlib.pyplot as plt

class matrix:
  def __init__(self,w,h):
    self.matrix = [[0 for x in range(w)] for y in range(h)]
    self.w = w
    self.h = h
    self.len = w * h
    self.number = 2

  def fill_with_test_data(self):
    index = 0
    for y in range(self.h):
      for x in range(self.w):
       self.matrix[y][x] = index
       index = index + 1

    
  def get_number(self):
    return  self.number

  def inc_number(self):
    self.number = self.number % 3 + 1

  def data_is_exist(self, xAct, yAct, data):
    for y in range(self.h): #Sorok ellenörzése
      if(self.matrix[y][xAct] == data):
        return True

    for x in range(self.w): #Oszlopok ellenörzése
      if(self.matrix[yAct][x] == data):
        return True
    
    return False



  def fill_with_test_data_circle(self):
    index = 0
    y,x = 0,0
    yF,xF = 0,0
    xF = 1
    xActual = self.w
    yActual = self.h
    path = []

    while(True):
      path.append((y, x))
      if(self.data_is_exist(x,y,self.get_number()) == False): 
        self.matrix[y][x] = self.get_number()
        self.inc_number()


      if(xF == 1): #Jobbra halad
        if(x == xActual - 1): #Lefele Fordul
          xF = 0
          yF = 1
      
      if(yF == 1): #Lefele halad
        if(y == yActual - 1): #Balra..
          yF = 0
          xF = -1

      if(xF == -1): #Balra halad
        if(x == self.w - xActual): #Fel..
          yF = -1
          xF = 0

          if(yActual > 0):
            yActual = yActual -1
          else:
            print("yActual elfogyott")
            break

          if(xActual > 0):
            xActual = xActual - 1 
          else:
            print("xActual elfogyott")
            break

      if(yF == -1): #Felfele halad
        if(y == self.h - yActual): #Jobbra..
          yF = 0
          xF = 1

      x = x + xF
      y = y + yF

      if(y == self.h - yActual and x == self.w - xActual and (x == xActual or y == yActual)):
        print("Finish")
        break

    return path 

  def display(self):
    for y in range(self.h):
      for x in range(self.w):
        print(f"{self.matrix[y][x]:02} ", end="")
      print("")

    # Spiral path generator
  def generate_edge_spiral_path(self, n: int):
      path = []
      top, bottom, left, right = 0, n - 1, 0, n - 1
      while top <= bottom and left <= right:
          for j in range(left, right + 1):
              path.append((top, j))
          top += 1
          for i in range(top, bottom + 1):
              path.append((i, right))
          right -= 1
          if top <= bottom:
              for j in range(right, left - 1, -1):
                  path.append((bottom, j))
              bottom -= 1
          if left <= right:
              for i in range(bottom, top - 1, -1):
                  path.append((i, left))
              left += 1
      return path

  def plot_spiral_path(self, path):
    size = len(self.matrix)
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xticks([])
    ax.set_yticks([])

    # Alaprács
    for i in range(size + 1):
        ax.plot([0, size], [i, i], color='black', linewidth=1)
        ax.plot([i, i], [0, size], color='black', linewidth=1)

    # Számok beírása
    for i in range(size):
        for j in range(size):
            val = self.matrix[i][j]
            if val != 0:
                ax.text(j + 0.5, size - i - 0.5, str(val),
                        ha='center', va='center', fontsize=16)

    # új megközelítés: a spirálvonal mentén a cellák éleihez igazítva
    hDir = 1
    vDir = 0
    for i in range(len(path) - 1):
        r1, c1 = path[i]
        r2, c2 = path[i + 1]

        print(f"r1:{r1} c1:{c1} - hDir:{hDir} vDir:{vDir}")

        if hDir == 1:  # #vizszintes vonal
            y = size - r1 
            if c2 > c1:  # jobbra
                x1, x2 = c1, c2
            elif c2 == c1:  # jobbra
                x1, x2 = c1, c2
            else:  # balra
                x1, x2 = c2, c1 + 1
                x1, x2 = c2 + 1, c1 + 1
            ax.plot([x1, x2], [y, y], color='red', linewidth=3)

        elif c1 == c2:  # függőleges vonal
            x = c1 + 1
            if r2 > r1:  # lefele
                y1, y2 = size - r1 ,size - r2
            else:  # felfel
                y1, y2 = size - r2 - 1, size - r1 + 1
                y1, y2 = size - r2, size - r1
            ax.plot([x, x], [y1, y2], color='red', linewidth=3)
    hDir = c2 - c1
    vDir = r2 - r1

    ax.set_xlim(0, size)
    ax.set_ylim(0, size)
    ax.set_aspect('equal')
    plt.tight_layout()
    plt.show()

#Matrix létrehozás / feltőltés
Matrix = matrix(6,6)
spiral_path = Matrix.fill_with_test_data_circle()
Matrix.display()

#Plototolt megjelenítés.
Matrix.plot_spiral_path(spiral_path)
  