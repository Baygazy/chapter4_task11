class User:
    def suda(func):
        def wrapper(*args, **kwargs):
            raise Exception(func(*args, **kwargs))
        return wrapper
    """ получить баланс счета """
    @suda
    def get_account_balance(self):
        return "No username defined!"
    """ изменить пароль """
    @suda
    def change_password(self):
        return "No password to change!"

u = User()
u.get_account_balance()
# u.change_password()
