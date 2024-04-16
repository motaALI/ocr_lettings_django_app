
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500
from oc_lettings_site import views
from django.conf import settings
from user_profile.views import profiles_index, profile
from letting.views import lettings_index, letting
from django.core.exceptions import PermissionDenied


"""
URL patterns for the application.

- The root path ('') maps to the 'index' view.
- 'lettings/' maps to the 'lettings_index' view, displaying a list of all lettings.
- 'lettings/<int:letting_id>/' maps to the 'letting' view, displaying details for a specific letting.
- 'profiles/' maps to the 'profiles_index' view, displaying a list of all user profiles.
- 'profiles/<str:username>/' maps to the 'profile' view, displaying details for a specific user profile.
- 'admin/' maps to the Django admin site.

Each path is associated with a specific view and has a corresponding name for reverse URL matching.
"""

handler403 = 'oc_lettings_site.views.custom_403'
handler404 = 'oc_lettings_site.views.custom_404'
handler500 = 'oc_lettings_site.views.custom_500'

def my_view(request):
    some_condition = False
    # Check some condition
    if not some_condition:
        # Raise PermissionDenied exception
        raise PermissionDenied

urlpatterns = [
    path('', views.index, name='index'),
    path('unauth', my_view, name='unauth'),
    path('lettings/', lettings_index, name='lettings_index'),
    path('lettings/<int:letting_id>/', letting, name='letting'),
    path('profiles/', profiles_index, name='profiles_index'),
    path('profiles/<str:username>/', profile, name='profile'),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)