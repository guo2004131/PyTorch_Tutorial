import numpy as np


class ConvertImageShape:
    def __init__(self):
        pass

    @staticmethod
    def convert_chw_to_hwc(img_chw):
        """
        To convert the image of shape C*H*W to H*W*C.
        :param img_chw: the input image of shape C*H*W
        :return: the converted image of shape H*W*C
        """
        # The shape index of image is C=0, H=1, W=2.
        img_hwc = np.transpose(img_chw, (1, 2, 0))
        return img_hwc

    @staticmethod
    def convert_hwc_to_chw(img_hwc):
        """
                To convert the image of shape C*H*W to C*H*W.
                :param img_hwc: the input image of shape H*W*C
                :return: the converted image of shape C*H*W
                """
        # The shape index of image is C=2, H=0, W=1.
        img_chw = np.transpose(img_hwc, (2, 0, 1))
        return img_chw
