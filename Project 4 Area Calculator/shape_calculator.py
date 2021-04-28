class Rectangle:
  width = 0
  height = 0
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    dimensions = "width="+str(self.width)+", height="+str(self.height)
    return("Rectangle("+dimensions+")")
  
  def set_width(self, amount):
    self.width = amount
  
  def set_height(self, amount):
    self.height = amount

  def get_area(self):
    area = self.width * self.height
    return(area)
  
  def get_perimeter(self):
    perimeter = 2 * self.width + 2 * self.height
    return(perimeter)

  def get_diagonal(self):
    diagonal = (self.width * self.width + self.height * self.height) ** .5
    return(diagonal)
  
  def get_picture(self):
    output = ""
    if (max(self.width, self.height) > 50):
      return("Too big for picture.")
    else:
      for i in range(self.height):
        for j in range(self.width):
          output += "*"
          j += 1
        output += "\n"
        i += 1
      return(output)

  def get_amount_inside(self, obj):
    if (obj.get_area() > self.get_area()):
      return 0
    elif (obj.get_area() == self.get_area()):
      return 1
    else:
      num = int(self.get_area() / obj.get_area())
      return (num)



class Square(Rectangle):
  def __init__(self, width):
    self.height = width
    self.width = width

  def __str__(self):
    dimensions = "side="+str(self.width)
    return ("Square("+dimensions+")")

  def set_side(self, amount):
    self.height = amount
    self.width = amount
  
  def set_width(self, amount):
    self.set_side(amount)

  def set_height(self, amount):
    self.set_side(amount)
