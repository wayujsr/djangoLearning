from django.shortcuts import render

# Create your views here.
def neta_list(request):
    return render(request, 'neta_DIR/neta_list.html', {})