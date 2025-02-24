

def previus(request, option):
    if 'HTTP_REFERER' in request.META:
        return request.META['HTTP_REFERER']
    return option