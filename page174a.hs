{-  run as

*Main> :l page174a.hs
[1 of 1] Compiling Main             ( page174a.hs, interpreted )
Ok, modules loaded: Main.
*Main> asymHor 2
1.0
*Main> asymHor (-1)
-0.5
*Main> asymHor (-0.05)
0.47435898

-}


asymHor :: Float -> Float
asymHor a = ((3*a) + 2) / ((2 * a) + 4)
