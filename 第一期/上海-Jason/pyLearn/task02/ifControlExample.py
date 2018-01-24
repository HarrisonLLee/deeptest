# _*_ coding : utf-8 _*_
__author__ = "Jason"
'''
基本上if条件控制结构是：
if condition:
    code
elif condition:
    code
else:
    code
'''
class today:
    def __init__(self,day):
        self.day = day

    def whichDay(self):
        if self.day == "Mon" or self.day == "Monday":
            print("今天是周一！")
        elif self.day == "Tue" or self.day == "Tuesday":
            print("今天是周二！")
        elif self.day == "Wednesday":
            print("今天是周三！")
        elif self.day == "Thursday":
            print("今天是周四！")
        elif self.day == "Fri" or self.day == "Friday":
            print("今天是周五！")
        else:
            wish = "周末happy！"
            if self.day == "Sat" or self.day == "Saturday":
                print("今天是周六，%s"%wish)
            elif self.day == "Sun" or self.day == "Sunday":
                print("今天是周日，%s"%wish)
#示例
if __name__ == '__main__':
    ifDay = today("Fri").whichDay()
    print(ifDay)
    print("-"*50)
    ifDay = today("Sunday").whichDay()
    print(ifDay)