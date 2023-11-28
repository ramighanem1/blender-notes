import bpy
import math 



radius_step = 0.1
current_radius = 0.1
number_triangle = 50

z_step = 10

for i in range(1,number_triangle):
    
    current_radius = i * radius_step
    bpy.ops.mesh.primitive_circle_add(vertices=3, radius=current_radius)
    
    triangle_mesh = bpy.context.active_object
    
    degrees=-90
    radians = math.radians(degrees)
    triangle_mesh.rotation_euler.x = radians


    degrees= z_step * i
    radians = math.radians(degrees)
    triangle_mesh.rotation_euler.z = radians
    
        
    
    bpy.ops.object.convert(target='CURVE')

    triangle_mesh.data.bevel_depth = 0.05
    triangle_mesh.data.bevel_resolution = 16

    bpy.ops.object.shade_smooth()