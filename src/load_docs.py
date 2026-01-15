from db_connect import get_connection
#we need to convert each row of the db into a document and load that doc.
def load_documents():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
       SELECT
            track.name,
            artist.name AS artist,
            album.title AS album,
            genre.name AS genre 
        FROM track
        JOIN album ON track.album_id = album.album_id
        JOIN artist ON album.artist_id = artist.artist_id
        JOIN genre ON track.genre_id = genre.genre_id 
        LIMIT 100;           
     """
    )

    rows = cur.fetchall()

    documents = []
    for name, artist, album, genre in rows:
        text = f"Track: {name}, Artist: {artist}, Album: {album}, Genre: {genre}"
        documents.append(text)
    cur.close()
    conn.close()
    return documents