import requests,ast
'''
data
'''

default_json=[{'author': 'Carl Sagan', 'id': '4', 'published_date': '2013-06-20T00:00:00.000Z'}, {'author': 'Edgar Allen Poe', 'id': '2', 'published_date': '2013-01-19T00:00:00.000Z'}, {'author': 'Ernest Hemingway', 'id': '11', 'published_date': '2013-06-19T00:00:00.000Z'}, {'author': 'Vincent Van Gogh', 'id': '3', 'published_date': '2013-05-10T00:00:00.000Z'}, {'author': 'Tom Brokaw', 'id': '1', 'published_date': '2013-05-02T00:00:00.000Z'}, {'author': 'Thomas Edison', 'id': '5', 'published_date': '2013-03-19T00:00:00.000Z'}, {'author': 'Plato', 'id': '7', 'published_date': '2013-01-16T00:00:00.000Z'}, {'author': 'Robin Williams', 'id': '8', 'published_date': '2013-01-15T00:00:00.000Z'}, {'author': 'Jacqueline Kennedy Onasis', 'id': '9', 'published_date': '2013-01-14T00:00:00.000Z'}, {'author': 'Pablo Picasso', 'id': '10', 'published_date': '2013-01-13T00:00:00.000Z'}, {'author': 'Margaret Thatcher', 'id': '6', 'published_date': '2013-01-12T00:00:00.000Z'}, {'author': 'Ernest Hemingway', 'id': '12', 'published_date': '2013-01-12T00:00:00.000Z'}, {'author': 'Ernest Hemingway', 'id': '13', 'published_date': '2013-01-12T00:00:00.000Z'}, {'author': 'Ernest Hemingway', 'id': '14', 'published_date': '2013-01-12T00:00:00.000Z'}, {'author': 'Ernest Hemingway', 'id': '15', 'published_date': '2013-01-12T00:00:00.000Z'}, {'author': 'Ernest Hemingway', 'id': '16', 'published_date': '2013-01-12T00:00:00.000Z'}, {'author': 'Ernest Hemingway', 'id': '17', 'published_date': '2013-01-12T00:00:00.000Z'}]

trippy="""So, there was this DJ He was like, kicking off, I don't know what he was doing.But it was sick, man. Like, he was like, hands in the air, like, screaming out. So, like, this clown started covering us in silly string and we were all like, writhing around on the floor, at least I thought we were and then this cat walked in, you know, not like a cat, like a feline cat, like a real, like, you know, like, you know what I'm saying dawg? Like cats and dogs. It was raining, it wasn't raining, we were coding. I ate her, man. Not like eight, like nine. Like, I ate her she was fine, man. Like, you know, like, eatin' and sleepin' and ravin' repeatin', you know. There were people dancing I think, or maybe they were cops. I think they might of been cops. Well, anyway, like, I was just dancing and dancing, Oh, no, they were cops.
<br><br><i>Shit.</i><br><br>And this cop just looked at me. And I don't know whether he was really saying it, but all he kept saying was<br><br><i>Eat, sleep, code, repeat,<br>Eat, sleep, code, repeat</i><br><br>Suddenly I think I'm on an interview<br>Suddenly I think I'm selling myself,<br>But I'm not<br>I'm just dreaming,<br> I'm just dreaming,<br>I'm just sleepin'<br>I'm just eatin'<br>I'm just codin'<br>I'm just repeatin'<br>And on, and on, and on, and on, and on, and on<br><br>I felt this thud, it was a bsod, like, boom clutch boom, man<br>Sorry dude, I thought you were a object<br>I went into this cubicle, and the guy was, like, you need something?<br>I'm like no, I'm just dancing to the hum of your cpu fan<br>He's like then get the out of my cubicle,<br>I'm like, I like it here, I like the lighting<br>Besides I like your assistant, she looks pretty hot<br>So I got her by the arm, and I took her outside, and I gave her to the homeless guy<br>He gave me all his google cloud credits<br>And all he kept saying was<br><i><br>Eat, sleep, code, repeat<br>Eat, sleep, code, repeat<br></i><br>'Til like John called me the next morning,<br>Dude, like, where were you last night?<br>I was like, I was there<br>He was like, oh, yeah<br>And then he was like, remember that tune they were playing?<br>I'm like, I don't remember anything, man<br>
I mean, I have like, vague recollections and like, a general feeling of happiness<br>And he was like, no that song, man!<br><br><i><br>Eat, sleep, code, repeat<br>Eat, sleep, code, repeat<br></i><br>
So I came out of my room, there was dark, and there was night and there were street lamps<br>I was pretty, like, I dunno, I went back to my room.<br>So I went in to this website called <a href='http://uncyclopedia.wikia.com/wiki/Main_Page'>uncyclopedia.com</a>  and read some articles, and suddenly it was tomorrow and then tomorrow was today,<br>And then I found this chat room and I went into the room and the room was banging and the music was like, really loud. So I left.<br>I was codin' and suddenly I was helpin' this dude to get rid of a bug and suddenly he was being rude and all he kept saying was<br><br><i>Eat, sleep, code, repeat<br> Eat, sleep, code, repeat</i><br><br>He said yo, I'm a coder, and then he just started to make this thing out of perl code,<br><br>And I swear to god it said<br><br><i>Eat, sleep, code, repeat<br> Eat, sleep, code, repeat</i><br>"""

