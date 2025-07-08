import cv2
from PyFlow.Core import NodeBase
from PyFlow.Core.Common import PinOptions
from PyFlow.Core import PinBase
from PyFlow.Core.Common import PinSpecifiers

class LoadImage1(NodeBase):
    def __init__(self, name):
        super(LoadImage1, self).__init__(name)
        # 指定输入Pin的控件为文件选择器
        self.pathIn = self.createInputPin(
            'path', 'StringPin',
            defaultValue=""
        )
        # 输出：图片矩阵
        self.imgOut = self.createOutputPin('image', 'AnyPin')
        self.imgOut.enableOptions(PinOptions.AllowAny)
        self.imgOut.enableOptions(PinOptions.DictSupported)

    @staticmethod
    def category():
        return 'Core Functions'

    def compute(self, *args, **kwargs):
        path = self.pathIn.getData()
        # convert windows style path string to unix style
        if isinstance(path, str):
                path = path.replace('\\', '/')
        img = None
        if path:
            img = cv2.imread(path)
        self.imgOut.setData(img)
