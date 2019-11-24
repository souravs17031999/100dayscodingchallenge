from sys import stdin, stdout
class Units_conversion:
    def __init__(self):
        self.units = {'INR':0.014, 'YEN':0.0092, 'USD':1, 'GBP':1.28}
    def convert(self, src_unit, dst_unit, value):
        if src_unit in self.units:
            temp_usd = self.units[src_unit] * value
            return temp_usd / self.units[dst_unit]
    def add_unit(self, new_unit, new_conversion_rate):
        self.units[new_unit] = new_conversion_rate        

if __name__ == '__main__':
    print('WELCOME TO CURRENCY CONVERSION PORTAL !')
    print('write your source currency, target currency and your value for conversion - ')
    l = list(stdin.readline().strip().split())
    unit = Units_conversion()
    print(f'converted value is {unit.convert(l[0], l[1], int(l[2]))}')
