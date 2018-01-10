MODULE1 = "test_module1"
MODULE2 = "test_module2"
version = (6, 7)

service = (MODULE1 if version < (6, 10)
           else MODULE2)
