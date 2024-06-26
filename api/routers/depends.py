from core import supabase_client

def user_exists(key: str = "email", value: str = None):
    user = supabase_client.from_("users").select("*").eq(key, value).execute()
    return len(user.data) > 0