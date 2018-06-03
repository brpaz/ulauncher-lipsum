import logging
import lorem
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction

logger = logging.getLogger(__name__)

TYPE_SENTENCE = "SENTENCE"
TYPE_TEXT = "TEXT"
TYPE_PARAGRAPH = "PARAGRAPH"

class LipsumExtension(Extension):

    def __init__(self):
        logger.info('init Lipsum Extension')
        super(LipsumExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())

class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []
 
        items.append(ExtensionResultItem(
             icon='images/icon.png',
             name="Sentence",
             highlightable=False,
             on_enter=ExtensionCustomAction(
                 {'type': TYPE_SENTENCE})
        ))

        items.append(ExtensionResultItem(
             icon='images/icon.png',
             name="Paragraph",
             highlightable=False,
             on_enter=ExtensionCustomAction(
                 {'type': TYPE_PARAGRAPH})
         ))

        items.append(ExtensionResultItem(
            icon='images/icon.png', 
            name="Text",
            highlightable=False,
            on_enter=ExtensionCustomAction(
                 {'type': TYPE_TEXT})
        ))

        return RenderResultListAction(items)

 
class ItemEnterEventListener(EventListener):

    def on_event(self, event, extension): 
        data = event.get_data()
        text = ""

        if(data['type'] == TYPE_PARAGRAPH):
            text = lorem.paragraph()
        
        if(data['type'] == TYPE_SENTENCE):
            text = lorem.sentence()
        
        if(data['type'] == TYPE_TEXT):
            text = lorem.text()

        return CopyToClipboardAction(text).run()

if __name__ == '__main__':
   LipsumExtension().run()
