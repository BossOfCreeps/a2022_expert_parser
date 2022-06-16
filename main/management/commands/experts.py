from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from selenium import webdriver

from main.models import Expert

URL_FORMAT = "https://experts.nti.work/e-registry?page={}"


class Command(BaseCommand):
    def handle(self, *args, **options):
        Expert.objects.all().delete()
        driver = webdriver.Chrome("chromedriver.exe")
        page = 1
        while True:
            driver.get(URL_FORMAT.format(page))
            if page == 1:
                input()
            page += 1

            experts = BeautifulSoup(driver.page_source).find_all("div", class_="expert-profile-card plate")

            if not experts:
                break

            for expert in experts:
                data = expert.find_all("div", class_="expert-profile-card__block")
                link = expert.find("a", class_="button button--primary global-profile__sidebar-btn-w-100")["href"]
                Expert.objects.get_or_create(
                    id=link.split("/")[4],
                    name=data[0].text,
                    text=data[1].text[6:],
                    help=data[2].text[24:],
                    expertise=data[3].text[10:],
                    competencies=data[4].text[11:],
                    link=link
                )
