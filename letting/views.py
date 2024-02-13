from django.shortcuts import render


from letting.models import Letting

def lettings_index(request):
    """
    View to display the list of all lettings.

    :param request: The Django HttpRequest object.
    :type request: django.http.HttpRequest

    :return: The HTTP response with the list of lettings rendered in the 'lettings_index.html' template.
    :rtype: django.http.HttpResponse
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings_index.html', context)


def letting(request, letting_id):
    """
    View to display a specific letting.

    :param request: The Django HttpRequest object.
    :type request: django.http.HttpRequest

    :param letting_id: The ID of the letting to display.
    :type letting_id: int

    :return: The HTTP response with the letting details rendered in the 'letting.html' template.
    :rtype: django.http.HttpResponse
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'letting.html', context)