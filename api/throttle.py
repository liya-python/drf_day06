from rest_framework.throttling import SimpleRateThrottle


class MyThrottle(SimpleRateThrottle):
    scope = 'sms'
    def get_cache_key(self, request, view):
        if request.user.is_authenticated:
            return True

