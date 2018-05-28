# -*- coding: UTF-8 -*-
import sys
# reload(sys)
sys.setdefaultencoding('utf-8')
import time
time1=time.time()
import os.path
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage

result=[]
class CPdf2TxtManager():
    def __init__(self):
        '''''
        Constructor
        '''

    def changePdfToText(self, filePath):
        file = open(path, 'rb') # 以二进制读模式打开
        #用文件对象来创建一个pdf文档分析器
        praser = PDFParser(file)
        # 创建一个PDF文档
        doc = PDFDocument(praser)
        # 检测文档是否提供txt转换，不提供就忽略
        if not doc.is_extractable:
            raise PDFTextExtractionNotAllowed

        # 创建PDf 资源管理器 来管理共享资源
        rsrcmgr = PDFResourceManager()
        # 创建一个PDF设备对象
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        # 创建一个PDF解释器对象
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        pdfStr = ''
        # 循环遍历列表，每次处理一个page的内容
        for page in PDFPage.create_pages(doc): # doc.get_pages() 获取page列表
            interpreter.process_page(page)
            # 接受该页面的LTPage对象
            layout = device.get_result()
            for x in layout:
                if hasattr(x, "get_text"):
                    # print x.get_text()
                    result.append(x.get_text())
                    fileNames = os.path.splitext(filePath)
                    with open(fileNames[0] + '.txt','wb') as f:
                        results = x.get_text()
                        print(results)
                        f.write(results + '\n')




if __name__ == '__main__':
    '''''
     解析pdf 文本，保存到txt文件中
    '''

    path = u'C:/36.pdf'
    pdf2TxtManager = CPdf2TxtManager()
    pdf2TxtManager.changePdfToText(path)

    # print result[0]
    time2 = time.time()

    # print "uok,解析pdf结束!'
    # print u'总共耗时：' + str(time2 - time1) + 's'
    #
