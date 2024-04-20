class BargainingAI:
    def __init__(self):
        # Product database (dummy data for demonstration)
        self.products = {
            'item1': {'price': 100, 'cost': 50},
            'item2': {'price': 200, 'cost': 100},
            'item3': {'price': 150, 'cost': 75}
        }

    def negotiate_price(self, product_name, customer_price):
        if product_name not in self.products:
            return "Product not found"
        
        actual_price = self.products[product_name]['price']
        cost_price = self.products[product_name]['cost']
        
        if customer_price < cost_price:
            return "Sorry, we can't sell below cost."
        elif customer_price == actual_price:
            return "The price is already as low as we can offer."
        elif customer_price > actual_price:
            return "Great! We accept your offer of ${}.".format(actual_price)
        else:
            discount = (actual_price - customer_price) / actual_price * 100
            return "We can offer a {}% discount, reducing the price to ${}.".format(int(discount), customer_price)


# Example usage
bargaining_ai = BargainingAI()

product_name = 'item2'  # The product the customer is interested in
customer_price = 180  # The price the customer is offering

response = bargaining_ai.negotiate_price(product_name, customer_price)
print(response)