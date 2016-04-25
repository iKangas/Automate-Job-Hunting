__author__ = 'ikangas'

import urllib
from bs4 import BeautifulSoup
from get_location_names import *

all_jobs = {
    'facebook': {
        'jobs': get_fb_jobs,
        'link': 'https://www.facebook.com'
    },
    'spotify': {
        'jobs': get_spotify_jobs,
        'link': 'https://www.spotify.com'
    }
}


#facebook
def get_fb_jobs(city_url):
    url = 'https://www.facebook.com/careers/locations/{}/'.format(city_url)
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml')
    jobs_url = soup.findAll("div", {"class": "_4hnn"})
    return jobs_url


#spotify
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