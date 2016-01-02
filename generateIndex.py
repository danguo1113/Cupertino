# -*- coding: utf-8 -*-

import os


def writeToOutfile(outfile, fn):
	with open(fn,'r') as infile:
		for line in infile:
			outfile.write(line)


def generateIndex():
	root = './Entries/'
	with open('index.html', 'w') as outfile:

		writeToOutfile(outfile,'docFirst.html')
		

		dirList = os.listdir(root)
		dirList = sorted(dirList)
		for fn in dirList:
			if not os.path.isdir(os.path.join(root, fn)): continue
			entryMetadataFn = open(os.path.join(os.path.join(root, fn),'meta.txt'),'r')
			entryLink = fn + '.html'
			entryTitle = entryMetadataFn.readline().strip()
			entryTagline = entryMetadataFn.readline().strip()
			entryDate = entryMetadataFn.readline().strip()
			line = """
			    <div class="post-preview">
                    <a href="{0}">
                        <h2 class="post-title">{1}</h2>
                        <h3 class="post-subtitle">{2}</h3>
                    </a>
                    <p class="post-meta">Posted on {3}</p>
                </div>
                <hr>"""
			outfile.write(line.format(entryLink,
									  entryTitle,
									  entryTagline,
                        			  entryDate))
		writeToOutfile(outfile,'docLast.html')


generateIndex()