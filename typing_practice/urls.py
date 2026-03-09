from django.urls import path
from .views import (
    HomeView, PracticeView, StatsAPIView, StatsHistoryView,
    DashboardView, ResourcesView, TracksView, TrackDetailView,
    PlaygroundView, ManageSnippetView, InterviewView, DsaInterviewView,
    DjangoSlideView, FastApiSlideView, DsaSlideView,
    UserManagementView, UserCreateView, UserEditView, UserDeleteView,
)

app_name = "typing_practice"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("practice/<int:snippet_id>/", PracticeView.as_view(), name="practice"),
    path("api/stats/", StatsAPIView.as_view(), name="stats_api"),
    path("history/", StatsHistoryView.as_view(), name="stats_history"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("resources/", ResourcesView.as_view(), name="resources"),
    path("tracks/", TracksView.as_view(), name="tracks"),
    path("tracks/<slug:track_slug>/", TrackDetailView.as_view(), name="track_detail"),
    path("playground/", PlaygroundView.as_view(), name="playground"),
    path("manage/snippet/", ManageSnippetView.as_view(), name="manage_snippet"),
    # Interview Q&A
    path("interview/", InterviewView.as_view(), name="interview"),
    path("dsa-interview/", DsaInterviewView.as_view(), name="dsa_interview"),
    # Framework slide Q&A
    path("django/", DjangoSlideView.as_view(), name="django_slides"),
    path("fastapi/", FastApiSlideView.as_view(), name="fastapi_slides"),
    path("dsa/", DsaSlideView.as_view(), name="dsa_slides"),
    # User management (staff only)
    path("users/", UserManagementView.as_view(), name="user_list"),
    path("users/create/", UserCreateView.as_view(), name="user_create"),
    path("users/<int:user_id>/edit/", UserEditView.as_view(), name="user_edit"),
    path("users/<int:user_id>/delete/", UserDeleteView.as_view(), name="user_delete"),
]
