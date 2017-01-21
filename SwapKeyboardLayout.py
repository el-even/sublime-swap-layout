import sublime
import sublime_plugin


class SwapKeyboardLayoutCommand(sublime_plugin.TextCommand):
    def run(self, edit, dictionary_file):
        s = sublime.load_settings(dictionary_file)
        dictionary = s.get('chars_mapping')

        # invert dict
        # reason: it was a problem loading dict with unicode keys in sublime
        dictionary = dict([[v, k] for k, v in dictionary.items()])
        # adding another direction
        dictionary.update(dict([[v, k] for k, v in dictionary.items()]))

        selections = self.view.sel()

        for sel in selections:
            selection_text = self.view.substr(sel)
            self.view.replace(edit, sel, swap(selection_text, dictionary))


def swap(input_string, dictionary):
    swap_string = []
    for char in input_string:
        swap_string.append(dictionary.get(char, char))
    return ''.join(swap_string)
