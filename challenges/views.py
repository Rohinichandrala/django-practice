from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.template.loader import render_to_string

monthly_text_map = {
    'january': 'Try to find the one fitness or game that you can do daily',
    'february': 'Walk for 20 minutes daily every day',
    'march': 'try to learn python in this month',
    'april': 'Start swimming session',
    'may': 'Search for violin tutor',
    'june': 'Become a pro in swimming',
    'july': 'Its your birthday month! Enjoy to the fullest',
    'august': 'Its getting cold! check for US visa',
    'september': 'Add some new goal',
    'october': None,
    'november': 'Learn pasurams',
    'december': 'Avoid non vegetarian'
}


# Create your views here.

def challenge_main(request):
    items_list = ''
    months_list = list(monthly_text_map.keys())
    # for month in months_list:
    #     month_path = reverse('month-by-name', args=[month])
    #     items_list += f'<li><a href=\"{month_path}\">{month.capitalize()}</a></li>'
    #
    # final_data = f'<ul>{items_list}</ul>'
    # return HttpResponse(final_data)
    return render(request, 'challenges/index.html', {
        'months_list': months_list
    })


def process_month_by_number(request, month_num):
    months = list(monthly_text_map.keys())

    if month_num > len(months):
        return HttpResponseNotFound("There is no such month")

    resolved_month = months[month_num - 1]
    resolved_path = reverse('month-by-name', args=[resolved_month])
    return HttpResponseRedirect(resolved_path)


def process_month(request, month):
    try:
        text = monthly_text_map[month]
        # html_data = f'<h1>{text}</h1>'
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(html_data)
        # return HttpResponse(response_data)
        return render(request, 'challenges/challenge.html', {
            "challenge_text": text,
            "month_text": month
        })
    except:
        # render_string = render_to_string('404.html')
        # return HttpResponseNotFound(render_string)
        raise Http404()

