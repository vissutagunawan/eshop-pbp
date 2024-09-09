from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        "nama_aplikasi": "Sutashop",
        "nama": "Vissuta Gunawan Lim",
        "kelas": "D"
    }

    return render(request, 'main.html', context)
