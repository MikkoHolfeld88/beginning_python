import wx
# -*- coding: utf-8 -*-

class Example(wx.Frame):

    def __init__(self, parent, title):
        super().__init__(parent, title=title,size=(800, 250))

        self.Centre()

def main():

    app = wx.App()
    ex = Example(None, title='Moving')
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
