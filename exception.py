class InvalidListNumberException(Exception):
    pass
class  account:
    account_list=[1001,1002,1003,1004,1005]

    def validate_account(self,account_id):
        status=0
        for acc_id in self.account_list:
            if (account_id==acc_id):
                status=1
                break
            if status!=0:
                return True
            else:

                raise InvalidListNumberException
try:
    a=account()
    a.validate_account(1006)
    print("valid number")
except  InvalidListNumberException:
    print("invalid number")

