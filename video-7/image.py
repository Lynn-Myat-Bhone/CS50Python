from  PIL import Image

img_list = ["D:\\CS50Python\\video-7\\1.png",
            "D:\\CS50Python\\video-7\\2.png",
            "D:\\CS50Python\\video-7\\3.png",
            "D:\\CS50Python\\video-7\\4.png"]
image_file = [Image.open(file).convert("P" )for file in img_list]
image_file[0].save(
    "RunningDuck.gif",
    save_all=True,
    append_images= image_file[1:],
    duration = 200,
    loop =0
)