
class UtilsService:

    @staticmethod
    def format_url(url: str) -> str:
        if not url:
            raise ValueError("Name cannot be None or empty.")
        # Check if RFC 1738 encoded
        return url.replace("%20", "+").replace(" ", "+").lower()
