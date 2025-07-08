from PyFlow.Core.Common import *
from PyFlow.Core import FunctionLibraryBase
from PyFlow.Core import IMPLEMENT_NODE
import numpy as np
import cv2
import os

class CoreFunctions(FunctionLibraryBase):
    '''doc string for CoreFunctions'''

    def __init__(self, packageName):
        super(CoreFunctions, self).__init__(packageName)

    @staticmethod
    @IMPLEMENT_NODE(returns=None, meta={NodeMeta.CATEGORY: 'I/O', NodeMeta.KEYWORDS: []})
    def loadImage2(path=('StringPin', "", {PinSpecifiers.INPUT_WIDGET_VARIANT: "FilePathWidget"}),
                   flag=('StringPin', 'IMREAD_COLOR',
                            {PinSpecifiers.VALUE_LIST: \
                             ['IMREAD_UNCHANGED', 'IMREAD_GRAYSCALE', 'IMREAD_COLOR', \
                              'IMREAD_ANYDEPTH','IMREAD_ANYCOLOR','IMREAD_LOAD_GDAL', \
                              'IMREAD_REDUCED_GRAYSCALE_2', 'IMREAD_REDUCED_COLOR_2', \
                              'IMREAD_REDUCED_GRAYSCALE_4', 'IMREAD_REDUCED_COLOR_4', \
                              'IMREAD_REDUCED_GRAYSCALE_8', 'IMREAD_REDUCED_COLOR_8', \
                              'IMREAD_IGNORE_ORIENTATION ']}), 
                   img=(REF, ('AnyPin', None))):
        path = os.path.normpath(path)
        if path:
            # Fix for CJK path: read as bytes and decode
            try:
                with open(path, 'rb') as f:
                    file_bytes = np.asarray(bytearray(f.read()), dtype=np.uint8)
                    image = cv2.imdecode(file_bytes, getattr(cv2, flag, cv2.IMREAD_COLOR))
                    img(image)
            except Exception as e:
                img(None)
