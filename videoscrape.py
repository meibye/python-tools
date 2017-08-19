#
# Scrape video's from Safari Online based on the
# "Safari Books Online Video Downloader" Chrome extension
#
# Usage: videoScrape [-h] [-e] [-s] -i <videoURL>
#    -h: print usage
#    -e: print environment variables
#    -s  use the chromedriver as a Service, i.e. do not terminate
#        the driver after each instantiations
#
# Reference material
# ------------------
#   XPath:      https://www.guru99.com/xpath-selenium.html
#   Selenium:   https://seleniumhq.github.io/selenium/docs/api/py/api.html#common
#               http://docs.seleniumhq.org/docs/03_webdriver.jsp#selenium-webdriver-api-commands-and-operations
#
import sys, os
import getopt
import time

#
# Usage description
#
def usage():
    print('Scrape video\'s from Safari Online based on the "Safari Books Online Video Downloader" Chrome extension\n')
    print('Usage:')
    print('   videoScrape.py [-e] [-h] -i: <safari URL>\n')
    print('      -h   show usage')
    print('      -e   show environment variables')
    # print('      -s   use the chromedriver as a Service, i.e. do not terminate the driver after each instantiations')
    print('      -i   followed by the URL for the Safari page containing video download buttons')

#
# Evaluate Command parameters
#
envShow = False
videoURL = ''
chromeService = False
try:
    opts, args = getopt.getopt(sys.argv[1:], 'hesi:', '[ifile=]')
except getopt.GetoptError as err:
    usage()
    print('Error: ', err)
    raise SystemExit(2)
for opt, arg in opts:
    if opt == '-h':
        usage()
        raise SystemExit()
    elif opt == '-e':
        envShow = True
    elif opt == '-s':
        chromeService = True
    elif opt in ('-i', '--ifile'):
        videoURL = arg
    else:
        print('Unknown command option ', opt)
if videoURL == '':
    usage()
    print ('Missing -i input option')
    raise SystemExit(2)

#
# Print Environment Variables
#
if envShow:
    print('Python path: {0}'.format(sys.prefix))

    print('Environment Variables:')
    print('======================')
    for e in os.environ:
        print('{k:25s}: {v:s}'.format(k=e, v=os.environ[e]))

#
# Test whether chromedriver as a service has been requested
#
if chromeService:
    print('chromedriver as a service is currently not supported!')

print('Video URL: ', videoURL)

#
# Add the requirement to load the "Safari Books Online Video Downloader" extension
# (id: ihgjlggckknakenjhgmfgaoalflhfihl)
#
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_extension('C:/Users/micha/AppData/Local/Google/Chrome/User Data/Default/Extensions/ihgjlggckknakenjhgmfgaoalflhfihl/')

#
# Open the Chrome browse with the given URL
#
from selenium import webdriver
try:
    driver = webdriver.Chrome(chrome_options=chrome_options)
except Exception as err:
    print('Exception')
    print(err)
    raise SystemExit(2)


#
# Load the requested web page. Wait until it is presented by waiting until the text "Now playing:"
# is available. Max wait 20 seconds
# Determine whether  video is playing. If this is the case then pause the video.
#
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver.get(videoURL)
try:
    element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "bcnowplaying")))
finally:
    print ('Web page not presented within 20 seconds')
    print ('Program terminates...')
    driver.quit()


time.sleep(10)
# driver.quit()
print('\nStop program')
raise SystemExit(0)



#
# # Define the Web page to present
# webPage = "http://my.safaribooksonline.com/video/programming/python/9781787285880"
# driver.get(webPage)
