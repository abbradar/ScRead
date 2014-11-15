""" core.py: provides init function for the plugin. """

from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *
from anki.hooks import addHook

from scread.constants import *
from scread import translate
from scread import estimate



def init(deck_global, translate, estimate, threshold):
   
    def add_text():
        showInfo('adding to %s' % deck_global)
    
    def supply_cards():
        showInfo('suppying cards')
    
    def update_estimations():
        showInfo('updating estimations')
    
    def test_item():
        pass

    def create_submenu():
        
        menuTools = mw.form.menuTools
        menuTools.menuScRead = mw.form.menuTools.addMenu('ScRead')
    
        def beautify(fname):
            return ' '.join([w.capitalize() for w in fname.split('_')])

        def add_menu_item(f):
            action = QAction(beautify(f.__name__), mw)
            mw.connect(action, SIGNAL("triggered()"), f)
            menuTools.menuScRead.addAction(action)

        map(add_menu_item, [
            add_text
          , supply_cards
          , update_estimations
          , test_item  
        ])


    def create_decks():
        mw.col.decks.id(deck_global)
        map(lambda s: mw.col.decks.id(deck_global + '::' + s), [
          DECK_TEXTS
        , DECK_WORDS
        , DECK_AVALABLE
        , DECK_FILTERING
        , DECK_MEMOIZING
        ])
        mw.deckBrowser.refresh()


    map(lambda f: addHook("profileLoaded", f), [
      create_submenu
    , create_decks
    ])


