# 웹 대시보드에 이미지파일, 동영상파일 넣는 방법

import streamlit as st

# 이미지 처리를 위한 라이브러리
from PIL import Image

def main() :
    img = Image.open('streamlit_data/image_03.jpg')
    
    st.image(img)

    st.image(img,use_column_width=True)

    img_url = 'https://item.kakaocdn.net/do/7f700f99dae0af12bcfc3164113869f0f43ad912ad8dd55b04db6a64cddaf76d'
    st.image(img_url)

    # 동영상 하는 방법
    video_file = open('streamlit_data/secret_of_success.mp4','rb')
    st.video(video_file)

if __name__ == '__main__' :
    main()