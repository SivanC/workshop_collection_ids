#!/usr/bin/env python

import requests
import json
import argparse

def main():
    """
    Uses the Steam Web API to retrieve the IDs of workshop items in a given
    collection and prints them in a comma separated list to stdout, or 
    optionally a file.

    usage: workshop_collection_ids.py [-h] [-f FILE] collection_id [collection_id]...
    """
    # json to send to API containing number of collections and IDs for each
    data = {}
    data['collectioncount'] = len(args.publishedfileids)
    for i in range(data['collectioncount']):
        data['publishedfileids[{n}]'.format(n=str(i))] = args.publishedfileids[i]

    # steam API GetCollectionDetails takes collectioncount and a number of collection ids
    url = "https://api.steampowered.com/ISteamRemoteStorage/GetCollectionDetails/v1/"
    res = requests.post(url, data=data)

    # generate and print list of item ids from collection
    collections = json.loads(res.text)
    for collection in collections['response']['collectiondetails']:
        item_ids = []
        for item in collection['children']:
            itemID = item['publishedfileid']
            item_ids.append("{itemID}".format(itemID=itemID))
        # format with collection id, quotes, and newlines
        if args.format:
            res = "Collection: {colID}: \n\"".format(colID=collection['publishedfileid']) +\
                  "\",\n\"".join(item_ids) + "\""
        # format as comma-separated list
        else:
            res = ",".join(item_ids) + "\n"
        # write to file
        if args.file:
            with open(args.file[0], 'w') as f:
                print(res, file=f)
        # write to stdout
        else:
            print(res)
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='workshop_collection_ids',
                        description="""
                        Uses the Steam Web API to retrieve the IDs of workshop
                        items in a given collection and prints them in a comma
                        separated list to stdout, or optionally a file.
                        """)
    parser.add_argument('publishedfileids', metavar='collection_id', nargs='+', type=int,
                        help='one or more space-separated Steam Workshop collection IDs')
    parser.add_argument('-f', '--file', nargs=1, type=str,
                        help='write the output to FILE')
    parser.add_argument('-F', '--format', action='store_true', required=False,
                        help='formats the list with collection ID, quotes, and newlines')
    args = parser.parse_args()
    main()
