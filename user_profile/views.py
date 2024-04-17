from django.shortcuts import render

from user_profile.models import Profile


def profiles_index(request):
    """
    View to display the list of all user profiles.

    :param request: The Django HttpRequest object.
    :type request: django.http.HttpRequest

    :return: The HTTP response with the list of profiles
     rendered in the 'profiles_index.html' template.
    :rtype: django.http.HttpResponse
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles_index.html", context)


def profile(request, username):
    """
    View to display a specific user's profile.

    :param request: The Django HttpRequest object.
    :type request: django.http.HttpRequest

    :param username: The username of the profile to display.
    :type username: str

    :return: The HTTP response with the profile rendered in the 'profile.html' template.
    :rtype: django.http.HttpResponse
    """
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profile.html", context)
