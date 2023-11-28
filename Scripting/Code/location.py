import bpy

# add cupe 
bpy.ops.mesh.primitive_cube_add()

# selecte active object
cube = bpy.context.active_object


start_frame = 1
cube.keyframe_insert("location",frame=start_frame)

#change location
cube.location.z = 5

middle_frame = 90
cube.keyframe_insert("location",frame=middle_frame)


cube.location.z = 1
last_frame = 180
cube.keyframe_insert("location",frame=last_frame)