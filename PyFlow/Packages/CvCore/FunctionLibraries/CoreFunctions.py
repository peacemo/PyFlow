from PyFlow.Core.Common import *
from PyFlow.Core import FunctionLibraryBase
from PyFlow.Core import IMPLEMENT_NODE
import cv2


class CoreFunctions(FunctionLibraryBase):
    '''doc string for DemoLib'''

    def __init__(self, packageName):
        super(CoreFunctions, self).__init__(packageName)

    @staticmethod
    @IMPLEMENT_NODE(returns=None, meta={NodeMeta.CATEGORY: 'Core Functions', NodeMeta.KEYWORDS: []})
    def loadImage2(path=('StringPin', "", {PinSpecifiers.INPUT_WIDGET_VARIANT: "FilePathWidget"}), 
                   img=(REF, ('AnyPin', None))):
        if isinstance(path, str):
            # convert windows style path string to unix style
            path = path.replace('\\', '/')
        if path:
            img(cv2.imread(path))
