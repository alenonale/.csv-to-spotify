

🎵 Spotify Playlist Creator - Descrizione del Programma

Questo script in Python consente di creare automaticamente una playlist su Spotify a partire da un file `.csv` contenente una lista di brani (tipicamente esportati da app come Shazam).

⚙️ Requisiti

Prima di eseguire lo script, assicurati di avere:
1. Un account Spotify attivo
2. Un'app registrata su https://developer.spotify.com/dashboard/
3. Le credenziali dell'app: CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
4. Il file `.csv` con almeno due colonne: Title (titolo della canzone) e Artist (nome dell'artista)

Installa le librerie richieste:
pip install pandas spotipy

🗂 File di input

Il file `.csv` deve contenere almeno due colonne chiamate:
- Title: il nome del brano
- Artist: l’artista che lo ha eseguito

Esempio:
Title,Artist
Blinding Lights,The Weeknd
Bad Habits,Ed Sheeran

🚀 Come funziona lo script

1. Autenticazione
Utilizza l’autenticazione OAuth di Spotify per collegarsi al tuo account e ottenere il permesso di creare/modificare playlist.

2. Caricamento CSV
Legge il file CSV contenente la libreria di brani esportata (es. da Shazam).

3. Ricerca dei brani
Per ogni riga del CSV, lo script esegue una ricerca su Spotify combinando il titolo e l’artista per ottenere l’URI (codice identificativo) del brano.

4. Creazione della playlist
Crea una nuova playlist nel tuo account Spotify con il nome definito (PLAYLIST_NAME).

5. Aggiunta dei brani
Aggiunge tutti i brani trovati alla playlist, gestendo l’aggiunta in batch da 100 per evitare limiti dell’API.

📝 Output finale

Alla fine del processo, lo script stampa:
- Il numero totale di brani trovati su Spotify
- Il nome della playlist creata
- Eventuali brani non trovati

✅ Come usare lo script

1. Inserisci le tue credenziali CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
2. Sostituisci il nome del file CSV nella variabile CSV_PATH
3. Avvia lo script:
   python crea_playlist.py
4. Si aprirà una finestra del browser per autorizzare l'accesso a Spotify
5. Al termine troverai la playlist nel tuo account Spotify


