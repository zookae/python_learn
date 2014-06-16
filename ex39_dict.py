### custom dictionary ###
def Map(num_buckets = 256):
    """Initializes a Map with a given number of buckets."""
    aMap = []
    # each bucket is a list of key-value tuples (pairs)
    for i in range(0, num_buckets):
        aMap.append([])
    return aMap

def Map_hash(aMap, key):
    """Given a key this will create a number and then convert it to an index for the aMap's buckets."""
    # hashes key, then uses remainder to index into the map
    return hash(key) % len(aMap)

def Map_get_bucket(aMap, key):
    """Given a key, find the bucket where it would go."""
    bucket_id = Map_hash(aMap, key)
    return aMap[bucket_id]

def Map_get_slot(aMap, key, default=None):
    """Returns the index, key, and value of a slot found in a bucket."""
    bucket = Map_get_bucket(aMap, key)

    # iterate over indices and key-value pairs in a map
    for i, kv in enumerate(bucket):
        # unpack key and value
        k, v = kv
        if key == k:
            # return when finding key
            return i, k, v

    return -1, key, default

def Map_get(aMap, key, default=None):
    """Gets the value in a bucket for the given key, or the default"""
    # wrapper to only given value
    i, k, v = Map_get_slot(aMap, key, default=default)
    return v

def Map_set(aMap, key, value):
    """Sets the key to the value, replacing any existing value."""
    bucket = Map_get_bucket(aMap, key)
    i, k, v = Map_get_slot(aMap, key)

    # default is None, so v existing means we replace
    if v:
        bucket[i] = (key, value)
    # otherwise we just append to the bucket list
    else:
        bucket.append((key, value))
    
def Map_delete(aMap, key):
    """Deletes the given key from the Map."""
    bucket = Map_get_bucket(aMap, key)

    # xrange is more efficient looping via a generator
    # gives object to iterate over
    for i in xrange(len(bucket)):
        # unpack key and value from bucket
        k, v = bucket[i]
        if key == k:
            del bucket[i]
            break

def Map_list(aMap):
    """Prints out what's in the Map."""
    for bucket in aMap:
        if bucket:
            for k, v in bucket:
                print k, v

# tests
jazz = Map()
Map_set(jazz, 'Miles Davis', 'Flamenco Sketches')

Map_set(jazz, 'Miles Davis', 'Kind of Blue')
Map_set(jazz, 'Duke Ellington', 'Beginning To See The Light')
Map_set(jazz, 'Billy Strayhorn', 'Lush Life')

print "---- list test ----"
Map_list(jazz)

print "---- get test ----"
print Map_get(jazz, 'Miles Davis')
print Map_get(jazz, 'Duke Ellington')
print Map_get(jazz, 'Billy Strayhorn')

print "---- delete test ----"
print "** goodbye Miles"
Map_delete(jazz, "Miles Davis")
Map_list(jazz)

print "** goodbye Duke"
Map_delete(jazz, "Duke Ellington")
Map_list(jazz)

print "** goodbye Billy"
Map_delete(jazz, "Billy Strayhorn")
Map_list(jazz)

print "** goodbye Pork Pie Hat"
Map_delete(jazz, "Charles Mingus")
Map_list(jazz)
