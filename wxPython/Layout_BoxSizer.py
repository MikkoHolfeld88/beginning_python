import wx
# -*- coding: utf-8 -*-


class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.InitUI()
        self.Centre()

    def InitUI(self):

        panel = wx.Panel(self)                                  # panel erstellen (parent, Objektself)

        panel.SetBackgroundColour('violet')
        vbox = wx.BoxSizer(wx.VERTICAL)                         # BoxSizer erstellen

        midPan = wx.Panel(panel)                                # 2. Panel erstellen
        midPan.SetBackgroundColour('red')

        vbox.Add(midPan, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)     # 20px Border on all 4 sides / EXPAND-flag uses available space / ALL = no align
        panel.SetSizer(vbox)                                    # BoxSizer auf Panel anwenden 

def main():

    app = wx.App()
    ex = Example(None, title='BoxSizer')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
