# """Github model."""
# from .meta import Base


# class GHModel(object):
#     """Github user model."""

#     def to_dict_results(self):
#         """Take a few model attributes and render them as a dictionary for results page."""
#         return {
#             "id": self.id,
#             "login": self.login,
#             "avatar_url": self.avatar_url,
#             "location": self.location,
#             "bio": self.bio
#         }

#     def to_dict_all(self):
#         """Take all model attributes and render them as a dictionary."""
#         return {
#             "login": self.login,
#             "id": self.id,
#             "avatar_url": self.avatar_url,
#             "gravatar_id": self.gravatar_id,
#             "url": self.url,
#             "html_url": self.html_url,
#             "followers_url": self.followers_url,
#             "following_url": self.following_url,
#             "gists_url": self.gists_url,
#             "starred_url": self.starred_url,
#             "subscriptions_url": self.subscriptions_url,
#             "organizations_url": self.organizations_url,
#             "repos_url": self.repos_url,
#             "events_url": self.events_url,
#             "received_events_url": self.received_events_url,
#             "type": self.type,
#             "site_admin": self.site_admin,
#             "name": self.name,
#             "company": self.company,
#             "blog": self.blog,
#             "location": self.location,
#             "email": self.email,
#             "hireable": self.hireable,
#             "bio": self.bio,
#             "public_repos": self.public_repos,
#             "public_gists": self.public_gists,
#             "followers": self.followers,
#             "following": self.following,
#             "created_at": self.created_at,
#             "updated_at": self.updated_at
#         }
