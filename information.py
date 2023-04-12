from datetime import datetime

class Information:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.buku = {
            "1" : {
                "Fisika Dasar I",
                "Fisika Dasar II"
            },
            "2" : {
                "Matematika Teknik",
                "Aljabar Linear"
            }
        }
        self.data = {
            "1": {
                "email" : "verrykurniawan@gmail.com",
                "password" : "1",
                "role" : "superadmin",
                "date" : "032623", #MMDDYY
                "buku" : self.buku["1"]
                },
            "kelompok21@gmail.com": {
                "email" : "kelompok21@gmail.com",
                "password" : "1234",
                "role" : 'manusia biasa',
                "date" : "041223", #MMDDYY
                "buku" : self.buku["2"]
            }    
        }





    def checkCredentials(self):
        for value in self.data:
            if value == self.email:
                get_data_user = self.data[value]
                if self.password == get_data_user["password"]:
                    return get_data_user
                else:
                    return False


    def login(self):
        get_data = self.checkCredentials()
        if get_data:
            print("\nWelcome", get_data["role"])
            print("Logged it as user email", get_data['email'], "\n")
            dataBuku = get_data["buku"]
            dataBuku = ', '.join(list(get_data["buku"])) #agar separator cuma comma
            print(get_data["email"], "telah meminjam buku :", dataBuku)
            date_str = get_data["date"]
            date_obj = datetime.strptime(date_str, "%m%d%y")
            formatted_date = datetime.strftime(date_obj, "%d-%m-%Y")
            print("Peminjaman buku pada tanggal", formatted_date)
        else:
            print("\nGagal Login\n") 