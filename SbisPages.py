from BaseApp import BasePage
from selenium.webdriver.common.by import By
import urllib.request
import os
import time
# from selenium.webdriver.common.action_chains import ActionChains


class SbisSeacrhLocators:
    LOCATOR_SBIS_SEARCH_TEXT_CONTACTS = (By.PARTIAL_LINK_TEXT, 'Контакты')
    LOCATOR_SBIS_SEARCH_LOGO = (By.CLASS_NAME, 'sbisru-Contacts__logo-tensor')
    LOCATOR_SBIS_SEARCH_BLOCK_POWER = (By.CSS_SELECTOR, 'p.tensor_ru-Index__card-title.tensor_ru-pb-16')
    LOCATOR_SBIS_SEARCH_LINK_BLOCK_POWER = (By.PARTIAL_LINK_TEXT, 'Подробнее')
    LOCATOR_SBIS_SEARCH_BLOCK_NEWS = (By.CLASS_NAME, 'nl-LastCovers__header_title')
    LOCATOR_SBIS_SEARCH_IMAGES = (By.CSS_SELECTOR, "img.tensor_ru-About__block3-image")
    LOCATOR_SBIS_SEARCH_REGION = (By.CLASS_NAME, "sbis_ru-Region-Chooser__text")
    LOCATOR_SBIS_SEARCH_PARTNERS = (By.CSS_SELECTOR, "div.sbisru-Contacts-List__name.sbisru-Contacts-List--ellipsis"
                                                     ".sbisru-Contacts__text--md.pb-4.pb-xm-12.pr-xm-32")
    LOCATOR_SBIS_SEARCH_REGION_LIST = (By.CLASS_NAME, "sbis_ru-link")
    LOCATOR_SBIS_SEARCH_REGION_PANEL = (By.CLASS_NAME, "sbis_ru-Region-Panel")
    LOCATOR_SBIS_SEARCH_FOOTER = (By.CLASS_NAME, "sbisru-Footer__copyright-text")
    LOCATOR_SBIS_SEARCH_FOOTER_BLOCK = (By.CSS_SELECTOR, "div.sbisru-Footer.sbisru-Header__scheme--default")
    LOCATOR_SBIS_SEARCH_PLUGIN_BLOCK = (By.XPATH, "//div[@data-for='plugin']")
    LOCATOR_SBIS_SEARCH_DOWNLOAD_SBIS = (By.LINK_TEXT, "Скачать СБИС")
    LOCATOR_SBIS_SEARCH_SECTOR_PLUGIN = (By.XPATH, "//div[@data-id='plugin']")
    LOCATOR_SBIS_SEARCH_DOWNLOAD_PLUGIN = (By.PARTIAL_LINK_TEXT, "Скачать")
    LOCATOR_SBIS_SEARCH_HTML = (By.TAG_NAME, "html")


class FirstScript(BasePage):
    def search_block_powerpeople(self):
        self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_SEARCH_TEXT_CONTACTS).click()
        self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_SEARCH_LOGO).click()
        self.switch_window(1)
        block_strength = self.find_elements(SbisSeacrhLocators.LOCATOR_SBIS_SEARCH_BLOCK_POWER)
        return block_strength[1].text

    def goto_about_window(self):
        link_block_power = self.find_elements(SbisSeacrhLocators.LOCATOR_SBIS_SEARCH_LINK_BLOCK_POWER)
        block_news = self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_SEARCH_BLOCK_NEWS)
        self.move_to(block_news)
        link_block_power[2].click()
        return self.driver.current_url

    def photo_size(self):
        images = self.find_elements(SbisSeacrhLocators.LOCATOR_SBIS_SEARCH_IMAGES)
        list_size = []
        for i in images:
            list_size.append(i.get_attribute('width'))
            list_size.append(i.get_attribute('height'))
        return set(list_size)


class SecondScript(BasePage):
    def my_region(self):
        self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_SEARCH_TEXT_CONTACTS).click()
        self.region_name = self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_SEARCH_REGION)
        return self.region_name.text

    def partners(self):
        region_partners = self.find_elements(SbisSeacrhLocators.LOCATOR_SBIS_SEARCH_PARTNERS)
        all_partners = []
        for i in region_partners:
            if len(i.text) > 0:
                all_partners.append(i.text)
        return all_partners

    def change_region(self):
        region_name = self.region_name
        region_name.click()
        self.visibility_of_element(SbisSeacrhLocators.LOCATOR_SBIS_SEARCH_REGION_PANEL)
        country_list = self.find_elements(SbisSeacrhLocators.LOCATOR_SBIS_SEARCH_REGION_LIST)
        for ix in country_list:
            if ix.text == "41 Камчатский край":
                ix.click()
                break
        time.sleep(1)  # к сожалению не успел найти другого решения)

        # self.invisibility_of_element(SbisSeacrhLocators.LOCATOR_SBIS_SEARCH_REGION_PANEL)
        # region_name = self.element_to_be_clickable(SbisSeacrhLocators.LOCATOR_SBIS_SEARCH_REGION)
        return region_name.text

    def url_title_info(self):
        return self.information_fields()


class ThirdScript(BasePage): #здесь вообще мрак, работает только в не фоновом режиме и с time.sleep
    def download_sbis(self):
        footer = self.find_element(SbisSeacrhLocators.LOCATOR_SBIS_SEARCH_FOOTER)
        self.move_to(footer)
        time.sleep(1)
        link = self.element_to_be_clickable(SbisSeacrhLocators.LOCATOR_SBIS_SEARCH_DOWNLOAD_SBIS)
        link.click()
        time.sleep(1)
        element_plugin = self.element_to_be_clickable(SbisSeacrhLocators.LOCATOR_SBIS_SEARCH_SECTOR_PLUGIN)
        element_plugin.click()
        time.sleep(1)
        download_link = self.find_elements(SbisSeacrhLocators.LOCATOR_SBIS_SEARCH_DOWNLOAD_PLUGIN)
        url = download_link[0].get_attribute("href")
        destination = 'sbis_plugin.exe'
        urllib.request.urlretrieve(url, destination)
        file_size = os.path.getsize(f'C:\\Users\\Nail\\PycharmProjects\\TenzorTests\\{destination}')
        return round(file_size / 1048576, 2)
