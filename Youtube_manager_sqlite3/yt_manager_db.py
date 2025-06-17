import sqlite3

conn=sqlite3.connect('youtube_database.db')#used to set_up connection with sqlite database if present ,if not then it will create it.


cursor=conn.cursor()# this will be used to work on database,with the help of writing queries.

cursor.execute('''
    CREATE TABLES IF NOT EXIST videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )
''')
def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name,time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_video(video_id,new_name,new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos where id = ?", (video_id,))
    conn.commit()


def main():
    while True:
        print(".......Youtube video manager.......")
        print("Choose what you want to do : ")
        print(" 1:List all the videos.\n 2.Add a video.\n 3.Update particular video details.\n 4.Delete a video from repo.\n 5.Exit  the program.")
        choice=int(input("Enter your choice: "))

        if(choice<1 or choice>5):
            print("Enter a valid input.")
        else:
            if choice==1:
                list_videos()
            elif choice==2:
                name=input("Enter video tittle : ")
                duration=input("Enter video duration : ")
                add_video(name,duration)
            elif choice==3:
                video_id=int(input("Enter video id you want to update : "))
                name=input("Enter video tittle : ")
                duration=input("Enter video duration : ")
                update_video(video_id,name,duration)
            elif choice==4:
                video_id=int(input("Enter video id you want to delete : "))
                delete_video(video_id)
            else:
                break

    conn.close()      

if __name__=='__main__':
    main()