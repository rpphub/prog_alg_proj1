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

    while(True):
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

      # Vonalakat rajzolunk a spirál mentén a cellák éleihez igazítva
      for i in range(len(path) - 1):
          r0, c0 = path[i]
          r1, c1 = path[i + 1]

          # Cellák élszélei spirál mentén: a négyzetháló vonalaihoz illeszkednek
          if r1 == r0:
              if c1 > c0:  # jobbra
                  x_start, y_start = c0, size - r0
                  x_end, y_end = c1 - 1, size - r1 +1
                  x_start, y_start = c0, size - r1
                  x_end, y_end = c1 + 1, size - r1
              else:  # balra
                  x_start, y_start = c0 - 1, size - r0
                  x_end, y_end = c1 - 1, size - r1
          else:
              if r1 > r0:  # le
                  x_start, y_start = c1, size - r0
                  x_end, y_end = c0, size - r1
                  x_start, y_start = c1 + 1, size - r0 + 2
                  x_end, y_end = c1 + 1, size - r1 + 2
              else:  # fel
                  x_start, y_start = c0, size - r0
                  x_end, y_end = c1, size - r1
                  x_start, y_start = c0, size - r0 
                  x_end, y_end = c1, size - r1

          ax.plot([x_start, x_end], [y_start, y_end], color='red', linewidth=5)

      ax.set_xlim(0, size)
      ax.set_ylim(0, size)
      ax.set_aspect('equal')
      plt.tight_layout()
      plt.show()


#Matrix létrehozás / feltőltés
Matrix = matrix(6,6)
Matrix.fill_with_test_data_circle()
Matrix.display()

#Plototolt megjelenítés.
spiral_path = Matrix.generate_edge_spiral_path(6)
Matrix.plot_spiral_path(spiral_path)
  