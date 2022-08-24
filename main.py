from string import digits, ascii_letters, punctuation
import datetime


class Password:
    def __init__(self, new_password='e9%876_54)3291Ktururrixnxn:>674rjd') -> None:
        self.new_password = new_password


    def write_password(self):
        with open('password.txt', 'w', encoding='UTF-8') as file:
            date_now = str(datetime.datetime.now())
            print(f'The password will be written: {self.new_password} at {date_now[:-7]}')
            file.write(f'{self.new_password}\n{date_now[: -7]}')


    def get_password(self):
        with open('password.txt', 'r') as read_file:
            reading_strings = read_file.readlines()
            reading_password = reading_strings[0].strip()
            reading_date = reading_strings[1].strip()
            print(f'Reading password from written file is: {reading_password}, the date is: {reading_date}.')

        return reading_password


    def guess_password(self):
        found_password= ''
        possible_symbols = punctuation + digits + ascii_letters 

        read_psw_object = Password()
        original_password = read_psw_object.get_password()

        for symbol in original_password:  
            for sign in possible_symbols:
                if symbol == sign:
                    found_password += symbol
                    print(f"!!!!! Sign '{symbol}' founded in password! :) Current password is: '{found_password}' :) !!!!!!!")
                else:
                    print(f"---- Sign '{symbol}' not founded in password :( -----")

        print(f"We found password '{found_password}'!")

        with open('found_password.txt', 'w', encoding='UTF-8') as found_psw_file:
            found_psw_file.write(found_password)


        return found_password



if __name__ == '__main__':
    password_object = Password()
    password_object.write_password()
    guess_psw_object = Password()
    guess_psw_object.guess_password()
