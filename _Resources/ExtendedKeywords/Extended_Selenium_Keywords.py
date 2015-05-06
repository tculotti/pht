from robot.libraries.BuiltIn import BuiltIn
from datetime import datetime as time
# Get the current running instance of Selenium
def _get_s2l():
    return BuiltIn().get_library_instance('Selenium2Library')


# Extends KeywordGroup like other built-in keyword classes do
class Extended_Selenium_Keywords():
    # Run the default _run_on_failure when any of the keywords defined in this class failed.
    def _run_on_failure(self):
        _get_s2l()._run_on_failure()

    def open_new_window(self, url):
        """Sets focus to element identified by `locator`."""
        browser = _get_s2l()._current_browser()
        a = browser.execute_script(
            "var d=document,a=d.createElement('a');a.target='_blank';a.href=arguments[0];a.innerHTML='.';d.body.appendChild(a);return a",
            url)
        a.click()

    def select_window_with_handle(self, handle_id):
        browser = _get_s2l()._current_browser()
        handles = browser.get_window_handles()
        browser.switch_to_window(handles[int(handle_id)])

    def get_elements_by_xpath(self, xpath):
        s2l = _get_s2l()
        browser = s2l._current_browser()
        elements = browser.find_elements_by_xpath(xpath)
        return [x.text for x in elements]

    def list_should_be_sorted_asc(self, list_to_validate):
        is_sorted = self.verify_list_is_sorted(list_to_validate)

        if not is_sorted:
            error_str = self.error_for_sorting(list_to_validate)
            raise Exception(error_str)

    def list_should_be_sorted_desc(self, list_to_validate):
        is_sorted = self.verify_list_is_sorted(list_to_validate, 'desc')

        if not is_sorted:
            error_str = self.error_for_sorting(list_to_validate)
            raise Exception(error_str)

    def error_for_sorting(self, list):
        return 'List is not sorted. The list is [%s]' % ', '.join(map(str, list))

    def verify_list_is_sorted(self, list_to_sort, direction='asc'):
        is_sorted = False
        if direction == 'asc':
            is_sorted = all(list_to_sort[i] <= list_to_sort[i + 1] for i in xrange(len(list_to_sort) - 1))
        else:
            is_sorted = all(list_to_sort[i] >= list_to_sort[i + 1] for i in xrange(len(list_to_sort) - 1))
        return is_sorted







