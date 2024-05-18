"""authentik oauth_provider urls"""

from django.contrib.auth.decorators import login_required
from django.urls import include, path

from authentik.providers.oauth2.views.authorize import AuthorizationFlowInitView
from authentik.providers.oauth2.views.device_init import DeviceEntryView
from authentik.providers.oauth2.views.github import GitHubUserTeamsView, GitHubUserView
from authentik.providers.oauth2.views.gitlab import GitLabUserView
from authentik.providers.oauth2.views.token import TokenView

github_urlpatterns = [
    path(
        "login/oauth/authorize",
        AuthorizationFlowInitView.as_view(github_compat=True),
        name="github-authorize",
    ),
    path(
        "login/oauth/access_token",
        TokenView.as_view(),
        name="github-access-token",
    ),
    path(
        "user",
        GitHubUserView.as_view(),
        name="github-user",
    ),
    path(
        "user/teams",
        GitHubUserTeamsView.as_view(),
        name="github-user-teams",
    ),
]

gitlab_urlpatterns = [
    path(
        "oauth/authorize",
        AuthorizationFlowInitView.as_view(),
        name="gitlab-authorize",
    ),
    path(
        "oauth/token",
        TokenView.as_view(),
        name="gitlab-token",
    ),
    path(
        "api/v4/user",
        GitLabUserView.as_view(),
        name="gitlab-user",
    ),
]

urlpatterns = [
    path("", include(github_urlpatterns)),
    path("", include(gitlab_urlpatterns)),
    path(
        "device",
        login_required(
            DeviceEntryView.as_view(),
        ),
        name="device-login",
    ),
]
