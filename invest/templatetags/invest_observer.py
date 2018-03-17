from django import template
from invest.views import Invest

register = template.Library()

def test():
    return "Here is a test"

#register.simple_tag(test, name='pusherable_script')

register.simple_tag(Invest.pusherable_script, name='pusherable_script')
register.filter('invest_update', Invest.update)#, name='update')
