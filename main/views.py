from django.shortcuts import render
import requests


def home(request):
    search_term = 'India'
    if request.method == 'POST':
        if request.POST.get('numero', False):
            search_term = request.POST['numero']
            print(search_term)

    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {"country": search_term}

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "8492c5bfefmsh8caa5bc74aeaccap1c41fdjsnae0a1605aca3"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    data = response['response']

    d = data[0]

    print(d)

    context = {
        'all': d['cases']['total'],
        'recovered': d['cases']['recovered'],
        'deaths': d['deaths']['total'],
        'new': d['cases']['new'],
        'critical': d['cases']['critical']
    }
    return render(request, 'index.html', context)

