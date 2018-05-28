import  win32com
import  win32com.client

def makeppt(path):
    ppt=win32com.client.Dispath("PowerPoint.Application")
    ppt.Visible=True

    pptFile=ppt.Presentations.Add()


    page1=pptFile.Slides.Add(1,1)
    t1=page1.Shapes[0].TextFrame.TextRange
    t1.Text="abc"

    t2 = page1.Shapes[1].TextFrame.TextRange
    t2.Text = "EFG"
    pptFile.SaveAs(path)
    pptFile.Close()
    ppt.Quit()

