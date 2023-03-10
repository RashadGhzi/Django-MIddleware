

class MultipleMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        print("First initialization after server start multiple middleware 1")

    def __call__(self, request):
        print("This is before view run multiple middleware 1 ")
        response = self.get_response(request)
        print("This is after view run multiple middleware 1")
        return response


class MultipleMiddleware_2:

    def __init__(self, get_response):
        self.get_response = get_response
        print("First initialization after server start multiple middleware 2")

    def __call__(self, request):
        print("This is before view run multiple middleware 2")
        response = self.get_response(request)
        print("This is after view run multiple middleware 2")
        return response
