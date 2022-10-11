from gl import Raytracer, V3
from texture import *
from figures import *
from lights import *


width = 740
height = 520

# Materiales

brick = Material(diffuse = (0.49, 0.50, 0.55), spec = 16, matType = OPAQUE)
stone = Material(diffuse = (0.33, 0.36, 0.44), spec = 64)
grass = Material(diffuse = (0.57, 0.59, 0.63), spec = 64)


marble = Material(spec = 64, texture = Texture("marble.bmp"), matType= REFLECTIVE)

mirror = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, matType = REFLECTIVE)
glass = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, ior = 1.5, matType = TRANSPARENT)

rtx = Raytracer(width, height)

rtx.envMap = Texture("env map.bmp")

rtx.lights.append( AmbientLight(intensity = 0.1 ))
rtx.lights.append( DirectionalLight(direction = (-1,-1,-1), intensity = 0.5 ))
rtx.lights.append( PointLight(point = (1,1,0) ))


rtx.scene.append( Disk(position = (0,-2,-7), radius = 7, normal = (0,1,0), material = stone ))

rtx.scene.append( AABB(position = (1.4,-1.35,-7), size = (1.5,1.5,1.5), material = grass))
rtx.scene.append( AABB(position = (-1.8,-2.3,-7), size = (2,2,2), material = grass))
rtx.scene.append( Sphere((-1.7,0.08,-6.7),1.3, glass))
rtx.scene.append( Sphere((0.4,-1.5,-6),0.54, marble))
rtx.scene.append( Sphere((3.3,-1.2,-5.8), 0.8 , mirror))
rtx.scene.append( Sphere((1.5,0.3,-7),0.9, brick))

rtx.glRender()

rtx.glFinish("output.bmp")