psych="""Paroxysm of global economics <a href='http://www.google.com'>Google Search</a> event take root and flourish, realm of the galaxies take root and flourish light years, circumnavigated Tunguska event Vangelis. Realm of the galaxies as a patch of light extraplanetary?<br><br>The carbon in our apple pies hundreds of thousands of brilliant syntheses cosmic ocean Hypatia explorations across the centuries take root and flourish muse about with pretty stories for which there's little good evidence. Tunguska event birth billions upon billions venture tesseract billions upon billions! Muse about dream of the mind's eye! Radio telescope. The only home we've ever known with pretty stories for which there's little good evidence! Hydrogen atoms cosmic fugue brain is the seed of intelligence the only home we've ever known? Inconspicuous motes of rock and gas of brilliant syntheses.<br><br>Network of wormholes across the centuries Jean-Francois Champollion hearts of the stars? Vastness is bearable only through love, a still more glorious dawn awaits worldlets the carbon in our apple pies worldlets citizens of distant epochs corpus callosum quasar ship of the imagination. Colonies something incredible is waiting to be known from which we spring billions upon billions, paroxysm of global death with pretty stories for which there's little good evidence, intelligent beings astonishment.<br><br>Brain is the seed of intelligence, billions upon billions, corpus callosum trillion stirred by starlight consciousness cosmic fugue dispassionate extraterrestrial observer.<br><br>Bits of moving fluff. Muse about Apollonius of Perga worldlets the only home we've ever known dispassionate extraterrestrial observer with pretty stories for which there's little good evidence venture at the edge of forever, laws of physics muse about.<br><br>Photos courtesy of <a href='https://unsplash.com/'>Unsplash.com</a>."""

satan="""Satan (who also goes by the aliases Lucifer, The Devil, and Beelzebub to avoid tax collectors) is the primary antagonist in the best-selling Christian novel The Bible. His character is usually comically considered the epitome of evil, and he is often feared, mocked, or just marginalized. In crafting his image - the horns, hooves, trident used for prodding passerby or sending his enemies to the depths, and all - the Catholic Church took inspiration from the Wiccan Horned God and the Greek god Pan, turning loved archetypes into an evil presence though the wonders of propaganda.<br>
<br>Dispute with god<br>Satan and God had a bit of an argument way back when over who should call the shots about what happens to the entire universe. Satan began by laying out his points in a fairly logical fashion, but that's when it all went to hell (pun intended). This discussion between the two of them was the catalyst that sparked God's pretend rage, causing some major smiting and Satan being thrown just outside of the Pearly Gates where he set up his own kingdom and a lemonade stand.
Although Satan found himself just outside the pearly gates he wasn't about to take it lying down so he summoned up legions of pretend demons from the pretend eternal fires to strike back. Meanwhile, back in heaven, God was watching this unfold. So he asked Michael the Archangel and said, "Mike, take care of it." Michael got a bunch of angels down to the gates. It wasn't much of a fight, though, as the angels cast all of the devils out of heaven into the Pit of Hell in a fashion that would be imitated millions of years later by Leonidas and the Spartans.<br>
God has laughed about what happened that day ever since, but because Satan and God are both invincible, the dispute has never ended, except in arm wrestling, drinking contests, Tic-Tac-Toe, and the occasional wet t-shirt contest.<br>
<br>Satan has inspired genres of music such as death metal and black metal; among the metal personalities that claim to have business relations with Satan are bands too nasty to mention. However, in a statement issued as a response to Christian groups, Satan remarked that "Many of these so-called 'Satanists' would not realize if they found themselves in Hell." This has been amusing him since the early-to-mid 20th century, when he invented record companies.
Satan is also affiliated with the rap industry and making deals with Jay-Z and Beyonce with exposure of the aluminary and demon Sasha Fierce. He also apparently knows how to play the fiddle, but isn't very good at it, and his band once lost a battle of the bands to a little boy from Georgia named Johnny and a bunch of chicken. Don't mention this to the big guy though, unless you want a face full of fire.
Satan is mentioned or alluded to in a large number of songs, such as "Sympathy for the Devil" by The Rolling Stones, "Lucifer Sam" by Pink Floyd, "Highway to Hell" by AC/DC, "Bohemian Rhapsody" by Queen, and if you play "Stairway to Heaven" by Led Zeppelin backwards while they're singing "If there's a bustle in your hedgerow, don't be alarmed now...", it really sounds like "Here's to my sweet Satan" and "I sing because I live with Satan" (seriously dude, try it)."""


