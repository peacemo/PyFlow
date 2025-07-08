import os
from PyFlow.Core.PackageBase import PackageBase

class CvCore(PackageBase):
    """Base pyflow package
    """
    def __init__(self):
        super(CvCore, self).__init__()
        self.analyzePackage(os.path.dirname(__file__))