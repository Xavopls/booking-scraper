class BookingDto:
    def __init__(self, name, location, average_price=None, description="", review_mark=0.0,
                 number_of_comments=0, photo_urls=None, amenities=None):
        self.name = name
        self.location = location
        self.average_price = average_price
        self.description = description
        self.review_mark = review_mark
        self.number_of_comments = number_of_comments
        self.photo_urls = photo_urls if photo_urls is not None else []
        self.amenities = amenities if amenities is not None else []

    def __str__(self):
        return self.name

    def add_amenity(self, amenity):
        """Manually add an amenity (since no DB is involved)."""
        self.amenities.append(amenity)

    def to_dict(self):
        """Convert the object to a dictionary for easy serialization (e.g., JSON)."""
        return {
            "name": self.name,
            "location": self.location,
            "average_price": self.average_price,
            "description": self.description,
            "review_mark": self.review_mark,
            "number_of_comments": self.number_of_comments,
            "photo_urls": self.photo_urls,
            "amenities": self.amenities
        }
