import dearpygui.dearpygui as dpg
import dearpygui.demo as demo
import subprocess as sp
import sys

Ark2Dir_InFile = ""
Ark2Dir_OutFolder = ""
Ark2Dir_DTA = ""
Ark2Dir_Inflate = ""

Dir2Ark_InFolder = ""
Dir2Ark_OutFolder = ""
Dir2Ark_Name = ""
Dir2Ark_Version = ""
Dir2Ark_Encrypt = ""

Patchcreator_ArkFiles_Path = ""
Patchcreator_outputPath = ""
Patchcreator_arkpath = ""
Patchcreator_exepath = ""

match sys.platform:
    case "win32":
        arkhelper =  "arkhelper.exe"
    case "darwin":
        arkhelper = "./arkhelper"
    case "linux":
        arkhelper = "./arkhelper"



def _help(message):
    last_item = dpg.last_item()
    group = dpg.add_group(horizontal=True)
    dpg.move_item(last_item, parent=group)
    dpg.capture_next_item(lambda s: dpg.move_item(s, parent=group))
    t = dpg.add_text("(?)", color=[0, 255, 0])
    with dpg.tooltip(t):
        dpg.add_text(message)

def DemoWindowCallback():
    demo.show_demo()
    
def QuitAppCallback():
    quit()

def UpdateVarCallback(sender, app_data, user_data):
    print(f"[DEBUG] app_data: {app_data}, user_data: {user_data}")
    globals()[user_data] = app_data
    print(f"[DEBUG] {user_data} updated to: {globals()[user_data]}")


def Ark2DirCallback():
    print(f"[DEBUG] Ark2Dir_InFile: {Ark2Dir_InFile}")
    print(f"[DEBUG] Ark2Dir_InFile: {Ark2Dir_OutFolder}")
    print(f"[DEBUG] Ark2Dir_DTA: {Ark2Dir_DTA}")
    print(f"[DEBUG] Ark2Dir_Inflate: {Ark2Dir_Inflate}")

    OptionalArgs = []

    if Ark2Dir_DTA == True:
        OptionalArgs.append("-s")

    if Ark2Dir_Inflate == True:
        OptionalArgs.append("-m")

    sp.run([arkhelper, "ark2dir", Ark2Dir_InFile, Ark2Dir_OutFolder] + OptionalArgs)

def Dir2ArkCallback():
    print(f"[DEBUG] Dir2Ark_InFolder: {Dir2Ark_InFolder}")
    print(f"[DEBUG] Dir2Ark_OutFolder: {Dir2Ark_OutFolder}")
    print(f"[DEBUG] Dir2Ark_Name: {Dir2Ark_Name}")
    print(f"[DEBUG] Dir2Ark_Version: {Dir2Ark_Version}")
    print(f"[DEBUG] Dir2Ark_Encrypt: {Dir2Ark_Encrypt}")

    OptionalArgs = []


    if Dir2Ark_Name != "":
        OptionalArgs.append(f"-n {Dir2Ark_Name}")
    if Dir2Ark_Version != "":
        OptionalArgs.append(f"-v {Dir2Ark_Version}")
    if Dir2Ark_Encrypt == True:
        OptionalArgs.append("-e")

    sp.run([arkhelper, "dir2ark", Dir2Ark_InFolder, Dir2Ark_OutFolder] + OptionalArgs)   

def PatchcreatorCallback():
    print(f"[DEBUG] Patchcreator_ArkFiles_Path: {Patchcreator_ArkFiles_Path}")
    print(f"[DEBUG] Patchcreator_outputPath: {Patchcreator_outputPath}")
    print(f"[DEBUG] Patchcreator_arkpath: {Patchcreator_arkpath}")
    print(f"[DEBUG] Patchcreator_exepath: {Patchcreator_exepath}")

    OptionalArgs = []
    OptionalArgs.append(f"-a {Patchcreator_ArkFiles_Path}")

    if Patchcreator_outputPath != "":
        OptionalArgs.append(f"-o {Patchcreator_outputPath}")

    sp.run([arkhelper, "patchcreator", Patchcreator_arkpath, arkhelper] + OptionalArgs)    



