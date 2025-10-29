from prompt_toolkit import HTML
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts import input_dialog, radiolist_dialog, checkboxlist_dialog
from prompt_toolkit.completion import WordCompleter, FuzzyCompleter


class TerminalModeDialogs:

    def __init__(self, parent=None) -> None:
        self.parent = parent

        #terminalHeadingTextColor = 'ansigreen'
        terminalResourceLinkColor = 'ansiyellow'
        #terminalCommandEntryColor1 = 'ansiyellow'
        #terminalPromptIndicatorColor1 = 'ansimagenta'
        terminalCommandEntryColor2 = 'ansigreen'
        terminalPromptIndicatorColor2 = 'ansicyan'
        #terminalSearchHighlightBackground = 'ansiblue'
        #terminalSearchHighlightForeground = 'ansidefault'

        self.style = Style.from_dict(
            {
                "dialog": "bg:ansiblack", # or "dialog": "bg:ansiwhite",
                "dialog text-area": f"bg:ansiblack {terminalCommandEntryColor2}",
                "dialog text-area.prompt": terminalPromptIndicatorColor2,
                "dialog radio-checked": terminalResourceLinkColor,
                "dialog checkbox-checked": terminalResourceLinkColor,
                "dialog button.arrow": terminalResourceLinkColor,
                "dialog button.focused": f"bg:{terminalResourceLinkColor} ansiblack",
                "dialog frame.border": terminalResourceLinkColor,
                "dialog frame.label": f"bg:ansiblack {terminalResourceLinkColor}",
                "dialog.body": "bg:ansiblack ansiwhite", # or "dialog.body": "bg:ansiwhite ansiblack",
                "dialog shadow": "bg:ansiblack", # or "dialog shadow": "bg:ansiwhite",
            }
        )

    async def getValidOptions(self, options=[], descriptions=[], bold_descriptions=False, filter="", default="", title="Available Options", text="Select an option:") -> str:
        if not options:
            return ""
        filter = filter.strip().lower()
        if descriptions:
            descriptionslower = [i.lower() for i in descriptions]
            values = [(option, HTML(f"<b>{descriptions[index]}</b>") if bold_descriptions else descriptions[index]) for index, option in enumerate(options) if (filter in option.lower() or filter in descriptionslower[index])]
        else:
            values = [(option, option) for option in options if filter in option.lower()]
        if not values:
            if descriptions:
                values = [(option, HTML(f"<b>{descriptions[index]}</b>") if bold_descriptions else descriptions[index]) for index, option in enumerate(options)]
            else:
                values = [(option, option) for option in options]
        result = await radiolist_dialog(
            title=title,
            text=text,
            values=values,
            default=default if default and default in options else values[0][0],
            style=self.style,
        ).run_async()
        return result if result else ""

    async def getMultipleSelection(self, title="Multiple Selection", text="Select item(s):", options=["ALL"], descriptions=[], default_values=["ALL"]):
        if descriptions:
            values = [(option, descriptions[index]) for index, option in enumerate(options)]
        else:
            values = [(option, option) for option in options]
        return await checkboxlist_dialog(
            title=title,
            text=text,
            values=values,
            default_values=default_values,
            style=self.style,
        ).run_async()

    async def getInputDialog(self, title="Input Dialog", text="Please type your entry:", default="", suggestions=None):
        if suggestions:
            if isinstance(suggestions, list):
                completer = FuzzyCompleter(WordCompleter(suggestions, ignore_case=True))
            else:
                completer = suggestions
        else:
            completer = None
        return await input_dialog(
            title=title,
            text=text,
            default=default,
            style=self.style,
            completer=completer,
        ).run_async()
    
    def getInputDialog_sync(self, title="Input Dialog", text="Please type your entry:", default="", suggestions=None):
        if suggestions:
            if isinstance(suggestions, list):
                completer = FuzzyCompleter(WordCompleter(suggestions, ignore_case=True))
            else:
                completer = suggestions
        else:
            completer = None
        return input_dialog(
            title=title,
            text=text,
            default=default,
            style=self.style,
            completer=completer,
        ).run()
