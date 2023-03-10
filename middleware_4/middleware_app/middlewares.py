
from django.shortcuts import HttpResponse


class Middleware4:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(request, *args, **kwargs):
        print("This is process_view function")
        # return HttpResponse('This is process view.')
        return None

    def process_exception(self, request, exception):
        msg = exception.__class__.__name__
        print(msg)
        print(exception)
        return HttpResponse(exception)
