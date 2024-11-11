import wx
import wx.grid
import pandas as pd
import re

from template_frame import WINELIST as MyFrame1

EVEN_ROW_COLOUR = '#CCE6FF'
GRID_LINE_COLOUR = '#ccc'


class DataTable(wx.grid.GridTableBase):
    def __init__(self, data=None):
        wx.grid.GridTableBase.__init__(self)
        self.headerRows = 1
        self.data = data


    def GetNumberRows(self):
        return len(self.data.index)

    def GetNumberCols(self):
        return len(self.data.columns)

    def GetValue(self, row, col):
        return self.data.iloc[row, col]

    def SetValue(self, row, col, value):
        self.data.iloc[row, col] = value

    # For better visualisation
    def GetColLabelValue(self, col):
        return self.data.columns[col]

    def GetAttr(self, row, col, prop):
        attr = wx.grid.GridCellAttr()
        if row % 2 == 1:
            attr.SetBackgroundColour(EVEN_ROW_COLOUR)
        return attr

    def SEARCH(self, event):
        print("SEARCH")

class CalcFrame(MyFrame1):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.df = pd.read_csv("./part_wine_reviews.csv")
        self.table = DataTable(self.df)
        self.m_grid3.SetTable(self.table, takeOwnership=True)
        self.m_grid3.AutoSize()
        self.Show(True)
        self.Layout()

    def OnSearch(self, event):
        event.Skip()
        keyword = self.m_textCtrl1.GetValue()
        min_value = float(self.m_textCtrl2.GetValue())
        max_value = float(self.m_textCtrl3.GetValue())

        # Filter the DataFrame based on price
        filtered_price = self.df[(self.df['price'] >= min_value) & (self.df['price'] <= max_value)]

        # Filter the descriptions based on the keyword
        index = []
        for description in filtered_price["description"]:
            if re.search(keyword, description, re.IGNORECASE):  # Added re.IGNORECASE for case-insensitive search
                index.append(True)
            else:
                index.append(False)

        df_filtered = filtered_price[index]
        self.m_grid3.ClearGrid()
        self.table = DataTable(df_filtered)
        self.m_grid3.SetTable(self.table, takeOwnership=True)
        self.m_grid3.AutoSize()
        text = f"The number of rows: {len(df_filtered)}"
        self.m_staticText5.SetLabel(text)


if __name__ == "__main__":
    app = wx.App()
    frame = CalcFrame()
    app.MainLoop()