
import json
import requests
import xmltodict
import operator
import urllib

topics = ["Java", "C programming", "C++", "C#", "Python", "PHP", ".NET Development", "JavaScript", "Pascal", "Perl", "Ruby", "Swift", "Assembly language", "Objective-C", "R programming", "Visual Basic", "MATLAB", "Golang", "Scratch", "SQL"]


states = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

number_of_jobs_by_topic = {}
number_of_jobs_by_state = {}

INDEED_API_KEY = "[GO HERE AND GET ONE https://www.indeed.com/publisher]"

for state in states:
    for topic in topics:

        encoded_topic = urllib.quote(topic)

        r = requests.get("http://api.indeed.com/ads/apisearch?" + "publisher=" + INDEED_API_KEY + "&q=" + encoded_topic + "&l=" + state + "&co=us&userip=1.2.3.4&useragent=Mozilla/%2F4.0%28Firefox%29&v=2")

        o = xmltodict.parse(r.content)
        data = json.dumps(o) # '{"e": {"a": ["text", "text"]}}'

        data2 = json.loads(data)
        try:
            number_of_jobs = int(data2["response"]["totalresults"])
        except:
            print "error"

        # print "{} {} jobs".format(number_of_jobs, topic)

        number_of_jobs_by_topic[topic] = number_of_jobs


    sorted_jobs_by_topic = sorted(number_of_jobs_by_topic.items(), key=operator.itemgetter(1), reverse=True)[:5]

    print state + " " + str(sorted_jobs_by_topic)

    # for topic in sorted_jobs_by_topic:
    #     print "{} {} jobs".format(topic[1], topic[0])

    number_of_jobs_by_state[state] = sorted_jobs_by_topic
