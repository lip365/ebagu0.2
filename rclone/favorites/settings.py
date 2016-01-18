#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.conf import settings
from django.utils.translation import ugettext

FAV_ADD = getattr(settings, 'FAV_ADD', ugettext('구독하기'))
FAV_REMOVE = getattr(settings, 'FAV_REMOVE', ugettext('구독취소'))
FAV_COUNT_SINGLE = getattr(settings, 'FAV_COUNT_SINGLE', ugettext('%d 구독중'))
FAV_COUNT_PLURAL = getattr(settings, 'FAV_COUNT_PLURAL', ugettext('%d 구독중'))
# for languages who destinguish another plural form, such as Polish if the last digit is 2
FAV_COUNT_PLURAL_SPECIAL = getattr(settings, 'FAV_COUNT_PLURAL_SPECIAL', ugettext('%d 구독중'))
FAV_COUNT_PLURAL_SPECIAL_LASTNUMBERS = getattr(settings, 'FAV_COUNT_PLURAL_SPECIAL_LASTNUMBERS', [2,])
FAV_COUNT_SHOW_ZERO = getattr(settings, 'FAV_COUNT_SHOW_ZERO', False)
