import bpy
import math
import os

radius = 10
object_location = bpy.data.objects['Cube'].location
num_frames = 100
save_frames = [x for x in range(1,10) if x%2==0] 
output_path = 'C:/Users/ramig/Desktop/Blender Scripting/images/'


cam = bpy.data.objects['Camera']
bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = num_frames


for frame in range(1, num_frames + 1):
    theta = 2 * math.pi * frame / num_frames
    x = radius * math.cos(theta) + object_location.x
    y = radius * math.sin(theta) + object_location.y
    z = object_location.z + 4


    cam.location = (x, y, z)


    direction = object_location - cam.location
    rot_quat = direction.to_track_quat('-Z', 'Y')
    cam.rotation_euler = rot_quat.to_euler()


    cam.keyframe_insert(data_path="location", frame=frame)
    cam.keyframe_insert(data_path="rotation_euler", frame=frame)
    

    if frame in save_frames:
        bpy.context.scene.frame_set(frame)
        bpy.context.scene.render.filepath = os.path.join(output_path, f"rendered_frame_{frame}.png")
        bpy.ops.render.render(write_still=True)
