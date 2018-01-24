import random
class MySort:
    # 生成随机数,返回排序后的结果
    # start, end为限制随机数生成的范围
    # count为生成的随机数个数
    def __init__(self, start, end, count):
        list = []
        i = 0
        for i in range(count):
            nub = random.randint(start, end)
            list.append(nub)
            i += 1
            self.count = count
            self.list = list
        print(list)


    # 冒泡实现排序（比较两个数大小，小的排前面）
    def mysort(self):
        for i in range(0, self.count):
            for j in range(i + 1, self.count):
                if self.list[i] > self.list[j]:
                    self.list[i], self.list[j] = self.list[j], self.list[i]
        return (self.list)


    #插入排序
    def insertsort(self):
        # 序列长度：
        lenght = len(self.list)
        for i in range(1, lenght):
            key = self.list[i]
            j = i - 1
            while j >= 0:
                # 比较，进行插入排序
                if self.list[j] > key:
                    self.list[j + 1] = self.list[j]
                    self.list[j] = key
                j = j - 1
        return self.list


# 使用示例
# if __name__ == "__main__":
sorted_data = MySort(10, 1000, 100)
sorted_data=sorted_data.mysort()
# 打印排序后的结果
print('冒泡排序后的结果是:%s'%sorted_data)
#sorted_data = MySort(10, 1000, 100)
sorted_data = MySort(10, 1000, 100)
sorted_data=sorted_data.insertsort()
print('插入排序的结果是:%s'%sorted_data)
