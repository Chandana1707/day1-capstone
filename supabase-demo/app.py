from supabase import create_client

SUPABASE_URL = "https://ohdnliutdfspyqmaktyv.supabase.co"
SUPABASE_KEY = "sb_publishable_q0oOUy3dIVk6Q7PS_gfw3g_5RncLS7b"

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)

users = [
    {"email": "user1@gmail.com"},
    {"email": "user2@gmail.com"},
    {"email": "user3@gmail.com"}
]

result = supabase.table("users").insert(users).execute()

print(result.data)