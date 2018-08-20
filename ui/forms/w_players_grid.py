import npyscreen

class WidgetPlayersGrid(npyscreen.GridColTitles):
    """docstring for SessionGridColTitles"""
    def __init__(self, *arg, **keywords):
        super(WidgetPlayersGrid, self).__init__(
            col_titles = [
                'Players'
            ],
            *arg, **keywords
        ) 

    def created(self, values=None):
        self.values = values

    def custom_print_cell(self, actual_cell, cell_display_value):
        if cell_display_value == 'Live':
            actual_cell.color = 'GOOD'
        elif cell_display_value == 'Full':
            actual_cell.color = 'DANGER'
        else:
            actual_cell.color = 'DEFAULT'