print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
🏴‍☠️ WELCOME TO TREASURE ISLAND 🏴‍☠️
''')

# Language Selection
print("Choose your language / Pilih bahasa:")
print("1. English")
print("2. Bahasa Indonesia")

language = input("Enter your choice (1/2): ")

if language == "1":
    # ENGLISH VERSION
    print("\n🏴‍☠️ WELCOME TO TREASURE ISLAND 🏴‍☠️")
    print("Welcome to Treasure Island!")
    print("Your mission is to find Captain Blackbeard's lost treasure.")
    print("Every choice you make will determine your fate...\n")

    # Get player name
    name = input("What's your adventurer's name? ")
    print(f"Alright, {name}! Let's begin your adventure...\n")

    # STAGE 1: Island entrance
    print("🏝️ You arrive at the beach of a mysterious island.")
    print("In front of you are three different paths:")
    print("- LEFT: A trail leading to a dark forest")
    print("- RIGHT: A rocky path heading to the northern beach")
    print("- CENTER: A dirt road leading to a tall hill")

    direction = input("Where will you go? (left/right/center): ").lower()

    if direction == "left":
        print(f"\n🌲 {name} enters the dark, mysterious forest...")
        print("You hear strange sounds from behind the trees!")
        print("What will you do?")

        action = input("ATTACK with a stick, HIDE behind a tree, or RUN? ").lower()

        if action == "attack":
            print(f"\n⚔️ {name} attacks bravely!")
            print("It turns out to be just a monkey looking for food.")
            print("The monkey gives you an old map as a token of gratitude!")

            # STAGE 2A: With map
            print("\n🗺️ With the map in hand, you discover a hidden cave.")
            print("There are three rooms inside the cave:")

            room = input("Choose a room: NORTH (dark), SOUTH (bright), EAST (smells weird)? ").lower()

            if room == "north":
                print(f"\n🕯️ {name} carefully enters the dark room...")
                print("CONGRATULATIONS! You found a treasure chest with 1000 gold coins!")
                print("🏆 VICTORY! You are a brave explorer!")

            elif room == "south":
                print(f"\n💡 {name} enters the bright room...")
                print("You discover an ancient library with valuable books!")
                print("📚 VICTORY! You gain knowledge and 500 gold coins!")

            elif room == "east":
                print(f"\n💀 {name} enters the weird-smelling room...")
                print("OH NO! This room is full of poisonous gas!")
                print("⚰️ GAME OVER! You faint and are never found again...")

            else:
                print("🚫 Invalid choice! You get lost in the cave...")
                print("💀 GAME OVER!")

        elif action == "hide":
            print(f"\n🤫 {name} cleverly hides behind a large tree...")
            print("You see a group of pirates pass by carrying a chest!")
            print("They drop a golden key!")

            # STAGE 2B: With key
            print("\n🔑 With the golden key, you follow the pirates' trail.")
            print("You find three locked doors:")

            door = input("Which door will you open? RED, BLUE, or YELLOW? ").lower()

            if door == "yellow":
                print(f"\n🟡 {name} opens the yellow door...")
                print("INCREDIBLE! This is the main treasure room!")
                print("💰 PERFECT WIN! You found 5000 gold coins and gems!")

            elif door == "blue":
                print(f"\n🔵 {name} opens the blue door...")
                print("You find a room filled with antique pirate equipment!")
                print("⚓ GOOD WIN! You get treasure worth 2000 coins!")

            elif door == "red":
                print(f"\n🔴 {name} opens the red door...")
                print("DANGER! Inside is a poisonous arrow trap!")
                print("🏹 GAME OVER! You're hit by an arrow and fall...")

            else:
                print("🚫 Invalid choice! Time's up, pirates return!")
                print("💀 GAME OVER!")

        elif action == "run":
            print(f"\n🏃‍♂️ {name} runs away in fear without looking back...")
            print("In panic, you fall into a hole!")
            print("🕳️ GAME OVER! You're trapped in a deep pit...")

        else:
            print("🚫 Invalid choice! You stand confused for too long...")
            print("🐅 A tiger appears and chases you!")
            print("💀 GAME OVER!")

    elif direction == "right":
        print(f"\n🏖️ {name} walks towards the northern beach...")
        print("You see an old ship stranded on the beach!")
        print("There's also a small lake with clear water.")

        choice = input("BOARD the old ship or SWIM in the lake? ").lower()

        if choice == "board":
            print(f"\n🚢 {name} boards the old pirate ship...")
            print("This ship is full of traps and ghosts!")
            print("💀 GAME OVER! Pirate ghosts drag you to the ocean floor...")

        elif choice == "swim":
            print(f"\n🏊‍♂️ {name} swims in the clear lake...")
            print("The lake water is very cold! What will you do?")

            swim_action = input("CONTINUE swimming or RETURN to shore? ").lower()

            if swim_action == "continue":
                print("\n❄️ The water gets colder, but you keep swimming...")
                print("In the middle of the lake is a small island with a strange tree!")

                island_choice = input("CLIMB onto the island or GO BACK? ").lower()

                if island_choice == "climb":
                    print(f"\n🏝️ {name} climbs onto the small island in the lake...")
                    print("The strange tree is hiding stairs leading underground!")
                    print("🏆 AMAZING WIN! You found an underwater treasure room!")
                    print("💎 You get rare gems worth 10,000 coins!")

                elif island_choice == "back":
                    print(f"\n🔄 {name} decides to go back...")
                    print("On the shore you find a bottle with a message!")
                    print("📜 GOOD WIN! The message contains clues to small treasure - 800 coins!")

                else:
                    print("🚫 Invalid choice! You get confused and drown...")
                    print("💀 GAME OVER!")

            elif swim_action == "return":
                print(f"\n↩️ {name} wisely returns to shore...")
                print("On the beach you find a hidden small cave!")
                print("🏺 SAFE WIN! In the cave is a pot with 300 gold coins!")

            else:
                print("🚫 Invalid choice! You panic and drown...")
                print("💀 GAME OVER!")

        else:
            print("🚫 Invalid choice! You stand confused...")
            print("🌊 High tide comes and drags the ship (and you) to sea!")
            print("💀 GAME OVER!")

    elif direction == "center":
        print(f"\n⛰️ {name} climbs the tall hill with difficulty...")
        print("From the hilltop, you can see the entire island!")
        print("You see an old tower in the distance.")

        tower_choice = input("GO to the tower or DESCEND from the hill? ").lower()

        if tower_choice == "go":
            print(f"\n🗼 {name} walks towards the old tower...")
            print("The tower is very tall and looks dangerous!")

            climb_choice = input("CLIMB the tower or FIND another way? ").lower()

            if climb_choice == "climb":
                print(f"\n🧗‍♂️ {name} carefully climbs the tower...")
                print("At the top of the tower is a lighthouse with strange light!")

                light_choice = input("TURN ON the lighthouse or LEAVE it? ").lower()

                if light_choice == "turn":
                    print(f"\n💡 {name} turns on the ancient lighthouse...")
                    print("The lighthouse beam opens a secret door at the tower's base!")
                    print("🏆 EPIC WIN! The secret room contains complete treasure!")
                    print("👑 You get a golden crown and 15,000 coins!")

                elif light_choice == "leave":
                    print(f"\n🚪 {name} leaves the lighthouse and climbs down...")
                    print("In the middle of the tower you find a room with a small chest!")
                    print("📦 DECENT WIN! The chest contains 1200 gold coins!")

                else:
                    print("🚫 Invalid choice! The tower starts to collapse!")
                    print("💀 GAME OVER! You're buried under tower ruins...")

            elif climb_choice == "find":
                print(f"\n🕵️‍♂️ {name} looks for another way around the tower...")
                print("You find a hidden basement door!")
                print("🚪 SMART WIN! The basement contains antique pirate gear!")
                print("⚓ You get treasure worth 2500 coins!")

            else:
                print("🚫 Invalid choice! You get lost around the tower...")
                print("🌙 Night falls, you get cold and are never found...")
                print("💀 GAME OVER!")

        elif tower_choice == "descend":
            print(f"\n⬇️ {name} carefully descends from the hill...")
            print("At the foot of the hill you find a tropical fruit garden!")
            print("🥭 PEACEFUL WIN! You live peacefully as a farmer!")
            print("🌴 Bonus: You find 600 hidden coins in the garden!")

        else:
            print("🚫 Invalid choice! You slip from the hill...")
            print("💀 GAME OVER! Fell from a great height...")

    else:
        print("🚫 Invalid choice!")
        print("While you're confused about which direction to take...")
        print("🌊 High tide rises and sweeps the entire beach!")
        print("💀 GAME OVER! You're swept by waves into the deep sea...")

    print(f"\n⭐ Thank you for playing, {name}!")
    print("🎮 Adventure complete!")

elif language == "2":
    # BAHASA INDONESIA VERSION
    print("\n🏴‍☠️ SELAMAT DATANG DI PULAU HARTA KARUN 🏴‍☠️")
    print("Selamat datang di Pulau Harta Karun!")
    print("Misimu adalah menemukan harta karun Captain Blackbeard yang hilang.")
    print("Setiap pilihan yang kamu ambil akan menentukan nasibmu...\n")

    # Mendapatkan nama pemain
    name = input("Siapa nama petualangmu? ")
    print(f"Baik, {name}! Mari kita mulai petualanganmu...\n")

    # TAHAP 1: Pintu masuk pulau
    print("🏝️ Kamu tiba di pantai pulau misterius.")
    print("Di depanmu ada tiga jalan berbeda:")
    print("- KIRI: Jalan setapak menuju hutan gelap")
    print("- KANAN: Jalan berbatu menuju pantai utara")
    print("- TENGAH: Jalan tanah menuju bukit tinggi")

    direction = input("Kemana kamu akan pergi? (kiri/kanan/tengah): ").lower()

    if direction == "kiri":
        print(f"\n🌲 {name} memasuki hutan gelap yang penuh misteri...")
        print("Kamu mendengar suara aneh dari balik pepohonan!")
        print("Apa yang akan kamu lakukan?")

        action = input("SERANG dengan tongkat, SEMBUNYI di balik pohon, atau LARI? ").lower()

        if action == "serang":
            print(f"\n⚔️ {name} menyerang dengan berani!")
            print("Ternyata hanya seekor monyet yang mencari makanan.")
            print("Monyet itu memberikan kamu peta kuno sebagai tanda terima kasih!")

            # TAHAP 2A: Dengan peta
            print("\n🗺️ Dengan peta di tangan, kamu menemukan gua tersembunyi.")
            print("Ada tiga ruangan di dalam gua:")

            room = input("Pilih ruangan: UTARA (gelap), SELATAN (terang), TIMUR (berbau aneh)? ").lower()

            if room == "utara":
                print(f"\n🕯️ {name} memasuki ruangan gelap dengan hati-hati...")
                print("SELAMAT! Kamu menemukan peti harta karun berisi 1000 koin emas!")
                print("🏆 KEMENANGAN! Kamu adalah penjelajah yang berani!")

            elif room == "selatan":
                print(f"\n💡 {name} memasuki ruangan terang...")
                print("Kamu menemukan perpustakaan kuno dengan buku-buku berharga!")
                print("📚 KEMENANGAN! Kamu mendapat pengetahuan dan 500 koin emas!")

            elif room == "timur":
                print(f"\n💀 {name} memasuki ruangan berbau aneh...")
                print("OH TIDAK! Ruangan ini penuh dengan gas beracun!")
                print("⚰️ GAME OVER! Kamu pingsan dan tidak pernah ditemukan lagi...")

            else:
                print("🚫 Pilihan tidak valid! Kamu tersesat di gua...")
                print("💀 GAME OVER!")

        elif action == "sembunyi":
            print(f"\n🤫 {name} bersembunyi dengan cerdik di balik pohon besar...")
            print("Kamu melihat sekelompok bajak laut lewat sambil membawa peti!")
            print("Mereka menjatuhkan kunci emas!")

            # TAHAP 2B: Dengan kunci
            print("\n🔑 Dengan kunci emas, kamu mengikuti jejak bajak laut.")
            print("Kamu menemukan tiga pintu terkunci:")

            door = input("Pintu mana yang akan kamu buka? MERAH, BIRU, atau KUNING? ").lower()

            if door == "kuning":
                print(f"\n🟡 {name} membuka pintu kuning...")
                print("LUAR BIASA! Ini adalah ruang harta karun utama!")
                print("💰 PERFECT WIN! Kamu menemukan 5000 koin emas dan permata!")

            elif door == "biru":
                print(f"\n🔵 {name} membuka pintu biru...")
                print("Kamu menemukan ruang berisi peralatan bajak laut antik!")
                print("⚓ GOOD WIN! Kamu mendapat harta senilai 2000 koin!")

            elif door == "merah":
                print(f"\n🔴 {name} membuka pintu merah...")
                print("BAHAYA! Di dalam ada jebakan panah beracun!")
                print("🏹 GAME OVER! Kamu terkena panah dan tumbang...")

            else:
                print("🚫 Pilihan tidak valid! Waktu habis, bajak laut kembali!")
                print("💀 GAME OVER!")

        elif action == "lari":
            print(f"\n🏃‍♂️ {name} berlari ketakutan tanpa melihat ke belakang...")
            print("Dalam kepanikan, kamu terjatuh ke dalam lubang!")
            print("🕳️ GAME OVER! Kamu terjebak di lubang yang dalam...")

        else:
            print("🚫 Pilihan tidak valid! Kamu berdiri bingung terlalu lama...")
            print("🐅 Seekor harimau muncul dan mengejarmu!")
            print("💀 GAME OVER!")

    elif direction == "kanan":
        print(f"\n🏖️ {name} berjalan menuju pantai utara...")
        print("Kamu melihat kapal tua terdampar di pantai!")
        print("Ada juga danau kecil dengan air jernih.")

        choice = input("NAIK ke kapal tua atau BERENANG di danau? ").lower()

        if choice == "naik":
            print(f"\n🚢 {name} naik ke kapal bajak laut tua...")
            print("Kapal ini penuh dengan jebakan dan hantu!")
            print("💀 GAME OVER! Hantu bajak laut menarikmu ke dasar laut...")

        elif choice == "berenang":
            print(f"\n🏊‍♂️ {name} berenang di danau jernih...")
            print("Air danau sangat dingin! Apa yang akan kamu lakukan?")

            swim_action = input("TERUS berenang atau KEMBALI ke pantai? ").lower()

            if swim_action == "terus":
                print("\n❄️ Air semakin dingin, tapi kamu terus berenang...")
                print("Di tengah danau ada pulau kecil dengan pohon aneh!")

                island_choice = input("NAIK ke pulau atau KEMBALI? ").lower()

                if island_choice == "naik":
                    print(f"\n🏝️ {name} naik ke pulau kecil di tengah danau...")
                    print("Pohon aneh itu ternyata menyembunyikan tangga ke bawah tanah!")
                    print("🏆 AMAZING WIN! Kamu menemukan ruang harta karun bawah air!")
                    print("💎 Kamu mendapat permata langka senilai 10,000 koin!")

                elif island_choice == "kembali":
                    print(f"\n🔄 {name} memutuskan untuk kembali...")
                    print("Di pantai kamu menemukan botol berisi pesan!")
                    print("📜 GOOD WIN! Pesan itu berisi petunjuk harta kecil - 800 koin!")

                else:
                    print("🚫 Pilihan tidak valid! Kamu kebingungan dan tenggelam...")
                    print("💀 GAME OVER!")

            elif swim_action == "kembali":
                print(f"\n↩️ {name} kembali ke pantai dengan bijak...")
                print("Di pantai kamu menemukan gua kecil yang tersembunyi!")
                print("🏺 SAFE WIN! Di gua ada pot berisi 300 koin emas!")

            else:
                print("🚫 Pilihan tidak valid! Kamu panik dan tenggelam...")
                print("💀 GAME OVER!")

        else:
            print("🚫 Pilihan tidak valid! Kamu berdiri bingung...")
            print("🌊 Air pasang datang dan menyeret kapal (dan kamu) ke laut!")
            print("💀 GAME OVER!")

    elif direction == "tengah":
        print(f"\n⛰️ {name} mendaki bukit tinggi dengan susah payah...")
        print("Dari puncak bukit, kamu bisa melihat seluruh pulau!")
        print("Kamu melihat ada menara tua di kejauhan.")

        tower_choice = input("PERGI ke menara atau TURUN dari bukit? ").lower()

        if tower_choice == "pergi":
            print(f"\n🗼 {name} berjalan menuju menara tua...")
            print("Menara itu sangat tinggi dan terlihat berbahaya!")

            climb_choice = input("NAIK menara atau CARI jalan lain? ").lower()

            if climb_choice == "naik":
                print(f"\n🧗‍♂️ {name} memanjat menara dengan hati-hati...")
                print("Di puncak menara ada mercusuar dengan cahaya aneh!")

                light_choice = input("NYALAKAN mercusuar atau TINGGALKAN? ").lower()

                if light_choice == "nyalakan":
                    print(f"\n💡 {name} menyalakan mercusuar kuno...")
                    print("Cahaya mercusuar membuka pintu rahasia di dasar menara!")
                    print("🏆 EPIC WIN! Ruang rahasia berisi harta karun lengkap!")
                    print("👑 Kamu mendapat mahkota emas dan 15,000 koin!")

                elif light_choice == "tinggalkan":
                    print(f"\n🚪 {name} meninggalkan mercusuar dan turun...")
                    print("Di tengah menara kamu menemukan ruang dengan peti kecil!")
                    print("📦 DECENT WIN! Peti berisi 1200 koin emas!")

                else:
                    print("🚫 Pilihan tidak valid! Menara mulai roboh!")
                    print("💀 GAME OVER! Kamu tertimbun reruntuhan menara...")

            elif climb_choice == "cari":
                print(f"\n🕵️‍♂️ {name} mencari jalan lain di sekitar menara...")
                print("Kamu menemukan pintu basement tersembunyi!")
                print("🚪 SMART WIN! Basement berisi perlengkapan bajak laut antik!")
                print("⚓ Kamu mendapat harta senilai 2500 koin!")

            else:
                print("🚫 Pilihan tidak valid! Kamu tersesat di sekitar menara...")
                print("🌙 Malam tiba, kamu kedinginan dan tidak ditemukan...")
                print("💀 GAME OVER!")

        elif tower_choice == "turun":
            print(f"\n⬇️ {name} turun dari bukit dengan hati-hati...")
            print("Di kaki bukit kamu menemukan kebun buah tropis!")
            print("🥭 PEACEFUL WIN! Kamu hidup tenang sebagai petani!")
            print("🌴 Bonus: Kamu menemukan 600 koin tersembunyi di kebun!")

        else:
            print("🚫 Pilihan tidak valid! Kamu terpeleset dari bukit...")
            print("💀 GAME OVER! Jatuh dari ketinggian...")

    else:
        print("🚫 Pilihan tidak valid!")
        print("Sementara kamu bingung menentukan arah...")
        print("🌊 Air pasang naik dan menyapu seluruh pantai!")
        print("💀 GAME OVER! Kamu terseret ombak ke laut dalam...")

    print(f"\n⭐ Terima kasih telah bermain, {name}!")
    print("🎮 Adventure selesai!")

else:
    print("🚫 Invalid language choice! / Pilihan bahasa tidak valid!")
    print("Please restart the game. / Silakan restart game.")