TEST_MODULE1 = "test_module1"
TEST_MODULE2 = "test_module2"

version = (6, 7)

service = (TEST_MODULE1 if version < (6, 10)
           else TEST_MODULE2)
