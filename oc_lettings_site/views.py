from django.shortcuts import render


def custom_403(request, exception):
    """
    Renders a custom 403 error page.
    Args:
        request: The HTTP request object.
        exception: The exception that triggered the 403 error.

    Returns: A rendered 403 error page.
    """
    return render(request, "403.html", status=403)


def custom_404(request, exception):
    """
    Renders a custom 404 error page.

    Args:
        request: The HTTP request object.
        exception: The exception that triggered the 404 error.

    Returns: A rendered 404 error page.
    """
    return render(request, "404.html", status=404)


def custom_500(request):
    """
    Renders a custom 500 error page.

    Args:
        request: The HTTP request object.

    Returns: A rendered 500 error page.
    """
    return render(request, "500.html", status=500)


# Home
def index(request):
    """
    Renders the home page.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered home page.
    """
    return render(request, "index.html")
