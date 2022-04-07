class Phone:
    def __init__(self, phone):
        self._current_phone = phone
        #self.current_phone = phone

    @property
    def value(self):
        try:
            ggg = int(self._current_phone[1:])

            if len(self._current_phone) < 13 and len(self._current_phone)>10 and isinstance(ggg, int):
                return self._current_phone   
            else: print("Please give correct phone10")

        except ValueError:
                print("Please give correct phone11")
                self._current_phone = ""
        

    @value.setter
    def value(self, phone_setter):
        if phone_setter != "":

            try:
                ff = int(phone_setter[1:])
                if len(phone_setter) < 13 and len(phone_setter)>10 and isinstance(ff, int):
                    self._current_phone = phone_setter
            
                ff = int(self._current_phone[1:])
                if len(self._current_phone) < 13 and len(self._current_phone)>10 and isinstance(ff, int):
                    self.current_phone = self._current_phone

            except ValueError:
                print("Please give correct phone12")
                self._current_phone = ""
        # print(self.value)


p1 = Phone("134")
print(p1.value) #134