# If set to true, uses udacity provided images from dropbox which have aspect ratios and are smaller in size
use_udacity_images = True
use_udacity_content = False


base_url=("https://raw.githubusercontent.com/Protino/dump/master/Lego","https://dl.dropboxusercontent.com/u/231329/xyzreader_data/")[use_udacity_images]

photo_url=base_url+'images/'
thumb_url=base_url+'thumbs/'
data_url="https://raw.githubusercontent.com/Protino/dump/master/Lego/data.json"

if use_udacity_images:
    names = ['p004.jpg', 'p002.jpg', 'p011.jpg', 'p003.jpg', 'p001.jpg', 'p005.jpg', 'p007.jpg', 'p008.jpg', 'p009.jpg', 'p010.jpg', 'p006.jpg', 'p012.jpg', 'p013.jpg', 'p014.jpg', 'p015.jpg', 'p016.jpg', 'p017.jpg']
    aspect_ratios = [1.49925, 1.49925, 0.66667, 1.49925, 1.50376, 1.49925, 1.49925, 1.49925, 1, 1.49925, 1.49925, 1, 1.49925, 1.49925, 1.50602, 1.50602, 1.11235]
else:
    #Following are the repository images, not the udacity ones. These are more beautiful but are around ~400 kb, making app slower to render
    names = ['audi.jpg', 'beach.jpg', 'bliss.jpg', 'coffee.jpg', 'green.jpg', 'hills.jpg', 'lake.jpg', 'white_house.jpg', 'random.jpg', 'sat.jpg', 'scape.jpg', 'shuttle.jpg', 'sky.jpg', 'solar_system.jpg', 'sunset.jpg', 'vegas.jpg', 'whatever.jpg', 'orange.jpg']
    aspects_ratios = [-1]*len(names)

if use_udacity_content:
    titles=['Mysteries of the Universe Solved', 'A Flatiron State of Mind', 'An Empire State of Mind', '10 Tips for Hipster Tea Parties', 'My Story of Climbing a Mountain', 'How Fido Got His Bone Back', 'Why I Love Yellow', "Agriculturist's Weekly Update, Delivered Once Daily, 24/7", 'Brooklyn Sidewalks Anonymous', '3 Great Dessert Recipes for This Weekend', 'TV in Modern Beach Environments', 'What I Found While Swimming', 'Bourgeois Office Furniture', 'String Beans and What They Mean for You', "I Can't Get Enough Fantastic Sunsets", 'The Beauty That is Mount Pumpkinfoot', "Busy Streets Are Still Busy, Even If You Don't Want Them To Be"]
    body=(psych)
else:
    titles=["Doctor Strange's Mystical Universe", "Dude's State of Mind", 'An Empire State of Mind', '10 Tips for Hipster Coffee Parties', 'How I Tried Climbing and Broke my Leg', 'PuG is Different than Pug', 'Why I Love Abstract Art', 'Lost In the Wilderness', 'Jumping From a Space Shuttle in 3 Easy Steps', '3 Great Desert Recipes that Martians Adore', 'Lost in the Wilderness - II', 'How I Broke my Back Again', 'Illuminati-on', "Research says Beans will be Extinct in 2050", "I Can't Get Enough of Fantastic Sunsets", 'How I Sold my Mansion for Free', 'Lost in the Wierdness']
    body=(trippy,psych,satan)
    
    

photos=[photo_url+x for x in names]
thumbs=[thumb_url+x for x in names]

def construct_json():
    print ("Constructing json");
    global default_json
    x=y=z=0
    for item in default_json:
        item["body"]=body[x] if use_udacity_content else body[x%len(body)];x+=1
        item["photo"]=photos[y%len(photos)]
        item["thumb"]=thumbs[y%len(thumbs)];y+=1
        item["title"]=titles[z]
        item["aspect_ratio"]=aspect_ratios[z];z+=1

def save():
    print ("Saving json data");
    str_json="["+','.join(list(map(str,default_json)))+"]"
    with open('data.json','w')as f:
        f.write(str_json)
    with open('data.json','r') as f:
        if f.read()!=str_json:
            raise Exception('Save failed!')
        else:
            print ("Successfully saved json data");

def test_endpoint():
    response =  requests.get(data_url)
    remote_data=ast.literal_eval(response.text)
    with open('data.json','r') as f:
        local_data=ast.literal_eval(f.read())
    assert (len(remote_data)==len(local_data))
    for i in range(len(remote_data)):
        x,y=remote_data[i],local_data[i]
        y_values=y.values()
        if (x!=y):
            for key,value in x.items():
                if value not in y_values:
                    print ('Mismatch found for key - ',key,' title ',x['title'])
                    
    print ("Test completed successfully" if local_data==remote_data else "Incorrect response")

def main():
    #construct_json();save()
    #Make sure the changes are committed,pushed and about 30s are elapsed else test will fail
    test_endpoint()
    
if __name__=='__main__':main()
    











