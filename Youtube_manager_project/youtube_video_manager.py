import json

def load_data():
    try:
        with open("youtube.txt","r") as file:
            return json.load(file) # this will go and take data from txt file and convert it into json form   [{},{}]-->json form.
    except FileNotFoundError:
        return []


def save_data(videos):
    with open("youtube.txt","w") as file:
        json.dump(videos,file)


def list_allvideos(videos):
    if not videos:
        print("No videos found.")
    else:
        for index, video in enumerate(videos, start=1):
            print(f"{index}. Name: {video['name']} | Duration: {video['time']}")


def add_video(videos):
    name=input("Enter video name : ")
    time=input("Enter video duration : ")
    videos.append({"name":name ,"time":time})
    save_data(videos)
    print("Video added successfully.")


def update_video(videos):
    list_allvideos(videos)
    index = int(input("Enter the index of the video to update: "))
    index-=1
    if 0 <= index < len(videos):
        name=input("Enter video name : ")
        time=input("Enter video duration : ")
        videos[index]=({"name":name ,"time":time})
        save_data(videos)
    else:
        print("Invalid index.")
    



def delete_video(videos):
    list_allvideos(videos)
    index = int(input("Enter the index of the video to delete: ")) 
    index-=1
    if 0 <= index < len(videos):
        removed = videos.pop(index)
        save_data(videos)
    else:
        print("Invalid index.")



def main():

    videos=load_data()
    while True:
        print(".......Youtube video manager.......")
        print("Choose what you want to do : ")
        print(" 1:List all the videos.\n 2.Add a video.\n 3.Update particular video details.\n 4.Delete a video from repo.\n 5.Exit  the program.")
        choice=int(input("Enter your choice: "))

        if(choice<1 or choice>5):
            print("Enter a valid input.")
        else:
            match choice:
                case 1:
                    list_allvideos(videos)
                case 2:
                    add_video(videos)
                case 3:
                    update_video(videos)
                case 4:
                    delete_video(videos)
                case 5:
                   break


if __name__=="__main__":
    main()