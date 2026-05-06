import NaverNewsCrawler as nnc
import streamlit as st

st.title("네이버 크롤링 결과")

keyword = st.text_input("검색할 키워드 : ")

if keyword:
    with st.spinner('뉴스 데이터를 가져오는 중...'):
        corpus = nnc.crawl_naver_news_all(keyword)
    
    if corpus:
        st.success(f"'{keyword}'에 대한 결과를 찾았습니다.")
        st.json(corpus[:3])
        df = nnc.crawl_csv(corpus)
        st.dataframe(df)
        
        # 1. 버튼을 여기에 배치하고 결과를 바로 변수에 저장합니다.
        save_btn = st.button("csv저장")
        
        # 2. 버튼 클릭에 대한 처리를 이 블록 안에서 수행합니다.
        if save_btn:
            df.to_csv("naver_news_results.csv", index=False, encoding='utf-8-sig')
            st.success("CSV 파일로 저장되었습니다!")
    else:
        st.warning("분석할 데이터가 없습니다.")
        
else:
    st.info("키워드를 입력해주세요.")