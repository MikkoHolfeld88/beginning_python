import wx
# -*- coding: utf-8 -*-


class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):

        panel = wx.Panel(self)                                  # panel erstellen (parent, Objektself)

        hbox = wx.BoxSizer(wx.HORIZONTAL)                         # BoxSizer erstellen

        fgs = wx.FlexGridSizer(3,2,9,25)

        title = wx.StaticText(panel, label="Titel")             # panel ist hier immer parent, d.h.
        autor = wx.StaticText(panel, label="Autor")             # diese Objekte werden auf dem Panel
        review = wx.StaticText(panel, label="Rezension")        # erzeugt

        tc1 = wx.TextCtrl(panel)
        tc2 = wx.TextCtrl(panel)
        tc3 = wx.TextCtrl(panel,style=wx.TE_MULTILINE)

        fgs.AddMany([(title),(tc1,2,wx.EXPAND), (autor),(tc2,1,wx.EXPAND),
                     (review,1,wx.EXPAND),(tc3,1,wx.EXPAND)])

        fgs.AddGrowableRow(2,1)     # das Objekt in der 3. Reihe, 2.Spalten soll Platz nutzen
        fgs.AddGrowableCol(1,1)     # das Objekt in der 2. Spalte, soll Platz nutzen

        hbox.Add(fgs, proportion=1, flag=wx.ALL|wx.EXPAND, border=15)
        panel.SetSizer(hbox)

def main():

    app = wx.App()
    ex = Example(None, title='FlexGridSizer')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
