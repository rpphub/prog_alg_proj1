class matrix:
  def __init__(self,w,h):
    self.matrix = [[0 for x in range(w)] for y in range(h)]
    self.w = w
    self.h = h
    self.len = w * h

  def fill_with_test_data(self):
    index = 0
    for y in range(self.h):
      for x in range(self.w):
       self.matrix[y][x] = index
       index = index + 1

  #def build_data(self)
    

  def fill_with_test_data_circle(self):
    index = 0
    y,x = 0,0
    yF,xF = 0,0
    xF = 1
    xActual = self.w
    yActual = self.h

    while(True):

      if(index <= 35):
        print(f"index:{index} yActual:{yActual}({self.h}) - xActual:{xActual}({self.w}) - x:{x} - y:{y} xF:{xF} - yF:{yF} sor:{xActual - y} osz:{yActual - y}")
  
        self.matrix[y][x] = index
        index = index + 1
      else:
        print(f"Hiba:x:{x}y:{y}")
        break

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

Matrix = matrix(6,6)
Matrix.fill_with_test_data_circle()
Matrix.display()
#