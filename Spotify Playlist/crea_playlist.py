import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# === CONFIGURA QUI ===
CLIENT_ID = 'Inserisci CLIENT_ID'
CLIENT_SECRET = 'Inserisci CLIENT_SECRET'
REDIRECT_URI = 'Inserisci REDIRECT_URI'
CSV_PATH = 'Inserisci FILE.csv'
PLAYLIST_NAME = 'Inserisci PLAYLIST_NAME'

# === Autenticazione Spotify ===
scope = "playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=scope
))

# === Carica il file CSV ===
df = pd.read_csv(CSV_PATH, header=0)

# Pulizia nomi colonne
df.columns = df.columns.str.strip()

# === Ottieni ID utente e crea playlist ===
user_id = sp.me()['id']
playlist = sp.user_playlist_create(user=user_id, name=PLAYLIST_NAME)
playlist_id = playlist['id']

# === Cerca e aggiungi i brani ===
track_uris = []

for index, row in df.iterrows():
    # Tenta diverse query per migliorare il matching
    queries = [
        f"{row['Title']} {row['Artist']}",
        f"{row['Title']} artist:{row['Artist']}",
        f"track:{row['Title']} artist:{row['Artist']}"
    ]
    found = False
    for q in queries:
        try:
            result = sp.search(q=q, type='track', limit=1)
            tracks = result['tracks']['items']
            if tracks:
                track_uris.append(tracks[0]['uri'])
                found = True
                break
        except Exception as e:
            print(f"Errore durante la ricerca: {e}")
    
    if not found:
        print(f"⚠️ Brano non trovato: {row['Title']} - {row['Artist']}")

# === Aggiungi in batch ===
batch_size = 100
for i in range(0, len(track_uris), batch_size):
    batch = track_uris[i:i+batch_size]
    try:
        sp.playlist_add_items(playlist_id, batch)
        print(f"Aggiunto batch {i // batch_size + 1} con {len(batch)} tracce.")
    except spotipy.exceptions.SpotifyException as e:
        print(f"Errore durante l'aggiunta del batch {i // batch_size + 1}: {e}")

# === Risultato finale ===
print(f"\n✅ Playlist '{PLAYLIST_NAME}' creata con {len(track_uris)} brani trovati su {len(df)} totali.")
