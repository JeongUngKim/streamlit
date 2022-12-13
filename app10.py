import streamlit as st
import numpy as np
#plotly 라이브러리
import plotly.express as px
import pandas as pd
# altair 라이브러리
import altair as alt


def main() :
    df = pd.read_csv('streamlit_data/lang_data.csv')
    st.dataframe(df.head())
    column_menu = df.columns[1:]
    choice_list = st.multiselect('프로그래밍언어를 선택하세요',column_menu)

    # 유저가 선택한 언어를 차트로 나타내기
    if len(choice_list) != 0 :
        df_selected = df[choice_list]

        ## 스트림릿에서 제공하는 라인차트
        st.line_chart(df_selected)

        ## 스트림릿에서 제공하는 영역차트
        st.area_chart(df_selected)
        
        ## 스트림릿에서 제공하는 바차트
        st.bar_chart(df_selected)

    df2 = pd.read_csv('streamlit_data/iris.csv')
    ### altair 라이브러리의 mark_circle 함수 사용법
    chart = alt.Chart(df2).mark_circle().encode(x='petal_length',y='petal_width',
            color = 'species')
    st.altair_chart(chart)

    ### 위치 정보를 지도에 표시하는 방법
    ### 스트림릿의 map 차트
    df3 = pd.read_csv('streamlit_data/location.csv',index_col=0)
    st.dataframe(df3.head(3))

    st.map(df3,zoom=5)

    df4 = pd.read_csv('streamlit_data/prog_languages_data.csv',index_col=0)
    st.dataframe(df4.head())
    ### plotly의 pie 차트 그리는 방법
    fig7=px.pie(df4,'lang','Sum',title='각 언어별 파이차트')
    st.plotly_chart(fig7)

    ### plotly의 bar 차트 그리는 방법
    df_sorted = df4.sort_values('Sum',ascending=False)
    fig8 = px.bar(df_sorted,'lang','Sum',title='각 언어별 파이차트')
    st.plotly_chart(fig8)

    
if __name__ == '__main__' :
    main()