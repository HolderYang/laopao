'''
在文件中匹配端口号对应的段落
在对应的段落中 匹配到对应的IP地址
'''
import re

def get_address(prot):
    f = open("msg.txt")
    while True:
        #获取一段内容
        data = ""
        for line in f :
            if line == "\n":
                break
            data += line
        #data为空时到文档结尾
        if not data :
            break
        obj  = re.match(port,data)
        #如果obj不为None,那么data就是目标段落
        if obj:
            pattern = r"[a-f0-9]{1,4}\.[a-f0-9]{1,4}\.[a-f0-9]{1,4}\.[a-f0-9]{1,4}"
            # pattern = r"(\d{1,3}\.){3}\d{1,3}"
            obj = re.search(pattern,data)
            # print(data)
            return obj.group()
    return "没有该端口"
if __name__ == "__main__":
    port = input("端口:")
    print(get_address(port))