import math
from django.core.paginator import Paginator
from rest_framework.permissions import BasePermission

def form_formatter(POST: dict, *args: str) -> dict:
    exclude = ['csrfmiddlewaretoken']
    exclude.extend(args)
    form = {key:value for key, value in POST.items() if key not in exclude}
    return form


def paginator(queryset: str, name_key: str, serializer: str, many_serializer: bool = True, page: int = 1, per_page: int = 100):
    if int(per_page) > 100 or int(per_page) < 1:
        per_page = 100

    paginator = Paginator(queryset, per_page).get_page(page)
    total_page = len(queryset) / int(per_page)
    dict_response = {}
    dict_response[name_key] = serializer(paginator, many=many_serializer).data

    dict_response["paging"] = {
        "total": len(queryset),
        "pages": math.ceil(total_page),
        "current_page": int(page),
        "per_page": per_page,
    }
    return dict_response

class PostAllow(BasePermission):
    def has_permission(self, request, view):
        return bool(request.method == "POST")


class GetAllow(BasePermission):
    def has_permission(self, request, view):
        return bool(request.method == "GET")
    
class PutAllow(BasePermission):
    def has_permission(self, request, view):
        return bool(request.method == "PUT")

class DeletePutAllow(BasePermission):
    def has_permission(self, request, view):
        return bool(request.method == "DELETE")