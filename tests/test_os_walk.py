#!python

from dirsync import syncer
res = syncer.os_walk("/Users/viv/WorkDocs/Sync/Notes/Perso/")

print("RESULT")
for r in res:
    print(r)


res = syncer.os_walk("/Users/viv/WorkDocs/Sync/Notes/Perso/", True)

print("RESULT")
for r in res:
    print(r)
