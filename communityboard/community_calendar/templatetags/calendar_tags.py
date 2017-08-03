from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def month_name(date):
    return date.strftime("%B")


@register.filter
def change_month(date, num):
    if num < 0:
        if date.month == 1:
            return f'12-{date.year - 1}'
        else:
            return f'{date.month - 1}-{date.year}'
    elif num > 0:
        if date.month == 12:
            return f'1-{date.year+1}'
        else:
            return f'{date.month+1}-{date.year}'


@register.filter
def change_year(date, num):
    return f'{date.month}-{date.year+num}'
