from .items import item


class Book(item):
    def __init__(self, Name: str = "", Contense: int = ""):
        super().__init__(Name, "readable", Contense)

    def GetContense(self):
        return self.value


books = [
    Book(
        "hidden echoes",
        """
In a small coastal village, whispers of the past linger in the salty air. Young Anna discovers an ancient diary buried beneath the floorboards of her grandmother’s attic. Each entry 
reveals
secrets of love, loss, and a hidden treasure that was never found. As she delves deeper, Anna realises that the echoes of the past are not merely stories; they shape the present. 
With the help
of her best friend, she sets out on a quest to uncover the truth behind the diary’s final entry. Along the way, they face challenges that test their friendship and courage. Will they 
unlock the
secrets of the hidden echoes, or will the past remain buried forever?
""",
    ),
    Book(
        "enchanted evening",
        """
On a chilly autumn night, a mysterious stranger arrives in the quaint town of Eldridge. Clara, a budding artist, finds herself drawn to the stranger, whose enchanting stories of 
far-off lands
ignite her imagination. As they stroll through the moonlit streets, Clara learns that the stranger is on a mission to reclaim a lost magical artifact that could save his realm. 
Together, they
embark on an adventure filled with whimsical creatures and ancient prophecies. As dawn approaches, Clara must decide whether to follow her heart or remain in the safety of her world. 
In this
enchanted evening, destiny intertwines their fates in ways they could never have imagined.
""",
    ),
    Book(
        "'book of mystery",
        """
Bill had been exploring the mansion for hours, uncovering hidden corners and old secrets layered in dust. At last, he found himself in the attic, where the faint scent of mildew and 
ancient
wood lingered in the air. Beneath a loose floorboard, he discovered a battered leather journal, its spine cracked and pages yellowed with age. The cover bore a faint spiral symbol 
flanked by
two crescent moons, almost glowing in the dim light.
He flipped the journal open, intrigued yet wary. Inside, the handwriting was spidery and uneven, as if the author had written in haste or fear. He read the first entry:
"To know what lies within these pages is to risk everything. Knowledge is a double-edged sword. If you seek the truth, be prepared to walk in shadows."
A chill crept over him, but he kept reading, unable to stop. The journal was filled with cryptic messages and peculiar symbols, alongside sketches of places he didn’t recognise—dark 
forests,
hidden rooms, and narrow passageways. Every few pages, the spiral symbol with the crescent moons appeared again, bringing with it a sense of déjà vu that Bill couldn’t shake.
"The path will reveal itself under the moonlight," another entry read. "But beware the shadows, for they hunger for those who wander unguarded."
The attic creaked as he turned another page, the silence around him growing heavier. He felt as if someone—or something—was watching him, hidden in the dark corners of the room. 
Ignoring his
growing unease, he continued reading, his heartbeat echoing in the quiet.
The final entry was more ominous than the rest:
"To find what is lost, one must walk the hidden path. But do not take this journey lightly, for the mansion keeps what it claims."
Bill closed the journal, his mind racing with questions. The mansion held secrets beyond what he’d imagined, secrets tied to the strange journal and its warnings. Yet he felt an 
unexplainable
urge to follow its instructions, to uncover the truth hidden within these walls.
Tucking the journal into his coat, he made his way down the attic stairs, resolved to walk the path it had promised. The night was still, the air thick with mystery as he stepped 
into the
shadows, ready—or not—for whatever waited ahead.
""",
    ),
    Book(
        "seelkind",
        """
In a world cloaked in mist, where memories whispered like wind, there lived a young Seelkind named Leora. The Seelkind were keepers of memories—guardians of joy, sorrow, and 
forgotten dreams.
Only they could venture into the Valley of Shadows, where lost memories lay hidden.
One dusk, as the silver moon rose, Leora heard a call from the Valley. A child’s laughter echoed, fading quickly, as if slipping from existence. She followed the sound, her heart 
heavy with the
duty she was born to fulfill.
In the Valley, she found a memory—a single, glowing fragment. It was a child’s first steps, small and uncertain but filled with wonder. Leora cradled the memory and whispered ancient 
words.
Slowly, the memory brightened, filling the valley with warmth.
As dawn broke, Leora returned the memory to its rightful place in the world. It was a small act, a single memory saved, but she knew each one mattered. For without memories, who were 
they? And
so, she continued her path as a Seelkind, keeper of moments, protector of souls.
""",
    ),
    Book(
        " the last lantern",
        """
In a village where twilight stretched endlessly, Mira was known as the Keeper of the Last Lantern. She hadn’t always been alone; once, every home held a lantern, lighting the town 
with a
comforting glow. But as seasons wore on, their lights dimmed, and one by one, each flickered out, leaving only Mira’s to push against the shadows.
Every evening, she would carry it to the edge of the village where an ancient tree stood. It was said that the first flame had been kindled there by the village’s founder. In hopes of
rekindling the others, Mira would hold her lantern to its roots and whisper the words of the old songs.
One night, a faint spark stirred beneath the soil. By dawn, new flames bloomed like flowers throughout the village, each one vibrant and warm. The village glowed once more, and Mira 
became a
legend. They called her The Bringer of Light, and in their hearts, her lantern would burn forever.
""",
    ),
    Book(
        "whispers from the wispwood",
        """
When winter descended upon Wispwood, strange whispers wove through the winds, whispering secrets long since lost. Willow, a wandering soul with a warm heart, wondered why the woods 
seemed so
wild and wary this season. With each wary step, whispers weaved around her like a winding song, words barely heard, yet deeply felt.
“Watch for the well,” they warned. “Within lies what was once forgotten.”
Willow reached an old well wrapped in weeds, water within as dark as midnight. When she leaned over, a wisp of silver light wound up, wrapping around her wrist. Suddenly, memories 
rushed back —
faces, places, things she wished were gone, yet now were somehow welcome. She remembered Wispwood, the home she’d hidden from her heart.
The whispering ceased, but the wisp remained, a thread linking her past and present. With a wistful smile, she walked back, finally whole, and as winter waned, the whispers faded, 
but Willow
would forever remember the wonder of the well.
""",
    ),
    Book(
        "a whisper from the dark",
        """
A soft whisper floated through the darkness, drawing Alina from her restless sleep. A shiver ran down her spine as she strained to listen, her eyes wide, searching the shadows. 
Around her, the
room was empty, save for the faint flicker of a candle casting long, eerie shapes against the walls.
Alina took a careful step, her heartbeat echoing in her ears. A distant memory tugged at her mind, hazy and out of reach, yet somehow familiar. As she moved closer to the room’s lone 
window,
the whisper grew louder, more insistent, like the pages of an old book turning by themselves.
"Awaken," it breathed, the voice woven with threads of both kindness and sorrow. Alina paused, feeling an invisible pull. A single word was etched onto the frosty glass: Remember.
A chill passed through her as memories began to unravel, revealing a hidden world of forgotten promises and lost dreams. Against the window, Alina pressed her trembling hand, 
realising that the
voice wasn’t from some stranger in the night.
It was hers.
""",
    ),
    Book(
        "tangled shadows",
        """
In a town veiled in perpetual mist, a young boy named Ellis discovers an old compass in his grandfather's attic. It's no ordinary compass; its needle spins not north, but toward the 
deepest
shadows, revealing hidden secrets when followed. One night, the compass leads Ellis to the edge of town, where shadows pool like liquid ink. The closer he gets, the more vivid his 
dreams
become, showing fragments of people he’s never met but feels he knows. The final vision shows a hooded figure with Ellis's own eyes staring back at him, lips moving in warning. The 
compass
shudders in his hand. "If you step into these shadows," the warning echoes, "you may never return."
""",
    ),
    Book(
        "celestial whispers",
        """
In the chill of winter, villagers gather around bonfires to listen to the stories of Mira, a stargazer who claims to hear whispers from the heavens. She insists the stars reveal 
warnings and
messages, though few believe her. One night, the stars tell of an approaching storm—no ordinary storm, but a celestial force capable of wiping away everything in its path. Mira urges 
the
villagers to take shelter deep in the forest’s heart, a place only spoken of in old tales. Desperate, some follow her. Hours later, the storm rolls in, altering the landscape 
forever, but those
who followed Mira survive. The whispers stop after that, leaving her with one final message: “It is time to go.”
""",
    ),
    Book(
        "hollow realm",
        """
Beneath the ancient oak tree lies a hidden realm, discovered by a traveler named Orin seeking shelter from a storm. The ground gives way, revealing a vast, hollow world suspended in 
twilight.
Time behaves strangely here, and Orin meets inhabitants who have aged centuries in what feels like hours. Each insists they were once travelers like him. Orin learns that escaping 
requires
solving the realm’s riddle, which no one has yet cracked. As his own age begins to creep up, Orin realises the riddle’s answer lies in choosing to forget, something none before him 
dared. With
a sigh, he closes his eyes and lets go.
""",
    ),
    Book(
        "inkbound",
        """
In an obscure library, Elena stumbles upon The Book of Lost Names. Each page she reads begins to transform her thoughts, replacing her memories with fragments of a different life. As 
she delves
deeper, she feels compelled to uncover the book’s story. Her reflection in the library window changes subtly, her hair shorter, eyes unfamiliar. Panicked, she tries to stop reading, 
but the
book won’t let her put it down. Just as her final memory slips away, she understands: The Book of Lost Names is rewriting her into someone else’s story. Her last thought is of a 
stranger named
Lucas… then darkness.
""",
    ),
    Book(
        "nighthawk’s call",
        """
Under the starlit sky, young Rook follows a strange bird’s call through dense woods to a forgotten chapel, where moonlight reveals an altar lined with feathers. The bird circles 
above, watching
him with uncanny intelligence, as if it expects something of him. Compelled, Rook kneels at the altar and closes his eyes. In that moment, his vision shifts to the bird’s, soaring 
over miles of
forest, hills, and forgotten roads. He sees places he’s never known but feels drawn to. When he opens his eyes, the bird is gone, leaving him with an unsettling urge to find each 
place. His
journey has only begun.
""",
    ),
    Book(
        "ghost of yew manor",
        """
At Yew Manor, the walls whisper, and the floors groan under invisible footsteps. Clara moves into the house after her grandmother’s passing, warned of its “occupant.” On her first 
night, she
encounters a young girl dressed in the style of centuries past, who stands by her bed, simply watching. Over the weeks, Clara learns the girl’s name was Isabelle, and she went 
missing decades
ago. Isabelle’s gaze is mournful, her hands outstretched as if beckoning Clara into the cold, dark halls. When Clara finally follows her, she finds a hidden door beneath the 
staircase. Inside
is a diary that ends with a single, unfinished sentence: “I am waiting.”
""",
    ),
    Book(
        " shadows of tomorrow",
        """
In the quiet town of Eldridge, a secret lay hidden beneath the sprawling oak trees. Every night, at the stroke of midnight, a soft glow emanated from the heart of the forest. 
Curiosity gripped
the townsfolk, but fear held them back.

Young Clara, with her heart full of courage, decided to uncover the truth. Armed with only a flickering lantern, she ventured into the depths of the woods. The air thickened with 
mystery as she
followed the light, each step echoing in the silence.

As she approached the source, Clara discovered an ancient stone archway, adorned with vines and shimmering with ethereal energy. Beyond the arch, a world unlike any other awaited—one 
where
shadows danced and dreams took flight. The glow beckoned her, whispering promises of adventure and forgotten tales.

Clara stepped through, leaving behind the mundane. In that moment, she knew she had crossed into the shadows of tomorrow, where her destiny awaited, woven into the fabric of time 
itself. What
lay ahead was unknown, but she was ready to embrace the magic of the journey.
""",
    ),
    Book(
        "yesterday's echoes",
        """
In a small, forgotten village, a young girl named Elara discovered an ancient locket while playing near the old oak tree. Inside, she found a faded photograph of a woman she 
recognised as her
grandmother. Intrigued, Elara ventured to her grandmother's house, where she uncovered stories of love, loss, and resilience. Each tale echoed the struggles and triumphs of 
generations past. As
she listened, Elara realised the power of her family's history, weaving it into her own identity. Inspired, she decided to write her own story, ensuring that the echoes of yesterday 
would
resonate in the future.
""",
    ),
    Book(
        "orchid's bloom",
        """
In a bustling city, Clara, a florist, tended to her shop with unwavering passion. Among her vibrant blooms, one orchid captured her heart—a rare, delicate flower that seemed to 
flourish despite
the chaos around it. Clara named it “Hope.” One rainy afternoon, a distraught customer entered her shop, overwhelmed by life’s burdens. Clara offered her the orchid, explaining how 
it thrived
in adversity. Touched by the gesture, the customer left with a renewed spirit, carrying Hope with her. Inspired by this connection, Clara began crafting floral arrangements infused 
with
messages of resilience, transforming her shop into a sanctuary of hope for all who entered.
""",
    ),
    Book(
        "under the starry sky",
        """
On a warm summer night, a group of friends gathered in a meadow, the sky above them a canvas of shimmering stars. They shared stories, laughter, and dreams, each revealing their 
aspirations for
the future. As the night deepened, they began to ponder their individual paths, feeling a blend of excitement and fear. One friend, Liam, suggested they create a time capsule, 
sealing their
dreams within. They agreed, writing letters to their future selves, filled with hopes and promises. Years later, under that same starry sky, they reunited, opening the capsule to 
reflect on how
far they had come. Their dreams had changed, yet the bond they shared remained unbreakable.
""",
    ),
    Book(
        "the keeper of the lost library",
        """
In a forgotten corner of the city, Lucy stumbled upon a library that no one else seemed to notice. The books were old, some nearly crumbling, but each whispered secrets and stories 
she had
never heard before. A man with a long, grey beard introduced himself as the Keeper and welcomed her.

“Choose a book carefully,” he said. “Once you open it, you’ll be part of its world.” Lucy picked one bound in emerald leather, its cover etched with golden vines. As she opened it, 
the room
faded, and she found herself in a dense, misty forest under a starlit sky. Her heart pounded, feeling both fear and thrill.

She looked back, and the Keeper’s voice echoed, “Remember, only those who seek true knowledge can return.” With a deep breath, Lucy stepped forward, her story just beginning.
""",
    ),
    Book(
        "the clockmaker’s daughter",
        """
Lucy returned to the Lost Library often, and on one visit, she met Elsa, the daughter of a clockmaker whose family had kept secrets almost as strange as the library itself. Elsa 
carried a
pocket watch, a delicate piece passed down through generations, inscribed with symbols that seemed to shimmer in the dim library light.

“Father says it holds a doorway to the past,” Elsa whispered, as they stood by a shelf filled with books about time. She placed the watch in Lucy’s hands, and Lucy felt herself 
slipping through
the library’s layers of time. When they reappeared, they found themselves in an ancient village, gears and clock towers scattered around.

The Keeper’s voice whispered in the wind, “Some doors take you backward to find the future.” Lucy and Elsa exchanged glances, sensing they were bound to explore more mysteries 
together.
""",
    ),
    Book(
        "the forgotten key",
        """
One day, Lucy and Elsa discovered a dusty, locked cabinet in the library. The Keeper gave them a tarnished, enchanted key, explaining that this door led to a realm beyond any they’d 
seen
before. With cautious excitement, they opened the cabinet, revealing a shimmering landscape filled with floating islands and ancient artefacts from across time.

Each artefact seemed to beckon, hinting at untold stories and ancient mysteries. Lucy held up a golden compass that began to spin wildly, directing them to a hidden map marking 
locations
throughout the world—each connected to a legend they’d read in the library.

The Keeper’s voice echoed, “Only those who seek knowledge for others can wield such power.” With the key and compass in hand, Lucy and Elsa realised their adventure was far from 
over. They had
become the library’s new guardians, charged with discovering and protecting the secrets that connected their world to countless others.
""",
    ),
    Book(
        "the mirror of worlds",
        """

Lucy and Elsa’s roles as guardians grew, and with each visit to the Lost Library, they unlocked more mysteries. One day, they discovered an ancient mirror hidden behind a curtain, 
its surface
rippling as if alive. The Keeper appeared beside them, his gaze somber.

“This mirror shows worlds within worlds,” he said. “Only enter if you dare to face your reflection.” Lucy touched the mirror, and suddenly she and Elsa were pulled into a world 
identical to
their own but with eerie differences. Here, they encountered shadowy versions of themselves, mirroring their every move but with dark, questioning eyes.

Understanding dawned as the shadows whispered, “Are you worthy of the library’s secrets?” The girls faced their fears and doubts, emerging from the mirror with renewed courage. The 
Keeper
nodded approvingly, knowing they were ready for the library’s deeper secrets.
""",
    ),
    Book(
        "the tides of memory",
        """
Following the encounter with their shadows, the Keeper entrusted Lucy and Elsa with a mysterious, water-stained book titled The Tides of Memory. Its pages seemed alive, flowing like 
waves as
they read. “This book can help you see hidden memories, but beware—they may not all be pleasant,” the Keeper warned.

They opened the book, and instantly, the library transformed into a vast, endless ocean. Floating there were fragments of people’s pasts—memories preserved by those who had once 
visited the
library. They saw glimpses of lost loves, ancient battles, and forgotten treasures.

As Lucy reached out to touch one, she was overcome by the memory of a young girl who once searched for the library’s secrets but disappeared before finding them. Realising that 
memories held
clues, Lucy and Elsa swore to honour the stories within the pages, carrying them forward and keeping the memories alive.
""",
    ),
    Book(
        "the map of echoes",
        """
One evening, Elsa found a strange map tucked inside an old atlas. The Keeper confirmed that this was The Map of Echoes, a guide to places in the library that only appeared when one 
listened
closely. Together, they followed faint whispers that seemed to echo through the halls, each leading to a hidden room or ancient scroll.

As they explored, the map revealed a forgotten wing filled with artefacts from different worlds the library had once connected to. Among them, they discovered a golden feather 
inscribed with an
ancient language and a lantern that never extinguished. Each object held the memories of the worlds they’d come from, waiting to be rediscovered.

“Echoes of the past can light your path,” the Keeper said softly. Lucy and Elsa knew their journey as guardians was far from over. Now, they had a map, a feather, and a lantern, 
symbols of
wisdom, courage, and light to guide them through the mysteries yet to be revealed.
""",
    ),
    Book(
        "the song of the forgotten",
        """
One day, Lucy and Elsa heard a haunting melody drifting through the shelves. Drawn by the music, they followed the sound to a secluded corner where they found a dusty music box 
adorned with
jewels and intricate carvings.

The Keeper explained, “This is the Song of the Forgotten. It plays the voices of those who have entered the library but left their stories unfinished.” Entranced, Lucy wound the box, 
and
ghostly figures appeared around them—forgotten writers, artists, and dreamers who had once sought the library’s secrets.

As the figures told their stories, Lucy and Elsa realised they had a duty not only to guard the library but to help these lost souls finish their tales. With each story completed, 
the figures
faded, leaving a golden glow in their place. The girls felt a sense of purpose; they were not just explorers but also keepers of stories left untold.
""",
    ),
    Book(
        "the lantern of evernight",
        """
During a particularly stormy evening, Lucy noticed a flickering light in the library’s highest tower, where no one had ventured before. Curious, she and Elsa climbed the winding 
staircase,
braving gusts of wind and shadows. At the top, they discovered a lantern emitting a dim but unwavering glow.

“This is the Lantern of Evernight,” the Keeper told them. “It guides those lost in the darkness.” When Lucy held the lantern, it shone brightly, revealing hidden passages and doors 
within the
library that they had never noticed. Each passage led to a room that illuminated knowledge forgotten by history—ancient inventions, rare languages, and extinct creatures.

Guided by the lantern, the girls understood that some knowledge could only be found in the darkest corners. They vowed to keep the lantern close, lighting the way for all who dared 
to seek the unknown.
""",
    ),
    Book(
        "the book of shadows",
        """
Lucy and Elsa discovered a locked, black-bound book with a single silver key dangling from it. Unlike the other books, this one seemed to avoid their touch, slipping away each time 
they reached
for it. When they finally grasped it, the Keeper appeared, his eyes cautious.

“This is the Book of Shadows,” he said gravely. “It reveals secrets hidden even from yourself.” With trepidation, they unlocked it, and strange symbols appeared, swirling to form 
words that
spoke directly to their hearts. Each page held a mystery about themselves—fears they hadn’t faced, dreams they hadn’t pursued.

As they read, the shadows of their hidden selves came to life, testing their courage and resolve. By the book’s end, Lucy and Elsa felt stronger, having faced their own hidden 
truths. They knew
the library demanded not just courage to explore the world, but to explore oneself.
""",
    ),
    Book(
        "the path of stars",
        """
One evening, the Keeper led Lucy and Elsa to the library’s observatory, where a map of stars was etched into the ceiling. “This is the Path of Stars,” he said. “It connects the 
library to
realms beyond imagination, visible only to those who seek it.”

With a touch, the star map glowed, and the ceiling opened up, revealing constellations that shimmered and shifted to form a radiant path. Taking a deep breath, Lucy and Elsa stepped 
onto the
starlit road, feeling themselves lift off the ground and into the cosmos. They visited realms woven from stardust, each representing an idea or dream from different worlds.

When they returned, they carried stardust in their hands, a reminder that their journey was boundless. The Keeper smiled, knowing they had embraced the library’s final truth—that 
knowledge has
no limits, and that curiosity was their guiding star. The library’s mysteries would unfold forever, as long as they dared to follow the path of stars.
""",
    ),
    Book(
        "The Warning",
        """
I’ve tried everything. The windows don’t open, the doors are all locked. If you’re reading this, you’ve made the same mistake I did. Don’t trust Neel-thee. Don’t listen to him. He 
knows how to get inside your mind. He will not let you leave. The walls are his prison, and now they are yours too.
"""
    ),
]
