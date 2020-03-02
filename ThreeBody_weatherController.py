# ThreeBody的天气控制程序
# 说明：
# era指纪元，可为恒纪元或乱纪元
# sun1指比较小的太阳
# sun2指中等大小的太阳
# sun3指最大的太阳

from ThreeBodyController import Controller
from random import randint


class weather_Controller(Controller):
    def era_controller(self):
        # 0为乱纪元，1为恒纪元
        self.era = randint(0, 1)
        print(self.era)
        # 0为飞星状态，1为太阳状态
        self.sun1 = randint(0, 1)
        self.sun2 = randint(0, 1)
        self.sun3 = randint(0, 1)
        print(self.sun1, self.sun2, self.sun3)
        # 确定太阳位置
        self.sun1_pos = randint(1, 3)
        self.sun2_pos = randint(1, 3)
        self.sun3_pos = randint(1, 3)
        print(self.sun1_pos, self.sun2_pos, self.sun3_pos)
        # 定义weather
        self.weather = ""
        self.era_mode = ""
        # 零个太阳的情况——三颗飞星
        if self.sun1 == self.sun2 == self.sun3 == 0:
            self.era_mode = "乱纪元"
            self.weather = "三颗飞星"
            print(self.era_mode, self.weather)
        # 一个太阳的情况——使era_mode为恒纪元
        elif self.sun1 == 1 and self.sun2 == self.sun3 == 0:
            self.era_mode = "恒纪元"
            print(self.era_mode)
        elif self.sun2 == 1 and self.sun1 == self.sun3 == 0:
            self.era_mode = "恒纪元"
            print(self.era_mode)
        elif self.sun3 == 1 and self.sun1 == self.sun2 == 0:
            self.era_mode = "恒纪元"
            print(self.era_mode)
        # 三个太阳的情况——三日凌空或三日连珠
        elif self.sun1 == self.sun2 == self.sun3 == 1:
            self.era_mode = "乱纪元"
            if self.sun1_pos == self.sun2_pos == self.sun3_pos:
                self.weather = "三日连珠"
                print(self.era_mode, self.weather)
            else:
                self.weather = "三日凌空"
                print(self.era_mode, self.weather)
        # 两个太阳的情况——二日凌空或二日连珠
        elif self.sun1 == self.sun2 == 1:
            self.era_mode = "乱纪元"
            if self.sun1_pos == self.sun2_pos:
                self.weather = "二日连珠"
                print(self.era_mode, self.weather)
            else:
                self.weather = "二日凌空"
                print(self.era_mode, self.weather)
        elif self.sun1 == self.sun3 == 1:
            self.era_mode = "乱纪元"
            if self.sun1_pos == self.sun3_pos:
                self.weather = "二日连珠"
                print(self.era_mode, self.weather)
            else:
                self.weather = "二里凌空"
                print(self.era_mode, self.weather)
        elif self.sun2 == self.sun3 == 1:
            self.era_mode = "乱纪元"
            if self.sun2_pos == self.sun3_pos:
                self.weather = "二日连珠"
                print(self.era_mode, self.weather)
            else:
                self.weather = "二日凌空"
                print(self.era_mode, self.weather)
