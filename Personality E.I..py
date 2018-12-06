import pyautogui as pg
import webbrowser as wb
import time as t

points = 0

pg.alert("Hi! Before we start this quiz please type everything with capital letters. Enjoy!")
show = pg.prompt("What is your favorite show? ")

if show == "Avatar the Last Airbender":
    pg.alert("I love that show so much!")
    wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&tbm=isch&q=avatar+the+last+airbender&chips=q:avatar+the+last+airbender,g_1:appa:-ZfTr1_L6V4%3D&usg=AI4_-kSz6LFsxitqEqKSfQQ-TtagFjO1Sw&sa=X&ved=0ahUKEwj76q2Ir7PeAhWpct8KHf_aC68Q4lYIQygO&biw=1120&bih=537&dpr=1.1")
    t.sleep(3)
    points += 5
elif show == "The Office":
    pg.alert("I've never seen that")
    wb.open("https://www.cheatsheet.com/wp-content/uploads/2016/03/The-Office-NBC.jpg")
    t.sleep(3)
    points += -5
elif show == "Friends":
    pg.alert("What even is that?")
    wb.open("https://cdn.vox-cdn.com/thumbor/yx8IVnVHKHVYq_wGjLo8oK2TJ8U=/0x142:2592x2086/1200x800/filters:focal(0x142:2592x2086)/cdn.vox-cdn.com/uploads/chorus_image/image/40348734/friendscast.0.0.jpg")
    t.sleep(3)
    points += -1
elif show == "Riverdale":
    pg.alert("That was okay, Jughead was definitly the best")
    wb.open("https://imgix.bustle.com/uploads/image/2018/7/23/f805b265-57a5-4aea-94e6-8375ea6d0ece-1200-this-is-jughead-s-real-name-on-riverdale.jpg?w=945&h=574&fit=crop&crop=faces&auto=format&q=70")
    t.sleep(3)
    points += 3
elif show == "Chopped":
    pg.alert("That show is so cool!")
    wb.open("https://www.seriouseats.com/images/2012/08/20120808-chopped.jpg")
    t.sleep(3)
    points += 4
elif show == "House Hunters":
    pg.alert("You are one of the only people I know who like that show! Don't worry, I like it too.")
    t.sleep(3)
    points += 5
else:
    pg.alert("I see you have no taste because " + show + " is bad.")
    points += -10

snake = pg.prompt("What is your favorite snake? ")

if snake == "Western Hognose":
    pg.alert("Those are the best! Aren't they so cute?")
    wb.open("http://www.reptilecalculator.com/Images/morphs/2/lavender.jpg")
    t.sleep(3)
    points += 10
elif snake == "Ball Python":
    pg.alert("Those are okay, I guess")
    wb.open("https://i.pinimg.com/originals/1f/10/45/1f1045f560e8072614befb99333b9034.jpg")
    t.sleep(3)
    points += 3
elif snake == "Hognose":
    pg.alert("Do you even know there are more than one types of Hognose snakes?")
    points += 2
elif snake == "Green Tree Python":
    pg.alert("That's great")
    wb.open("https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Gruenebaumpython4cele4.jpg/220px-Gruenebaumpython4cele4.jpg")
    t.sleep(3)
    points += 1
elif snake == "Cobra":
    pg.alert("Ummmmm, that's great?")
    wb.open("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQnBB_kxxpt-CV__P0m8_IvQ_4_7z8jicosBHsV4hWwyUxlWI5d")
    t.sleep(3)
    points += 7
elif snake == "Rattlesnake":
    pg.alert("Do you live in an desert?")
    wb.open("https://thumbs-prod.si-cdn.com/2iBQE9MMbrMCxrCSM6TV2OJyrsM=/800x600/filters:no_upscale()/https://public-media.smithsonianmag.com/filer/f2/94/f294516b-db3d-4f7b-9a60-ca3cd5f3d9b2/fbby1h_1.jpg")
    t.sleep(3)
    points += 3
else:
    pg.alert("Just for the record, Western Hognose snakes are better than the " + snake)
    points += -3

food = pg.prompt("What is you favorite food? ")

if food == "Hamburger":
    pg.alert("Ew")
    wb.open("http://www.konbini.com/wp-content/blogs.dir/9/files/2016/05/burger-480x279.jpg")
    t.sleep(3)
    points += -10
elif food == "Mac and Cheese":
    pg.alert("I love that too!")
    wb.open("https://i2.wp.com/www.peanutbutterandpeppers.com/wp-content/uploads/2014/05/Buffalo-Chicken-Mac-Cheese-015a.jpg")
    t.sleep(3)
    points += 5
elif food == "Candy":
    wb.open("https://www.candy.com/media/wysiwyg/candyByColor.jpg")
    t.sleep(3)
    pg.alert("You are going to get diabetes.")
    points += 3
