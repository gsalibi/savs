from django.contrib import admin
from django.db.models import Count, Sum, Min, Max, DateTimeField
from django.db.models.functions import Trunc
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter,
    ChoiceDropdownFilter,
)

# Register your models here.
from .models import (
    AnonymousComplaint,
    IdentifiedComplaint,
    EnvolvedPerson,
    AnonComplainSummary,
    IdentComplainSummary,

)


def get_next_in_date_hierarchy(request, date_hierarchy):
    if date_hierarchy + "__day" in request.GET:
        return "hour"
    if date_hierarchy + "__month" in request.GET:
        return "day"
    if date_hierarchy + "__year" in request.GET:
        return "week"
    return "month"

class EnvolvedPersonAdmin(admin.ModelAdmin):
    list_display = (
        "person_name",
        "person_connecton_unicamp",
        "person_relationship_victim",
        "is_accused",
    )
    list_filter =(
        ("person_connecton_unicamp", ChoiceDropdownFilter),
        "is_accused", 

    )

@admin.register(IdentifiedComplaint)
class IdentifiedComplaintAdmin(admin.ModelAdmin):
    list_display = (
        "identified_name",
        "identified_current_status",
        "identified_created",
        "identified_updated_at",
        "identified_position",
        "identified_gender",
        "identified_race",
        "identified_email",
    )
    
    list_filter = (
        ("identified_current_status", ChoiceDropdownFilter),
        ("identified_position", ChoiceDropdownFilter),
        ("identified_gender", ChoiceDropdownFilter),
        ("identified_race", ChoiceDropdownFilter),
        ("identified_connection_unicamp", ChoiceDropdownFilter),
    )

@admin.register(AnonymousComplaint)
class AnonymousComplaintAdmin(admin.ModelAdmin):
    list_display = (
        "anonymous_created",
        "anonymous_current_status",
        "anonymous_updated_at",
        "anonymous_gender",
        "anonymous_race",
        "anonymous_connection_unicamp",
        "anonymous_support_requested",
    )
    list_filter = (
        ("anonymous_current_status", ChoiceDropdownFilter),
        ("anonymous_support_requested", ChoiceDropdownFilter),
        ("anonymous_position", ChoiceDropdownFilter),
        ("anonymous_gender", ChoiceDropdownFilter),
        ("anonymous_race", ChoiceDropdownFilter),
        ("anonymous_connection_unicamp", ChoiceDropdownFilter),
    )


@admin.register(AnonComplainSummary)
class AnonComplainAdmin(admin.ModelAdmin):
    change_list_template = "admin/anon_complains.html"
    date_hierarchy = "anonymous_created"
    actions = None
    # Prevent additional queries for pagination.
    show_full_result_count = False

    list_filter = (
        ("anonymous_current_status", ChoiceDropdownFilter),
        ("anonymous_position", ChoiceDropdownFilter),
        ("anonymous_gender", ChoiceDropdownFilter),
        ("anonymous_race", ChoiceDropdownFilter),
        ("anonymous_connection_unicamp", ChoiceDropdownFilter),
    )

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context,)

        period = get_next_in_date_hierarchy(request, self.date_hierarchy,)

        response.context_data["period"] = period

        try:
            qs = response.context_data["cl"].queryset
        except (AttributeError, KeyError):
            return response

        metrics = {
            "total_genero": Count("anonymous_gender"),
        }

        response.context_data["summary"] = list(
            qs.values("anonymous_created").annotate(**metrics).order_by("anonymous_created")
        )

        response.context_data["summary_total"] = dict(qs.aggregate(**metrics))

        # Chart

        summary_over_time = (
            qs.annotate(
                period=Trunc(
                    "anonymous_created", period, output_field=DateTimeField(),
                ),
            )
            .values("period")
            .annotate(total=Count("anonymous_created"))
            .order_by("period")
        )

        summary_range = summary_over_time.aggregate(
            low=Min("total"), high=Max("total"),
        )
        high = summary_range.get("high", 0)
        low = summary_range.get("low", 0)

        response.context_data["summary_over_time"] = [
            {
                "period": x["period"],
                "total": x["total"] or 0,
                "pct": ((x["total"] or 0)) / (high) * 100
                if high > low
                else 100
                if high == low
                else 0,
            }
            for x in summary_over_time
        ]

        return response



@admin.register(IdentComplainSummary)
class IdentComplainAdmin(admin.ModelAdmin):
    change_list_template = "admin/identified_complains.html"
    date_hierarchy = "identified_created"

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context,)

        try:
            qs = response.context_data["cl"].queryset
        except (AttributeError, KeyError):
            return response

        metrics = {
            "total_genero": Count("identified_gender"),
        }

        response.context_data["summary"] = list(
            qs.values("identified_created").annotate(**metrics).order_by("identified_created")
        )
        response.context_data["summary_total"] = dict(qs.aggregate(**metrics))

        # Chart

        period = get_next_in_date_hierarchy(request, self.date_hierarchy,)
        response.context_data["period"] = period

        summary_over_time = (
            qs.annotate(
                period=Trunc(
                    "identified_created", period, output_field=DateTimeField(),
                ),
            )
            .values("period")
            .annotate(total=Count("identified_created"))
            .order_by("period")
        )

        summary_range = summary_over_time.aggregate(
            low=Min("total"), high=Max("total"),
        )
        high = summary_range.get("high", 0)
        low = summary_range.get("low", 0)

        response.context_data["summary_over_time"] = [
            {
                "period": x["period"],
                "total": x["total"] or 0,
                "pct": ((x["total"] or 0)) / (high) * 100
                if high > low
                else 100
                if high == low
                else 0,
            }
            for x in summary_over_time
        ]

        return response

    list_filter = (
        ("identified_current_status", ChoiceDropdownFilter),
        ("identified_position", ChoiceDropdownFilter),
        ("identified_gender", ChoiceDropdownFilter),
        ("identified_race", ChoiceDropdownFilter),
        ("identified_connection_unicamp", ChoiceDropdownFilter),
    )


#admin.site.register(AnonymousComplaint, AnonymousComplaintAdmin)
#admin.site.register(IdentifiedComplaint, IdentifiedComplaintAdmin)
admin.site.register(EnvolvedPerson, EnvolvedPersonAdmin)
