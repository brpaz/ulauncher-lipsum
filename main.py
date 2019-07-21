""" Ulauncher Lipsum Extension """
import logging
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
import lorem

LOGGER = logging.getLogger(__name__)

TYPE_SENTENCE = "SENTENCE"
TYPE_TEXT = "TEXT"
TYPE_PARAGRAPH = "PARAGRAPH"


class LipsumExtension(Extension):
    """ Extension entrypoint """

    def __init__(self):
        LOGGER.info('init Lipsum Extension')
        super(LipsumExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())


class KeywordQueryEventListener(EventListener):
    """ Listens Query event """

    def on_event(self, event, extension):
        """ Handles event """
        items = []

        items.append(
            ExtensionResultItem(icon='images/icon.png',
                                name="Sentence",
                                highlightable=False,
                                on_enter=ExtensionCustomAction(
                                    {'type': TYPE_SENTENCE})))

        items.append(
            ExtensionResultItem(icon='images/icon.png',
                                name="Paragraph",
                                highlightable=False,
                                on_enter=ExtensionCustomAction(
                                    {'type': TYPE_PARAGRAPH})))

        items.append(
            ExtensionResultItem(icon='images/icon.png',
                                name="Text",
                                highlightable=False,
                                on_enter=ExtensionCustomAction(
                                    {'type': TYPE_TEXT})))

        return RenderResultListAction(items)


class ItemEnterEventListener(EventListener):
    """ Handles ItenEvent """
    def on_event(self, event, extension):
        """ Handle function """
        data = event.get_data()
        text = ""

        if data['type'] == TYPE_PARAGRAPH:
            text = lorem.paragraph()

        if data['type'] == TYPE_SENTENCE:
            text = lorem.sentence()

        if data['type'] == TYPE_TEXT:
            text = lorem.text()

        return CopyToClipboardAction(text).run()


if __name__ == '__main__':
    LipsumExtension().run()
