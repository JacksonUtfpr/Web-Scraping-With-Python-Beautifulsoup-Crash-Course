"""
  ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !

  These are didactic files, they are with a lots of comments to be consulted at some point 

  ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !
"""
from bs4 import BeautifulSoup
import requests

# Behind the scenes, the request library is requesting information from a specific website 

# The goal it is to get the jobs in the category python in the web site times.jobs.com with the date of post being ' posted few days ago'
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
# print(html_text)
# a large html file was printed
soup =  BeautifulSoup(html_text, 'lxml')

# each job post is a li from a ul

# jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
# print(jobs)
# prints another html kind structure

jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    
counter = 1

for job in jobs:
    published_date = job.find('span', class_='sim-posted').text.replace('Work from Home','')
    # print(published_date)


    if 'few' in published_date:
        print('\n')
        # the name of the company hiring is in h3 tag with a class of name joblist-comp-name 
        company_name = job.find('h3', class_="joblist-comp-name").text
        # print(company_name)
        # # It prints the company name correctly, but with spaces around

        company_name = job.find('h3', class_="joblist-comp-name").text.replace(' ','').replace('(MoreJobs)','')
        # print(company_name)
        # # now it only shows the company name, with no tab at the left side, as it was before

        skills_needed = job.find('span', class_='srp-skills').text.replace(' ','').replace('"','')
        # print(skills_needed)

        # print(f" Company Name: {company_name}")
        # print(f" Needed Skills:{skills_needed}")
        # print(f" Published Date: {published_date}")
        # It's getting printed with a lot os spaces, gonna take them out in the following lines:
        print(f" Job number:{counter}")
        print(f" Company Name: {company_name.strip()}")
        print(f" Needed Skills:{skills_needed.strip()}")
        print(f" Published Date: {published_date.strip()}")
        
        counter = counter+1

    # published_data = job.find('span', class_='sim-posted').text.replace('Work from Home','')
    # print(published_data)

    # print(f'''
    # Company Name: {company_name}
    # Needed Skills:{skills_needed}
    # ''')
# print('\n')
# for word in published_data:
#     print(word)

