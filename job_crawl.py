__author__ = 'ikangas'

from get_jobs import *


def loop_input(ask_for):
    result = []
    while True:
        inp = raw_input('Enter a {} (or plain to continue): '.format(ask_for))
        if inp == '':
            break
        result.append(inp)
    return result

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
