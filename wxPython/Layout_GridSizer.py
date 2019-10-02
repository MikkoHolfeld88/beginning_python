import wx


class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.InitUI()
        self.SetSize(400,400)
        self.Centre()

    def InitUI(self):

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        menubar.Append(fileMenu, '&Datei')
        self.SetMenuBar(menubar)

        vbox = wx.BoxSizer(wx.VERTICAL)
        self.display = wx.TextCtrl(self, style=wx.TE_LEFT)
        vbox.Add(self.display, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=6)
        gs = wx.GridSizer(5, 4, 5, 5)   # Grid(Rows, Columns, Border Rows, Border Columns)

        gs.AddMany( [(wx.Button(self, label='Clear'), 0, wx.EXPAND),    #1st Row 1
            (wx.Button(self, label='Zurück'), 0, wx.EXPAND),            #1st Row 2
            (wx.StaticText(self), wx.EXPAND),                           #1st Row 3
            (wx.Button(self, label='Ende'), 0, wx.EXPAND),              #1st Row 4
            (wx.Button(self, label='7'), 0, wx.EXPAND),                 #2nd Row 1
            (wx.Button(self, label='8'), 0, wx.EXPAND),
            (wx.Button(self, label='9'), 0, wx.EXPAND),
            (wx.Button(self, label='/'), 0, wx.EXPAND),
            (wx.Button(self, label='4'), 0, wx.EXPAND),                 #3rd Row
            (wx.Button(self, label='5'), 0, wx.EXPAND),
            (wx.Button(self, label='6'), 0, wx.EXPAND),
            (wx.Button(self, label='*'), 0, wx.EXPAND),
            (wx.Button(self, label='1'), 0, wx.EXPAND),                 #4th Row
            (wx.Button(self, label='2'), 0, wx.EXPAND),
            (wx.Button(self, label='3'), 0, wx.EXPAND),
            (wx.Button(self, label='-'), 0, wx.EXPAND),
            (wx.Button(self, label='0'), 0, wx.EXPAND),                 #5th Row
            (wx.Button(self, label='.'), 0, wx.EXPAND),
            (wx.Button(self, label='='), 0, wx.EXPAND),
            (wx.Button(self, label='+'), 0, wx.EXPAND) ])

        vbox.Add(gs, proportion=1, flag=wx.EXPAND)
        self.SetSizer(vbox)


def main():

    app = wx.App()
    ex = Example(None, title='Taschenrechner')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
