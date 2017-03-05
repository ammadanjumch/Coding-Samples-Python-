import re, urllib
#!/usr/bin/python
myurl='http://defence.pk/forums/economy-development.18/'
ListOfTopics=re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(myurl).read(), re.I)
NoOfTopics=0
for i in ListOfTopics:
	if str(i).find('threads/')>=0:
		if str(i).find('page-')==-1:
				NoOfTopics=NoOfTopics+1
count=0
for i in ListOfTopics:
	if str(i).find('threads/')>=0:
		if str(i).find('page-')==-1:
			count=count+1
			topicurl='http://defence.pk/'+str(i)
			filename=str(i)
			filename=filename.replace('threads/',"")
			filename=filename.replace('.',"")
			filename=filename.replace('/',"")
			filename=filename+'.txt'
			fileout=open(filename,"a+")
			page=str(urllib.urlopen(topicurl).read())
			IndexOfPageNos=page.find('<span class="pageNavHeader">Page')
			NoOfPages=page[IndexOfPageNos+33:IndexOfPageNos+45]
			fileout.write(str(page));
			if str(NoOfPages).find('lang=')==-1:
				print 'No of Topics '+str(NoOfTopics)
				print 'Topic Number '+ str(count)
				print topicurl
				Pages=str(NoOfPages).split(" ")
				split= str(Pages[2]).split("<")
				StartPage=Pages[0]
				LastPage=split[0]
				LastPage = int(LastPage)
				print 'Number of Pages ' + str(LastPage)
				print ' '
				for counter in range(2, LastPage):
					print 'Page Number: ' + str(counter)
					topicurl=topicurl+'page-'+str(counter)
					page=str(urllib.urlopen(topicurl).read())
					fileout.write(str(page));