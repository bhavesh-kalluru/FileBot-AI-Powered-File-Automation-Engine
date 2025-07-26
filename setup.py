from setuptools import setup

APP = ["filebot_menu.py"]
OPTIONS = {
    "argv_emulation": True,
    "packages": ["rumps", "tkinter", "file_agent", "utils"],
    "iconfile": None,    # you can add a .icns icon here
}

setup(
    app=APP,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
