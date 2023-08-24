import streamlit as st
import streamlit_analytics
import requests
from streamlit.components.v1 import html

def nav_page(page_name, timeout_secs=3):
    nav_script = """
        <script type="text/javascript">
            function attempt_nav_page(page_name, start_time, timeout_secs) {
                var links = window.parent.document.getElementsByTagName("a");
                for (var i = 0; i < links.length; i++) {
                    if (links[i].href.toLowerCase().endsWith("/" + page_name.toLowerCase())) {
                        links[i].click();
                        return;
                    }
                }
                var elasped = new Date() - start_time;
                if (elasped < timeout_secs * 1000) {
                    setTimeout(attempt_nav_page, 100, page_name, start_time, timeout_secs);
                } else {
                    alert("Unable to navigate to page '" + page_name + "' after " + timeout_secs + " second(s).");
                }
            }
            window.addEventListener("load", function() {
                attempt_nav_page("%s", new Date(), %d);
            });
        </script>
    """ % (page_name, timeout_secs)
    html(nav_script)


def _page_config():
    st.set_page_config(
        page_title='맛잘알AI',
        page_icon='👋',
        layout='wide',
        # initial_sidebar_state="collapsed"
    )
    hide_decoration_bar_style = '''
        <style>
            header {visibility: hidden;}
            footer {visibility: hidden;}
        </style>
    '''
    st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)
    reduce_header_height_style = """
        <style>
            div.block-container {padding-top:1rem;}
        </style>
    """
    st.markdown(reduce_header_height_style, unsafe_allow_html=True)
    

def _content():
    st.text("👋 안녕하세요~")
    st.header('레시피 기반 대화형 검색 서비스 입니다.')

    # Post request 로 텍스트를 전송하기 위한 form
    form = st.form(key='my_form')
    text = form.text_input(label='명령어를 입력해주세요.')
    submit_button = form.form_submit_button(label='전송')
    if submit_button:
        # with loading, requests post to localhost:8000/inference with text
        with st.spinner('고민중입니다...'):
            # post request
            response = requests.post(
                'http://localhost:8000/inference/',
                json={
                    "text": text,
                    "document_k": 10,
                    "document_search_type": "similarity",
                    "temperature": 0.9
                }
            )
        
            # response
            st.write(response.json())

    

def app():
    with streamlit_analytics.track():
        _page_config()
        _, content, _ = st.columns([2, 7, 2], gap='large')
        with content:
            _content()


if __name__ == '__main__':
    app()