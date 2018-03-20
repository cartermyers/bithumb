from django import template
from invest.views import Invest

register = template.Library()

register.simple_tag(Invest.pusherable_script, name='pusherable_script')
register.filter('invest_update', Invest.update)#, name='update')
