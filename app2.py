import streamlit as st

def main() :
    # 큰글씨
    st.title('웹 대시보드')
    print('웹 대시보드')
    #작은글씨
    st.text('웹 대시보드 개발')
    # 중간글씨
    st.header('이 영역은 헤더 영역')
    st.subheader('이 영역은 서브 헤더 영역')
    #색으로 다음을 알림
    st.success('성공했을때 메시지를 보여줄때 사용')
    st.warning('경고 메시지를 보여주고 싶을때')
    st.info('정보성 메시지를 보여주고 싶을때')
    st.error('문제가 발생했음을 보여주고 싶을때')
    #파이선의 함수들의 설명을 보여주고 싶을때
    st.help(sum)
    st.help(len)

if __name__ == '__main__' :
    main()

