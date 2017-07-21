
# Scrape
#
# Usage: videoScrape [-h] [-e] -i <videoURL>
#    -h: print usage
#    -e: print environment variables
#
import sys, getopt
import os

#
# Evaluate Command parameters
#
envShow = False
videoURL = ''
try:
    opts, args  = getopt.getopt(argv, 'hei:', '[ifile=]')
except getopt.GetoptError as err:
    print ('videoScrape.py -i: <safari URL>')
    print ('Error: ', err)
    raise SystemExit(2)
for opt, arg in opts:
    if opt == '-h':
        print ('videoScrape.py -i: <safari URL>')
        raise SystemExit()
    elif opt == '-e':
        envShow = True
    elif opt in ('-i', '--ifile'):
        videoURL = arg
    else:
        print ('Unkown command option', opt)
if videoURL == '':
    print ('videoScrape.py -i: <safari URL>')
    raise SystemExit()
print ('Video URL: ', videoURL)

#
# Print Environment Variables
#
if envShow:
    print ('Python path: {0}'.format(sys.prefix))
    print (os.environ)
    print ('Environment Variables:')
    print ('======================')
    for e in os.environ:
        print ('{k:25s}: {v:s}'.format(k=e, v=os.environ[e]))

print ('Stop program')
raise SystemExit(0)

# from selenium import webdriver
#
# driver = webdriver.Chrome()
#
# # Define the Web page to present
# webPage = "http://my.safaribooksonline.com/video/programming/python/9781787285880"
# driver.get(webPage)
