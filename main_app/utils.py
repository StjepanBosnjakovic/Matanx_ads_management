# main_app/utils.py

from .models import PricingRule
from django.utils import timezone

def get_applicable_pricing_rule(city_area, run_datetime):
    """
    Determines the pricing rule that applies based on the city area and time.
    """
    # Get all pricing rules
    pricing_rules = PricingRule.objects.all()

    # Filter out the default rule
    default_rules = pricing_rules.filter(is_default=True)
    default_rule = default_rules.first() if default_rules.exists() else None

    # Find rules that match the criteria
    applicable_rules = pricing_rules.exclude(is_default=True)

    # Filter by city area
    applicable_rules = applicable_rules.filter(
        models.Q(city_areas__isnull=True) | models.Q(city_areas=city_area)
    )

    # Filter by day of week
    day_of_week = run_datetime.weekday()  # 0 = Monday, 6 = Sunday
    applicable_rules = applicable_rules.filter(
        models.Q(days_of_week__isnull=True) | models.Q(days_of_week__contains=[day_of_week])
    )

    # Filter by time
    time = run_datetime.time()
    applicable_rules = applicable_rules.filter(
        models.Q(start_time__isnull=True, end_time__isnull=True) |
        models.Q(start_time__lte=time, end_time__gte=time)
    )

    # Get the highest priority rule (you can define a priority system if needed)
    if applicable_rules.exists():
        # For simplicity, pick the first matching rule
        return applicable_rules.first()
    else:
        return default_rule
