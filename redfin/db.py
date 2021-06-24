import psycopg2


class Postgres(object):
    def __init__(self, db_name, user, pswd) -> None:
        super().__init__()
        try:
            self.conn = psycopg2.connect(
                dbname=db_name, user=user, password=pswd, host="localhost"
            )

            self.cursor = self.conn.cursor()
        except psycopg2.OperationalError:
            print("Wrong Database credentials!")
            exit()

    def create_table(self):
        cmd = """CREATE TABLE redfin(
            id SERIAL PRIMARY KEY, 
            ListPrice VARCHAR(30) NOT NULL, 
            PriceSqFt VARCHAR(30) NOT NULL, 
            EstMoPayment VARCHAR(30) NOT NULL, 
            BuyersBrokerage VARCHAR(30) NOT NULL, 
            RedfinEstimate VARCHAR(30) NOT NULL,
            HOADues VARCHAR(30) NOT NULL,
            HomeFacts VARCHAR(30) NOT NULL,
            Status VARCHAR(30) NOT NULL,
            TimeOnRedfin VARCHAR(30) NOT NULL,
            PropertyType VARCHAR(30) NOT NULL,
            YearBuilt VARCHAR(30) NOT NULL,
            Style VARCHAR(30) NOT NULL,
            Community VARCHAR(30) NOT NULL,
            LotSize VARCHAR(30) NOT NULL,
            Style VARCHAR(30) NOT NULL,
            MLS VARCHAR(30) NOT NULL);"""

        self.cursor.execute(cmd)
        self.conn.commit()

    def insert_data(self, data):
        cmd = f"""INSERT INTO redfin(
            ListPrice
            PriceSqFt
            EstMoPayment
            BuyersBrokerage
            RedfinEstimate
            HOADues
            HomeFacts
            Status
            TimeOnRedfin
            PropertyType
            YearBuilt
            Style
            Community
            LotSize
            Style
            MLS VALUES {data};"""

        self.cursor.execute(cmd)
        self.conn.commit()

        cmd = """List Price
                Price Sq.Ft
                Est. Mo. Payment
                Buyer's Brokerage
                Redfin estimate
                HOA Dues
                Home Facts
                Status
                Time on Redfin
                Property Type
                Year Built
                Style
                Community
                Lot Size
                Style
                MLS#"""

    def end(self):
        self.conn.close()
