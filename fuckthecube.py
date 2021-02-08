bl_info = {
    "name": "FuckTheCube",
    "description": "Fuck that default cube"
    "author": ("RamenSlayer")
    "version": (0, 0, 1)
    "blender": (2, 80, 0),
    "category": "Object"
}

import bpy

class FuckTheCube(bpy.types.Menu):
    bl_label = "FuckTheCube"
    bl_idname = "cube_get_fucked"
    
    def execute(self, context):
        bpy.data.objects['Cube'].select_set(True)
        bpy.ops.object.delete(use_global=False)
        
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(FuckTheCube.bl_idname)

def register():
    bpy.utils.register_class(FuckTheCube)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(FuckTheCube)
    
if __name__ == "__main__":
    register()
