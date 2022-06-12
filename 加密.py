#  -*-coding:utf-8-*-
class 加密(object):
    def __init__(self, 密钥: str, 内容: str):
        # 密钥和内容长度
        self.密钥 = 密钥
        self.密钥和 = 0
        if self.密钥.isdigit():
            if len(self.密钥) > 5:
                for i in self.密钥:
                    self.密钥和 += int(i)
            else:
                self.密钥和 = int(self.密钥)
        else:
            for i in self.密钥:
                self.密钥和 += int(ord(i))
        self.内容 = 内容
        self.加密结果列表 = []
        self.加密结果 = ''

    def 加密(self):
        for i in self.内容:
            self.加密结果列表.append(chr(ord(i) + self.密钥和))
        for i in self.加密结果列表:
            self.加密结果 += i

    def 输出(self):
        return self.加密结果


if __name__ == '__main__':
    密钥 = input('请输入密钥：')
    内容 = input('请输入内容：')
    加密 = 加密(密钥, 内容)
    加密.加密()
    print(加密.输出())
