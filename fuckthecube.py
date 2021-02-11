#just description
bl_info = {
    "name": "Fuck The Cube",
    "author": "RamenSlayer",
    "version": (0, 1, 5),
    "blender": (2, 80, 0),
    "location": "View3D > Object",
    "description": "Delete the default cube (if there isn't one won't do anything, must be called Cube.",
    "category": "Object",
}

#importing the things that might be used here, idk if they even are

import bpy
from bpy.types import (
    AddonPreferences,
    Operator,
    Panel,
    PropertyGroup,
)

#defining the first command (delete cube by name)

class OBJECT_OT_killonecube(Operator):
#setting up options
    bl_label = "Kill the cube by name"
    bl_idname = "object.cube_die"
    bl_description = "Kills any object called cube"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_options = {'REGISTER', 'UNDO'}
#finally the command itself
    def execute(self, context):
        bpy.ops.object.select_all(action='DESELECT') #unselecting everything so it doesn't delete anything it shouldn't
        try:
            bpy.data.objects['Cube'].select_set(True) #finding the object called Cube, selecting it
            bpy.ops.object.delete(use_global=False) #deleting the object
        except:
            print("Probably nothing named cube in the scene") #people will see it only in the system console but whatever
        finally:    
            return {'FINISHED'} #ending the command either way

class OBJECT_OT_killallcubes(Operator):
#setting up options again
    bl_label = "Kill all cubes by name"
    bl_idname = "object.cubes_die"
    bl_description = "Kills all objects with cube in the name"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_options = {'REGISTER', 'UNDO'}
#finally the command itself x2
    def execute(self, context):
        bpy.ops.object.select_all(action='DESELECT')
        for object in bpy.data.objects:
            if "cube" in object.name.lower():
                object.select_set(True)
        bpy.ops.object.delete(use_global=False)
        return {'FINISHED'}


#gotta define menu to add the functions to ui
def menu_func(self, context):
    self.layout.operator(OBJECT_OT_killonecube.bl_idname)
    self.layout.operator(OBJECT_OT_killallcubes.bl_idname)

#registering the commands so it actually exists
def register():
    bpy.utils.register_class(OBJECT_OT_killonecube)
    bpy.utils.register_class(OBJECT_OT_killallcubes)
    bpy.types.VIEW3D_MT_object.append(menu_func)

#basically deleting them when addon disabled
def unregister():
    bpy.utils.unregister_class(OBJECT_OT_killonecube)
    bpy.types.VIEW3D_MT_object.remove(menu_func)

#idk you have to have this for the addon to actually work
if __name__ == "__main__":
    register()
