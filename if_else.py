MODULE1 = "test1"
MODULE2 = "test2"
version = (6, 7)

service = (const.MODULE1 if version < (6, 10)
           else .MODULE2)
