import requests
from django.shortcuts import render
from django.conf import settings


def index(request):
    return render(request, 'app_predicc/index.html')


def predict(request):
    area_m2 = request.POST.get('area_m2')
    context = {
        'area_m2': area_m2,
        'predicted_price': None,
        'error': None,
    }

    if not area_m2:
        context['error'] = 'Por favor ingresa un valor de superficie.'
        return render(request, 'app_predicc/index.html', context)

    try:
        area_m2 = float(area_m2)
        if area_m2 <= 0:
            context['error'] = 'La superficie debe ser mayor a 0 m².'
            return render(request, 'app_predicc/index.html', context)
    except ValueError:
        context['error'] = 'El valor ingresado no es válido.'
        return render(request, 'app_predicc/index.html', context)

    try:
        api_url = f"{settings.BACKEND_API_URL}/predict"
        response = requests.post(
            api_url,
            json={"area_m2": area_m2},
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
        context['predicted_price'] = data['predicted_price']
    except requests.exceptions.ConnectionError:
        context['error'] = 'No se pudo conectar con el servidor de predicción.'
    except requests.exceptions.Timeout:
        context['error'] = 'El servidor tardó demasiado en responder.'
    except requests.exceptions.HTTPError as e:
        context['error'] = f'Error del servidor: {e.response.status_code}'
    except Exception as e:
        context['error'] = f'Error inesperado: {str(e)}'

    return render(request, 'app_predicc/index.html', context)
