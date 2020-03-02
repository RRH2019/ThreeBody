# ThreeBody的天气控制程序
# 说明：
# era指纪元，可为恒纪元或乱纪元
# sun1指比较小的太阳
# sun2指中等大小的太阳
# sun3指最大的太阳

from ThreeBodyController import Controller
from random import randint


class weather_Controller(Controller):
    def __init__(self):
        self.weather = ""
        # 0为乱纪元，1为恒纪元
        self.era = randint(0, 1)
        if self.era == 0:
            # 0为飞星状态，1为太阳状态
            self.sun1 = randint(0, 1)
            self.sun2 = randint(0, 1)
            self.sun3 = randint(0, 1)
            if self.sun1 and self.sun2 or \
                    self.sun1 and self.sun2 or \
                    self.sun2 and self.sun3 == 1:
                self.weather = "二日凌空"
                print(self.weather)
            elif self.sun1 and self.sun2 and self.sun3 == 1:
                pass
