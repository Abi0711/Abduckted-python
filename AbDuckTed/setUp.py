import cx_Freeze

executables = [cx_Freeze.Executable("AbDuckTed.py")]

cx_Freeze.setup(
    name = "AbDuckTed",
    options = {"build_exe":{"packages": ["pygame"], "include_files":
                            ["blueKey.png", "bossKey.png",
                             "bread.png", "down.png", "happy.wav", "healthUp.wav", "jump2.wav", "jumpP.wav",
                             "keyFrag1.png", "keyFrag2.png", "last1.png",
                             "last2.png", "last3.png", "last4.png", "last5.png",
                             "last6.png","last7.png","last8.png", "last9.png","last10.png",
                             "lBoss.png", "lBossFinal.png", "lDuck.png", "lEasy.png",
                             "level1.txt", "level1Back.png", "level2.txt", "level2Back.png",
                             "lMedium.png", "lock.png", "lShoot.png", "lSpace.png",
                             "lSpaceShoot.png", "map.png", "music.mp3", "punch.wav",
                             "quack.wav", "rBoss.png", "rBossFinal.png", "rDuck.png",
                             "rEasy.png", "rMedium.png", "rShoot.png", "rSpace.png",
                             "rSpaceShoot.png", "save.txt", "shoot.wav", "slide0.png",
                             "slide1.png", "slide2.png", "spikes.png", "teleporter.wav",
                             "tutorial.txt", "ufoDuck.png", "up.png", "victory.wav"]}},

    description = "A duck gets abducted",
    executables = executables
    

    )
