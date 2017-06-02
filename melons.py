"""Classes for melon orders."""

class AbstractMelonOrder(object):
    """An abstract base class that other Melon Orders inherit from."""
    
    def __init__(self, species, qty):
        """Initialize AbstractMelonOrder attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False



    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species.lower() == "christmas melon":
            base_price = base_price * 1.5
       
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True






class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super(DomesticMelonOrder, self).__init__(species, qty)

        # self.species = species
        # self.qty = qty
        # self.shipped = False
        self.order_type = "domestic"
        self.tax = 0.08

    # def get_total(self):
    #     """Calculate price, including tax."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price

    #     return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    #     self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):

        super(InternationalMelonOrder, self).__init__(species, qty)
        # self.species = species
        # self.qty = qty
        self.country_code = country_code
        # self.shipped = False
        self.order_type = "international"
        self.tax = 0.17

       
    def get_total(self):
        """Calculate price, including tax."""


        total = super(InternationalMelonOrder, self).get_total()

        if self.qty < 10:
            total = total + 3

        return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    #     self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order from the government."""

    def __init__(self, species, qty):

        super(GovernmentMelonOrder, self).__init__(species, qty)
        self.tax = 0.0
        self.passed_inspection = False
        self.order_type = "government"

    def mark_inspection(self, passed):
        if passed == 'True':
            self.passed_inspection = True

