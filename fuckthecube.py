bl_info = {
    "name": "Fuck The Cube",
    "author": "RamenSlayer",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "View3D > Object",
    "description": "Delete the default cube (if there isn't one won't do anything, must be called Cube.",
    "category": "Object",
}

import bpy

class FuckTheCube(bpy.types.Menu):
    bl_label = "FuckTheCube"
    bl_idname = "cube_get_fucked"
    
    def execute(self, context):
        try:
            bpy.data.objects['Cube'].select_set(True)
            bpy.ops.object.delete(use_global=False)
            return {'FINISHED'}
        except:
            return ('Oops, something went wrong')
     
    def draw(self, context):    
        layout = self.layout
        object = context.active_object
        
        scene = context.scene
        col = layout.column(align=True)


def menu_func(self, context):
    self.layout.operator(FuckTheCube.bl_idname)

def register():
    bpy.utils.register_class(FuckTheCube)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(FuckTheCube)
    
if __name__ == "__main__":
    register()
