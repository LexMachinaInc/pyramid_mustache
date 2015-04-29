
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

