import streamlit as st
import random
from datetime import datetime

# アプリケーションタイトル
st.title("カテゴリー別占いアプリ")

# ユーザーの名前を入力
name = st.text_input("あなたの名前を入力してください:")

# ユーザーの生年月日を入力
birthdate = st.date_input("生年月日を選んでください:")

# カテゴリー選択のセクション
st.header("占いたいカテゴリーを選んでください")

categories = ["恋愛", "仕事", "健康"]
category = st.selectbox("カテゴリーを選んでください:", categories)

# 占いボタンが押されたとき
if st.button("占う"):
    if name and birthdate:
        # 生年月日から年齢を計算
        today = datetime.today()
        age = today.year - birthdate.year
        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age -= 1  # 誕生日が来ていない場合は1年引く

        # 各カテゴリーに対応した占い結果
        if category == "恋愛":
            fortunes = [
                f"{name}さん、今は恋愛運がとても良い時期です！積極的にアプローチしてみてください。",
                f"{name}さん、少し落ち着いて周りの状況を見てみましょう。焦らず進んでください。",
                f"{name}さん、運命の人が近くにいるかもしれません。少しの勇気で新しい扉が開くでしょう。",
            ]
        elif category == "仕事":
            fortunes = [
                f"{name}さん、今は仕事運が上昇しています！新しいチャンスが訪れるでしょう。",
        
