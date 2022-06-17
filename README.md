# 文本混淆器_html版 V1.1.1-brython版
## 功能
- 将文本混淆为不可读文本（指伪乱码)
## 使用方法
    1.下载最新Releases，解压
    2.打开index.html或index_onlyone.html
    3.按照提示输入所需文本
    4.点击“加密”或“解密”按钮，获得加密或解密后的文本
Tip:‘index.html’需要浏览器开启axel（好像是这个词），而使用‘index_onlyone.html’不需要额外支持，即开即用，建议个人用‘index.html’，服务器网站用‘index_onlyone.html’
## 用途
    1.混淆网站链接（某度云盘链接等），防止被软件和谐
    2.密文传递，保护隐私
## 原理
    通过将密钥的ascii码之和（或数字之和）与文本的ascii码相加，得到新的ascii码，
    再转换为字符，得到新的文本。
##更新日志
    v1.1.1
    修复一个溢出bug
    v1.1.0
    解决的v1.0.0的无法部署问题，改用brython，可在网站部署
    v1.0.0
    初版，用eel与js交互，无法在网站上部署，只可本地使用
    
    