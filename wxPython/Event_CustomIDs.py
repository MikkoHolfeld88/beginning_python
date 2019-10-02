import wx

ID_MENU_NEW = wx.NewId()
labapape = wx.NewId()
ID_MENU_SAVE = wx.NewId()


class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        self.CreateMenuBar()
        self.CreateStatusBar()

        self.SetSize((350, 250))
        self.SetTitle('Custom ids')
        self.Centre()

    def CreateMenuBar(self):

        mb = wx.MenuBar()

        fMenu = wx.Menu()
        fMenu.Append(ID_MENU_NEW, 'New')
        fMenu.Append(labapape, 'Open')
        fMenu.Append(ID_MENU_SAVE, 'Save')

        mb.Append(fMenu, '&File')
        self.SetMenuBar(mb)

        self.Bind(wx.EVT_MENU, self.DisplayMessage, id=ID_MENU_NEW)
        self.Bind(wx.EVT_MENU, self.DisplayMessage, id=labapape)
        self.Bind(wx.EVT_MENU, self.DisplayMessage, id=ID_MENU_SAVE)

    def DisplayMessage(self, e):

        sb = self.GetStatusBar()

        eid = e.GetId()

        if eid == ID_MENU_NEW:
            msg = 'Menu New ausgewählt'
        elif eid == labapape:
            msg = 'Open menu item selected'
        elif eid == ID_MENU_SAVE:
            msg = 'Save menu item selected'

        sb.SetStatusText(msg)


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
