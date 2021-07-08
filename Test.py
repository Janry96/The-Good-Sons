import unittest
import main


class Test(unittest.TestCase):
    def test1(self):
        all_total = main.equals1('2+1')

        self.assertEqual(all_total, '3')

    def test2(self):
        all_total = main.equals1('Sin(5)')

        self.assertEqual(all_total, '-0.9589242746631385')

    def test3(self):
        all_total = main.equals1('2x3x4')

        self.assertEqual(all_total, '24')
    
    def test4(self):
    	all_total = main.equals1('13^2')
    	
    	self.assertEqual(all_total, '169')
    
    def test5(self):
    	all_total = main.equals1('99/0')
    	
    	self.assertEqual(all_total, ' error ')
    
    def test6(self):
    	self.assertEqual(main.equals1('1/100'), '0.01')
    	
    def test7(self):
    	self.assertEqual(main.equals1('Cos(90)'), '-0.4480736161291701')
    
    def test8(self):
    	self.assertEqual(main.equals1('Tan(45)'), '1.6197751905438615')
    	
    def test9(self):
    	self.assertEqual(main.equals1('log(10)'), '1.0')
    	
    def test10(self):
    	self.assertEqual(main.equals1('asin(0)'), '0.0')
    
    def test11(self):
    	self.assertEqual(main.equals1('1-2-3-4-5'), '-13')
    
    def test12(self):
    	self.assertEqual(main.equals1('Sin(60)^0'), '1.0')

    def test13(self):
        self.assertEqual(main.equals1('acos(1)'), '0.0')

    def test14(self):
        self.assertEqual(main.equals1('a+b-c*d/e'), ' error ')

    def test15(self):
        self.assertEqual(main.equals1('25(5)'), '125')

    def test16(self):
        self.assertEqual(main.equals1('4(2)+10'), '18')

    def test17(self):
        self.assertEqual(main.equals1('e(2)'), '7.38905609893065')

    def test18(self):
        self.assertEqual(main.equals1('100^ (1/2)'), '10.0')

if __name__ =="__main__":
    unittest.main()
