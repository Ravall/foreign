from __future__ import unicode_literals
from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView


# pylint: disable=C0103
urlpatterns = patterns('',
    url(
        r'^article/how_to_order_food_in_a_restaurant',
        RedirectView.as_view(
            url='/article/kak_zakazat_edu_v_restorane_na_angliyskom'
        ),
    ),
    url(r'^article/voprositelnye_slova_v_anglijskom_jazyke',
        RedirectView.as_view(
            url='/article/voprositelnye_slova_v_angliyskom_yazyke'
        ),
    ),
    url(r'^article/globalnyj-anglijskij-vzgljad-evropejca',
        RedirectView.as_view(
            url='/article/globalnyy_angliyskiy_vzglyad_evropyayca'
        ),
    )

)