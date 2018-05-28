import win32com
import win32com.client

def readWordFlile(path):
    #调用系统Word功能
    mw=win32com.client.Dispatch("Word.Application")
    # 打开文件
    doc=mw.Documents.Open(path)
    for par in doc.Paragraphs:
        line=par.Range.Text
        print(line)
    #关闭文件
    doc.Close()
    #退出Word
    mw.Quit()