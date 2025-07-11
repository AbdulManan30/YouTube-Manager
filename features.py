import json
def helper(videos):
    with open('Youtube.txt','w') as file:
        json.dump(videos, file)

def load_data():
    try:
        with open('Youtube.txt', "r") as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['duration']} ")
    print("*" * 70)

def add_video(videos):
    name = input("Enter Video Name: ")
    duration = input("Enter Video Duration: ")
    videos.append({"name": name, "duration": duration})
    helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Please Enter video number that you wnat to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter The New Video Name: ")
        duration = input("Enter The New Video Duration: ")
        videos[index-1] = {'name': name, 'duration': duration}
        helper(videos)
    else:
        print('Invalid Number Selected!!')
def delete_video(videos):
    
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted"))
    if 1<= index <= len(videos):
        del videos[index-1]
        helper(videos)
    else:
        print("Invalid video index selected")
    