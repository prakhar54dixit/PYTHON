import sqlite3

# Connect to the SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect('youtube_database.db')
cursor = conn.cursor()

# Create the table if it doesn't already exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')
conn.commit()

# ===========================
# CRUD Functions
# ===========================

def list_videos():
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()
    if not rows:
        print("\nNo videos found in the database.\n")
    else:
        print("\nList of Videos:")
        print("-" * 30)
        for row in rows:
            print(f"ID: {row[0]}, Title: {row[1]}, Duration: {row[2]}")
        print("-" * 30)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()
    print(f" Added video '{name}' successfully!")

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    if cursor.rowcount == 0:
        print(" No video found with that ID.")
    else:
        conn.commit()
        print(" Video updated successfully!")

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    if cursor.rowcount == 0:
        print(" No video found with that ID.")
    else:
        conn.commit()
        print(" Video deleted successfully!")

# ===========================
# Main Program Loop
# ===========================

def main():
    while True:
        print("\n======= YouTube Video Manager =======")
        print("1. List all videos")
        print("2. Add a video")
        print("3. Update video details")
        print("4. Delete a video")
        print("5. Exit")
        print("=====================================")

        try:
            choice = int(input("Enter your choice (1–5): "))
        except ValueError:
            print("⚠️ Please enter a valid number.")
            continue

        if choice == 1:
            list_videos()
        elif choice == 2:
            name = input("Enter video title: ")
            duration = input("Enter video duration: ")
            add_video(name, duration)
        elif choice == 3:
            try:
                video_id = int(input("Enter video ID to update: "))
                new_name = input("Enter new video title: ")
                new_duration = input("Enter new video duration: ")
                update_video(video_id, new_name, new_duration)
            except ValueError:
                print(" Invalid ID. Please enter a number.")
        elif choice == 4:
            try:
                video_id = int(input("Enter video ID to delete: "))
                delete_video(video_id)
            except ValueError:
                print(" Invalid ID. Please enter a number.")
        elif choice == 5:
            print(" Exiting program. Goodbye!")
            break
        else:
            print(" Please enter a number between 1 and 5.")

    conn.close()

if __name__ == '__main__':
    main()
