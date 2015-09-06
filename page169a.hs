{-  run as

[1 of 1] Compiling Main             ( page169a.hs, interpreted )
Ok, modules loaded: Main.
*Main> asymAa (-0.8)
-0.5632
*Main> asymAa (-2)
32.0
*Main> asymAa 0.5
-0.1875
*Main> asymAa 1.5
14.0625

-}


asymAa :: Float -> Float
asymAa a = (a**2)*((3*a) - 2)*(a + 1)
