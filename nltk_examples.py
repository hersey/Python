

from nltk.corpus import inaugural

cfd = nltk.ConditionalFreqDist(
	(target, file[:4])
	for fileid in inaugural.fileids() 
	for w in inaugural.words(fileid)
	for target in ['america', 'citizen','opportunity']
	if w.lower().startswith(target))

cfd.plot()
