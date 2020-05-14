### To DO:
# Need a random integer generator from 0 to 9 for each team
#   - easiest approach is to do a shuffle of the 10 numbers (DONE)
#   - option two is to use randint on the numbers and remove a number from the list once selected
# Print out to GUI or text doc (DONE)
# Cycle through numbers quickly and end on value one at a time.  *add a delay to slow the reveal
# package as android app
# create function to text message numbers.

import wx
import wx.adv
from random import shuffle


class Marty(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'MARTY', size=(800, 600))
        self.answer_font = wx.Font(25, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD)
        self.num_font = wx.Font(33, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        self.CenterOnScreen()
        self.CreateStatusBar()

        self.panel=wx.Panel(self)
        self.panel.SetBackgroundColour('green')

        # Quit button
        exit_button = wx.Button(self.panel, label='Quit', pos=(700, 500), size=(60, 60))
        exit_button.Bind(wx.EVT_BUTTON, self.close_button, exit_button)
        exit_button.Bind(wx.EVT_CLOSE, self.close_window)

        # Header text
        wx.StaticText(self.panel, -1, 'Click to Generate Randomness', (320, 250))
        wx.StaticText(self.panel, -1, 'TEAM 1', (125, 50))
        wx.StaticText(self.panel, -1, 'TEAM 2', (475, 50))

        ### Empty static text to destroy for purposes of resetting
        self.teamOne_1 = wx.StaticText(self.panel, -1, '')
        self.teamOne_2 = wx.StaticText(self.panel, -1, '')
        self.teamOne_3 = wx.StaticText(self.panel, -1, '')
        self.teamOne_4 = wx.StaticText(self.panel, -1, '')
        self.teamOne_5 = wx.StaticText(self.panel, -1, '')
        self.teamOne_6 = wx.StaticText(self.panel, -1, '')
        self.teamOne_7 = wx.StaticText(self.panel, -1, '')
        self.teamOne_8 = wx.StaticText(self.panel, -1, '')
        self.teamOne_9 = wx.StaticText(self.panel, -1, '')
        self.teamOne_10 = wx.StaticText(self.panel, -1, '')

        self.teamTwo_1 = wx.StaticText(self.panel, -1, '')
        self.teamTwo_2 = wx.StaticText(self.panel, -1, '')
        self.teamTwo_3 = wx.StaticText(self.panel, -1, '')
        self.teamTwo_4 = wx.StaticText(self.panel, -1, '')
        self.teamTwo_5 = wx.StaticText(self.panel, -1, '')
        self.teamTwo_6 = wx.StaticText(self.panel, -1, '')
        self.teamTwo_7 = wx.StaticText(self.panel, -1, '')
        self.teamTwo_8 = wx.StaticText(self.panel, -1, '')
        self.teamTwo_9 = wx.StaticText(self.panel, -1, '')
        self.teamTwo_10 = wx.StaticText(self.panel, -1, '')

        # Creating a bitmap button
        image_random = wx.Bitmap('/Users/delue003/PycharmProjects/random_button.jpg')
        self.random_button = wx.BitmapButton(self.panel, -1, image_random, pos=(300,275), name='eric')
        self.Bind(wx.EVT_BUTTON, self.delay_1sec, self.random_button)
        self.Bind(wx.EVT_BUTTON, self.delay_2sec, self.random_button)
        self.Bind(wx.EVT_BUTTON, self.delay_3sec, self.random_button)
        self.Bind(wx.EVT_BUTTON, self.delay_4sec, self.random_button)
        self.Bind(wx.EVT_BUTTON, self.delay_5sec, self.random_button)
        self.Bind(wx.EVT_BUTTON, self.delay_6sec, self.random_button)
        self.Bind(wx.EVT_BUTTON, self.delay_7sec, self.random_button)
        self.Bind(wx.EVT_BUTTON, self.delay_8sec, self.random_button)
        self.Bind(wx.EVT_BUTTON, self.delay_9sec, self.random_button)
        self.Bind(wx.EVT_BUTTON, self.delay_10sec, self.random_button)
        
        self.Bind(wx.EVT_BUTTON, self.delay_1sec_b, self.random_button)
        self.Bind(wx.EVT_BUTTON, self.delay_2sec_b, self.random_button)
        self.Bind(wx.EVT_BUTTON, self.delay_3sec_b, self.random_button)
        self.Bind(wx.EVT_BUTTON, self.delay_4sec_b, self.random_button)
        self.Bind(wx.EVT_BUTTON, self.delay_5sec_b, self.random_button)
        self.Bind(wx.EVT_BUTTON, self.delay_6sec_b, self.random_button)
        self.Bind(wx.EVT_BUTTON, self.delay_7sec_b, self.random_button)
        self.Bind(wx.EVT_BUTTON, self.delay_8sec_b, self.random_button)
        self.Bind(wx.EVT_BUTTON, self.delay_9sec_b, self.random_button)
        self.Bind(wx.EVT_BUTTON, self.delay_10sec_b, self.random_button)
        
        
        self.Bind(wx.EVT_BUTTON, self.randomizer, self.random_button)
        self.Bind(wx.EVT_BUTTON, self.sfx, self.random_button)
        self.rand_seq = []
        self.rand_seq2= []
        self.random_button.SetDefault()

        # Menus
        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        item_quit = wx.MenuItem(file_menu, 500, '&Quit\tCtrl-Q', 'Quit the program....obviously')
        file_menu.Append(item_quit)
        menu_bar.Append(file_menu, '&File')
        self.SetMenuBar(menu_bar)
        self.Bind(wx.EVT_CLOSE, self.close_window, id=500)

        # Team Input Dialogue boxes
        text_box1 = wx.TextEntryDialog(None, 'Hello, who is the first team?', 'TEAM 1', 'enter name ')
        if text_box1.ShowModal() == wx.ID_OK:
            team1 = text_box1.GetValue()
            one = wx.StaticText(self.panel, -1, team1, (90, 75))
            one.SetFont(self.answer_font)

        text_box2 = wx.TextEntryDialog(None, 'and who is their opponent?', 'TEAM 2', 'enter name ')
        if text_box2.ShowModal() == wx.ID_OK:
            team2 = text_box2.GetValue()
            two = wx.StaticText(self.panel, -1, team2, (465, 75))
            two.SetFont(self.answer_font)



    # def foo(self, event):
    #     print('This should appear after 5sec')

    # for i in range(1, 11):
    #     print('self.T1' + str(i))


    def delay_1sec(self, event):
        wx.CallLater(1000, self.T11)

    def delay_2sec(self, event):
        wx.CallLater(2000, self.T12)
        event.Skip()

    def delay_3sec(self, event):
        wx.CallLater(3000, self.T13)
        event.Skip()

    def delay_4sec(self, event):
        wx.CallLater(4000, self.T14)
        event.Skip()

    def delay_5sec(self, event):
        wx.CallLater(5000, self.T15)
        event.Skip()

    def delay_6sec(self, event):
        wx.CallLater(6000, self.T16)
        event.Skip()

    def delay_7sec(self, event):
        wx.CallLater(7000, self.T17)
        event.Skip()

    def delay_8sec(self, event):
        wx.CallLater(8000, self.T18)
        event.Skip()

    def delay_9sec(self, event):
        wx.CallLater(9000, self.T19)
        event.Skip()

    def delay_10sec(self, event):
        wx.CallLater(10000, self.T110)
        event.Skip()


    def delay_1sec_b(self, event):
        wx.CallLater(1000, self.T21)
        event.Skip()

    def delay_2sec_b(self, event):
        wx.CallLater(2000, self.T22)
        event.Skip()

    def delay_3sec_b(self, event):
        wx.CallLater(3000, self.T23)
        event.Skip()

    def delay_4sec_b(self, event):
        wx.CallLater(4000, self.T24)
        event.Skip()

    def delay_5sec_b(self, event):
        wx.CallLater(5000, self.T25)
        event.Skip()

    def delay_6sec_b(self, event):
        wx.CallLater(6000, self.T26)
        event.Skip()

    def delay_7sec_b(self, event):
        wx.CallLater(7000, self.T27)
        event.Skip()

    def delay_8sec_b(self, event):
        wx.CallLater(8000, self.T28)
        event.Skip()

    def delay_9sec_b(self, event):
        wx.CallLater(9000, self.T29)
        event.Skip()

    def delay_10sec_b(self, event):
        wx.CallLater(10000, self.T210)
        event.Skip()


    def T11(self):
        self.teamOne_1.Destroy()
        self.teamOne_1 = wx.StaticText(self.panel, -1, str(self.rand_seq[0]), pos=(140, 130))
        self.teamOne_1.SetFont(self.num_font)

    def T12(self):
        self.teamOne_2.Destroy()
        self.teamOne_2 = wx.StaticText(self.panel, -1, str(self.rand_seq[1]), pos=(140, 170))
        self.teamOne_2.SetFont(self.num_font)

    def T13(self):
        self.teamOne_3.Destroy()
        self.teamOne_3 = wx.StaticText(self.panel, -1, str(self.rand_seq[2]), pos=(140, 210))
        self.teamOne_3.SetFont(self.num_font)

    def T14(self):
        self.teamOne_4.Destroy()
        self.teamOne_4 = wx.StaticText(self.panel, -1, str(self.rand_seq[3]), pos=(140, 250))
        self.teamOne_4.SetFont(self.num_font)

    def T15(self):
        self.teamOne_5.Destroy()
        self.teamOne_5 = wx.StaticText(self.panel, -1, str(self.rand_seq[4]), pos=(140, 290))
        self.teamOne_5.SetFont(self.num_font)

    def T16(self):
        self.teamOne_6.Destroy()
        self.teamOne_6 = wx.StaticText(self.panel, -1, str(self.rand_seq[5]), pos=(140, 330))
        self.teamOne_6.SetFont(self.num_font)

    def T17(self):
        self.teamOne_7.Destroy()
        self.teamOne_7 = wx.StaticText(self.panel, -1, str(self.rand_seq[6]), pos=(140, 370))
        self.teamOne_7.SetFont(self.num_font)

    def T18(self):
        self.teamOne_8.Destroy()
        self.teamOne_8 = wx.StaticText(self.panel, -1, str(self.rand_seq[7]), pos=(140, 410))
        self.teamOne_8.SetFont(self.num_font)

    def T19(self):
        self.teamOne_9.Destroy()
        self.teamOne_9 = wx.StaticText(self.panel, -1, str(self.rand_seq[8]), pos=(140, 450))
        self.teamOne_9.SetFont(self.num_font)

    def T110(self):
        self.teamOne_10.Destroy()
        self.teamOne_10 = wx.StaticText(self.panel, -1, str(self.rand_seq[9]), pos=(140, 490))
        self.teamOne_10.SetFont(self.num_font)


    def T21(self):
        self.teamTwo_1.Destroy()
        self.teamTwo_1 = wx.StaticText(self.panel, -1, str(self.rand_seq2[0]), pos=(260, 130))
        self.teamTwo_1.SetFont(self.num_font)

    def T22(self):
        self.teamTwo_2.Destroy()
        self.teamTwo_2 = wx.StaticText(self.panel, -1, str(self.rand_seq2[1]), pos=(300, 130))
        self.teamTwo_2.SetFont(self.num_font)

    def T23(self):
        self.teamTwo_3.Destroy()
        self.teamTwo_3 = wx.StaticText(self.panel, -1, str(self.rand_seq2[2]), pos=(340, 130))
        self.teamTwo_3.SetFont(self.num_font)

    def T24(self):
        self.teamTwo_4.Destroy()
        self.teamTwo_4 = wx.StaticText(self.panel, -1, str(self.rand_seq2[3]), pos=(380, 130))
        self.teamTwo_4.SetFont(self.num_font)

    def T25(self):
        self.teamTwo_5.Destroy()
        self.teamTwo_5 = wx.StaticText(self.panel, -1, str(self.rand_seq2[4]), pos=(420, 130))
        self.teamTwo_5.SetFont(self.num_font)

    def T26(self):
        self.teamTwo_6.Destroy()
        self.teamTwo_6 = wx.StaticText(self.panel, -1, str(self.rand_seq2[5]), pos=(460, 130))
        self.teamTwo_6.SetFont(self.num_font)

    def T27(self):
        self.teamTwo_7.Destroy()
        self.teamTwo_7 = wx.StaticText(self.panel, -1, str(self.rand_seq2[6]), pos=(500, 130))
        self.teamTwo_7.SetFont(self.num_font)

    def T28(self):
        self.teamTwo_8.Destroy()
        self.teamTwo_8 = wx.StaticText(self.panel, -1, str(self.rand_seq2[7]), pos=(540, 130))
        self.teamTwo_8.SetFont(self.num_font)

    def T29(self):
        self.teamTwo_9.Destroy()
        self.teamTwo_9 = wx.StaticText(self.panel, -1, str(self.rand_seq2[8]), pos=(580, 130))
        self.teamTwo_9.SetFont(self.num_font)

    def T210(self):
        self.teamTwo_10.Destroy()
        self.teamTwo_10 = wx.StaticText(self.panel, -1, str(self.rand_seq2[9]), pos=(620, 130))
        self.teamTwo_10.SetFont(self.num_font)


    def randomizer(self, event):
        self.rand_seq = [i for i in range(10)]
        shuffle(self.rand_seq)
        self.rand_seq2 = [j for j in range(10)]
        shuffle(self.rand_seq2)
        print('Team 1: ' + str(self.rand_seq))
        print('Team 2: ' + str(self.rand_seq2))
        event.Skip()


    def sfx(self, event):
        try:
            coin = wx.adv.Sound('/Users/delue003/PycharmProjects/coin.wav')
            coin.Play(wx.adv.SOUND_SYNC)
        except NotImplementedError as v:
            wx.MessageBox(str(v), 'Exception Message')
        event.Skip()


    def close_button(self, event):
        self.Close(True)


    def close_window(self, event):
        self.Destroy()



if __name__=='__main__':
    app=wx.App()
    frame=Marty(parent=None, id=-1)
    frame.Show()
    app.MainLoop()