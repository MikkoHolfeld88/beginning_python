import wx
# -*- coding: utf-8 -*-

class MyPopupMenu(wx.Menu):

    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        mmi = wx.MenuItem(self, wx.NewId(), 'Minimieren')   # neues MenuItem wird kriiert
        self.Append(mmi)                                    # und dem MyPopupMenu hinzugefügt
        self.Bind(wx.EVT_MENU, self.OnMinimize, mmi)        # EventHandler, sorgt dafür das bei Auswhal OnMinimize aufgerufen wird

        sayHello = wx.MenuItem(self, wx.NewId(), 'Hallo sagen')
        self.Append(sayHello)
        self.Bind(wx.EVT_MENU, self.SayHello, sayHello)

        cmi = wx.MenuItem(self, wx.NewId(), 'Beenden')
        self.Append(cmi)
        self.Bind(wx.EVT_MENU, self.OnClose, cmi)

    def SayHello(self, e):
        print("Hallo da draußen!")

    def OnMinimize(self, e):
        self.parent.Iconize()

    def OnClose(self, e):
        self.parent.Close()


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)

        self.SetSize((350, 250))
        self.SetTitle('Context menu')
        self.Centre()

    def OnRightDown(self, e):
        self.PopupMenu(MyPopupMenu(self),e.GetPosition())

def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
