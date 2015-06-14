import sublime_plugin

class SelectByIndexFromRightCommand(sublime_plugin.WindowCommand):
    def run(self, index):
        group = self.window.active_group()
        views = self.window.views_in_group(group)
        
        if index >= -len(views) and index < 0:
            view = views[index]
            self.window.focus_view(view)