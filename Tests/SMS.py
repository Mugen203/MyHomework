from config import client
import CarWash

class SMS(Customer):
    def send_message(self):
        client_no = customer_info[4]
        for number in client_no:
            client.messages.create(
                body= "You will be notified as soon as your car is ready. Thank you for using our service!",
                from_="7753641017",
                to = "client_no"
        )

