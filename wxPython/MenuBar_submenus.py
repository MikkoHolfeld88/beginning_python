import wx
# -*- coding: utf-8 -*-

class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__initUI()

    def __initUI(self):

        menubar = wx.MenuBar()          # erstellt Menubar (komplette Leiste)

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
        self.SetMenuBar(menubar) # menubar wird mit Menu initialisiert

        self.SetSize((350,250))
        self.SetTitle("Untermenü")
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
