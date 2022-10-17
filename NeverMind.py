from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from numpy import floor
from perlin_noise import PerlinNoise 

app = Ursina()

window.color = color.rgb(0,200,211)
window.exit_button.visible = False

GrassTex = load_texture('dirt_moss_top.png')

def input(key):
    if key == 'q' or key == 'escape':
        quit()
 
def update():
    pass

terrain = Entity(model=None,collider=None)
noise = PerlinNoise(octaves=1,seed=2021)
amp = 3
freq = 12

terrainWidth = 32
for i in range(terrainWidth*terrainWidth):
    bud = Entity(model='cube',color=color.green)
    bud.x = floor(i/terrainWidth)
    bud.z = floor(i%terrainWidth)
    bud.y = floor((noise([bud.x/freq,bud.z/freq]))*amp)
    bud.parent = terrain

terrain.combine()
terrain.collider = 'mesh'
terrain.texture = GrassTex

subject = FirstPersonController()
subject.x = subject.z = 6
subject.y = 12

app.run()