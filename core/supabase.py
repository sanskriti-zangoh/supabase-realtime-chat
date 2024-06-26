from supabase import create_client, Client
from core.settings import load_settings

def create_supabase_client() -> Client:
    """
    Create Supabase client.

    Returns:
        Client: Supabase client.
    """
    settings = load_settings('SupabaseSettings')
    return create_client(settings.url, settings.api)


supabase_client: Client = create_supabase_client()