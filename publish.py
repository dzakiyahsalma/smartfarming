import redis
import time
import traceback
import random
import string
 
def WorkCheck():
    try:

        # HERE SOME INITIAL WORK IS DONE THAT SCRIPTS 1 & 2 NEED TO WAIT FOR
        # IDs SERIAL PORTS
        # SAVE TO db
	
	def randomStringDigits(stringLength=64):
	    Digits = string.digits
	    return ''.join(random.choice(Digits) for i in range(stringLength))

        r = redis.StrictRedis(host='localhost', port=6379)                # Connect to local Redis instance

        p = r.pubsub()                                                    # See https://github.com/andymccurdy/redis-py/#publish--subscribe
 	while True: 
		##kirim data##
		kirim = randomStringDigits(5)
		#r.set("serversend",kirim)


		print("Starting main scripts...")

		r.publish('startScripts', kirim)                                # PUBLISH START message on startScripts channel

		print("Done")

    except Exception as e:
        print("!!!!!!!!!! EXCEPTION !!!!!!!!!")
        print(str(e))
        print(traceback.format_exc())

if __name__ == '__main__':
	WorkCheck()
