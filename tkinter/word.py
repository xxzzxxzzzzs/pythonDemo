# -*- coding: cp936 -*-
# -*- coding: UTF-8 -*-
import docx
import  os

from docx import Document
path="/Users/zzs/Documents/����Git�ͻ��˵��÷�.docx"
def readWord(path):
    document = Document(path)
    for paragraph in document.paragraphs:
        print(paragraph.text)
def makeWord(names):
    for name in  names:
        path=os.path.join(os.getcwd(),name)
        doc=docx.Document()
        doc.add_paragraph("��")
        doc.add_paragraph("ɽ����ĺܸ�"+name+"    ")
        doc.add_paragraph("�ߵ�����")
        doc.add_paragraph("������")
        doc.add_paragraph("ʵ���Ǹ�")
        doc.save(path+".docx")




# readWord(path)

makeWord(["zzs1","zzs2","zzs3"])


