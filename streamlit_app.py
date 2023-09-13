import streamlit as st

# ページ設定（タブに表示されるタイトル、表示幅）
st.set_page_config(page_title="ゆずき", layout="wide")


# ユーザーからの入力を受け取るUIを作成
st.title("麻雀点数計算アプリ")

# 役の選択
st.header("役の選択")
yaku_options = {
    "リーチ": 1,
    "ツモ": 1,
    "一発": 1,
    "門前清自摸和": 1,
    "断么九": 1,
    "平和": 1,
    "役牌（自風、場風、白、發、中）": 1,
    "一盃口": 1,
    "三色同順": 2,
    "一気通貫": 2,
    "混全帯幺九": 2,
    "二盃口": 3,
    "純全帯幺九": 3,
    "混一色": 3,
    "清一色": 6,
    "大三元": 13,
    "四暗刻": 13,
    "小四喜": 13,
    "字一色": 13,
    "緑一色": 13,
    "清老頭": 13,
    "九蓮宝燈": 13,
    "国士無双": 26,
    "大四喜": 26,
    "四槓子": 26,
    "天和": 26,
    "地和": 26,
}

selected_yaku = st.multiselect("役を選択してください（複数選択可）", list(yaku_options.keys()))

# 点数計算
st.header("点数計算")
total_score = sum([yaku_options[yaku] for yaku in selected_yaku])

# 点数を表示
st.write(f"合計点数: {total_score} 点")
