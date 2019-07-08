from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.http import Http404

from .utils import get_duration, format_duration, is_visit_long


def passcard_info_view(request, passcode):
    try:
        passcard = Passcard.objects.get(passcode=passcode)
    except Passcard.DoesNotExist:
        raise Http404('Passcode not found!')

    this_passcard_visits = Visit.objects.filter(
        passcard=passcard, leaved_at__isnull=False
    ).all()

    visits_to_render = []
    for visit_obj in this_passcard_visits:
        duration = get_duration(visit_obj)
        visits_to_render.append({
            'entered_at': visit_obj.entered_at,
            'duration': format_duration(duration),
            'is_strange': is_visit_long(visit_obj)
        })

    context = {
        "passcard": passcard,
        "this_passcard_visits": visits_to_render
    }
    return render(request, 'passcard_info.html', context)