elif food == "Pancakes":
    food1 = pg.prompt("What is your favorite pancake topping? ")
    if food1 == "Syrup":
        pg.alert("I like syrup, but I hate how its so sticky.")
        points += 5
    elif food1 == "Chcolate chips":
        pg.alert("I loooooveeee chocolate.")
        wb.open("https://schrammsflowers.com/wp-content/uploads/2017/12/chocolate.jpg")
        t.sleep(3)
        points += 7
    else:
        pg.alert("Even if you don't know what to put on pancakes, at least you eat pancakes.")
elif food == "Grilled Cheese":
      pg.alert("YESSSSSSSSSS I love Grilled Cheese so much!")
      wb.open("https://assets.kraftfoods.com/recipe_images/opendeploy/183819_640x428.jpg")
      t.sleep(3)
      points += 4
else:
    pg.alert("If you like this than you have no taste.")

hair = pg.prompt("What color would you dye your hair if you had to?")

if hair == "Blue":
    pg.alert("You are now my best friend.")
    wb.open("https://limecrime-weblinc.netdna-ssl.com/product_images/blue-smoke/Blue%20Smoke/5b639ad561707062640002c3/detail.jpg?c=1533254357")
    t.sleep(3)
    points += 6
elif hair == "Brown":
    pg.alert("Seriously? That is so boring.")
    points += -1
elif hair == "Ombre":
    hair1 = pg.prompt("What color would be at the end of the ombre?")
    if hair1 == "White":
        pg.alert("That is so cool!")
        wb.open("https://i.pinimg.com/originals/18/9e/a5/189ea5b4ee395cee1fe685f8a4ae59b5.jpg")
        t.sleep(3)
        points += 7
elif hair == "Red":
    pg.alert("You would look like Ariel from the Little Mermaid.")
    wb.open("https://vignette.wikia.nocookie.net/disney/images/a/a0/Ariel-1.png/revision/latest?cb=20151005124057")
    t.sleep(3)
    points += 5
elif hair == "Black":
      hair2 = pg.prompt("Is that your natural hair color?")
      if hair2 == "Yes":
        pg.alert("Amazing!")
        points += 5
      elif hair2 == "No":
          pg.alert("Cool!")
          points += 5
      else:
          pg.alert("Great.")
          points += 3
elif hair == "Rainbow":
    pg.alert ("That is sooooo cool!!")
    wb.open("https://vignette.wikia.nocookie.net/mlp/images/4/4b/Rainbow_Dash_Wonderbolt_fantasy_cropped_S1E3.png/revision/latest?cb=20130307050701")
    t.sleep(3)
    points += 6
else:
    pg.alert("That's fine... I guess.")

sport = pg.prompt("What sport do you play?")

if sport == "Soccer":
    sport1 = pg.prompt("Me too! What position do you play?")
    if sport1 == "Forward":
        pg.alert("You must be really fast.")
        wb.open("https://i.dailymail.co.uk/i/pix/2016/02/29/15/31B3E0F900000578-3469640-image-a-8_1456760739429.jpg")
        t.sleep(3)
        points += 5
    elif sport1 == "Defense":
        pg.alert("Same!!! :) ")
        points += 7
    elif sport1 == "Midfield":
        pg.alert("I used to play that position.")
        points += 4
    else:
        pg.alert("That's not even a position.")
        points += -4
elif sport == "Dance":
    pg.alert("Wow you must be flexible! My mom says I'm as flexible as a piece of wood.")
    wb.open("https://cdn.arstechnica.net/wp-content/uploads/2018/06/Baobab_Drink.f1950dda.fill-1200x620-c100-800x413.jpg")
    t.sleep(3)
    points += 3
elif sport == "Field Hockey":
    pg.alert("Awesome! I've never played that before.")
    wb.open("https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/UVA_field_hockey.jpg/220px-UVA_field_hockey.jpg")
    t.sleep(3)
    points += 2
elif sport == "Hockey":
    pg.alert("I'm playing hockey now! I am literally awful at it though.")
    wb.open("https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Capitals-Maple_Leafs_%2834075134291%29.jpg/1200px-Capitals-Maple_Leafs_%2834075134291%29.jpg")
    t.sleep(3)
    points += 5
elif sport == "Squash":
    pg.alert("Great!")
    wb.open("https://www.strongertogether.coop/sites/default/files/wp-content/uploads/2012/10/Winter_Squash_Guide_0.jpg")
    t.sleep(3)
    points += 4
elif sport == "Tennis":
    pg.alert("I loooove playing tennis so much!")
    wb.open ("https://cdn.images.express.co.uk/img/dynamic/72/590x/1051567_1.jpg?r=1543413927306")
    t.sleep(3)
    points += 4
else:
    pg.alert("Is " + sport + " even a real sport?")
    points += -1

pg.alert ("You scored: " + str(points) + " points.")
