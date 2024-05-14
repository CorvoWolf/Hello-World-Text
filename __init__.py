# 最开头的列表填写插件信息
# 这些信息会显示在插件面板
bl_info = {
    "name" : "Hello World Text",    # 插件名
    "author" : "岑轩漠 CorvoWolf",     # 作者名
    "description" : "在 3D视图 的 N面板 生成一个按钮，运行后生成一个内容为“Hello World”的文本物体", # 插件描述
    "blender" : (2, 80, 0),     # 支持的blender版本
    "version" : (0, 0, 0, 2333),      # 插件版本，好像只能填数字。我试图填X，但插件直接装不上（摊手）¯\_(ツ)_/¯
    "location" : "3D视图 > N面板 > Hello World Category",       # 插件位置
    "warning" : "暂时没啥警告。这只是个练手插件，捋插件基本结构用",     # 警告写这里
    "category" : "Add Curve"       # 插件筛选面板的类型
}

# 导入Blender Python API
# 导入后bpy相关代码才有效，否则沾bpy就报错
import bpy

# 定义一个新建‘Hello World’文本的操作类
class HelloWorldOperator(bpy.types.Operator):
    bl_idname = "curve.hello_world_add"   # 操作类的唯一标识名，F3面板中可以搜到，选中运行
    bl_label = "Hello World"    # ？
    
    # 定义具体方法（操作）
    def execute(self, context):
        if "Hello World" not in bpy.data.objects:       # 如果场景中没有名为“Hello World”的物体
            bpy.ops.object.text_add(location =(0,0,0))      # 新建一个文本物体，本质是曲线
            bpy.context.object.name = "Hello World"     # 将新建的文本物体改名为“Hello World”
            bpy.context.object.data.body = "Hello World"    # 将文本内容改为“Hello World”
            return {'FINISHED'}
        else:       # 如果已有名为“Hello World”的物体
            bpy.data.objects["Hello World"].data.body = "Hello World"       # 将文本内容改为“Hello World”
            return {'FINISHED'}

# 定义一个面板            
class HelloWorldPanel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_hello_world"     # 面板类的唯一标识名
    bl_label = "Hello World Label"      #
    bl_space_type = 'VIEW_3D'   # 空间类型，面板放什么编辑器
    bl_region_type = 'UI'       # 区域类型，面板要放在编辑器哪一块
    bl_category = "Hello World Category"        # 面板实际名称

    def draw(self, context):        # 绘制面板
        self.layout.label(text="Hello World Text")      # 画一个标题栏
        layout = self.layout        # draw方法内部参数，为了简化，给layout重新赋值了
        layout.operator("curve.hello_world_add")        # 生成一个按钮，括号里写操作的标识名

def register():     # 启用插件时运行，一般是注册自定义的操作类和面板类
    bpy.utils.register_class(HelloWorldPanel)       # 注册面板类
    bpy.utils.register_class(HelloWorldOperator)        # 注册操作类

def unregister():       # 停用插件时运行，一般是注册自定义的操作类和面板类
    bpy.utils.unregister_class(HelloWorldPanel)     # 注销面板类
    bpy.utils.unregister_class(HelloWorldOperator)      # 注销操作类