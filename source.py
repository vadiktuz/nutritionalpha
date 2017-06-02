import wolframalpha
import cPickle as pkl
import os.path
import hashlib


def get_respond(quiery, refresh = False):

    """
    Checks if the respond for the _query has been saved to DB and if not, reconnects to WolframAlpha API
    TODO: Come to some primitive database pickling arrays of respond objects hashing their corresponding queries

    :param _query: string natural language-like _query for WolframAlpha
    :param refresh: boolean if to refresh packed respond
    :return:
    """
    picklename = "respond.alpha"
    if os.path.isfile(picklename) and not refresh:
        return pkl.load(picklename)
    else:
        client = wolframalpha.Client("VJX97W-E4AEVEEYVK")
        respond = client.query(_query)
        with open(picklename, 'wb') as pickle_file:
            pkl.dump(respond, pickle_file)
        return respond



query = (r"(3 eggs) plus (2/7 kg raw chicken breasts)" +
    r" plus (200g cottage chease fat free) plus (1/7 kg tomatoes)" +
    r"  plus (1.5/7 kg cucumbers)")

respond = get_respond(query, refresh=True)

#hash_object = hashlib.md5(quiery.strip())
#print(hash_object.hexdigest())

for pod in respond:
    print pod.keys()
