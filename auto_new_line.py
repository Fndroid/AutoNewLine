import sublime
import sublime_plugin
import os


class AutoNewLineCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		settings = sublime.load_settings('auto_new_line.sublime-settings')
		ignore_subfix = settings.get('ignore_subfix')
		file_name = self.view.file_name().split('\\')[-1]
		for region in self.view.sel():
			line = self.view.line(region)
			line_content = self.view.substr(line)
			dis = 0
			if ';' not in line_content and file_name.split('.')[-1] not in ignore_subfix:
				self.view.insert(edit, line.b, ';')
				dis = 1
			self.view.sel().clear()
			line_end = line.b + dis
			self.view.sel().add(sublime.Region(line_end, line_end))
			self.view.run_command('insert', args={"characters": "\n"})

class AutoNewLineSettingOptionsCommand(sublime_plugin.TextCommand):
	def run(self, _):
		window = self.view.window()
		home_path = '\\'.join(__file__.split('\\')[:-1])
		window.open_file(home_path + '\\auto_new_line.sublime-settings')

class AutoNewLineKeymapOptionsCommand(sublime_plugin.TextCommand):
	def run(self, _):
		window = self.view.window()
		home_path = '\\'.join(__file__.split('\\')[:-1])
		window.open_file(home_path + '\\Default (Windows).sublime-keymap')