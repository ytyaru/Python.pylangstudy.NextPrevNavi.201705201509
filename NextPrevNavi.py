#!python3
#encoding: utf-8
import HtmlWrapper
class NextPrevNavi(object):
#    def __init__(self, directional_icon_type='FontAwesome'):
    def __init__(self, is_prev_left=True, directional_icon_type='FontAwesome'):
        self.__is_prev_left = is_prev_left
        self.__directional_icon_type = directional_icon_type
        self.__wrapper = HtmlWrapper.HtmlWrapper()
    
    """
    前後ナビのHTML文字列を生成する。
    @param {list} datas=[{'href': '', 'text': ''},{...},...]
    @param {bool} is_next_firstがTrueなら"次,前"の順に並ぶ。Falseなら"前,次"の順に並ぶ。
    """
    def CreateHtml(self, datas):
#    def CreateHtml(self, datas, is_next_first=False):
        if not datas:
            return None
#        return self.__wrapper.Wrap(self.__CreateInnerHtml(datas, is_next_first), 'ul', id_='NextPrevNavi')
        return self.__wrapper.Wrap(self.__CreateInnerHtml(datas), 'ul', id_='NextPrevNavi')
    
    """
    パンくずリストのHTML文字列を生成するためにdict引数を分解して内部メソッドに渡す。
    @param {list} datas=[{'href': '', 'text': ''},{...},...]
    @param {bool} is_next_firstがTrueなら"次,前"の順に並ぶ。Falseなら"前,次"の順に並ぶ。
    """
    def __CreateInnerHtml(self, datas):
#    def __CreateInnerHtml(self, datas, is_next_first=False):
#        is_left = not(is_next_first)
        is_left = self.__is_prev_left
        li_str = ''
        for data in datas:
            text_node_value = data['text']
            del data['text']
            li_str += self.__wrapper.Wrap(
                self.__AppendDirectionalIcon(
                    is_left, 
                    self.__wrapper.CreateElement('a', text_node_value=text_node_value, **data)
                ), 'li')
            is_left = not(is_left)
        return li_str
    
    def __AppendDirectionalIcon(self, is_left, a_str):
        if is_left:
            a_str = self.__CreateDirectionalIcon(is_left=is_left) + a_str
        else:
            a_str += self.__CreateDirectionalIcon(is_left=is_left)
        return a_str

    def __CreateDirectionalIcon(self, is_left=False):
        if self.__directional_icon_type == "FontAwesome":
            return self.__CreateDirectionalIcon_FontAwesome(is_left)
        else:
            return self.__CreateDirectionalIcon_Character(is_left)
    
    def __CreateDirectionalIcon_FontAwesome(self, is_left=False):
        if is_left:
            return '<i class="fa fa-angle-left" aria-hidden="true"></i>'
        else:
            return '<i class="fa fa-angle-right" aria-hidden="true"></i>'
    
    def __CreateDirectionalIcon_Character(self, is_left=False):
        text_node_value = ''
        if is_left:
            text_node_value = '&lt;'
        else:
            text_node_value = '&gt;'
        return self.__wrapper.CreateElement('span', text_node_value=text_node_value, class_='DirectionalIcon')


if __name__ == '__main__':
    """
    n = NextPrevNavi()
    html = n.CreateHtml([
        {'text': '前のページ', 'href': 'http://prev'},
        {'text': '次のページ', 'href': 'http://next'}], is_next_first=False)
    html = n.CreateHtml([
        {'text': '次のページ', 'href': 'http://next'},
        {'text': '前のページ', 'href': 'http://prev'}], is_next_first=True)
    html = n.CreateHtml([
        {'text': '前のページ', 'href': 'http://prev'},
        {'text': '次のページ', 'href': 'http://next'}], is_next_first=True)
    """
    """
    n = NextPrevNavi(is_prev_left=True)
    html = n.CreateHtml([
        {'text': '前のページ', 'href': 'http://prev'},
        {'text': '次のページ', 'href': 'http://next'}])
    """
    n = NextPrevNavi(is_prev_left=False)
    html = n.CreateHtml([
        {'text': '次のページ', 'href': 'http://next'},
        {'text': '前のページ', 'href': 'http://prev'}])
    print(html)

