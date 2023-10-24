import bpy
bl_info = {
    "name": "Auto Split",
    "location": "View3D > Add > Mesh > Auto Split",
    "description": "Auto Split vertex, edge, face",
    "author": "nguyendinhat",
    "version": (1,0),
    "blender": (3,6,3),
    "category": "Mesh",
}

class VIEW3D_OT_auto_split(bpy.types.Operator):
    bl_idname = "view3d.auto_split"
    bl_label = "Auto Split"
    bl_options = {'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None
    def execute(self, context):
        select_mode = bpy.context.tool_settings.mesh_select_mode
        if select_mode[0]:
            bpy.ops.mesh.edge_split(type='VERT')
            self.report({"INFO"}, "bpy.ops.mesh.edge_split(type='VERT')")
        if select_mode[1] and not select_mode[2]:
            bpy.ops.mesh.edge_split(type='EDGE')
            self.report({"INFO"}, "bpy.ops.mesh.edge_split(type='EDGE')")
        if select_mode[2] and not select_mode[1]:
            bpy.ops.mesh.split()
            self.report({"INFO"}, "bpy.ops.mesh.split()")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(VIEW3D_OT_auto_split)

def unregister():
    bpy.utils.unregister_class(VIEW3D_OT_auto_split)

if __name__ == "__main__":
    register()