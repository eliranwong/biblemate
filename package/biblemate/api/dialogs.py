from biblemate import config, DIALOGS
from agentmake.plugins.uba.lib.BibleBooks import BibleBooks
from agentmake.plugins.uba.lib.BibleParser import BibleVerseParser
import re

BIBLE_SEARCH_SCOPES = [
    "search",
    "genesis",
    "exodus",
    "leviticus",
    "numbers",
    "deuteronomy",
    "joshua",
    "judges",
    "ruth",
    "samuel1",
    "samuel2",
    "kings1",
    "kings2",
    "chronicles1",
    "chronicles2",
    "ezra",
    "nehemiah",
    "esther",
    "job",
    "psalms",
    "proverbs",
    "ecclesiastes",
    "songs",
    "isaiah",
    "jeremiah",
    "lamentations",
    "ezekiel",
    "daniel",
    "hosea",
    "joel",
    "amos",
    "obadiah",
    "jonah",
    "micah",
    "nahum",
    "habakkuk",
    "zephaniah",
    "haggai",
    "zechariah",
    "malachi",
    "matthew",
    "mark",
    "luke",
    "john",
    "acts",
    "romans",
    "corinthians1",
    "corinthians2",
    "galatians",
    "ephesians",
    "philippians",
    "colossians",
    "thessalonians1",
    "thessalonians2",
    "timothy1",
    "timothy2",
    "titus",
    "philemon",
    "hebrews",
    "james",
    "peter1",
    "peter2",
    "john1",
    "john2",
    "john3",
    "jude",
    "revelation",
]

# shared dialogs

async def get_multiple_bibles(options, descriptions):
    select = await DIALOGS.getMultipleSelection(
        default_values=config.last_multi_bible_selection,
        options=options,
        descriptions=descriptions,
        title="Bibles",
        text="Select versions to continue:"
    )
    if select:
        config.last_multi_bible_selection = select
        return select
    return []

async def get_reference(verse_reference=True, exhaustiveReferences=False):
    abbr = BibleBooks.abbrev["eng"]
    input_suggestions = []
    for book in range(1,67):
        input_suggestions += list(abbr[str(book)])
    result = await DIALOGS.getInputDialog(title="Bible Verse Reference", text="Enter a verse reference, e.g. John 3:16", default=config.last_bible_reference, suggestions=input_suggestions)
    if result:
        parser = BibleVerseParser(False)
        result = parser.extractExhaustiveReferencesReadable(result) if exhaustiveReferences else parser.extractAllReferencesReadable(result)
        if result and not verse_reference:
            result = re.sub(r":[\-0-9]+?;", ";", f"{result};")[:-1]
    if result:
        config.last_bible_reference = result
        return result
    if not result:
        abbr = BibleBooks.abbrev["eng"]
        book = await DIALOGS.getValidOptions(
            default=str(config.last_book),
            options=[str(book) for book in range(1,67)],
            descriptions=[abbr[str(book)][-1] for book in range(1,67)],
            title="Bible Book",
            text="Select a book to continue:"
        )
        if not book:
            return ""
        config.last_book = book = int(book)
        chapter = await DIALOGS.getValidOptions(
            default=str(config.last_chapter),
            options=[str(chapter) for chapter in range(1,BibleBooks.chapters[int(book)]+1)],
            title="Bible Chapter",
            text="Select a chapter to continue:"
        )
        if not chapter:
            return ""
        config.last_chapter = chapter = int(chapter)
        if verse_reference:
            verse = await DIALOGS.getValidOptions(
                default=str(config.last_verse),
                options=[str(verse) for verse in range(1,BibleBooks.verses[int(book)][int(chapter)]+1)],
                title="Bible Verse",
                text="Select a verse to continue:"
            )
            if not verse:
                return ""
            config.last_verse = verse = int(verse)
            return f"{abbr[str(book)][0]} {chapter}:{verse}"
        return f"{abbr[str(book)][0]} {chapter}"

# dialogs for content retrieval

async def uba_search_bible(options, descriptions):
    select = await DIALOGS.getValidOptions(
        default=config.default_bible,
        options=options,
        descriptions=descriptions,
        title="Search Bible",
        text="Select a bible version to continue:"
    )
    if not select:
        return ""
    abbr = BibleBooks.abbrev["eng"]
    book = await DIALOGS.getValidOptions(
        default=str(config.last_book),
        options=["0"]+[str(book) for book in range(1,67)],
        descriptions=["ALL"]+[abbr[str(book)][-1] for book in range(1,67)],
        title="Search in Book(s)",
        text="Select all books or a book to continue:"
    )
    if not book:
        return ""
    template = BIBLE_SEARCH_SCOPES[int(book)]
    result = await DIALOGS.getInputDialog(title="Search Item", text="Enter an item to search for:")
    if not result:
        return ""
    return f"//{template}/{select}/{result}" if result else ""

async def uba_bible(options, descriptions):
    select = await DIALOGS.getValidOptions(
        default=config.default_bible,
        options=options,
        descriptions=descriptions,
        title="Bible",
        text="Select a bible version to continue:"
    )
    if not select:
        return ""
    result = await get_reference()
    return f"//bible/{select}/{result}" if result else ""

async def uba_ref(options, descriptions):
    select = await DIALOGS.getValidOptions(
        default=config.default_bible,
        options=options,
        descriptions=descriptions,
        title="Cross-References",
        text="Select a bible version to continue:"
    )
    if not select:
        return ""
    result = await get_reference()
    return f"//xref/{select}/{result}" if result else ""

async def uba_treasury(options, descriptions):
    select = await DIALOGS.getValidOptions(
        default=config.default_bible,
        options=options,
        descriptions=descriptions,
        title="Treasury of Scripture Knowledge",
        text="Select a bible version to continue:"
    )
    if not select:
        return ""
    result = await get_reference()
    return f"//treasury/{select}/{result}" if result else ""

