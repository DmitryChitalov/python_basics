class Date:

    def __init__(self, date_attrs):
        self.date_attrs = date_attrs

    @classmethod
    def extract_str(cls, date_attrs):
        date = date_attrs.split('-')
        num_date = []
        for el in date:
            num_date.append(int(el))
        return num_date

    @staticmethod
    def validation(date_attrs):
        date = date_attrs.split('-')
        if 1 <= int(date[0]) <= 31 and 1 <= int(date[1]) <= 12 and 1900 <= int(date[2]):
            return True
        else:
            print('Неверная дата')
            return False

print(Date.validation('01-01-2001'))
print(Date.extract_str('01-01-2001'))

