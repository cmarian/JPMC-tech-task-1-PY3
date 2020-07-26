import unittest
from client3 import *

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))
 


  """ ------------ Add more unit tests ------------ """
  
  #check getDataPoint - if calculated price is between the bid_price and ask_price
  def test_correct_average(self):
      quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())
      for quote in quotes:
          a = getDataPoint(quote)[1]  #bid
          b = getDataPoint(quote)[2]  #ask
          c = getDataPoint(quote)[3]  #calculated price
          self.assertTrue( a < c or b < c)
      
  # check getRatio - the case when price_b is zero
  def test_priceB_zero (self):
      self.assertIsNone(getRatio (120, 0))
   
  #check getRatio - the case when price_a is zero
  def test_priceA_zero(self):
      self.assertEqual(getRatio (0, 125), 0)
        

      



if __name__ == '__main__':
    unittest.main()
