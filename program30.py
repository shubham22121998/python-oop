class Example:
    num=5
    @staticmethod
    def sum_of_number(num1,num2):
        result=(num1+num2)*Example.num
        print(result)
Example.sum_of_number(100,200)
