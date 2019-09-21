class Init:
    _fields = []
    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError(f"Expected {len(self._fields)} arguments")
        #setting the arguments in instance variable
        for field, value in zip(self._fields, args):
            setattr(self, field, value)

        for field in self._fields[len(args):]:
            setattr(self, field, kwargs.pop(field))
        
        if kwargs:
            raise TypeError("Invalid keyword argument(s): {}".format(''.join(kwargs)))

if __name__ == "__main__":

    class Order(Init):
        _fields = ["product_name", "quantity"]

    class Product(Init):
        _fields = ["product_name", "price", "no_in_stock"]

    order_item = Order("Laptop", 3)
    item = Product("Laptop", 3500, no_in_stock=10)

    print("Inspect Order Property: ", order_item.product_name)
    print("Inspect Product Property: ", f"Product Name: {item.product_name}\nStock count: {item.no_in_stock}")

