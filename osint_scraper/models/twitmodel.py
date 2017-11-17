# """Github model."""
# from .meta import Base


# class TwitModel(object):
#     """Github user model."""

#     def to_dict_results(self):
#         """Take a few model attributes and render them as a dictionary for results page."""
#         return {
#             "name": self.name,
#             "screen_name": self.screen_name,
#             "profile_image_url": self.profile_image_url,
#             "location": self.location,
#             "description": self.description
#         }

#     def to_dict_all(self):
#         """Take all model attributes and render them as a dictionary."""
#         return {}
#         #     # "profile_sidebar_fill_color": "DDEEF6",
#         #     # "profile_background_tile": true,
#         #     # "profile_sidebar_border_color": "C0DEED",
#         #     "name": self.name,
#         #     "created_at": self.created_at,
#         #     "profile_image_url": self.profile_image_url,
#         #     "location": self.location,
#         #     # "follow_request_sent": false,
#         #     # "id_str": "6253282",
#         #     # "is_translator": false,
#         #     # "profile_link_color": "0084B4",
#         #     "entities": self.entities,
#         #     # "default_profile": false,
#         #     # "contributors_enabled": false,
#         #     "favourites_count": self.favourites_count,
#         #     "url": self.url,
#         #     "profile_banner_url": self.profile_banner_url,
#         #     "utc_offset": self.utc_offset,
#         #     "profile_image_url_https": self.profile_image_url_https,
#         #     "id": self.id,
#         #     "listed_count": self.listed_count,
#         #     # "profile_use_background_image": true,
#         #     "lang": self.lang,
#         #     # "profile_text_color": "333333",
#         #     "followers_count": self.followers_count,
#         #     "protected": self.protected,
#         #     "verified": self.verified,
#         #     "description": self.description,
#         #     "geo_enabled": self.geo_enabled,
#         #     "time_zone": self.time_zone,
#         #     "notifications": self.notifications,
#         #     # "profile_background_image_url_https": "https://twimg0-a.akamaihd.net/profile_background_images/656927849/miyt9dpjz77sc0w3d4vj.png",
#         #     # "profile_background_color": "C0DEED",
#         #     "status": self.status,
#         #     "friends_count": self.friends_count,
#         #     # "profile_background_image_url": "http://a0.twimg.com/profile_background_images/656927849/miyt9dpjz77sc0w3d4vj.png",
#         #     # "default_profile_image": false,
#         #     "statuses_count": self.statuses_count,
#         #     "screen_name": self.screen_name,
#         #     "following": self.following
#         # }
#             # "profile_sidebar_fill_color": "DDEEF6",
#             # "profile_background_tile": true,
#             # "profile_sidebar_border_color": "C0DEED",
#         #     "name": self.name,
#         #     "created_at": "Tue Apr 10 01:20:52 +0000 2007",
#         #     "profile_image_url": "http://a0.twimg.com/profile_images/2284174879/uqyatg9dtld0rxx9anic_normal.png",
#         #     "location": "San Francisco, CA",
#         #     "is_translator": false,
#         #     "follow_request_sent": false,
#         #     "id_str": "3963481",
#         #     "profile_link_color": "0084B4",
#         #     "entities": {
#         #       "url": {
#         #         "urls": [
#         #           {
#         #             "expanded_url": null,
#         #             "url": "http://twitter.com",
#         #             "indices": [
#         #               0,
#         #               18
#         #             ],
#         #             "display_url": null
#         #           }
#         #         ]
#         #       },
#         #       "description": {
#         #         "urls": [
#         #
#         #         ]
#         #       }
#         #     },
#         #     "default_profile": false,
#         #     "contributors_enabled": false,
#         #     "favourites_count": 2,
#         #     "url": "http://twitter.com",
#         #     "profile_image_url_https": "https://twimg0-a.akamaihd.net/profile_images/2284174879/uqyatg9dtld0rxx9anic_normal.png",
#         #     "profile_banner_url": "https://twimg0-a.akamaihd.net/profile_banners/3963481/1347394599",
#         #     "utc_offset": -28800,
#         #     "id": 3963481,
#         #     "listed_count": 7303,
#         #     "profile_use_background_image": true,
#         #     "lang": "en",
#         #     "profile_text_color": "333333",
#         #     "followers_count": 2359548,
#         #     "protected": false,
#         #     "verified": true,
#         #     "description": null,
#         #     "geo_enabled": true,
#         #     "time_zone": "Pacific Time (US & Canada)",
#         #     "notifications": false,
#         #     "profile_background_image_url_https": "https://twimg0-a.akamaihd.net/profile_background_images/656932170/urr667rpqtg6l7psohaf.png",
#         #     "profile_background_color": "C0DEED",
#         #     "status": {
#         #       "coordinates": null,
#         #       "truncated": false,
#         #       "favorited": false,
#         #       "created_at": "Wed Mar 20 12:55:51 +0000 2013",
#         #       "id_str": "314359633311588355",
#         #       "in_reply_to_user_id_str": null,
#         #       "entities": {
#         #         "urls": [
#           #
#         #         ],
#         #         "hashtags": [
#           #
#         #         ],
#         #         "user_mentions": [
#           #
#         #         ]
#         #       },
#         #       "text": "Beeline subscribers in Armenia can now send and receive Tweets via SMS. Begin by sending START to 40404. Welcome to Twitter!",
#         #       "contributors": null,
#         #       "id": 314359633311588355,
#         #       "in_reply_to_status_id_str": null,
#         #       "retweet_count": 31,
#         #       "geo": null,
#         #       "retweeted": false,
#         #       "in_reply_to_user_id": null,
#         #       "source": "web",
#         #       "place": null,
#         #       "in_reply_to_screen_name": null,
#         #       "in_reply_to_status_id": null
#         #     },
#         #     "friends_count": 28,
#         #     "profile_background_image_url": "http://a0.twimg.com/profile_background_images/656932170/urr667rpqtg6l7psohaf.png",
#         #     "default_profile_image": false,
#         #     "statuses_count": 338,
#         #     "screen_name": "twittermobile",
#         #     "following": true
#         #   },
#         #   {
#         #     "profile_sidebar_fill_color": "DAECF4",
#         #     "profile_background_tile": false,
#         #     "profile_sidebar_border_color": "C6E2EE",
#         #     "name": "Twitter Engineering",
#         #     "created_at": "Sat Jun 16 00:14:36 +0000 2007",
#         #     "profile_image_url": "http://a0.twimg.com/profile_images/2284174594/apcu4c9tu2zkefnev0jt_normal.png",
#         #     "location": "San Francisco, CA",
#         #     "follow_request_sent": false,
#         #     "is_translator": false,
#         #     "id_str": "6844292",
#         #     "profile_link_color": "1F98C7",
#         #     "entities": {
#         #       "url": {
#         #         "urls": [
#         #           {
#         #             "expanded_url": null,
#         #             "url": "http://engineering.twitter.com",
#         #             "indices": [
#         #               0,
#         #               30
#         #             ],
#         #             "display_url": null
#         #           }
#         #         ]
#         #       },
#         #       "description": {
#         #         "urls": [
#           #
#         #         ]
#         #       }
#         #     },
#         #     "default_profile": false,
#         #     "contributors_enabled": false,
#         #     "favourites_count": 0,
#         #     "url": "http://engineering.twitter.com",
#         #     "profile_image_url_https": "https://twimg0-a.akamaihd.net/profile_images/2284174594/apcu4c9tu2zkefnev0jt_normal.png",
#         #     "utc_offset": -28800,
#         #     "id": 6844292,
#         #     "listed_count": 2304,
#         #     "profile_use_background_image": true,
#         #     "lang": "en",
#         #     "profile_text_color": "663B12",
#         #     "followers_count": 343156,
#         #     "protected": false,
#         #     "verified": true,
#         #     "description": "The official account for Twitter Engineering.",
#         #     "geo_enabled": true,
#         #     "time_zone": "Pacific Time (US & Canada)",
#         #     "notifications": false,
#         #     "profile_background_image_url_https": "https://twimg0-a.akamaihd.net/images/themes/theme2/bg.gif",
#         #     "profile_background_color": "C6E2EE",
#         #     "status": {
#         #       "coordinates": null,
#         #       "truncated": false,
#         #       "favorited": false,
#         #       "created_at": "Mon Mar 18 17:50:28 +0000 2013",
#         #       "id_str": "313708997167419393",
#         #       "retweeted_status": {
#         #         "coordinates": null,
#         #         "truncated": false,
#         #         "favorited": false,
#         #         "created_at": "Thu Mar 14 10:57:20 +0000 2013",
#         #         "id_str": "312155480858431488",
#         #         "in_reply_to_user_id_str": null,
#         #         "entities": {
#         #           "urls": [
#         #             {
#         #               "expanded_url": "http://tweetdeck.posterous.com/flight-at-tweetdeck",
#         #               "url": "http://t.co/G9sRrGHgJY",
#         #               "indices": [
#         #                 56,
#         #                 78
#         #               ],
#         #               "display_url": "tweetdeck.posterous.com/flight-at-twee"
#         #             }
#         #           ],
#         #           "hashtags": [
#           #
#         #           ],
#         #           "user_mentions": [
#           #
#         #           ]
#         #         },
#         #         "text": "Our use of the Flight JavaScript framework in TweetDeck http://t.co/G9sRrGHgJY",
#         #         "contributors": null,
#         #         "id": 312155480858431488,
#         #         "in_reply_to_status_id_str": null,
#         #         "retweet_count": 100,
#         #         "geo": null,
#         #         "retweeted": false,
#         #         "in_reply_to_user_id": null,
#         #         "possibly_sensitive": false,
#         #         "source": "TweetDeck",
#         #         "place": null,
#         #         "in_reply_to_screen_name": null,
#         #         "in_reply_to_status_id": null
#         #       },
#         #       "in_reply_to_user_id_str": null,
#         #       "entities": {
#         #         "urls": [
#         #           {
#         #             "expanded_url": "http://tweetdeck.posterous.com/flight-at-tweetdeck",
#         #             "url": "http://t.co/G9sRrGHgJY",
#         #             "indices": [
#         #               71,
#         #               93
#         #             ],
#         #             "display_url": "tweetdeck.posterous.com/flight-at-twee"
#         #           }
#         #         ],
#         #         "hashtags": [
#           #
#         #         ],
#         #         "user_mentions": [
#         #           {
#         #             "name": "TweetDeck",
#         #             "id_str": "14803701",
#         #             "id": 14803701,
#         #             "indices": [
#         #               3,
#         #               13
#         #             ],
#         #             "screen_name": "TweetDeck"
#         #           }
#         #         ]
#         #       },
#         #       "text": "RT @TweetDeck: Our use of the Flight JavaScript framework in TweetDeck http://t.co/G9sRrGHgJY",
#         #       "contributors": null,
#         #       "id": 313708997167419393,
#         #       "in_reply_to_status_id_str": null,
#         #       "retweet_count": 100,
#         #       "geo": null,
#         #       "retweeted": false,
#         #       "in_reply_to_user_id": null,
#         #       "possibly_sensitive": false,
#         #       "source": "web",
#         #       "place": null,
#         #       "in_reply_to_screen_name": null,
#         #       "in_reply_to_status_id": null
#         #     },
#         #     "friends_count": 0,
#         #     "profile_background_image_url": "http://a0.twimg.com/images/themes/theme2/bg.gif",
#         #     "default_profile_image": false,
#         #     "statuses_count": 153,
#         #     "screen_name": "TwitterEng",
#         #     "following": true
#         #   }
