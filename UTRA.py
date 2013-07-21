# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.lib.mixins.listctrl as listmix

###########################################################################
## Class MyFrame1
###########################################################################
class ListCtrl(wx.ListCtrl, listmix.CheckListCtrlMixin, listmix.ListCtrlAutoWidthMixin):
    def __init__(self, *args, **kwargs):
        wx.ListCtrl.__init__(self, *args, **kwargs)
        listmix.CheckListCtrlMixin.__init__(self)
        listmix.ListCtrlAutoWidthMixin.__init__(self)
        self.InsertColumn(0, "Name")
        self.InsertColumn(1, "Size",width = 85)
        self.setResizeColumn(0)              

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 475,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 475,600 ), wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel3 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		#self.m_staticText4 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Save As", wx.DefaultPosition, wx.DefaultSize, 0 )
		#self.m_staticText4.Wrap( -1 )
		#bSizer7.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		#bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		#m_comboBox3Choices = []
		#self.m_comboBox3 = wx.ComboBox( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox3Choices, 0 )
		#bSizer8.Add( self.m_comboBox3, 1, wx.ALL, 5 )
		
		#self.m_button4 = wx.Button( self.m_panel3, wx.ID_ANY, u"...", wx.DefaultPosition, wx.Size( 30,25 ), 0 )
		#bSizer8.Add( self.m_button4, 0, wx.ALL, 5 )
		
		#bSizer7.Add( bSizer8, 1, wx.EXPAND, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer0 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_checkBox1 = wx.CheckBox( self.m_panel3, wx.ID_ANY, u"start torrent", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox1.SetValue(1)
		bSizer0.Add( self.m_checkBox1, 0, wx.ALL, 5 )
		
		self.m_checkBox0 = wx.CheckBox( self.m_panel3, wx.ID_ANY, u"delete .torrent file", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox0.SetValue(1)
		bSizer0.Add( self.m_checkBox0, 0, wx.ALL, 5 )
		
		self.infiniteupload = wx.CheckBox( self.m_panel3, wx.ID_ANY, u"enable infinite upload", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.infiniteupload.SetValue(0)
		bSizer0.Add( self.infiniteupload, 0, wx.ALL, 5 )
		
		bSizer9.Add(bSizer0, 1, wx.EXPAND, 5 )
		bSizer9.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText5 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Label:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer9.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		m_comboBox4Choices = []
		self.m_comboBox4 = wx.ComboBox( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox4Choices, 0 )
		self.m_comboBox4.SetMinSize( wx.Size( 150,-1 ) )
		
		bSizer9.Add( self.m_comboBox4, 0, wx.ALL, 5 )
		
		bSizer7.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		self.m_staticline2 = wx.StaticLine( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer7.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel3.SetSizer( bSizer7 )
		self.m_panel3.Layout()
		bSizer7.Fit( self.m_panel3 )
		bSizer4.Add( self.m_panel3, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel4 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText6 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Torrent Content", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer10.Add( self.m_staticText6, 0, wx.ALIGN_LEFT|wx.ALIGN_TOP|wx.ALL, 5 )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer1 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText19 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		fgSizer1.Add( self.m_staticText19, 0, wx.ALL, 5 )
		
		self.m_staticText20 = wx.StaticText( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( 1 )
		fgSizer1.Add( self.m_staticText20, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText21 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Comment:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		fgSizer1.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		self.m_staticText22 = wx.StaticText( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( 1 )
		fgSizer1.Add( self.m_staticText22, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText23 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Size:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		fgSizer1.Add( self.m_staticText23, 0, wx.ALL, 5 )
		
		self.m_staticText24 = wx.StaticText( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( 1 )
		fgSizer1.Add( self.m_staticText24, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText25 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Date:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		fgSizer1.Add( self.m_staticText25, 0, wx.ALL, 5 )
		
		self.m_staticText26 = wx.StaticText( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		fgSizer1.Add( self.m_staticText26, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer11.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		self.m_button5 = wx.Button( self.m_panel4, wx.ID_ANY, u"Select All", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button5, 0, wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_button6 = wx.Button( self.m_panel4, wx.ID_ANY, u"Select None", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button6, 0, wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		bSizer10.Add( bSizer11, 0, wx.EXPAND, 5 )
		
		self.m_treeCtrl1 = ListCtrl( self.m_panel4,  style=wx.LC_REPORT)
		bSizer10.Add( self.m_treeCtrl1, 1, wx.ALIGN_BOTTOM|wx.EXPAND, 5 )
		
		self.m_panel4.SetSizer( bSizer10 )
		self.m_panel4.Layout()
		bSizer10.Fit( self.m_panel4 )
		bSizer4.Add( self.m_panel4, 3, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline4 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LC_SORT_ASCENDING )
		bSizer4.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel5 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button1 = wx.Button( self.m_panel5, wx.ID_ANY, u"Advanced...", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button1, 0, wx.ALL, 5 )
		
		
		bSizer6.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button2 = wx.Button( self.m_panel5, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button2.SetDefault() 
		bSizer6.Add( self.m_button2, 0, wx.ALL, 5 )
		
		self.m_button3 = wx.Button( self.m_panel5, wx.ID_ANY, u"CANCEL", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button3, 0, wx.ALL, 5 )
		
		self.m_panel5.SetSizer( bSizer6 )
		self.m_panel5.Layout()
		bSizer6.Fit( self.m_panel5 )
		bSizer4.Add( self.m_panel5, 0, wx.EXPAND|wx.LEFT|wx.RIGHT, 5 )
		
		self.m_panel1.SetSizer( bSizer4 )
		self.m_panel1.Layout()
		bSizer4.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		#self.m_button4.Bind( wx.EVT_BUTTON, self.savefiledialogbuttonclick )
		self.m_button5.Bind( wx.EVT_BUTTON, self.selectallbuttonclick )
		self.m_button6.Bind( wx.EVT_BUTTON, self.selectnonebuttonclick )
		self.m_button1.Bind( wx.EVT_BUTTON, self.advancedbuttonclick )
		self.m_button2.Bind( wx.EVT_BUTTON, self.okbuttonclick )
		self.m_button3.Bind( wx.EVT_BUTTON, self.cancelbuttonclick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def savefiledialogbuttonclick( self, event ):
		event.Skip()
	
	def selectallbuttonclick( self, event ):
		event.Skip()
	
	def selectnonebuttonclick( self, event ):
		event.Skip()
	
	def advancedbuttonclick( self, event ):
		event.Skip()
	
	def okbuttonclick( self, event ):
		event.Skip()
	
	def cancelbuttonclick( self, event ):
		event.Skip()
	

