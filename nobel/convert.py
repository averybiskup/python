#Person(id, givenName, familyName, gender)

#Org(id, orgName, date)

#Location(id, city, country)

#Award(awardYear, category, sortOrder, awardeeId)

#Affiliation(name, id) 

"""
What is the id of “Marie Curie”? (Answer: 6)
What country is the affiliation “CERN” located in? (Answer: Switzerland)
Find the family names associated with five or more Nobel prizes (Answer: Smith, Wilson)
How many different locations does the affiliation “University of California” have? 
Assume that a location is uniquely identified by its city and country. (Answer: 6)
In how many years a Nobel prize was awarded to an organization (as opposed to a person) in at least one category?
(Answer: 26)
"""

import json

with open('nobel-laureates.json', 'r') as f:
    DATA = json.load(f)

LAUREATES = DATA['laureates']

def person_table():
    with open('person.del', 'w+') as f:
        for lrt in LAUREATES:
            if "orgName" not in lrt:
                lrt_id = lrt['id']
                familyName = '\\N'
                givenName = '\\N'
                if ('givenName' in lrt):
                    givenName = lrt['givenName']['en'] or ''
                    

                if ('familyName' in lrt):
                    familyName = lrt['familyName']['en']

                gender = lrt['gender']
                f.write('{},"{}","{}","{}"\n'.format(lrt_id,
                                        givenName,
                                        familyName,
                                        gender))
        
def org_table():
    with open('org.del', 'w+') as f:
        for lrt in LAUREATES:
            if "orgName" in lrt:
                lrt_id = lrt['id']
                orgName = lrt['orgName']['en']
                date = '\\N'

                try:
                    date = lrt['founded']['date'] 
                except:
                    pass

                f.write('{},"{}",{}\n'.format(lrt_id, orgName, date))

def location_table():
    with open('location.del', 'w+') as f:
        for lrt in LAUREATES:
            lrt_id = lrt['id']
            city = '\\N'
            country = '\\N'

            if "orgName" in lrt:
                try: city = lrt['founded']['place']['city']['en']
                except: pass

                try: country = lrt['founded']['place']['country']['en']
                except: pass
            else:
                try: city = lrt['birth']['place']['city']['en']
                except: pass

                try: country = lrt['birth']['place']['country']['en']
                except: pass

            f.write('{},"{}","{}"\n'.format(lrt_id, city, country))

def award_table():
    with open('award.del', 'w+') as f:
        for lrt in LAUREATES:
            lrt_id = lrt['id']

            prizes = lrt['nobelPrizes']
            for award in prizes:
                year = award['awardYear']
                category = award['category']['en']
                sort_order = award['sortOrder']

                f.write('{},{},"{}",{}\n'.format(lrt_id, year, category, sort_order));

def affiliation_table():
    with open('affiliation.del', 'w+') as f:
        for lrt in LAUREATES:
            lrt_id = lrt['id']

            prizes = lrt['nobelPrizes']
            for award in prizes:
                if ('affiliations' in award):
                    for af in award['affiliations']:
                        name = af['name']['en']
                        
                        f.write('{},"{}"\n'.format(lrt_id, name));
    

person_table()
org_table()
location_table()
award_table()
affiliation_table()
