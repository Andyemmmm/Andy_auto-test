from Page_Object.page_index import Page_Index


def 首页开始搜索商品(driver, goods):
    Page_Index(driver).send_搜索商品(goods)
    Page_Index(driver).click_搜索商品按钮()
