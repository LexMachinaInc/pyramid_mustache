
from unittest import TestCase
from pyramid_mustache import (
    LexRenderer,
)
import pystache
from pystache import Renderer

our_template=u"""{{#Patent}}
       <h4>
         <a href="/patent/{{link_number}}">
           <span class="label label-patent-big">{{link_number}}</span>
         </a>
         {{#title}}{{.}}{{/title}}
       </h4>
 {{/Patent}}"""

our_other_template=u"""{{#Patent}}
       <h4>
         {{#link_number}}
         <a href="/patent/{{.}}">
           <span class="label label-patent-big">{{.}}</span>
         </a>
         {{/link_number}}
         {{#title}}{{.}}{{/title}}
       </h4>
 {{/Patent}}"""


class TestMustache(TestCase):

    def test_mustache_default(self):
        renderer = Renderer()
        output = renderer.render(our_template, {'Patent':{'title':'foo-bar','link_number':[u'1234']}})
        print 'default output %s', output
        self.assertIn('[u', output)


    def test_mustache_lex(self):
        renderer = LexRenderer()
        output = renderer.render(our_template, {'Patent':{'title':'foo-bar','link_number':[u'1234']}})
        print 'output %s', output
        self.assertNotIn('[u', output)

    def test_mustache_lex_string(self):
        renderer = LexRenderer()
        output = renderer.render(our_template, {'Patent':[{'title':['foo-bar','baz'],'link_number': u'1234'}, {'title':'Balloons','link_number': u'999999'}]})
        print 'output %s', output
        self.assertIn('1234', output)
        self.assertNotIn('[u', output)

    def test_mustache_lex_list_error(self):
        renderer = LexRenderer()
        with self.assertRaises(ValueError):
            renderer.render(our_template, {'Patent':{'title':'foo-bar','link_number':[u'1234',u'5678']}})

    def test_mustache_lex_list_success(self):
        renderer = LexRenderer()
        output= renderer.render(our_other_template, {'Patent':{'title':'foo-bar','link_number':[u'1234',u'5678']}})
        print 'output %s', output
        self.assertIn('1234', output)
        self.assertIn('5678', output)
        self.assertNotIn('[u',output)
    