async def uba_chapter(options, descriptions):
    select = await DIALOGS.getValidOptions(
        default=config.default_bible,
        options=options,
        descriptions=descriptions,
        title="Bible",
        text="Select a bible version to continue:"
    )
    if not select:
        return ""
    result = await get_reference(verse_reference=False)
    return f"//chapter/{select}/{result}" if result else ""

async def uba_compare(options, descriptions):
    select = await get_multiple_bibles(options, descriptions)
    if not select:
        return ""
    else:
        select = ",".join(select)
    result = await get_reference()
    return f"//bm/verses:::{select}:::{result}" if result else ""

async def uba_compare_chapter(options, descriptions):
    select = await get_multiple_bibles(options, descriptions)
    if not select:
        return ""
    else:
        select = ",".join(select)
    result = await get_reference(verse_reference=False)
    return f"//bm/comparechapter:::{select}:::{result}" if result else ""

async def uba_commentary(options, descriptions):
    select = await DIALOGS.getValidOptions(
        default=config.default_commentary,
        options=options,
        descriptions=descriptions,
        title="Bible Commentary",
        text="Select a commentary to continue:"
    )
    if not select:
        return ""
    result = await get_reference()
    return f"//commentary/{select}/{result}" if result else ""

async def uba_aicommentary():
    result = await get_reference()
    return f"//aicommentary/{result}" if result else ""

async def uba_index():
    result = await get_reference()
    return f"//index/{result}" if result else ""

async def uba_translation():
    result = await get_reference()
    return f"//translation/{result}" if result else ""

async def uba_discourse():
    result = await get_reference()
    return f"//discourse/{result}" if result else ""

async def uba_morphology():
    result = await get_reference()
    return f"//morphology/{result}" if result else ""

async def uba_dictionary():
    result = await DIALOGS.getInputDialog(title="Search Dictionary", text="Enter a search item:")
    return f"//dictionary/{result.strip()}" if result and result.strip() else ""

async def uba_parallel(options, descriptions):
    select = await DIALOGS.getValidOptions(
        default=config.default_bible,
        options=options,
        descriptions=descriptions,
        title="Search Bible Parallels",
        text="Select a bible version to continue:"
    )
    if not select:
        return ""
    result = await DIALOGS.getInputDialog(title="Search Bible Parallels", text="Enter a search item:")
    return f"//parallel/{select}/{result.strip()}" if result and result.strip() else ""

async def uba_promise(options, descriptions):
    select = await DIALOGS.getValidOptions(
        default=config.default_bible,
        options=options,
        descriptions=descriptions,
        title="Search Bible Promises",
        text="Select a bible version to continue:"
    )
    if not select:
        return ""
    result = await DIALOGS.getInputDialog(title="Search Bible Promises", text="Enter a search item:")
    return f"//promise/{select}/{result.strip()}" if result and result.strip() else ""

async def uba_topic():
    result = await DIALOGS.getInputDialog(title="Search Bible Topics", text="Enter a search item:")
    return f"//topic/{result.strip()}" if result and result.strip() else ""

async def uba_name():
    result = await DIALOGS.getInputDialog(title="Search Bible Names", text="Enter a search item:")
    return f"//name/{result.strip()}" if result and result.strip() else ""

async def uba_character():
    result = await DIALOGS.getInputDialog(title="Search Bible Characters", text="Enter a search item:")
    return f"//character/{result.strip()}" if result and result.strip() else ""

async def uba_location():
    result = await DIALOGS.getInputDialog(title="Search Bible Locations", text="Enter a search item:")
    return f"//location/{result.strip()}" if result and result.strip() else ""

async def uba_encyclopedia(options, descriptions):
    select = await DIALOGS.getValidOptions(
        default=config.default_encyclopedia,
        options=options,
        descriptions=descriptions,
        title="Encyclopedia",
        text="Select one of them to continue:"
    )
    if not select:
        return ""
    result = await DIALOGS.getInputDialog(title=f"Search Encyclopedia - {select}", text="Enter a search item:")
    return f"//encyclopedia/{select}/{result.strip()}" if result and result.strip() else ""

async def uba_lexicon(options):
    select = await DIALOGS.getValidOptions(
        default=config.default_lexicon,
        options=options,
        title="Lexicon",
        text="Select one of them to continue:"
    )
    if not select:
        return ""
    result = await DIALOGS.getInputDialog(title=f"Search Lexicon - {select}", text="Enter a search item:")
    return f"//lexicon/{select}/{result.strip()}" if result and result.strip() else ""

# Configure default modules

async def uba_default_bible(options, descriptions):
    select = await DIALOGS.getValidOptions(
        default=config.default_bible,
        options=options,
        descriptions=descriptions,
        title="Configure Default Bible",
        text="Select a bible version:"
    )
    return select if select else ""

async def uba_default_commentary(options, descriptions):
    select = await DIALOGS.getValidOptions(
        default=config.default_commentary,
        options=options,
        descriptions=descriptions,
        title="Configure Default Commentary",
        text="Select a commentary:"
    )
    return select if select else ""

async def uba_default_encyclopedia(options, descriptions):
    select = await DIALOGS.getValidOptions(
        default=config.default_encyclopedia,
        options=options,
        descriptions=descriptions,
        title="Configure Default Encyclopedia",
        text="Select an encyclopedia:"
    )
    return select if select else ""

async def uba_default_lexicon(options):
    select = await DIALOGS.getValidOptions(
        default=config.default_lexicon,
        options=options,
        title="Configure Default Lexicon",
        text="Select a lexicon:"
    )
    return select if select else ""