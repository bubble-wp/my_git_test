#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
__author__ = 'wp'

import string

def addWord(w, theSet):
    """
    Add the word to the set. No word smaller than length 3.
    :param w:
    :param theSet:
    :return:
    """
    if len(w) > 3:
        theSet.add(w)

def processLine(line, theSet):
    wordList = line.strip().split()
    for word in wordList:
        if word != '--':
            word = word.strip().strip(string.punctuation).lower()
            addWord(word, theSet)

def prettyPrint(gaSet, doiSet):
    print 'Count of unique words of length 4 or greater.'

    print 'GettysBurg Addr: %d, Decl of Ind: %d\n' % (len(gaSet), len(doiSet))
    print '%15s %15s' % ('Operation', 'Count')
    print '-'*35
    print '%15s %15d' % ('Union', len(gaSet.union(doiSet)))
    print '%15s %15d' % ('Intersection', len(gaSet.intersection(doiSet)))
    print '%15s %15d' % ('Sym Diff', len(gaSet.symmetric_difference(doiSet)))
    print '%15s %15d' % ('GA-DOI', len(gaSet.difference(doiSet)))
    print '%15s %15d' % ('DOI-GA', len(doiSet.difference(gaSet)))

    intersectionSet = gaSet.intersection(doiSet)
    wordList = list(intersectionSet)
    wordList.sort()
    print '\n Common words to both:'
    print '-' * 23
    cnt = 0
    for w in wordList:
        if cnt % 5 == 0:
            print
        print '%13s' % (w),
        cnt += 1

def main():
    GASet = set()
    DoISet = set()
    GAFileObj = open('gettysburg_speech.txt')
    DoiFileObj = open('THE_DECLARATION_OF_INDEPENDENCE.txt')
    for line in GAFileObj:
        processLine(line, GASet)
    for line in DoiFileObj:
        processLine(line, DoISet)
    prettyPrint(GASet, DoISet)


