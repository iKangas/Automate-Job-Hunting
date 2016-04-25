import urllib
from bs4 import BeautifulSoup

spotify_full_name = {
    'london': 'london-united-kingdom',
    'new-york': 'new-york-ny-united-states',
    'stockholm': 'stockholm-sweden'
}

def loop_input(ask_for):
    result = []
    while True:
        inp = raw_input('Enter a {} (or plain to continue): '.format(ask_for))
        if inp == '':
            break
        result.append(inp)
    return result


def get_fb_jobs(city_url):
    url = 'https://www.facebook.com/careers/locations/{}/'.format(city_url)
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml')
    jobs_url = soup.findAll("div", {"class": "_4hnn"})
    return jobs_url


def get_spotify_jobs(city_url):
    if city_url in spotify_full_name.keys():
        city_url = spotify_full_name[city_url]
        url = 'https://www.spotify.com/gr/jobs/opportunities/all/all/{}/'.format(city_url)
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html, 'lxml')
        jobs_url = soup.findAll("h3", {"class": "job-title"})
        return jobs_url
    else:
        return []

# get input data for keywords and cities to search
job_keys = loop_input('job key')
print
cities = loop_input('city')
print
print 'Let\'s check for {} in {}\n'.format(job_keys, cities)

# lets check
for city in cities:
    print '*** City: {} ***'.format(city)
    print
    # FACEBOOK
    fb_jobs = get_fb_jobs(city)
    for job in fb_jobs:
        if any(k in job.text for k in job_keys):
            print 'Title: {}'.format(job.text.encode('ascii', 'ignore'))
            print 'link: https://www.facebook.com{}\n'.format(job.a['href'])
    # SPOTIFY
    spotify_jobs = get_spotify_jobs(city)
    for job in spotify_jobs:
        if any(k in job.text for k in job_keys):
            print 'Title: {}'.format(job.text.encode('ascii', 'ignore'))
            print 'link: https://www.spotify.com{}\n'.format(job.a['href'])
    print
