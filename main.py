""" Ulauncher Lipsum Extension """
import logging
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
import lorem

LOGGER = logging.getLogger(__name__)

class LipsumExtension(Extension):
    """ Extension entrypoint """

    def __init__(self):
        LOGGER.info('init Lipsum Extension')
        super(LipsumExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

class KeywordQueryEventListener(EventListener):
    """ Listens Query event """

    def on_event(self, event, extension):
        """ Handles event """
        items = []

        items.append(
            ExtensionResultItem(icon='images/icon.png',
                                name="Sentence",
                                highlightable=False,
                                on_enter=CopyToClipboardAction(lorem.sentence())
                                ))

        items.append(
            ExtensionResultItem(icon='images/icon.png',
                                name="Paragraph",
                                highlightable=False,
                                on_enter=CopyToClipboardAction(lorem.paragraph())
                                ))

        items.append(
            ExtensionResultItem(icon='images/icon.png',
                                name="Text",
                                highlightable=False,
                                on_enter=CopyToClipboardAction(lorem.text())
                                ))

        return RenderResultListAction(items)


if __name__ == '__main__':
    LipsumExtension().run()
