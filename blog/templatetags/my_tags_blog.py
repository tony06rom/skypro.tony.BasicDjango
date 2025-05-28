from django import template


register = template.Library()


@register.filter()
def media_filter(path):
    if path:
        return f"/data/media/{path}"
    return "#"
