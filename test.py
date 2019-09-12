import unittest
from flask import Flask ,request
from app import app

class FlaskTestCase(unittest.TestCase):

       def test_capital(self):
             data={"country":"cuba"}
             result = app.test_client().get("/capital",query_string =data)
             #print(result)
             self.assertEquals(result.status_code, 200)
             #print(result)
             #self.assertEquals(result.status_code,500)

if __name__ == '__main__':
    unittest.main()
