from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
#from .views import PostListView
from . import views
from users import views as user_views

urlpatterns = [
	path('comments/<int:pk>', views.comment_section, name='comment-section'),
    #path('home/', PostListView.as_view(), name='home'),
    path('home/', views.postlist, name='home'),
    path('like/<int:pk>', views.post_likes, name='liked'),
    path('comment/<int:pk>', views.post_comment, name='comment'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
