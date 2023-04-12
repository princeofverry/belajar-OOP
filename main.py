from information import Information

email = input("masukkan email anda : ")
password = input("masukkan password anda: ")

info = Information(email, password)
info.login()