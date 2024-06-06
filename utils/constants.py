import os

SBIS_LINK = "https://sbis.ru/"
TENZOR_LINK = "https://tensor.ru/"
ABOUT_LINK = "https://tensor.ru/about"
USER_REGION = "Пермский край"
KAMCHATKA_REGION = "Камчатский край"
KAMCHATKA_PARTIAL_URL = "41-kamchatskij-kraj"

download_dir = os.path.join(os.getcwd(), "downloads")
os.makedirs(download_dir, exist_ok=True)
