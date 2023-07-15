"""authentik pretend GitLab Views"""

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.utils.text import slugify
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from authentik.providers.oauth2.constants import SCOPE_GITHUB_USER_EMAIL
from authentik.providers.oauth2.models import RefreshToken
from authentik.providers.oauth2.utils import protected_resource_view


@method_decorator(csrf_exempt, name="dispatch")
# not sure about this
@method_decorator(protected_resource_view([]), name="dispatch")
class GitLabUserView(View):
    """Emulate GitLab's /user API Endpoint"""

    def get(self, request: HttpRequest, token: RefreshToken) -> HttpResponse:
        """Emulate GitLab's /user API Endpoint, currently just a copy of the GitHub one"""
        user = token.user
        return JsonResponse(
            {
                #"login": user.username,
                "login": '-'.join(user.name.split()),
                "id": user.pk,
                "node_id": "",
                "avatar_url": "",
                "gravatar_id": "",
                "url": "",
                "html_url": "",
                "followers_url": "",
                "following_url": "",
                "gists_url": "",
                "starred_url": "",
                "subscriptions_url": "",
                "organizations_url": "",
                "repos_url": "",
                "events_url": "",
                "received_events_url": "",
                "type": "User",
                "site_admin": False,
                "name": user.name,
                "company": "",
                "blog": "",
                "location": "",
                "email": user.email,
                "hireable": False,
                "bio": "",
                "public_repos": 0,
                "public_gists": 0,
                "followers": 0,
                "following": 0,
                "created_at": user.date_joined,
                "updated_at": user.date_joined,
                "private_gists": 0,
                "total_private_repos": 0,
                "owned_private_repos": 0,
                "disk_usage": 0,
                "collaborators": 0,
                "two_factor_authentication": True,
                "plan": {
                    "name": "None",
                    "space": 0,
                    "private_repos": 0,
                    "collaborators": 0,
                },
            }
        )
