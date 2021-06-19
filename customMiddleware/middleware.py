import requests
from django.conf import settings


class DebugException(object):

    def __init__(self, response):
        self.response = response

    def __call__(self, request):
        response = self.response(request)
        return response

    def process_exception(self, request, exception):
        if settings.DEBUG:
            intitle = u'{}: {}'.format(exception.__class__.__name__,  exception)
            print("intitle: ", intitle)

            print("Second line:", exception)
            print("Error class: ", exception.__class__)

            url = 'https://api.stackexchange.com/2.2/search'
            headers = {'User-Agent': 'github.com/gi-rish/customMiddleware'}
            params = {
                'order': 'desc',
                'sort': 'votes',
                'site': 'stackoverflow',
                'pagesize': 3,
                'tagged': 'python;django',
                'intitle': intitle
            }

            r = requests.get(url, params=params, headers=headers)
            questions = r.json()

            print("******")

            for question in questions['items']:
                print(question['title'])
                print(question['link'])
                print('')
            print("*****")

            return None
