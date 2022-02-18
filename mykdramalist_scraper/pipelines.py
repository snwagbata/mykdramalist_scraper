# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# Possible here in pipeline - set different pipelines for each of the spiders
# All pipelines will check if item is in db before adding to db
# TODO: if item is in db, then change the drama status field to [completed, ongoing, upcomign]
# this will eliminate the need for having to store the data from each spider in a different collection.


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from google.cloud import firestore

import os;


class MykdramalistScraperPipeline:
    def process_item(self, item, spider):
        return item

    def __init__(self):
        # use below with github actions as that will infer project_id based on environment
        self.db = firestore.Client()
        # self.db = firestore.Client.from_service_account_json('./test-1a77a-167f4c077928.json')
        # self.db = firestore.Client.from_service_account_json('./mydramalist-520e5-aaf4d4cbbb0b.json')

    def process_item(self, item, spider):
        """
        Method that is performed on each item returned by our spider and which
        allows us to insert it into the DB
        Args:
            item (dict): item returned by our Scrapy spider
            spider (scrapy.Spider): Scrapy spider object
        """
        # get item's slug
        slug = item['slug']
        if slug is not None:
            # # add to firestore using item's slug as id
            #TODO: we'll most likely use timestamp to check delete items from collections like the upcoming and ongoing
            # if not self.db.collection('dramas').document(slug).get().exists:
            self.db.collection(u'dramas').document(slug).set(ItemAdapter(item).asdict())
        else:
            self.db.collection('dramas').add(ItemAdapter(item).asdict())


# class DuplicatesPipeline:

#     def __init__(self):
#         self.ids_seen = set()

#     def process_item(self, item, spider):
#         adapter = ItemAdapter(item)
#         if adapter['id'] i self.ids_seen:
#             raise DropItem(f"Duplicate item found: {item!r}")
#         else:
#             self.ids_seen.add(adapter['id'])
#             return item
