
import redis
import time
import traceback


def RedisCheck():
    try:
        r = redis.StrictRedis(host='localhost', port=6379)                          # Connect to local Redis instance

        p = r.pubsub()                                                              # See https://github.com/andymccurdy/redis-py/#publish--subscribe
        p.subscribe('startScripts')                                                 # Subscribe to startScripts channel
	

        while True:                                                               # Will stay in loop until START message received
            #print("Waiting For redisStarter...")
            message = p.get_message()                                               # Checks for message
            if message:
                command = message['data']                                        # Get data from message
		print(command)

                if command == b'START':                                             # Checks for START message
                    PAUSE = False                                                   # Breaks loop

            time.sleep(0.5)

        print("Permission to start...")
	 
	##terima data##
	#pesan=r.get("serversend")
	#print(pesan)
	##----------##

    except Exception as e:
        print("!!!!!!!!!! EXCEPTION !!!!!!!!!")
        print(str(e))
        print(traceback.format_exc())

if __name__ == '__main__':
	RedisCheck()
