from SbisPages import FirstScript, SecondScript, ThirdScript
from confest import browser


def test_sbis_firstscript(browser):
    sbis_first = FirstScript(browser)
    sbis_first.go_to_site()
    block_element = sbis_first.search_block_powerpeople()
    assert "Сила в людях" in block_element

    about_window = sbis_first.goto_about_window()
    assert "https://tensor.ru/about" in about_window

    photo = sbis_first.photo_size()
    assert len(photo) == 2


def test_sbis_secondscript(browser):
    sbis_second = SecondScript(browser)
    sbis_second.go_to_site()
    region_element = sbis_second.my_region()
    assert "Республика Башкортостан" in region_element

    partners_region = sbis_second.partners()
    assert len(partners_region) > 0

    change_country = sbis_second.change_region()
    assert "Камчатский край" in change_country

    partners_changed_region = sbis_second.partners()
    assert len(partners_changed_region) > 0 and partners_changed_region[0] != partners_region[0]

    information_fields = sbis_second.url_title_info()
    assert information_fields == ['СБИС Контакты — Камчатский край',
                                  'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients']

# def test_sbis_thirdscript(browser):
#     sbis_third = ThirdScript(browser)
#     sbis_third.go_to_site()
#     file = sbis_third.download_sbis()
#     assert file == 3.66

