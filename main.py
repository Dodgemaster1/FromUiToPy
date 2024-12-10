import os

ui_list = []
uic = ""
directory = os.getcwd()
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".ui"):
            ui_list.append(os.path.abspath(os.path.join(root, file)))
        elif file == "pyside6-uic.exe":
            uic = os.path.abspath(os.path.join(root, file))

if uic == "":
    print("pyside6-uic.exe not found")
else:
    for ui in ui_list:
        py = ui.replace(".ui", ".py")
        os.system(rf"{uic} {ui} -o {py}")

os.system("pause")
