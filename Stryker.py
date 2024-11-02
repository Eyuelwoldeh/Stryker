import random

x = mouse_x
y = mouse_y

missiles = []
cars = []

a = random.randint(-200, 100)
b = 350


class Car:
    
    def __init__(self, x, y):
        
        self.x = x
        self.y = y
        self.width = 80
        self.height = 40
        self.body_color = color(255, 69, 0)  
        self.window_color = color(30, 144, 255)  
        self.wheel_color = color(0) 
    
    def display(self):
        
        fill(self.body_color)
        stroke(255)
        self.x += 2
        
        if self.x > 800:
            self.x = 0
        
        rect(self.x, self.y, self.width, self.height, 10)
        
        fill(self.wheel_color)
        ellipse(self.x + 20, self.y + self.height, 20, 20)
        ellipse(self.x + self.width - 20, self.y + self.height, 20, 20)

        push()
        no_fill()
        rect(self.x - 5, self.y - 5, self.width + 5, self.height + 10, 10)
        pop()


class Missile:
    
    def __init__(self, x, y):
        
        self.x = x
        self.y = y  
        self.width = 15
        self.height = 30
        self.color = color(255, 0, 0)
        self.warhead_radius = 5
        self.flame_length = 20

    def display(self):
        
        fill(255, 165, 0)
        for i in range(3):
            triangle(self.x - 5 - i * 5, self.y + self.height + 5,
                     self.x + self.width / 2, self.y + self.height + self.flame_length,
                     self.x + self.width + 5 + i * 5, self.y + self.height + 5)

        fill(self.color)
        rect(self.x, self.y, self.width, self.height)
        fill(100)
        triangle(self.x - 5, self.y,
                 self.x + self.width / 2, self.y - 15,
                 self.x + self.width + 5, self.y)


def restart():
    
    for i in range(4):
        random_factor = random.uniform(0.5, 2.0)
        x_position = a * (i / random_factor)
        cars.append(Car(x_position, b - i * 100))


def setup():
    
    size(800, 800)

def draw():
    
    global count
    
    img = load_image("Background1.jpg") # Goolge Coding ad on
    
    background(img)
    
    push()
    
    fill(255)
    
    line(0, 500, 800, 500)
    
    pop()
    
    push()
    
    fill(128, 128, 0)
    
    rect(mouse_x - 15, mouse_y - 30, 30, 70)
    
    fill(1, 50, 32)
    
    rect(mouse_x - 18, mouse_y - 32, 36, 5)
    
    quad(mouse_x - 18, mouse_y + 35, mouse_x + 18, mouse_y + 35, mouse_x + 24, mouse_y + 50,  mouse_x - 24, mouse_y + 50)
    
    pop()
    

    for car in cars:
        car.display() 

    for missile in missiles:
        missile.display()
        missile.y -= 5  

        for car in cars:
            if (
                missile.x >= (car.x - 5)
                and missile.x <= (car.x + 150)
                and missile.y <= (car.y + 80)
                and missile.y >= (car.y - 10)
            ):
                missiles.remove(missile)
                cars.remove(car)
                break

        if missile.y < 0:
            missiles.remove(missile)
    
    if len(cars) == 0:
        
        game_over_message()
    
    if mouse_y < 500:
        game_lost_message()

def game_lost_message():
   
    background(200, 150, 0)
    text_size(50)
    fill(0, 102, 153, 204)
    text("Out of bounds!", 250, 400)

def game_over_message(): # Stack overflow
    
    background(200, 150, 0)
    text_size(50)
    fill(0, 102, 153, 204)
    text("YOU WON!", 300, 400) # Classroom PRIM slides
    fill(0, 255, 0)
    rect(300, 650, 200, 50, 10)
    fill(0)
    text_size(20)
    text("Restart", 370, 680)

def mouse_pressed():
    
    missile = Missile(mouse_x - 8, (mouse_y - 70)) # Py5 coding website
    missiles.append(missile)
    if len(cars) == 0:
        if 300 <= mouse_x <= 500 and 650 <= mouse_y <= 700:
            restart()
