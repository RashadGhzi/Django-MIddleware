

def func_based_middleware(get_response):
    print('First initialization function based middleware')

    def mid_item(requset):
        print('This is before view run.')
        response = get_response(requset)
        print('This is after view run.')
        return response
    return mid_item
