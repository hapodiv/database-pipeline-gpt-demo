import pinecone
import openai
import os
from dotenv import load_dotenv
# Load environment variables
load_dotenv()
# Pinecone settings
index_name =  os.getenv("PINECONE_INDEX_NAME")
print(index_name)
# OpenAI settings
embed_model = "text-embedding-ada-002"

# Connect to Pinecone
api_key = os.getenv("PINECONE_API_KEY")
env = os.getenv("PINECONE_ENVIRONMENT")
pinecone.init(api_key=api_key, environment=env)

# Initialize OpenAI embedding engine
embedding = openai.Embedding.create(
    input=[
        """Plan title: 〜　シンプル STAY　〜　　早朝５時３０分〜モリッと無料朝食バイキング付き！【全室wifi完備】

Term: 【期間】2009年04月21日〜2023年12月31日

Plan description: 【お部屋】　　　広さ：１４㎡ ベット幅１４０ｃｍ（ダブルサイズ）快眠ベッド採用　　　WiFi/LANダブル接続可能!　ウォシュレット　リセッシュ　デスクスタンド『フレーバーコーヒー』※フロント設置(15時00分から23時30分まで）　3種類のコーヒーフレーバーをご用意。こちらは、12月までの企画です。　※フレーバーコーヒーとはコーヒーの新しい楽しみ方です。様々な香りづけをして少しリッチな気分で楽しめます。【駐車場】□無料駐車場70台！（普通車のみ。アネックスプリンセスホテルと共用です。）━▼主婦がつくるモリッと無料朝食バイキング時間帯▼━━━━━━━━━━━・平日の朝食　洋食5：30〜　和食6：30〜　朝食終了時間　⇒　９：００迄です。　・日曜日の朝食は和洋食６：３０〜　朝食終了時間　⇒　９：００迄です。　━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""",
        "5,728円/人, 5,728円/人, 5,728円/人, 5,728円/人, 5,728円/室"
    ], engine=embed_model
)

# Create Pinecone database
if index_name not in pinecone.list_indexes():
    print("Creating pinecone index: " + index_name)
    pinecone.create_index(
        index_name,
        dimension=len(embedding['data'][0]['embedding']),
        metric='cosine',
        metadata_config={'indexed': ['source', 'id']}
    )
