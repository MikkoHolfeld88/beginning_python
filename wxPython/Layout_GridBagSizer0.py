import wx
# -*- coding: utf-8 -*-


class Example(wx.Frame):

    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        self.InitUI()
        self.Centre()

    def InitUI(self):

        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(4, 4)   # 4 rows and 4 columns

        text = wx.StaticText(panel, label="Umbennenen als")
        sizer.Add(text, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5) # flags = sides where border will be used

        tc = wx.TextCtrl(panel)
        sizer.Add(tc, pos=(1, 0), span=(1, 5), # sizer = GridBagSizer /  span of (1, 5) spans a widget across 1 row and 5 columns
            flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)

        buttonOk = wx.Button(panel, label="Ok", size=(90, 28))
        buttonClose = wx.Button(panel, label="Close", size=(90, 28))
        sizer.Add(buttonOk, pos=(3, 3)) # 4th row and 4th column
        sizer.Add(buttonClose, pos=(3, 4), flag=wx.RIGHT|wx.BOTTOM, border=10) # 4th row, 5th column

        sizer.AddGrowableCol(1) # column 2, grows
        sizer.AddGrowableRow(2) # row 3 grows
        panel.SetSizer(sizer)   # Sizer wird auf Panel angewendet

def main():

    app = wx.App()
    ex = Example(None, title='GridBagSizer')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
