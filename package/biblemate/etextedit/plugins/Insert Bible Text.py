def insert_bible_text(event=None):
    from agentmake.plugins.uba.lib.BibleParser import BibleVerseParser
    from biblemate.api.api import run_bm_api
    from biblemate import config

    buffer = event.app.current_buffer if event is not None else text_field.buffer
    selectedText = buffer.copy_selection().text
    references = BibleVerseParser(False).extractAllReferencesReadable(selectedText)
    bible_text = run_bm_api(f"verses:::{config.default_bible}:::{references}")
    buffer.insert_text(format_assistant_content(bible_text))
    get_app().reset()
