from fan_blog.models import Browse


class BrowseMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        browse_flag = request.COOKIES.get('browse_flag', '')
        if not browse_flag:
            browse = Browse.objects.all()[0]
            browse.number += 1
            browse.save()
            response.set_cookie('browse_flag', 'true', expires=60 * 60 * 24 * 7)
        # Code to be executed for each request/response after
        # the view is called.

        return response

    # def process_response(self, request, response):
    #     browse_flag = request.COOKIES.get('browse_flag', '')
    #     if not browse_flag:
    #         browse = Browse.objects.all()[0]
    #         browse.number += 1
    #         browse.save()
    #         response.set_cookie('browse_flag', 'true', expires=60*60*24*7)
    #
    #     return response
