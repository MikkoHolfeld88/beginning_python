import wx
# -*- coding: utf-8 -*-

class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__initUI()

    def __initUI(self):

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileItem = fileMenu.Append(wx.ID_EXIT, "Beenden","App beenden") #(ID, Name of the Item, Help Message on Statusbar)
        self.Bind(wx.EVT_MENU, self.OnQuit, fileItem) # Binding EVT_MENU to OnQuit Method

        menubar.Append(fileMenu, "&Datei") # Adding Menu to the MenuBar
        self.SetMenuBar(menubar) # sets up the MenuBar

        self.SetSize((300,200))
        self.SetTitle("Einfaches Menü")
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
