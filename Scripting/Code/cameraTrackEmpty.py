# give Python access to Blender's functionality
import bpy


def set_end_frame(frame_count):
    """set the end frame"""
    bpy.context.scene.frame_end = frame_count


def set_fps(fps):
    """set the fps"""
    bpy.context.scene.render.fps = fps


def create_row(cube_count, location_offset):
    """create a row of cubes along the Y-axis"""
    for i in range(cube_count):
        bpy.ops.mesh.primitive_cube_add(size=2, location=(0, i * location_offset, 0))


def create_empty():
    """create an empty for tracking"""
    bpy.ops.object.empty_add()
    empty = bpy.context.active_object
    return empty


def animate_empty(empty, cube_count, location_offset, frame_count):
    """animate the location property of the empty"""
    empty.keyframe_insert("location", frame=1)
    empty.location.y = cube_count * location_offset
    empty.keyframe_insert("location", frame=frame_count)


def add_camera():
    """add a camera into the scene"""
    bpy.ops.object.camera_add()
    camera = bpy.context.active_object
    camera.location.x = 15
    camera.location.z = 2
    return camera


def animate_camera(camera, cube_count, location_offset, frame_count):
    """animate the location property of the camera"""
    camera.keyframe_insert("location", frame=1)
    camera.location.y = cube_count * location_offset
    camera.keyframe_insert("location", frame=frame_count)


def track_empty(obj, empty):
    """add a constraint to track the empty"""
    bpy.ops.object.constraint_add(type="TRACK_TO")
    obj.constraints["Track To"].target = empty


# create parameters
cube_count = 10
location_offset = 3
frame_count = 300
fps = 30

set_end_frame(frame_count)
set_fps(fps)

create_row(cube_count, location_offset)

empty = create_empty()
animate_empty(empty, cube_count, location_offset, frame_count)

camera = add_camera()
animate_camera(camera, cube_count, location_offset, frame_count)
track_empty(camera, empty)