from django.shortcuts import render



def loading_page(request):
    return render(request, 'loading.html')

def main_page(request):
    return render(request, 'main.html')  # 메인 페이지 템플릿
