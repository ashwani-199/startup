import enum
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render





class Status(enum.Enum):
    success = "SUCCESS"
    fail = "FAIL"
    error = "ERROR"


class MainService:
    def __init__(self, request):
        self.request = request
        self.currentSite = get_current_site(self.request)
        self.user = None

    @staticmethod
    def error_404(request, exception):
        data = {}
        return render(request, 'errors/404.html', data)

    @staticmethod
    def error_500(request, *args, **argv):
        return render(request, 'errors/500.html', status=500)

    @staticmethod
    def error_400(request, *args, **argv):
        return render(request, 'errors/400.html', status=400)

    @staticmethod
    def error_403(request, *args, **argv):
        return render(request, 'errors/403.html', status=403)

    
