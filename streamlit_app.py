import streamlit as st
import random
from datetime import datetime

# アプリケーションタイトル
st.title("占いアプリ")

# ユーザーの名前を入力
name = st.text_input("あなたの名前を入力してください:")

# ユーザーの生年月日を入力
birthdate = st.date_input("生年月日を選んでください:")

# 占いの質問
st.header("今日の占い結果")

# 占いボタンが押されたとき
if st.button("占う"):
    if name and birthdate:
        # 生年月日から年齢を計算
        today = datetime.today()
        age = today.year - birthdate.year
        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age -= 1  # 誕生日が来ていない場合は1年引く

        # 簡単な占いの結果を生成
        fortunes = [
            "今日は良い日になるでしょう！前向きに行動してください。",
            "少し注意が必要な日です。慎重に行動しましょう。",
            "思いがけないチャンスが訪れるかもしれません。チャンスを逃さないように！",
            "今日はリラックスして過ごすと良い日です。無理をせずに、休養しましょう。",
            "周りの人との関係に気をつけて。コミュニケーションを大切に。",
        ]

        # 年齢に基づく占いの傾向
        if age < 18:
            st.write(f"{name}さん、あなたは若いエネルギーに満ち溢れています。")
        elif 18 <= age < 30:
            st.write(f"{name}さん、あなたは今、成長の時期にいます。")
        else:
            st.write(f"{name}さん、あなたの経験が大きな力になります。")
        
        # ランダムに占いの結果を表示
        fortune_result = random.choice(fortunes)
        st.write(f"あなたの占い結果: {fortune_result}")
    else:
        st.warning("名前と生年月日を入力してください。")

# アプリケーションの説明
st.write("""
このアプリは、名前と生年月日を入力して占いを行います。簡単な占い結果を楽しんでください。
""")
