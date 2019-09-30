import wx
# -*- coding: utf-8 -*-

APP_EXIT = 1

class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__initUI()

    def __initUI(self):

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        qmi = wx.MenuItem(fileMenu, APP_EXIT, '&Quit\tStrg+Q')
        qmi.SetBitmap(wx.Bitmap("icon/exit.png"))
        fileMenu.Append(qmi)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=APP_EXIT) # Binding EVT_MENU to OnQuit Method

        menubar.Append(fileMenu, "&Datei") # Adding Menu to the MenuBar
        self.SetMenuBar(menubar) # sets up the MenuBar

        self.SetSize((300,600))
        self.SetTitle("Personalisiertes Menü")
        self.Centre()

    def OnQuit(self, e):
        self.Close()


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
