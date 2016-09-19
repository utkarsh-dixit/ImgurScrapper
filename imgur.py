from imgurpython import ImgurClient
import string
import unicodedata
import urllib
import base64
import re
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
client_id = 'xMyClientIdx'
client_secret = 'xMyClientSecretx'
client = ImgurClient(client_id, client_secret)
db = MySQLdb.connect(host="localhost", user="root", passwd="",
db="imgur")
#Change the limit if you like
for num in range(0,100):
    items = client.gallery(section='hot', sort='viral', page=num, window='day', show_viral=True)
    for item in items:
        url = item.link
        if(url.split("//i.")[0]!=url):
            file_name = item.title

            print "DOWNLOADING: " + item.id
            testfile = urllib.URLopener()
	    t=""
	    t = re.sub(r'[^\x00-\x7F]+',' ', item.title)
            testfile.retrieve(url, "pics1/"+item.id+"."+url.split(".")[-1])
	    cursor = db.cursor()
	    cursor.execute("INSERT INTO post(id,title,likes,type) VALUES('"+item.id+"','"+str(MySQLdb.escape_string(t)).encode('utf-8')+"',0,'"+url.split(".")[-1]+"')" )
	    db.commit()
            with open("crawled.txt", "a") as crawled:
                crawled.write(item.id + "\n")

	else:

		with open("not_crawled.txt", "a") as not_crawled:
                	not_crawled.write(item.id +"\n")
