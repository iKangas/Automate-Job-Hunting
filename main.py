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

#run for each city
for raw_city in cities:
    city = raw_city.lower()
    print '*** City: {} ***\n'.format(city.upper())
    #run for each company
    for company in all_jobs.keys():
        jobs = all_jobs[company]['jobs'](city)
        if len(jobs) > 0:
            print '-- Company: {} --\n'.format(company.title())
            #filter jobs based on keywords
            for job in jobs:
                if any(k.title() in job.text for k in job_keys):
                    print 'Title: {}'.format(job.text.encode('ascii', 'ignore'))
                    print 'link: {}{}\n'.format(all_jobs[company]['link'], job.a['href'])
            print
