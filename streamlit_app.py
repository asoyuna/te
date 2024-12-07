import streamlit as st
import random

# アプリケーションのタイトル
st.title("今日の運勢占い")

# ユーザーの名前を入力
name = st.text_input("あなたの名前を入力してください:")

# カテゴリーの選択
st.header("占いたいカテゴリーを選んでください")

categories = ["恋愛", "仕事", "健康", "金運", "人間関係", "旅行", "星座"]
category = st.selectbox("カテゴリーを選んでください:", categories)

# 各カテゴリーごとの運勢データ（運勢メッセージ、詳細アドバイス、ラッキーアイテム、ラッキーカラー）
fortune_data = {
    "恋愛": [
        {
            "fortune": "今日は恋愛運が好調！新しい出会いがあるかもしれません。",
            "detail": "新しい場所に出かけることで、素敵な出会いが期待できるかもしれません。積極的に人と話してみましょう！",
            "lucky_item": "ピンクのアクセサリー",
            "lucky_color": "ピンク"
        },
        {
            "fortune": "少し焦りがちですが、落ち着いて自分の気持ちを大切にしましょう。",
            "detail": "焦って行動すると、失敗の元です。深呼吸をして、自分の気持ちに正直になることが大切です。",
            "lucky_item": "香水",
            "lucky_color": "ホワイト"
        },
        {
            "fortune": "パートナーとの絆が深まる日。素直な気持ちを伝えてみて。",
            "detail": "パートナーと心を通わせることができる日です。感謝の気持ちを素直に伝えると、関係がより深まります。",
            "lucky_item": "ハート型の小物",
            "lucky_color": "レッド"
        },
    ],
    "仕事": [
        {
            "fortune": "今日は仕事で新しいチャンスが訪れる日。積極的に挑戦してみましょう。",
            "detail": "新しいプロジェクトや任務に取り組むことで、キャリアに大きな進展があるかもしれません。恐れずに挑戦を！",
            "lucky_item": "ノートパソコン",
            "lucky_color": "ブラック"
        },
        {
            "fortune": "少し注意が必要な日。焦らず一つ一つ確実に進めることが大切。",
            "detail": "急いで決断を下すと後悔するかもしれません。慎重に計画を立て、冷静に行動しましょう。",
            "lucky_item": "時計",
            "lucky_color": "グレー"
        },
        {
            "fortune": "同僚との協力がカギ。みんなで力を合わせることで結果が出る日です。",
            "detail": "チームで協力することで、より良い結果が出せる日です。お互いの強みを活かして、協力し合いましょう。",
            "lucky_item": "ビジネスバッグ",
            "lucky_color": "ネイビー"
        },
    ],
    "健康": [
        {
            "fortune": "今日は体調が良い日。軽い運動をしてエネルギーを維持しましょう。",
            "detail": "体調が良いので、軽いジョギングやウォーキングをして、エネルギーを維持しましょう。体を動かすことで気分もリフレッシュ。",
            "lucky_item": "ヨガマット",
            "lucky_color": "グリーン"
        },
        {
            "fortune": "少し疲れが溜まっているかもしれません。休息を取ることを忘れずに。",
            "detail": "疲れが溜まっていると感じたら、無理をせずしっかりと休むことが大切です。リラックスして心身の回復を促しましょう。",
            "lucky_item": "アロマキャンドル",
            "lucky_color": "ラベンダー"
        },
        {
            "fortune": "食生活に気をつけることで、心身のバランスが整います。",
            "detail": "健康な食事を心がけることが、体調改善のカギです。バランスの取れた食事を摂ることを意識しましょう。",
            "lucky_item": "フルーツ",
            "lucky_color": "オレンジ"
        },
    ],
    "金運": [
        {
            "fortune": "今日は金運が上昇しています。小さな投資や買い物が良い結果を生むかも。",
            "detail": "手堅い投資や無駄な買い物を避けることで、金運が良くなる日です。注意深くお金を管理しましょう。",
            "lucky_item": "財布",
            "lucky_color": "ゴールド"
        },
        {
            "fortune": "予期しない収入があるかもしれません。臨時収入が期待できそうです。",
            "detail": "普段の努力が報われる形で、臨時収入があるかもしれません。贅沢せず、堅実に使うと良い結果に繋がります。",
            "lucky_item": "コイン",
            "lucky_color": "シルバー"
        },
        {
            "fortune": "今日は節約がカギ。無駄な出費を抑え、将来のために貯金をしましょう。",
            "detail": "出費を控えめにし、貯金に回すことが大切です。金運を安定させるために、計画的に使いましょう。",
            "lucky_item": "貯金箱",
            "lucky_color": "グリーン"
        },
    ],
    "人間関係": [
        {
            "fortune": "今日は友人や同僚との関係が良好です。ポジティブな交流ができそう。",
            "detail": "コミュニケーションが円滑に進む日です。人間関係を大切にし、感謝の気持ちを伝えましょう。",
            "lucky_item": "手紙",
            "lucky_color": "ピンク"
        },
        {
            "fortune": "少し誤解が生じるかもしれません。慎重に言葉を選んでください。",
            "detail": "言葉が誤解を招くことがあります。感情を押さえ、冷静に対応することがカギです。",
            "lucky_item": "ノート",
            "lucky_color": "ブルー"
        },
        {
            "fortune": "家族との絆が深まる日。大切な人との時間を大切にしましょう。",
            "detail": "家族や親しい人との関係が深まる日です。心を通わせて、リラックスした時間を過ごしましょう。",
            "lucky_item": "アルバム",
            "lucky_color": "ホワイト"
        },
    ],
    "旅行": [
        {
            "fortune": "旅行運が好調です！新しい場所への旅行を計画してみましょう。",
            "detail": "今は新しい場所を訪れるのに最適なタイミングです。リフレッシュするための旅行を計画してみて。",
            "lucky_item": "パスポート",
            "lucky_color": "ターコイズ"
        },
        {
            "fortune": "遠出は避けた方が良いかもしれません。近場でリラックスしましょう。",
            "detail": "遠くへ行くことは避け、近くでリラックスするのがベストです。旅行は近場で楽しみましょう。",
            "lucky_item": "カメラ",
            "lucky_color": "グリーン"
        },
        {
            "fortune": "旅行の計画は慎重に。詳細を確認して、スムーズな旅にしましょう。",
            "detail": "旅行の計画は綿密に行うことで、トラブルなく楽しめます。詳細を確認して、万全の準備をしましょう。",
            "lucky_item": "地図",
            "lucky_color": "ブルー"
        },
    ],
    "星座": [
        {
            "fortune": "今日はあなたの星座が輝いています。新たなチャンスが訪れる予感。",
            "detail": "自分の直感を信じて行動すると、新たなチャンスが見つかる日です。焦らず、着実に進んでいきましょう。",
            "lucky_item": "星形のアクセサリー",
            "lucky_color": "紫"
        },
        {
            "fortune": "冷静さを保ち、感情をコントロールすることが大切な日。",
            "detail": "感情に流されず、冷静な判断をすることが成功のカギです。落ち着いて行動しましょう。",
            "lucky_item": "水晶",
            "lucky_color": "青"
        },
        {
            "fortune": "他人との協力がカギ。助け合いの精神を大切に。",
            "detail": "協力して作業を進めることで、大きな成果を得られる日です。周囲のサポートを活用しましょう。",
            "lucky_item": "ペンダント",
            "lucky_color": "シルバー"
        },
    ]
}

# 占い結果を選択して表示
if category:
    fortune = random.choice(fortune_data[category])
    st.write(f"**運勢:** {fortune['fortune']}")
    st.write(f"**詳細アドバイス:** {fortune['detail']}")
    st.write(f"**ラッキーアイテム:** {fortune['lucky_item']}")
    st.write(f"**ラッキーカラー:** {fortune['lucky_color']}")