dpg.create_context()
dpg.create_viewport(title='Mackiloha-GUI - v1.0p', width=1280, height=720)


with dpg.window(label="Mackiloha-GUI", width=800, height=400):
    
    with dpg.collapsing_header(label="--DEBUG--"):
        dpg.add_button(label="Open Demo Window", callback=DemoWindowCallback)
        with dpg.group(horizontal=True):
            dpg.add_button(label="Test Button")
            dpg.add_text("Unused Button Pressed?")
        dpg.add_button(label="Exit", callback=QuitAppCallback)

    with dpg.tab_bar():
                            
        with dpg.tab(label="Arkhelper"):

            with dpg.tab_bar():
                            
                with dpg.tab(label="Ark2Dir"):
                    dpg.add_text("Options for Ark2Dir:")                     
                    with dpg.group(horizontal=True):
                        #dpg.add_button(label="Open")
                        dpg.add_input_text(label="Ark Path", hint="Enter File Path Here", callback=UpdateVarCallback, user_data="Ark2Dir_InFile")

                    with dpg.group(horizontal=True):
                        #dpg.add_button(label="Open")
                        dpg.add_input_text(label="Extract Path", hint="Enter Folder Path Here", callback=UpdateVarCallback, user_data="Ark2Dir_OutFolder")

                    dpg.add_checkbox(label="Convert scripts to .dta?", callback=UpdateVarCallback, user_data="Ark2Dir_DTA")
                    dpg.add_checkbox(label="Inflate .milo files", callback=UpdateVarCallback, user_data="Ark2Dir_Inflate")
                    dpg.add_button(label="Run Arkhelper", callback=Ark2DirCallback)

                with dpg.tab(label="Dir2Ark"):
                    dpg.add_text("Options for Dir2Ark:")
                    with dpg.group(horizontal=True):
                        #dpg.add_button(label="Open")
                        dpg.add_input_text(label="Folder Path", hint="Enter Folder Path Here", callback=UpdateVarCallback, user_data="Dir2Ark_InFolder")
                    with dpg.group(horizontal=True):
                        #dpg.add_button(label="Open")
                        dpg.add_input_text(label="Ark Path", hint="Enter Ark Path Here", callback=UpdateVarCallback, user_data="Dir2Ark_OutFolder")
                    dpg.add_input_text(label="input text", default_value="main", callback=UpdateVarCallback, user_data="Dir2Ark_Name")
                    dpg.add_input_int(label="input text", default_value=3, callback=UpdateVarCallback, user_data="Dir2Ark_Version")
                    _help("Ark Versions:\n"
                    "0 = Frequency (Unsupported)\n1 = Amplitude Demo (Unsupported)\n2 = Amplutde - Eyetoy: AntiGrav\n"
                    "3 = Guitar Hero 1 - Guitar Hero 2 (360)\n4 = Rock Band 1\n5 = The Beatles Rock Band - Green Day Rock Band\n6 = Rock Band 3 - Dance Central 3"
                    "\n7 = Fantasia/DCS (Unsupported)\n8/9 Unknown (Unsupported)\n10 = Rock Band 4 - Super Beat Sports (Unsupported)")
                    dpg.add_checkbox(label="Encrypt Ark Files?", callback=UpdateVarCallback, user_data="Dir2Ark_Encrypt")
                    dpg.add_button(label="Run Arkhelper", callback=Dir2ArkCallback)                 

                with dpg.tab(label="Patchcreator"):
                    dpg.add_text("Options for Patchcreator (Only recommended for advanced users):")
                    dpg.add_input_text(label="Path to the base HDR", callback=UpdateVarCallback, user_data="Patchcreator_arkpath")
                    dpg.add_input_text(label="Base Base Arks", callback=UpdateVarCallback, user_data="Patchcreator_ArkFiles_Path")
                    dpg.add_input_text(label="Output", callback=UpdateVarCallback, user_data="Patchcreator_outputPath")
                    dpg.add_button(label="Run Arkhelper", callback=PatchcreatorCallback)   



                     

        with dpg.tab(label="Superfreq"):
            dpg.add_text("This is the broccoli tab!")

            



dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()