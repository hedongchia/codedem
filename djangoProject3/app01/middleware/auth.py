from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect
class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path_info == '/login/':
            return None
        info_dict = request.session.get('info')
        print(info_dict)
        if info_dict:
            return None
        return redirect('http://127.0.0.1:8000/login/')
