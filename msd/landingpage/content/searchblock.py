"""Definition of the SearchBlock content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.Archetypes.utils import DisplayList
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from Products.DataGridField import DataGridField, DataGridWidget
from Products.DataGridField.Column import Column

from msd.landingpage import landingpageMessageFactory as _
from msd.landingpage.interfaces import ISearchBlock
from msd.landingpage.config import PROJECTNAME

from msd.landingpage.content import littleblock

SearchBlockSchema = littleblock.LittleBlockSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.BooleanField(
        'showTitle',
        widget=atapi.BooleanWidget(
            label=_(u"Show block title?"),
            description=_(u"Untick to hide block's title"),
        ),
        default=True,
    ),
    
    atapi.StringField(
        'search_mode',
        widget=atapi.SelectionWidget(
            label=_(u"Mode"),
            description=_(u"Select search mode: \"Browse\" - renders selection control and redirets to the content just after it's being selected and \"Search\" - renders text input field for searching by given value."),
            format='radio',
        ),
        default='0',
        required=True,
        vocabulary="getModesVocabulary",
    ),

    atapi.StringField(
        'browse_label',
        widget=atapi.StringWidget(
            label=_(u"Browse label"),
        ),

    ),

    DataGridField('browse_criteria',
        columns=("b_key", "b_value",),
        widget = DataGridWidget(
            label='Browse criteria',
            description='Enter key and value for each browse criterum.',
            columns={
                'b_key' : Column("Key"),
                'b_value' : Column("Value"),
            },
         ),
    ),


    atapi.StringField(
        'search_label',
        widget=atapi.StringWidget(
            label=_(u"Search label"),
        ),

    ),

    atapi.StringField(
        'search_field_name',
        widget=atapi.StringWidget(
            label=_(u"Search field name"),
        ),

    ),

    DataGridField('search_criteria',
        columns=("s_key", "s_value",),
        widget = DataGridWidget(
            label='Search criteria',
            description='Enter key and value for each search criterum. Note: for boolean values use:True or False strings.',
            columns={
                's_key' : Column("Key"),
                's_value' : Column("Value"),
            },
         ),
    ),

    atapi.StringField(
        'search_url',
        widget=atapi.StringWidget(
            label=_(u"Search url"),
            description=_(u"Enter search form action url where the form will be submitted (only \"search\" mode)."),
        ),
    ),

    atapi.StringField(
        'search_button',
        widget=atapi.StringWidget(
            label=_(u"Search button"),
            description=_(u"Enter a label of the search button (only \"search\" mode)."),
        ),
        default=u'Search'
    ),

    atapi.StringField(
        'search_link_class',
        widget=atapi.StringWidget(
            label=_(u"Search link (css) class"),
            description=_(u"Enter an alternative search link's css id. This link will be hidden and can be used to mount " \
                                    u"additional functionality using external javascrpts for the form submitting (only \"search\" mode)."),
        ),
    ),
    
    atapi.StringField(
        'unique_id',
        widget=atapi.StringWidget(
            label=_(u"Unique ID"),
            description=_(u"Used as css id for the search input/select control."),
        ),
    ),

    atapi.StringField(
        'form_class',
        widget=atapi.StringWidget(
            label=_(u"Form (css) class"),
            description=_(u"Enter optional css class for the form (only \"search\" mode)."),
        ),
    ),

    atapi.StringField(
        'colour',
        widget=atapi.SelectionWidget(
            label=_(u"Colour"),
            description=_(u"Styling colour for the box"),
            format='select',
        ),
        vocabulary="getColoursVocabulary",
    ),
    
    atapi.StringField(
        'link',
        widget=atapi.StringWidget(
            label=_(u"Link"),
            description=_(u"Link for image and title. http://www.google.com"),
        ),

    ),
))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

schemata.finalizeATCTSchema(SearchBlockSchema, moveDiscussion=False)


class SearchBlock(littleblock.LittleBlock):
    """Description of the Example Type"""
    implements(ISearchBlock)

    meta_type = "SearchBlock"
    schema = SearchBlockSchema

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

    def getColoursVocabulary(self):
        """ Returns just the css class from the name|class colour setting"""
        colours = self.getColours()
        return [c.split("|")[2] for c in colours if c.split('|')[0] == 'search']


    def getModesVocabulary(self):
        """ Returns search mode options """
        return DisplayList((
                ('0', _(u'Browse')),
                ('1', _(u'Search'))
                ))

atapi.registerType(SearchBlock, PROJECTNAME)
