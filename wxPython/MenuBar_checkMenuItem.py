import wx
# -*- coding: utf-8 -*-

class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__initUI()

    def __initUI(self):

        menubar = wx.MenuBar()          # erstellt Menubar (komplette Leiste)

        ansichtsMenu = wx.Menu()        # Erstellt Menu für die Leiste namens Ansichtsmenu (einen Reiter)
        self.shst = ansichtsMenu.Append(wx.ID_ANY, "Statusleiste anzeigen","Statusleite anzeigen",kind=wx.ITEM_CHECK)
        self.shtl = ansichtsMenu.Append(wx.ID_ANY, "Werkzeugleiste anzeigen","Werkzeugleiste anzeigen",kind=wx.ITEM_CHECK)
        ansichtsMenu.Check(self.shst.GetId(), True)
        ansichtsMenu.Check(self.shtl.GetId(), True)

        self.Bind(wx.EVT_MENU, self.ToggleStatusBar, self.shst)
        self.Bind(wx.EVT_MENU, self.ToggleToolBar, self.shtl)

        dateiMenu = wx.Menu()           # Erstellt Menu für die Leiste namens Dateimenu (einen Reiter)
        dateiMenu.Append(wx.ID_NEW, '&Neu')
        dateiMenu.Append(wx.ID_OPEN, '&Öffnen')
        dateiMenu.Append(wx.ID_SAVE, '&Speichern')
        dateiMenu.AppendSeparator()
        importMenu = wx.Menu()          # Erstellt Menu Import
        importMenu.Append(wx.ID_ANY, '&Importieren_a')
        importMenu.Append(wx.ID_ANY, '&Importieren_b')
        importMenu.Append(wx.ID_ANY, '&Importieren_c')
        dateiMenu.AppendMenu(wx.ID_ANY, '&Importieren', importMenu) # hängt Menu Import an DateiMenu

        qmi = wx.MenuItem(dateiMenu, wx.ID_EXIT, '&Beenden\tSTRG+Q') # Neuer Unterpunkt für Dateimenu
        icon = wx.Bitmap("icon/exit.png")
        icon.SetSize((20,20))
        qmi.SetBitmap(icon)

        dateiMenu.Append(qmi)  # und hängt es an

        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)

        menubar.Append(dateiMenu, "Datei") # Datei Menu wird an Menubar gehangen
        menubar.Append(ansichtsMenu, "Ansicht")
        self.SetMenuBar(menubar) # menubar wird mit Menu initialisiert

        self.toolbar = self.CreateToolBar()
        self.toolbar.AddTool(1, '', wx.Bitmap('icon/write.png'))
        self.toolbar.Realize()

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('Bereit')

        self.SetSize((350,250))
        self.SetTitle("Untermenü")
        self.Centre()


    def ToggleStatusBar(self, e):

        if self.shst.IsChecked():
            self.statusbar.Show()
        else:
            self.statusbar.Hide()

    def ToggleToolBar(self, e):

        if self.shtl.IsChecked():
            self.toolbar.Show()
        else:
            self.toolbar.Hide()

    def OnQuit(self, e):
        self.Close()


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
