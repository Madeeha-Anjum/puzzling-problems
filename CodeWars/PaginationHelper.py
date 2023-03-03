# TODO: complete this class

import math


class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        # if self.item_count() % self.items_per_page != 0:
        #     return (self.item_count() // self.items_per_page) + 1
        # return self.item_count() // self.items_per_page

        return (
            (self.item_count() // self.items_per_page) + 1
            if self.item_count() % self.items_per_page != 0
            else self.item_count() // self.items_per_page
        )

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index > self.page_count():
            return -1
        if page_index == self.page_count():
            return self.item_count() % self.items_per_page
        else:
            return self.items_per_page

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):

        if item_index < 0:
            return -1
        if item_index > self.item_count():
            return -1

        return item_index // self.items_per_page


if __name__ == "__main__":
    collection = range(1, 25)
    # PaginationHelper takes in an array of values and an integer indicating how many items will be allowed per each page
    helper = PaginationHelper(collection, 10)

    assert helper.page_count() == 3
    assert helper.item_count() == 24
    assert helper.page_index(23) == 2
