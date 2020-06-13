
from django.urls import path
from .views import polls_list, polls_detail
from .apiviews import PollList, PollDetail
from .apiviews import ChoiceList, CreateVote, UserCreate


urlpatterns = [
    path("poll/", polls_list, name="polls_list"),
    path("poll/<int:pk>/", polls_detail, name="polls_detail"),
    path("pollz/", PollList.as_view(), name="polls_list"),
    path("pollr/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("choices/", ChoiceList.as_view(), name="choice_list"),
    path("vote/", CreateVote.as_view(), name="create_vote"),
    path("users/", UserCreate.as_view(), name="user_create"),

]


