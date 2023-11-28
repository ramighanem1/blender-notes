import bpy
import math 

# add cupe
bpy.ops.mesh.primitive_cube_add()


cube = bpy.context.active_object


start_frame = 1
cube.keyframe_insert("rotation_euler",frame=start_frame)


# rotation cupe
degrees=360
radians = math.radians(degrees)
cube.rotation_euler.y = radians




last_frame = 180
cube.keyframe_insert("rotation_euler",frame=last_frame)