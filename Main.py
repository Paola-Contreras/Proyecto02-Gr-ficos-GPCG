from gl import Raytracer, V3
from texture import *
from figures import *
from lights import *


width = 740
height = 520

# Materiales
floor  = Material(diffuse = (0.33, 0.36, 0.44), spec = 64)
grey_white = Material(diffuse = (0.57, 0.59, 0.63), spec = 64)
mirror = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, matType = REFLECTIVE)
light_grey = Material(diffuse = (0.49, 0.50, 0.55), spec = 16, matType = OPAQUE)
marble = Material(spec = 64, texture = Texture("marble.bmp"), matType= REFLECTIVE)
glass = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, ior = 1.5, matType = TRANSPARENT)


#Try
marble1 = Material(spec = 64, texture = Texture("H.bmp"))
irror = Material(diffuse = (0.3, 0.3, 0.3), spec = 64, matType = REFLECTIVE)



#Renderer & map 
rtx = Raytracer(width, height)
rtx.envMap = Texture("env map.bmp")

rtx.lights.append( AmbientLight(intensity = 0.1 ))
rtx.lights.append( DirectionalLight(direction = (-1,-1,-1), intensity = 0.5 ))
rtx.lights.append( PointLight(point = (1,1,0) ))

#Shapes 
rtx.scene.append( Sphere((0.4,-1.5,-6),0.54, marble))
rtx.scene.append( Sphere((-1.7,0.08,-6.7),1.3, glass))
rtx.scene.append( Sphere((1.5,0.3,-7),0.9, light_grey))
rtx.scene.append( Sphere((3.3,-1.2,-5.8), 0.8 , mirror))
rtx.scene.append( Torus3D((-3.08,-1.3,-5),0.75, 0.29, marble1 ))

rtx.scene.append( AABB(position = (-1.8,-2.3,-7), size = (2,2,2), material = grey_white))
rtx.scene.append( Disk(position = (0,-2,-7), radius = 7, normal = (0,1,0), material = floor))
rtx.scene.append( AABB(position = (1.4,-1.35,-7), size = (1.5,1.5,1.5), material = grey_white))

#rtx.scene.append( Torus2D(position = (1,-1,-7), radius = 1, radius2 =0.3, normal = (0,0,1), material = glass ))
#rtx.scene.append( Torus2D(position = (1,2,-7), radius = 1.5, radius2 =0.6, normal = (0,0,1), material = mirror ))


rtx.glRender()

rtx.glFinish("output.bmp")