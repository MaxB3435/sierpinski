def setup():
    size(600,600)
    
def draw():
    background(255)
    translate(50,450)
    sierpinski(400,0)
    
def sierpinski(sz, level):
    if level == 0:
        fill(0)
        triangle(0,0,sz,0,sz/2.0,-sz*sqrt(3)/2.0)
