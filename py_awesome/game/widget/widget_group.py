from ...game.widget.widget import Widget

class WidgetGroup:
    '''
    WidgetGroup is a group of widgets.
    widgets: list - the list of widgets
    '''
    def __init__(self):
        self.widgets = []
    
    def add(self, widget: Widget):
        self.widgets.append(widget)
    
    def remove(self, widget: Widget):
        self.widgets.remove(widget)
    
    def __render__(self, display):
        for widget in self.widgets:
            widget.__render__(display)
    def __update__(self, event):
        for widget in self.widgets:
            widget.__update__(event) 