import user_info

class seats:
    global matrix,total_seats_booked
    matrix = []


    def __init__(self):
        self.no_of_rows = 20
        self.no_of_seats = 20
        

    def capacity(self):
        for i in range(self.no_of_rows + 1):
            a = []
            for j in range(self.no_of_seats + 1):
                a.append("S")
            matrix.append(a)

        total_seats = self.no_of_seats * self.no_of_rows
        return total_seats, self.no_of_rows,self.no_of_seats

    def show_the_seats(self):

        for i in range(0, self.no_of_rows + 1):
            if i == 0:
                for j in range(0, self.no_of_seats + 1):
                    print(j, end=" ")
            else:
                print(i, end=" ")
                for k in range(self.no_of_seats):
                    print(matrix[i - 1][k], end=" ")
            print()



class tickets:
    global price_each_ticket,p

    def __init__(self):
        self.book_row = int(input("Please enter the row no. you want to book: "))
        self.book_column = int(input("Please enter the column no. you want to book: "))


    def buy_ticket(self, total_seats, no_of_rows,total_income,total_seats_booked ):

        p = tickets.price_per_ticket(self,total_seats, no_of_rows,total_income)
        print(p)

        print("The Price of your ticket will be: Inr.", p)
        confirmation = input("Please Confirm to book your ticket (1/0)")

        if confirmation == '1':

            matrix[self.book_row - 1][self.book_column - 1] = "B"
            u=user_info.user_info()
            u.user(self.book_row,self.book_column)
            return True,p

        else:
            print("No ticket booked")
            return None,None

    def price_per_ticket(self, total_seats, no_of_rows,total_income):
        current_income=0
        if self.book_row <= 15:
            current_income=120
            total_income=total_income + current_income
            return  120

        else:
            if self.book_row >= 16:
                current_income = 100
            return 100

class statistics:
    def stats(self,total_seats_booked,total_seats,c,total_income):


        print("Number of Purchased Tickets: ",total_seats_booked)
        print("Percentage of Tickets Booked: ",(total_seats_booked/total_seats)*100)
        print("Inr.","Current Income: ",c)
        print("Total_income: ","Inr.",total_income)
