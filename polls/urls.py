from django.urls import path
from .apiviews import Poll_detail,Poll_list,ChoiceList, CreateVote
from rest_framework.routers import DefaultRouter
from .apiviews import PollViewSet , ChoiceList ,CreateVote , UserCreate ,LoginView
from rest_framework.authtoken import views
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls


schema_view = get_swagger_view(title='Polls API')

router = DefaultRouter()
router.register('polls',PollViewSet , basename= 'polls')

urlpatterns = [
        path('polls', Poll_list.as_view(), name='polls_list'),
        path('polls/<int:pk>/', Poll_detail.as_view(), name='poll_detail'),
        path('polls/<int:pk>/choices', ChoiceList.as_view(), name='choice_list'),
        path('polls/<int:pk>/choices/<int:choice_pk>/vote', CreateVote.as_view(), name='create_vote'),
        path('users/', UserCreate.as_view(), name='user_create'),
        path('login/', LoginView.as_view(), name='login'),
        path('swagger-docs/', schema_view),
        path(r'docs/', include_docs_urls(title= 'Polls API')),
]

urlpatterns += router.urls