# _*_coding:utf-8 _*_
# 习题39：可爱的字典

# Create a mapping of state to abbreviation
states = {
    'Oregon':'OR',
    'Florida':'FL',
    'California':'CA',
    'New York':'NY',
    'Michigan':'MI'
}

# Create a basic set of states and some cities in them
cities = {
    'CA':'San francisco',
    'MI':'Detroit',
    'FL':'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cites
print '-' * 10
print "NY States has: ",cities['NY']
print "OR State has: ",cities['OR']

# print some states
print '-' * 10
print "Micigan----%s" % states['Michigan']
print "Florida----",states['Florida']

print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state,abbrev)

print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s and has city %s" % (
    state,abbrev,cities[abbrev])

print '-' * 10
states = states.get('Texas', None)
if not state:
    print "Sorry,no Texas."

city = cities.get('TX','Does Not Exist')
print city
