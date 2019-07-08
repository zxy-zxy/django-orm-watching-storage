from datacenter.models import Visit
from django.shortcuts import render

from .utils import get_duration, format_duration, is_visit_long


def storage_information_view(request):
    non_closed_visits = Visit.objects.select_related('passcard').filter(
        leaved_at__isnull=True).all()

    non_closed_visits = [
        {
            'who_entered': visit_obj.passcard.owner_name,
            'entered_at': visit_obj.entered_at,
            'duration': format_duration(get_duration(visit_obj)),
            'is_strange': is_visit_long(visit_obj)
        }
        for visit_obj in non_closed_visits
    ]

    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
