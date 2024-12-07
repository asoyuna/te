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
                f"{name}さん、今は安定を求める時期かもしれません。焦らず計画的に進めていきましょう。",
                f"{name}さん、同僚との関係を大切にすることで、仕事の成果が上がります。",
            ]
        elif category == "健康":
            fortunes = [
                f"{name}さん、健康運は良好です！運動や食事に気を使ってさらに調子を上げましょう。",
                f"{name}さん、少し休養が必要かもしれません。ストレスを解消して心身をリフレッシュしてください。",
                f"{name}さん、最近の生活習慣を見直してみると、健康に良い影響を与えるかもしれません。",
            ]

        # ランダムに占い結果を表示
        fortune_result = random.choice(fortunes)
        st.write(f"あなたの{category}占い結果: {fortune_result}")
        
        # 年齢に基づくアドバイス
        if age < 18:
            st.write(f"{name}さん、あなたは若いエネルギーに満ち溢れています。")
        elif 18 <= age < 30:
            st.write(f"{name}さん、あなたは今、成長の時期にいます。")
        else:
            st.write(f"{name}さん、あなたの経験が大きな力になります。")
    else:
        st.warning("名前と生年月日を入力してください。")

# アプリケーションの説明
st.write("""
このアプリは、名前と生年月日を入力して、カテゴリー別の占い結果を楽しむことができます。
占いたいカテゴリーを選んで、あなたの運命を知りましょう！
""")
