from Common.app_library.base import Base


class Window(Base):
    def switch_to_window_title(self, title):
        """通过 title 包含关系跳转标签页"""
        self.logger.info(f"根据 title 跳转标签页：{title}")
        if title in self.driver.title:
            return
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if title in self.driver.current_url:
                return

    def switch_to_window_url(self, url):
        """通过 url 包含关系跳转标签页"""
        self.logger.info(f"根据 title 跳转标签页：{url}")
        if url in self.driver.current_url:
            return
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if url in self.driver.current_url:
                return
