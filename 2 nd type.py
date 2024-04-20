class BoatBargainingAI:
    def __init__(self):
        self.product_info = {
            'boat1': {'price': 50000, 'cost': 40000},
            'boat2': {'price': 60000, 'cost': 45000},
            'boat3': {'price': 70000, 'cost': 50000}
        }

    def negotiate(self, product_name, customer_price):
        if product_name not in self.product_info:
            return "Product not found"

        actual_price = self.product_info[product_name]['price']
        cost_price = self.product_info[product_name]['cost']

        if customer_price < cost_price:
            return "We can't sell below cost."
        elif customer_price == actual_price:
            return "The price is already as low as we can offer."
        elif customer_price > actual_price:
            return "Great! We accept your offer of ${}.".format(actual_price)
        else:
            discount = (actual_price - customer_price) / actual_price * 100
            return "We can offer a {}% discount, reducing the price to ${}.".format(int(discount), customer_price)


# Example usage
boat_ai = BoatBargainingAI()

product_name = 'boat2'
customer_price = 55000

response = boat_ai.negotiate(product_name, customer_price)
print(response)