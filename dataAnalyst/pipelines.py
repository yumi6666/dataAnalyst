# -*- coding: utf-8 -*-
import json


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DataanalystPipeline(object):
    def process_item(self, item, spider):
        # city	companyFullName	companyId	companyLabelList
        # companySize	businessZones	firstType	secondType	education	industryField
        # positionId	positionName	salary	workYear

        city = item['city'].encode('utf-8')
        companyFullName = item['companyFullName'].encode('utf-8')
        companyLabelList = item['companyLabelList'].encode('utf-8')
        companySize = item['companySize'].encode('utf-8')
        businessZones = item['businessZones'].encode('utf-8')
        firstType = item['firstType'].encode('utf-8')
        secondType = item['secondType'].encode('utf-8')

        education = item['education'].encode('utf-8')

        industryField = item['industryField'].encode('utf-8')
        positionName = item['positionName'].encode('utf-8')
        salary = item['salary'].encode('utf-8')
        workYear = item['workYear'].encode('utf-8')
        companyIdURL = item['companyIdURL'].encode('utf-8')
        positionId = item['positionId'].encode('utf-8')
        positionMessage = item['positionMessage'].encode('utf-8')



        return item

