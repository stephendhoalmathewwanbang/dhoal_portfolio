from django.shortcuts import render


def portfolio(request):
    """Portfolio page for Upwork profile."""
    return render(request, 'kong/portfolio.html')
