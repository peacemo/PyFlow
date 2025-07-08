from PyFlow.UI.Canvas.UINodeBase import UINodeBase
from PyFlow.Packages.CvCore.UI.UIDemoNode import UIDemoNode

def createUINode(raw_instance):
    if raw_instance.__class__.__name__== "DemoNode":
        return UIDemoNode(raw_instance)
    return UINodeBase(raw_instance)
