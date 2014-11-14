import bpy
import os
import string
import re

def clearGlpProperties():
    object = bpy.context.active_object
    if object:
        object.glpTypes = "none"
        object.glpTriggerTypes = "none"             
    
        
class addDoor(bpy.types.Operator):
    bl_idname = "wm.add_door"
    bl_label = "Mark the selection as door."

    def execute(self, context):
        realpath = os.path.expanduser("~/.glportal/data/meshes/Door.obj")
        bpy.ops.import_scene.obj(filepath=realpath)
        bpy.ops.transform.translate(value=(bpy.context.scene.cursor_location))
        bpy.types.Object.glpType = bpy.props.StringProperty()
        object = bpy.context.active_object
        clearGlpProperties()
        if object:
            object["glpType"] = "door" 
        return {'FINISHED'}    

def getMaterial(texturePath):
    realpath = os.path.expanduser(texturePath)
    try:
        portableWallImage = bpy.data.images.load(realpath)
    except:
        raise NameError("Cannot load image %s" % realpath)
    
    portableWallTexture = bpy.data.textures.new('ColorTex', type = 'IMAGE')
    portableWallTexture.image = portableWallImage
        
    mat = bpy.data.materials.new('TexMat')
 
    # Add texture slot for color texture
    mtex = mat.texture_slots.add()
    mtex.texture = portableWallTexture
    mtex.texture_coords = 'UV'
    mtex.use_map_color_diffuse = True 
    mtex.use_map_color_emission = True 
    mtex.emission_color_factor = 0.5
    mtex.use_map_density = True 
    mtex.mapping = 'FLAT'
    return mat


class addWin(bpy.types.Operator):
    bl_idname = "wm.add_win"
    bl_label = "Mark the selection as win trigger."
    
    def execute(self, context):
        bpy.ops.mesh.primitive_cube_add()
        object = bpy.context.active_object
        clearGlpProperties()
        if object:
            object.glpTypes = "trigger"
            object.glpTriggerTypes = "win"
        return {'FINISHED'}    

class addDeath(bpy.types.Operator):
    bl_idname = "wm.add_death"
    bl_label = "Mark the selection as death trigger."
    
    def execute(self, context):
        bpy.ops.mesh.primitive_cube_add()
        object = bpy.context.active_object
        clearGlpProperties()
        if object:
            object.glpTypes = "trigger"
            object.glpTriggerTypes = "death"
        return {'FINISHED'}    

class addRadiation(bpy.types.Operator):
    bl_idname = "wm.add_radiation"
    bl_label = "Mark the selection as radiation trigger."
    
    def execute(self, context):
        bpy.ops.mesh.primitive_cube_add()
        object = bpy.context.active_object
        clearGlpProperties()
        if object:
            object.glpTypes = "trigger"
            object.glpTriggerTypes = "radiation"
        return {'FINISHED'}    
    
class addPortable(bpy.types.Operator):
    bl_idname = "wm.add_portable"
    bl_label = "Mark the selection as portable."
    
    def execute(self, context):
        bpy.ops.mesh.primitive_cube_add()
        mat = getMaterial('~/.glportal/data/textures/wall.png')
        bpy.types.Object.glpType = bpy.props.StringProperty()
        object = bpy.context.active_object
        clearGlpProperties()
        if object:
            object.glpTypes = "wall"
            object.glpWallTypes = "portable"
            me = object.data
            me.materials.append(mat)
        return {'FINISHED'}    

    
class addWall(bpy.types.Operator):
    bl_idname = "wm.add_wall"
    bl_label = "Mark the selection as portable."

    def execute(self, context):
        bpy.ops.mesh.primitive_cube_add()
        mat = getMaterial('~/.glportal/data/textures/tiles.png')        
        bpy.types.Object.glpType = bpy.props.StringProperty()
        object = bpy.context.active_object
        clearGlpProperties()
        if object:
            object.glpTypes = "wall"
            me = object.data
            me.materials.append(mat)
        return {'FINISHED'}    
    
