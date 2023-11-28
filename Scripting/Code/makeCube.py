import bpy

verts = [
    (-1.0, -1.0, -1.0),
    (-1.0, 1.0, -1.0),
    (1.0, 1.0, -1.0),
    (1.0, -1.0, -1.0),
    (-1.0, -1.0, 1.0),
    (-1.0, 1.0, 1.0),
    (1.0, 1.0, 1.0),
    (1.0, -1.0, 1.0),]

faces = [
        (0, 1, 2, 3), # index of verts
        (7, 6, 5, 4),
        (4, 5, 1, 0),
        (7, 4, 0, 3),
        (6, 7, 3, 2),
        (5, 6, 2, 1),]

edges = []

mesh_data = bpy.data.meshes.new("cube_data")
mesh_data.from_pydata(verts,edges,faces)


mesh_obj = bpy.data.objects.new("cube_object",mesh_data)




bpy.context.collection.objects.link(mesh_obj)