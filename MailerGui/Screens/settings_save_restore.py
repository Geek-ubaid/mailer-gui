from PyQt5.QtCore import QFileInfo
from PyQt5.QtWidgets import qApp


def restore(settings):
    finfo = QFileInfo(settings.fileName())

    if finfo.exists() and finfo.isFile():
        for w in qApp.allWidgets():
            mo = w.metaObject()
            if w.objectName() in ['username_text_box', 'password_text_box', 'forget_password']:
                for i in range(mo.propertyCount()):
                    name = mo.property(i).name()
                    val = settings.value("{}/{}".format(w.objectName(), name), w.property(name))
                    w.setProperty(name, val)


def save(settings):
    for w in qApp.allWidgets():
        mo = w.metaObject()
        if w.objectName() in ['username_text_box', 'password_text_box', 'forget_password']:
            for i in range(mo.propertyCount()):
                name = mo.property(i).name()
                settings.setValue("{}/{}".format(w.objectName(), name), w.property(name))