# == Script to run a small sanity check over the quotes ==

import yaml
import glob

files = glob.glob("*.yaml")

validTags = ['important','morning']
validLangs = ['es', 'en', 'ca', 'fr']  # ca: catalan

quoteCount = {}
for lng in validLangs:
    quoteCount[lng] = 0

idx = 0
for f in files:
    fd = open(f)
    docs = yaml.load_all(fd)
    
    for doc in docs:
        if doc is None:
            continue
        
        for tag in doc['tags']:
            if not tag in validTags:
                print "Invalid tag: ", tag

        for lng in validLangs:
            if doc.has_key(lng):
                quoteCount[lng] += 1
    fd.close()

# Show how many quotes there are in each language
print "Number of quotes per language:"
print quoteCount