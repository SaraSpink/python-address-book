from contact import Contact


class Phonebook():
    def __init__(self):

        ollie = Contact('Ollie Diablo', '360-628-3383', '5270 SW Franklin', 'Poodle')
        argos = Contact('Argos Blackdog', '503-555-5555', '742 Evergreen Terrace', 'Mutt')
        lucky = Contact('Lucky Dog', '503-555-1234', '2828 Corbett Ave', 'Poodle')
        cody = Contact('Cody McFuzzy', '719-555-5500', '2828 Corbett Ave', 'Shiba Inu')

        self.new = [ollie, argos, lucky, cody]

    def add_contact(self):

        new_contact = Contact(
            name=input("Enter contact name:  "),
            number=input("Enter contact phone:  "),
            address=input("Enter contact address:  "),
            note=input("Enter notes about contact:  ")
        )

        self.new.append(new_contact)

    def find(self):
        search_name=input("Name to search:")
        found = False
        for contact in self.new:
            if contact.name == search_name:
                contact.all()
                found = True
        if found == False:
            print("Your query did not return a match! Too bad.")


if __name__ == '__main__':
    pb = Phonebook()
    pb.add_contact()
    pb.find()
    # for i in range(0, len(pb.new)):
    #     pb.new[i].all()

    print('Just ran phonebook')


# print(ollie.name)
#
# ollie.name = 'Ollie Spink'
# ollie.all()
