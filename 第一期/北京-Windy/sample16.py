#!/usr/bin/env  python
# -*- coding: UTF-8 -*-


class Sample:

    '''一个小球其实高度为100米，每次落到地面后可以弹起到原来高度的一半，求第10次弹起后的高度和小球一共运动了多少米'''

    def __init__(self, height, tim):
        self.height = height
        self.tim = tim

    def sample(self):
        tour = []
        heights = []
        '''从第二次开始，落地时经过的距离应该是反弹高度乘以2（弹到最高点后落地）'''
        for i in range(1, self.tim+1):
            if i == 1:
                tour.append(self.height)
            else:
                tour.append(2*self.height)
            self.height /= 2
            heights.append(self.height)
        print("总高度:tour =", format(sum(tour)))
        print("第十次反弹高度：heights = ", format(heights[-1]))


if __name__ == '__main__':
    s = Sample(int(input('请输入原始高度：')), int(input('请输入反弹次数：')))
    s.sample()