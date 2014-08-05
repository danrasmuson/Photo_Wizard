import os
import wx
 
class PhotoCtrl(wx.App):
    def __init__(self, redirect=False, filename=None):
        wx.App.__init__(self, redirect, filename)
        # wx.Frame.__init__(self, None, title=title, pos=(150,150), size=(600,600))

        self.frame = wx.Frame(None, title='Photo Control')
 
        self.panel = wx.Panel(self.frame)
 
        self.PhotoMaxSize = 240
 
        self.createWidgets()
        self.frame.Show()

        # input box
        box = wx.BoxSizer(wx.VERTICAL)
        self.m_text = wx.TextCtrl(self.panel, -1, "Hello World!")
        self.m_text.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        self.m_text.SetSize((200,100))
        box.Add(self.m_text, 0, wx.ALL, 10)
 
    def createWidgets(self):
        img = wx.EmptyImage(240,240)
        self.imageCtrl = wx.StaticBitmap(self.panel, wx.ID_ANY, 
                                         wx.BitmapFromImage(img))
 
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
 
        self.mainSizer.Add(wx.StaticLine(self.panel, wx.ID_ANY),
                           0, wx.ALL|wx.EXPAND, 5)
        self.mainSizer.Add(self.imageCtrl, 0, wx.ALL, 5)
        self.mainSizer.Add(self.sizer, 0, wx.ALL, 5)
 
        self.panel.SetSizer(self.mainSizer)
        self.mainSizer.Fit(self.frame)
 
        self.panel.Layout()

 
    def setPhoto(self, filepath):
        img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
        # scale the image, preserving the aspect ratio
        W = img.GetWidth()
        H = img.GetHeight()
        if W > H:
            NewW = self.PhotoMaxSize
            NewH = self.PhotoMaxSize * H / W
        else:
            NewH = self.PhotoMaxSize
            NewW = self.PhotoMaxSize * W / H
        img = img.Scale(NewW,NewH)
 
        self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
        self.panel.Refresh()
 
if __name__ == '__main__':
    app = PhotoCtrl()
    app.setPhoto("c:\Users\Daniel\Pictures\desk1.JPG")
    app.MainLoop()