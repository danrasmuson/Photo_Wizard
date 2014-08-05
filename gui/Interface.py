import wxversion
import wx, wx.html, wx.grid
import sys

class HtmlWindow(wx.html.HtmlWindow):
    def __init__(self, parent, id, size=(600,400)):
        wx.html.HtmlWindow.__init__(self,parent, id, size=size)
        if "gtk2" in wx.PlatformInfo:
            self.SetStandardFonts()

    def OnLinkClicked(self, link):
        wx.LaunchDefaultBrowser(link.GetHref())

class AboutBox(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, "About <<project>>",
            style=wx.DEFAULT_DIALOG_STYLE|wx.THICK_FRAME|wx.RESIZE_BORDER|
                wx.TAB_TRAVERSAL)
        hwin = HtmlWindow(self, -1, size=(400,200))
        vers = {}
        vers["python"] = sys.version.split()[0]
        vers["wxpy"] = wx.VERSION_STRING
        hwin.SetPage(aboutText % vers)
        btn = hwin.FindWindowById(wx.ID_OK)
        irep = hwin.GetInternalRepresentation()
        hwin.SetSize((irep.GetWidth()+25, irep.GetHeight()+10))
        self.SetClientSize(hwin.GetSize())
        self.CentreOnParent(wx.BOTH)
        self.SetFocus()

class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, pos=(150,150), size=(600,600))
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.panel = wx.Panel(wx.Frame)

        # menuBar = wx.MenuBar()
        # menu = wx.Menu()
        # m_exit = menu.Append(wx.ID_EXIT, "E&xit\tAlt-X", "Close window and exit program.")
        # self.Bind(wx.EVT_MENU, self.OnClose, m_exit)
        # menuBar.Append(menu, "&File")
        # menu = wx.Menu()
        # m_about = menu.Append(wx.ID_ABOUT, "&About", "Information about this program")
        # self.Bind(wx.EVT_MENU, self.OnAbout, m_about)
        # menuBar.Append(menu, "&Help")
        # self.SetMenuBar(menuBar)

        # self.statusbar = self.CreateStatusBar()
        self.frame = wx.Frame(None, title='Photo Control')
        # self.panel = wx.Panel(self.frame)
 
        # self.PhotoMaxSize = 240
 
        self.createWidgets()
        self.frame.Show()




        box = wx.BoxSizer(wx.VERTICAL)
        self.m_text = wx.TextCtrl(self.panel, -1, "Hello World!")
        self.m_text.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
        self.m_text.SetSize(self.m_text.GetBestSize())
        box.Add(self.m_text, 0, wx.ALL, 10)

        # grid = SimpleGrid(self)
        self.createWidgets()


        # m_close = wx.Button(panel, wx.ID_CLOSE, "Close")
        # m_close.Bind(wx.EVT_BUTTON, self.OnClose)
        # box.Add(m_close, 0, wx.ALL, 10)

        self.panel.SetSizer(box)
        self.panel.Layout()

    def setBodyText(self, message):
        self.m_text.SetLabel(message)

    def OnClose(self, event):
        dlg = wx.MessageDialog(self,
            "Do you really want to close this application?",
            "Confirm Exit", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == wx.ID_OK:
            self.Destroy()

    def OnAbout(self, event):
        dlg = AboutBox()
        dlg.ShowModal()
        dlg.Destroy()

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

app = wx.App(redirect=True)   # Error messages go to popup window
top = Frame("<<project>>")
top.setBodyText("daniel")
top.Show()
app.MainLoop()

# class TestFrame(wx.Frame):
#     def __init__(self, parent):
#         wx.Frame.__init__(self, parent, -1, "A Grid",
#                 size=(275, 275))
        # grid = SimpleGrid(self)

# app = wx.PySimpleApp()
# frame = TestFrame(None)
# frame.Show(True)
# app.MainLoop()
