# coding=utf-8

import leancloud


class CloudUtil(object):

    @classmethod
    def createWithoutData(cls, table_name, objectId):
        TableClass = leancloud.Object.extend(table_name)
        return TableClass.create_without_data(objectId)

    @classmethod
    def updateByKwargs(cls, table_name, objectId, **kwargs):
        TableClass = leancloud.Object.extend(table_name)
        tableclass = TableClass.create_without_data(objectId)
        for k, v in kwargs.items():
            tableclass.set(k, v)
        tableclass.save()

    @classmethod
    def queryByKeyValue(cls, table_name, key, value):
        TableClass = leancloud.Object.extend(table_name)
        query = TableClass.query
        query.equal_to(key, value)
        return query.find()

    @classmethod
    def queryByField(cls, table_name, *args):
        TableClass = leancloud.Object.extend(table_name)
        query = TableClass.query
        query.select(*args)
        query.limit(1000)
        return query.find()

    @classmethod
    def queryByObjectId(cls, table_name, objectId):
        TableClass = leancloud.Object.extend(table_name)
        query = TableClass.query
        return query.get(objectId)

    @classmethod
    def queryPointers(cls, table_name, pointer_table_name, pointer_objectId):
        TableClass = leancloud.Object.extend(pointer_table_name)
        tableclass = TableClass.create_without_data(pointer_objectId)
        query = leancloud.Query(table_name)
        query.equal_to("target"+pointer_table_name, tableclass)
        query.add_ascending('orderNum')
        return query.find()

    @classmethod
    def queryCountByKeyValue(cls, table_name, key, value):
        TableClass = leancloud.Object.extend(table_name)
        query = TableClass.query
        query.equal_to(key, value)
        return query.count()