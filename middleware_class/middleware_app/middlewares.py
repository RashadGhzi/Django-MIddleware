

class ClassBasedMiddleware:

    def __init__(self, get_response) -> None:
        self.get_response = get_response
        print("This is class based __init__ funtion.")
        print('get_response : ', get_response)

    def __call__(self, request, *args, **kwds):
        print('This is before view run')
        print('args : ', args)
        print('kwargs : ', kwds)

        response = self.get_response(request)
        print('This is after view run.')
        print('args : ', args)
        print('kwargs : ', kwds)
        return response
