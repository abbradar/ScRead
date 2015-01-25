# -*- coding: utf-8 -*-

""" conf.py: provides configuration variables for plugin. """


from anki.decks import defaultDeck, defaultConf

from style import css, templates
from tools import *


beautify = lambda s: ' '.join(map(str.capitalize, s.split('_')))

menu = {
  'name': 'ScRead'
  , 'items': {s:beautify(s) for s in [
      'init'
    , 'reset'
    , 'parse_texts'
    , 'mark_as_known'
    , 'mark_as_new'
    , 'supply_cards'
    , 'update_estimations'
    , 'test'
    ]}
}



make_templates = lambda m, xs: dict(map(
      lambda x: (x, merge(templates[m+'.'+x], {'name': m.capitalize()+'.'+x.capitalize()}))
    , xs))


models = {
    'text': {
          'name': 'ScRead.Text'
        , 'css': css['text']
        , 'fields': ['Source', 'Text']
        , 'templates': make_templates('text', ['default'])
    },

    'word': {
          'name': 'ScRead.Word'
        , 'css': css['word']
        , 'fields': ['Word', 'TextId', 'Count', 'Meaning', 'Context']
        , 'templates': make_templates('word', ['unsorted', 'filtered'])
    }
}


tags = {
    'parsed': 'ScRead.parsed'
  , 'available': 'ScRead.available'
  , 'visible': 'ScRead.visible'
}   



due_threshold = 1000


make_deck = lambda name, description, conf = None: {
    'name': name
  , 'type': merge(defaultDeck, {'desc': description})
  , 'conf': None if conf is None else merge(defaultConf, conf)
}


decks = {
    'global': make_deck(
          'ScRead'
        , """Global deck for ScRead. A system deck (don't touch it)."""
        , {
              'new': {'perDay': 9999}
            , 'rev': {'perDay': 9999}
        }
    ),

    'texts': make_deck(
          'ScRead::Texts'
        , """All texts. Here you add texts you want to read."""
        , {
              'new': {'perDay': 0}
            , 'rev': {'perDay': 0}
        }
    ),

    'available': make_deck(
          u'ScRead::Texts→Available'
        , """Available texts."""
        , {
              'new': {
                  'perDay': 10
                  , 'delays': [24*60, 3*24*60]
              }

            , 'rev': {'perDay': 0}
          }
    ),

    'words': make_deck(
          'ScRead::Words'
        , """All words. A system deck (don't touch it)."""
        , {
              'new': {'perDay': 0}
            , 'rev': {'perDay': 0}
        }
    ),

    'unsorted': make_deck(
          u'ScRead::Words→Unsorted'
        , """Unsorted words. Here you check the words you don't know."""
        , {
              'new': {
                  'perDay': 9999
                  , 'delays': [1*365*24*60, 10*365*24*60]
              }

            , 'rev': {'perDay': 0}
          }
    ),

    'filtered': make_deck(
          u'ScRead::Words→Filtered'
        , """Filtered words. Here you memoize the words."""
        , {
              'new': {'perDay': 25}
            , 'rev': {'perDay': 250}
          }
    )
}



