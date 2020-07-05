from django.db import models


class CommonModel(models.Model):
    """
    This is an abstract model and this model provides some basic fields,
    which are going to be in every models.
    """
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Bank(CommonModel):
    """
    This model will store names of all the banks.
    """
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        """Returns String representation of the model"""
        return self.name


class State(CommonModel):
    """
    This model will store all the names of the states.
    """
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        """Returns String representation of the model"""
        return self.name


class Location(CommonModel):
    """
    This model will store the city name, district name and foreign key to state model.
    """
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="location_state")

    def __str__(self):
        """Returns String representation of the model"""
        return str(self.city) + ", " + str(self.district) + ", " + str(self.state)


class Branch(CommonModel):
    """
    This model will store branch information such as
    name of the branch, bank name, IFSC code, location.
    """
    name = models.CharField(max_length=255)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name="branch_bank")
    address = models.TextField()
    ifsc_code = models.CharField(max_length=255, unique=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="branch_location")

    def __str__(self):
        """Returns String representation of the model"""
        return str(self.name) + ", " + str(self.bank)
