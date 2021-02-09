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
from bpy.types import (
    AddonPreferences,
    Operator,
    Panel,
    PropertyGroup,
)


class OBJECT_OT_killonecube(Operator):
    bl_label = "Kill the cube"
    bl_idname = "object.cube_die"
    bl_description = "Kills any object called cube"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.context.active_object.select_set(False)
        try:
            bpy.data.objects['Cube'].select_set(True)
            bpy.ops.object.delete(use_global=False)
        except:
            print("there probably isn't an object named 'Cube' in the scene" 
        return {'FINISHED'}



def menu_func(self, context):
    self.layout.operator(OBJECT_OT_killonecube.bl_idname)

def register():
    bpy.utils.register_class(OBJECT_OT_killonecube)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_killonecube)
    bpy.types.VIEW3D_MT_object.remove(menu_func)

if __name__ == "__main__":
    register()
