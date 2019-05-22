# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.item import Item, Field 
 
class DataanalystItem(scrapy.Item):
    # Primary fields 
    city = Field() 
    companyFullName = Field() 
    companyLabelList = Field()
    companySize = Field() 
    businessZones = Field() 
    firstType = Field() 
    secondType = Field()
    education = Field()
    industryField = Field()
    positionName = Field()
    salary = Field()
    workYear = Field()
    positionId= Field()
    companyIdURL= Field()
    positionMessage = Field()
    #
    ## Calculated fields 
    #images = Field() 
    #location = Field() 
    #
    ## Housekeeping fields 
    url = Field() 
    #project = Field() 
    #spider = Field() 
    #server = Field() 
    date = Field() 