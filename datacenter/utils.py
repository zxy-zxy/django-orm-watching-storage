from datetime import timedelta

from django.utils import timezone

import humanize


def get_duration(visit):
    if visit.leaved_at is None:
        upper_bound = timezone.now()
    else:
        upper_bound = visit.leaved_at
    return upper_bound - visit.entered_at


def format_duration(duration):
    return humanize.naturaldelta(duration)


def is_visit_long(visit, minutes=60):
    is_long_visit_timedelta_upper_bound = timedelta(minutes=minutes)
    duration = get_duration(visit)
    return duration >= is_long_visit_timedelta_upper_bound
