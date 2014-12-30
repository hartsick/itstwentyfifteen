import logging
from time import sleep
from multiprocessing import Process
from stream import UserStreamer, PublicStreamer
from common import twitter_cred
from phrases import search_phrases

def run_user_stream():
    # start Twitter stream for user, restart with delay on crash
    #   -- for detecting user interaction with bot
    while True:
        try:
            stream = UserStreamer(*twitter_cred)
            stream.user(**{'with': 'user'})
        except Exception as e:
            logging.exception(e)

        sleep(60)

def run_public_stream():
    # start Twitter stream for search, restart with delay on crash
    #   -- for pulling random resolutions from twitter
    while True:
        try:
            stream = PublicStreamer(*twitter_cred)
            # note to self with internet: need to look up how to track multiple phrases
            stream.statuses.filter(track=search_phrases)
        except Exception as e:
            logging.exception(e)

        sleep(60)


if __name__ == "__main__":

    p1 = Process(target=run_user_stream)
    p2 = Process(target=run_public_stream)

    processes = [
        p1, p2
    ]

    # start then join all processes
    for process in processes:
        process.start()

    for process in processes:
        process.join
