import eel
from 加密 import 加密
from 解密 import 解密

error = '密钥长度错误,请重新输入(密钥长度不能大于8)'


@eel.expose
def jiamimain(密钥, 内容):
    # 加密
    if len(密钥) >= 8:
        return error
    elif len(密钥) == 0:
        return '密钥不能为空'
        a = 加密(密钥, 内容)
        a.加密()
        return a.输出()
    a = 加密(密钥, 内容)
    a.加密()
    return a.输出()


@eel.expose
def jiemimain(密钥, 内容):
    # 解密
    if len(密钥) >= 8:
        return error
    elif len(密钥) == 0:
        return '密钥不能为空'
    a = 解密(密钥, 内容)
    a.解密()
    return a.输出()


eel.init('web')
eel.start('index.html', size=(400, 400), port=1234)
