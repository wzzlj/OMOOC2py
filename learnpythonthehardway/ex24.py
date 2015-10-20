# _*_ coding:utf-8 _*_

print "Let's practice everything"
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
\n\twhere there is none/
"""

print "____________"
print poem
print "____________"


five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def sf(started):
    jb = started * 500
    jars = jb / 1000
    crates = jars / 100
    return jb,jars,crates

sp = 10000
beans,jars,crates = sf(sp)


print "With a starting point of: %d" % sp
print "We'd have %d beans, %d jars, and %d crates." % (beans,jars,crates)

sp = sp / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % sf(sp)
